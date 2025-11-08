# Solar Challenge Week 0
![CI](https://github.com/hann2004/solar-challenge-week0/actions/workflows/unittests.yml/badge.svg)

# 🌞 Solar Energy Dataset EDA & Cleaning

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/) 
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Author:** Hanan (hann2004)  
**Project:** KAIM Week 0 – Solar Energy Challenge  
**Date:** November 2025

---

##  Project Overview

This project performs **data cleaning, profiling, and exploratory data analysis (EDA)** on solar energy datasets from multiple countries: **Benin, Sierra Leone, and Togo**.  

**Objectives:**

- Understand data quality and patterns.  
- Identify correlations between solar irradiance, temperature, wind speed, and humidity.  
- Prepare datasets for modeling or regional comparison.  

---

##  Project Structure

notebooks/
benin_eda.ipynb
sierraleone_eda.ipynb
togo_eda.ipynb
data/
benin_clean.csv
sierraleone_clean.csv
togo_clean.csv
README.md


- **notebooks/** – Jupyter notebooks with EDA and visualizations.  
- **data/** – Cleaned CSV datasets.  
- **README.md** – Project description & instructions.  

---

## 📊 Dataset Overview

| Country        | Rows   | Columns | Key Features                                      |
|----------------|-------|---------|--------------------------------------------------|
| Benin          | 8760  | 9       | GHI, DNI, DHI, TModA, TModB, Tamb, RH, WS, WSgust |
| Sierra Leone   | 8760  | 9       | Same as Benin                                     |
| Togo           | 8760  | 9       | Same as Benin                                     |

**Column Descriptions:**

- **GHI:** Global Horizontal Irradiance (W/m²)  
- **DNI:** Direct Normal Irradiance (W/m²)  
- **DHI:** Diffuse Horizontal Irradiance (W/m²)  
- **TModA / TModB:** Module temperatures (°C)  
- **Tamb:** Ambient temperature (°C)  
- **RH:** Relative humidity (%)  
- **WS / WSgust:** Wind speed & gusts (m/s)

---

##  Data Cleaning & Preprocessing

- Handled missing values using **median imputation**.  
- Detected and treated outliers using **IQR method**.  
- Standardized column names & data types across all datasets.  

---

##  Exploratory Data Analysis (EDA)

### 1. Summary Statistics
- Calculated mean, median, min, max, and standard deviation for all numeric features.

### 2. Correlation Analysis
- Heatmaps reveal relationships:
  - **GHI ↔ Tamb:** Strong positive correlation  
  - **RH ↔ Tamb:** Negative correlation  

![Correlation Heatmap](images/correlation_heatmap.png)  

### 3. Scatter Plots
- Wind Speed vs GHI  
- Relative Humidity vs Ambient Temperature  

![Scatter Plot Example](images/scatter_plot.png)  

### 4. Distribution & Wind Analysis
- Histograms for GHI, temperature, wind speed  
- Wind roses to visualize wind patterns  

![Wind Rose](images/wind_rose.png)  

---

##  Key Insights

- Benin & Togo have higher GHI than Sierra Leone.  
- Wind speed slightly reduces GHI.  
- Temperature & humidity are inversely correlated.  
- Outliers in TModA/TModB often coincide with missing irradiance data.

---

## 📌 Notebooks

| Country      | Notebook Link |
|-------------|----------------|
| Benin       | [benin_eda.ipynb](notebooks/benin_eda.ipynb) |
| Sierra Leone| [sierraleone_eda.ipynb](notebooks/sierraleone_eda.ipynb) |
| Togo        | [togo_eda.ipynb](notebooks/togo_eda.ipynb) |

---

## 🚀 How to Run

```bash
conda create -n solar-week0 python=3.10
conda activate solar-week0
pip install -r requirements.txt
jupyter notebook

Open the notebooks to explore plots and analysis.

Cleaned datasets are in data/.

 Next Steps

Regional comparison of solar potential.

Feature engineering for predictive modeling.

Expand dataset with more countries for analysis.
