import ee
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from libpysal import weights
from esda import Moran
import matplotlib.colors as mcolors

# 1. Initialize Earth Engine
ee.Initialize(project='atiq-project-july2025')

# 2a. ERA5-Land monthly aggregated 2m air temperature dataset
era5 = ee.ImageCollection("ECMWF/ERA5_LAND/MONTHLY_AGGR") \
            .filterDate("2018-07-01", "2022-06-30") \
            .select("temperature_2m")
avg_temp = era5.mean()

# 2b. CHIRPS rainfall dataset
chirps = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY") \
            .filterDate("2018-07-01", "2022-06-30")
total_rainfall = chirps.sum()

# 3. Load polygons
districts = ee.FeatureCollection("users/atiqka/BGD_2")

# 4a. Aggregate temperature
district_temp = avg_temp.reduceRegions(
    collection=districts,
    reducer=ee.Reducer.mean(),
    scale=5000
)
temp_dict = district_temp.getInfo()
temp_df = pd.DataFrame([f["properties"] for f in temp_dict["features"]])
temp_df["temp_celsius"] = (temp_df["mean"] - 273.15).round(1)

# 4b. Aggregate rainfall
district_rain = total_rainfall.reduceRegions(
    collection=districts,
    reducer=ee.Reducer.mean(),
    scale=5000
)
rain_dict = district_rain.getInfo()
rain_df = pd.DataFrame([f["properties"] for f in rain_dict["features"]])
rain_df["rainfall_cm"] = (rain_df["mean"] / 10).round(0)

# 5. Load shapefile
shp_path = "/Users/atiq/Pyvs_2026/gadm41_BGD_shp.zip"
districts_gdf = gpd.read_file(shp_path, layer="gadm41_BGD_2")

# 6. Merge both datasets
districts_gdf = districts_gdf.merge(temp_df, on="NAME_2")
districts_gdf = districts_gdf.merge(rain_df, on="NAME_2")

# 7. Moran’s I (optional diagnostics)
w = weights.Queen.from_dataframe(districts_gdf)
w.transform = "r"
moran_temp = Moran(districts_gdf["temp_celsius"], w)
moran_rain = Moran(districts_gdf["rainfall_cm"], w)
print(f"Temperature Moran's I: {moran_temp.I:.3f}, p={moran_temp.p_sim:.4f}")
print(f"Rainfall Moran's I: {moran_rain.I:.3f}, p={moran_rain.p_sim:.4f}")

# 8. Reproject
districts_gdf = districts_gdf.to_crs(epsg=3857)

# 9. Plot side-by-side maps
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# --- Temperature map ---
values_temp = districts_gdf["temp_celsius"].fillna(0).values
norm_temp = mcolors.Normalize(vmin=values_temp.min(), vmax=values_temp.max())
cmap_temp = plt.get_cmap("inferno_r")
districts_gdf.plot(ax=axes[0],
                   color=[cmap_temp(norm_temp(v)) for v in values_temp],
                   edgecolor="lightgray", linewidth=0.3)
axes[0].set_title("Bangladesh Avg Annual Temperature (2018–2022)",
                  fontsize=14, weight="bold", pad=20)
axes[0].axis("off")
sm_temp = plt.cm.ScalarMappable(cmap=cmap_temp, norm=norm_temp)
sm_temp.set_array([])
cbar_temp = fig.colorbar(sm_temp, ax=axes[0], orientation="horizontal",
                         fraction=0.025, pad=0.05)
# Legend title ABOVE the bar
cbar_temp.ax.set_title("Temperature (°C)", fontsize=11, weight="bold", pad=10)

# --- Rainfall map ---
values_rain = districts_gdf["rainfall_cm"].fillna(0).values
norm_rain = mcolors.Normalize(vmin=values_rain.min(), vmax=values_rain.max())
cmap_rain = plt.get_cmap("viridis_r")
districts_gdf.plot(ax=axes[1],
                   color=[cmap_rain(norm_rain(v)) for v in values_rain],
                   edgecolor="lightgray", linewidth=0.3)
axes[1].set_title("Bangladesh Avg Annual Rainfall (2018–2022)",
                  fontsize=14, weight="bold", pad=20)
axes[1].axis("off")
sm_rain = plt.cm.ScalarMappable(cmap=cmap_rain, norm=norm_rain)
sm_rain.set_array([])
cbar_rain = fig.colorbar(sm_rain, ax=axes[1], orientation="horizontal",
                         fraction=0.025, pad=0.05)
# Legend title ABOVE the bar
cbar_rain.ax.set_title("Rainfall (cm)", fontsize=11, weight="bold", pad=10)

# 10. Save and show
plt.tight_layout()
plt.savefig("/Users/atiq/Pyvs_2026/bangladesh_temp_rainfall_combined_2018-2022.png",
            dpi=300, bbox_inches="tight")
plt.show()

