# Bangladesh District-Level Temperature and Rainfall Mapping (2018–2022)

## Author: Atiq Kainan Ahmed. 
Email: atiqka@yahoo.com

## Background

Understanding spatial patterns of climate variability is critical for climate adaptation planning, disaster risk reduction, agricultural management, public health studies, and climate finance allocation. Bangladesh is among the world's most climate-vulnerable countries, facing increasing challenges associated with rising temperatures, changing rainfall regimes, riverine flooding, drought, and extreme weather events.

While global climate datasets provide valuable information, they often require substantial processing before they can be used in local-scale planning and analysis. Policymakers and researchers frequently require climate indicators summarized at administrative levels such as districts, where planning decisions and development investments are commonly implemented.

This project was developed to address that need by providing a reproducible workflow for aggregating climate information directly to Bangladesh's district boundaries (ADM2 level). Using Google Earth Engine, the script extracts and processes multi-year temperature and rainfall observations and converts them into easily interpretable district-level indicators. The resulting outputs can be used independently or integrated with socio-economic, health, agricultural, disaster risk, or climate finance datasets for further analysis.

## Output 

The output map can be found here https://github.com/atiqka/BGD_temp-rf_2018-22/blob/main/bangladesh_temp_rainfall_combined_2018-2022.png


---

## Objective

The primary objective of this project is to generate district-level climate indicators for Bangladesh using globally recognized climate datasets and modern cloud-based geospatial processing techniques.

Specifically, the workflow aims to:

- Extract temperature information from the ERA5-Land climate reanalysis dataset.
- Extract rainfall information from the CHIRPS precipitation dataset.
- Aggregate both datasets to district (ADM2) boundaries across Bangladesh.
- Compute district-level climate indicators for the period July 2018 to June 2022.
- Evaluate spatial clustering using Moran’s I statistics.
- Produce publication-quality thematic maps showing spatial variation in climate conditions.
- Demonstrate a reproducible workflow that can be adapted to other countries, administrative levels, or climate variables.

---


## Technical Information

This project was developed using **Python 3.14** and leverages the capabilities of **Google Earth Engine (GEE)** for cloud-based climate data extraction and processing. Spatial analysis and visualization are conducted using a suite of open-source Python libraries including GeoPandas, Pandas, Matplotlib, NumPy, PySAL, and ESDA.

The workflow demonstrates how large-scale Earth observation and climate reanalysis datasets can be integrated with administrative boundary data to produce district-level climate indicators suitable for research, planning, and decision-making applications.

### Software Environment

| Component | Version |
|------------|------------|
| Python | 3.14 |
| Earth Engine API | 1.7.39 |
| GeoPandas | Latest Stable Release |
| Pandas | Latest Stable Release |
| Matplotlib | Latest Stable Release |
| NumPy | Latest Stable Release |
| libpysal | Latest Stable Release |
| esda | Latest Stable Release |

---

## Overview of the Workflow

The workflow consists of five major steps.

### Step 1 – Climate Data Retrieval

The script accesses climate datasets hosted on Google Earth Engine, including:

- ERA5-Land Monthly Aggregated Temperature
- CHIRPS Daily Rainfall

Google Earth Engine enables efficient processing of large climate archives without requiring local storage of raster datasets.

### Step 2 – Temporal Aggregation

Climate observations are aggregated across the study period spanning July 2018 through June 2022.

For temperature, mean conditions are calculated using monthly ERA5-Land observations.

For rainfall, precipitation totals are accumulated across all available daily observations.

### Step 3 – Spatial Aggregation

Using Bangladesh district boundaries, raster climate information is summarized into district-level statistics through Earth Engine's `reduceRegions()` functionality.

This process converts pixel-level climate information into administrative-level indicators suitable for policy analysis and reporting.

### Step 4 – Spatial Statistical Analysis

The project computes Moran's I statistics to evaluate whether climate conditions exhibit significant spatial clustering.

Spatial autocorrelation analysis helps identify whether neighboring districts experience similar climate conditions and provides additional insight into the geographical structure of climate variability.

### Step 5 – Cartographic Visualization

Publication-quality maps are generated using GeoPandas and Matplotlib.

The final outputs include:

- Average Temperature Map (°C)
- Average Rainfall Map (cm)

Both maps use continuous color scales and are designed for research publications, technical reports, presentations, and policy briefs.

---

## Why Use Google Earth Engine?

Google Earth Engine provides a scalable cloud-computing environment for environmental analysis and Earth observation applications. For climate analyses such as this project, Earth Engine offers several advantages:

- Direct access to global climate archives.
- Elimination of local raster storage requirements.
- Fast processing of large spatio-temporal datasets.
- Reproducible workflows.
- Easy integration with Python.

By combining Google Earth Engine with Python's geospatial ecosystem, the workflow creates a powerful framework for climate and environmental analysis.

---

## Potential Applications

Although this project focuses on temperature and rainfall mapping, the methodology can be readily extended to a wide range of applications, including:

### Climate Change Research

- Climate baseline development
- Temperature trend assessment
- Rainfall variability analysis
- Climate hotspot identification

### Public Health Research

- Climate-health interaction studies
- Heat exposure assessments
- Disease-climate modelling
- Child health vulnerability analysis

### Disaster Risk Management

- Flood risk assessments
- Drought monitoring
- Early warning system support
- Hazard exposure assessments

### Climate Finance and Adaptation Planning

- Climate vulnerability assessments
- Equity-focused resource allocation
- Adaptation investment prioritization
- Climate resilience planning

### Agriculture and Food Security

- Agricultural climate zoning
- Rainfall suitability analysis
- Crop risk assessment
- Climate-smart agriculture planning

---

## Key Output

The primary deliverable is a high-resolution figure showing district-level climate conditions across Bangladesh for the study period.

The output figure allows users to:

- Compare temperature variation across districts.
- Compare rainfall variation across districts.
- Identify spatial climate gradients.
- Support evidence-based planning and decision-making.
- Integrate climate indicators into further statistical analyses.

The figure is exported as:

```text
https://github.com/atiqka/BGD_temp-rf_2018-22/blob/main/bangladesh_temp_rainfall_combined_2018-2022.png
```

with a resolution of 300 DPI suitable for publication and reporting purposes.


## License 

MIT License

Copyright (c) 2025 Atiq Kainan Ahmed.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
