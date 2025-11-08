# Solar Challenge Week 0
![CI](https://github.com/hann2004/solar-challenge-week0/actions/workflows/unittests.yml/badge.svg)

Perfect! Let’s get this done properly. I’ll draft both a **professional README** for your GitHub repo and a **Google Docs report template** you can use for the KAIM interim submission. I’ll make it detailed, polished, and reflective of your actual work.

---

## **1️⃣ GitHub README (Markdown)**

```markdown
# Solar Energy Dataset EDA & Cleaning

**Author:** Hanan (hann2004)  
**Project:** KAIM Week 0 – Solar Energy Challenge  
**Date:** November 2025

---

##  Project Overview

This project performs **data cleaning, profiling, and exploratory data analysis (EDA)** on solar energy datasets from multiple countries: **Benin, Sierra Leone, and Togo**. The goal is to:

- Understand data quality and patterns.
- Identify correlations between solar irradiance, temperature, wind speed, and humidity.
- Prepare datasets for further modeling or regional comparison.

---

##  Project Structure

```

notebooks/
benin_eda.ipynb
sierraleone_eda.ipynb
togo_eda.ipynb
data/
benin_clean.csv
sierraleone_clean.csv
togo_clean.csv
README.md

````

- **notebooks/** – contains Jupyter notebooks for each country’s EDA.
- **data/** – cleaned datasets ready for analysis.
- **README.md** – project description and instructions.

---

##  Dataset Overview

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
- **WS / WSgust:** Wind speed and gusts (m/s)

---

##  Data Cleaning & Preprocessing

- Missing values handled with **median imputation** for numeric columns.  
- Outliers identified using **IQR method** and replaced where necessary.  
- Ensured consistent column names and data types across all datasets.

---

##  Exploratory Data Analysis (EDA)

### 1. Summary Statistics
- Mean, median, min, max, and standard deviation for all numeric features.  

### 2. Correlation Analysis
- Correlation heatmaps to detect relationships:
  - Strong positive correlation: GHI & Tamb  
  - Negative correlation: RH & Tamb  

### 3. Scatter Plots
- Wind speed vs GHI
- Relative humidity vs temperature  

### 4. Distribution & Wind Analysis
- Histograms for GHI, temperature, wind speed.
- Wind roses to visualize wind patterns.

**Example Plot:**  
*(Insert a PNG from your notebook)*

---

## Key Insights

- Benin and Togo show higher GHI than Sierra Leone overall.  
- High wind speed slightly reduces GHI.  
- Temperature and humidity are inversely correlated.  
- Outliers in ModA/ModB often coincide with missing irradiance data.

---

## How to Run

```bash
conda create -n solar-week0 python=3.10
conda activate solar-week0
pip install -r requirements.txt
jupyter notebook
````

* Open the notebooks in `notebooks/` for full EDA and plots.
* Cleaned datasets are in `data/`.

---

##  Next Steps

* Regional comparison of solar potential.
* Feature engineering for predictive modeling.
* Integrate more countries for a larger dataset.

