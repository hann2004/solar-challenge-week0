# Solar Challenge Week 0
![CI](https://github.com/hann2004/solar-challenge-week0/actions/workflows/unittests.yml/badge.svg)

# 🌞 Solar Farm Analysis - Cross-Country Comparison

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/) 
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Author:** Hanan (hann2004)  
**Project:** 10 Academy - Solar Data Discovery Challenge  
**Date:** November 2025

---

##  Project Overview

This project performs comprehensive analysis of solar farm data from **Benin, Sierra Leone, and Togo** to identify high-potential regions for solar investments. The analysis supports MoonLight Energy Solutions in developing strategic approaches for operational efficiency and sustainability.

**Objectives:**
- Perform data cleaning, profiling, and exploratory data analysis (EDA)
- Compare solar potential across three West African countries
- Identify correlations between solar irradiance and environmental factors
- Provide data-driven recommendations for solar farm investments
- Develop interactive dashboard for visualization

---

Sure — here’s a clean, copy-paste-ready version you can put directly in your **README.md** on GitHub:

---

## 🗂️ Project Structure

```bash
solar-challenge-week0/
├── app/                          # Streamlit dashboard
│   ├── main.py                   # Main dashboard application
│   └── utils.py                  # Utility functions for the app
│
├── data/                         # Cleaned data files
│   ├── benin_clean.csv
│   ├── sierra_leone_clean.csv
│   └── togo_clean.csv
│
├── notebooks/                    # Jupyter notebooks for analysis
│   ├── benin_eda.ipynb           # Exploratory Data Analysis for Benin
│   ├── sierra_leone_eda.ipynb    # EDA for Sierra Leone
│   ├── togo_eda.ipynb            # EDA for Togo
│   └── compare_countries.ipynb   # Cross-country comparative analysis
│
├── src/                          # Modular Python scripts
│   ├── data_processing/
│   │   └── cleaner.py            # Data cleaning utilities
│   └── visualization/
│       └── plotter.py            # Visualization utilities
│
├── tests/                        # Unit and integration tests
│
├── scripts/                      # Automation and helper scripts
│
├── dashboard_screenshots/        # Screenshots of the Streamlit dashboard
│
├── requirements.txt              # Python dependencies
│
└── README.md                     # Project documentation
```

---

Would you like me to add a short description *below* it (e.g., “Each directory plays a specific role in maintaining modularity and clarity…”)? It makes README files look more polished and professional.

## 📊 Dataset Overview

The dataset contains solar radiation measurement data with the following key metrics:

| Column | Description | Unit |
|--------|-------------|------|
| **GHI** | Global Horizontal Irradiance | W/m² |
| **DNI** | Direct Normal Irradiance | W/m² |
| **DHI** | Diffuse Horizontal Irradiance | W/m² |
| **Tamb** | Ambient Temperature | °C |
| **RH** | Relative Humidity | % |
| **WS** | Wind Speed | m/s |
| **WSgust** | Wind Gust Speed | m/s |
| **TModA/B** | Module Temperatures | °C |
| **BP** | Barometric Pressure | hPa |

**Dataset Statistics:**
- **Benin**: 525,600 rows × 19 columns
- **Sierra Leone**: 525,600 rows × 19 columns  
- **Togo**: 525,600 rows × 19 columns

---

## 🔧 Data Processing Pipeline

### 1. Data Cleaning & Preprocessing
- **Missing Values**: Handled using median imputation for numeric columns
- **Outlier Detection**: Z-score method (|Z| > 3) for key solar metrics
- **Data Validation**: Checked for negative irradiance values and implausible measurements

### 2. Exploratory Data Analysis (EDA)
- **Summary Statistics**: Mean, median, standard deviation for all numeric features
- **Correlation Analysis**: Heatmaps revealing relationships between variables
- **Time Series Analysis**: Patterns in solar irradiance and temperature over time
- **Distribution Analysis**: Histograms and boxplots for key metrics

### 3. Cross-Country Comparison
- **Statistical Testing**: ANOVA and Kruskal-Wallis tests for significance
- **Visual Comparison**: Side-by-side boxplots and summary tables
- **Performance Ranking**: Countries ranked by solar potential and consistency

---

## 📈 Key Insights & Findings

### Solar Potential Ranking:
1. **Togo** - Highest average GHI (250+ W/m²) and most consistent performance
2. **Benin** - Strong solar resources (240+ W/m²) with good reliability
3. **Sierra Leone** - Moderate potential (220+ W/m²) with higher variability

### Statistical Significance:
- **ANOVA Tests**: Confirmed significant differences in GHI across countries (p < 0.05)
- **Correlation Patterns**: Strong positive correlation between GHI and temperature
- **Seasonal Patterns**: Clear diurnal and seasonal variations in solar irradiance

### Environmental Factors:
- **Wind Impact**: Higher wind speeds slightly reduce GHI efficiency
- **Temperature Effects**: Optimal performance within specific temperature ranges
- **Humidity Influence**: Inverse correlation between relative humidity and solar efficiency

---

## 🎮 Streamlit Dashboard

**Live Dashboard URL:** 

### Features:
- **Interactive Country Selection**: Compare any combination of countries
- **Metric Comparison**: Analyze GHI, DNI, DHI, Temperature, and Wind Speed
- **File Upload**: Upload cleaned CSV files for custom analysis
- **Real-time Visualizations**: Boxplots, summary tables, and statistical insights
- **Strategic Recommendations**: Data-driven investment guidance

### Usage:
```bash
streamlit run app/main.py
```


##  Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/hann2004/solar-challenge-week0.git
cd solar-challenge-week0

# Create and activate conda environment
conda create -n solar-week0 python=3.10
conda activate solar-week0

# Install dependencies
pip install -r requirements.txt
```

### Running the Analysis
1. **Exploratory Data Analysis (EDA):**
   ```bash
   jupyter notebook notebooks/
   ```
   Open and run the country-specific EDA notebooks.

2. **Cross-Country Comparison:**
   ```bash
   jupyter notebook notebooks/compare_countries.ipynb
   ```

3. **Interactive Dashboard:**
   ```bash
   streamlit run app/main.py
   ```

---

## Strategic Recommendations

Based on comprehensive analysis, MoonLight Energy Solutions should:

### Investment Priority:
1. **Primary Focus**: Togo - Highest solar potential and consistency
2. **Secondary Focus**: Benin - Strong performance with reliable conditions
3. **Opportunistic**: Sierra Leone - Site-specific opportunities in optimal micro-climates

### Operational Considerations:
- **Panel Maintenance**: Regular cleaning shows measurable performance improvements
- **Site Selection**: Consider local wind patterns and temperature variations
- **Monitoring**: Implement continuous performance tracking across sites

### Long-term Strategy:
- **Expansion Planning**: Use cross-country insights for regional expansion
- **Technology Selection**: Optimize panel technology based on local conditions
- **Risk Management**: Account for seasonal variability in energy production forecasts

---

##  Notebooks

| Country | Notebook | Description |
|---------|----------|-------------|
| Benin | [benin_eda.ipynb](notebooks/benin_eda.ipynb) | Complete EDA for Benin solar data |
| Sierra Leone | [sierra_leone_eda.ipynb](notebooks/sierra_leone_eda.ipynb) | EDA for Sierra Leone dataset |
| Togo | [togo_eda.ipynb](notebooks/togo_eda.ipynb) | Comprehensive Togo analysis |
| Comparison | [compare_countries.ipynb](notebooks/compare_countries.ipynb) | Cross-country statistical analysis |

---

##  Testing

Run the test suite to verify functionality:
```bash
python tests/test_cleaner.py
python tests/test_plotter.py
python tests/test_dashboard.py
```

---

##  Project Timeline

- **Challenge Introduction**: November 5, 2025
- **Interim Submission**: November 9, 2025  
- **Final Submission**: November 12, 2025

---

## Acknowledgments

This project was completed as part of the 10 Academy training program in Data Engineering, Financial Analytics, and Machine Learning Engineering.

**Facilitators:**
- Yabebal
- Kerod
- Mahbubah  
- Filimon

---

##  License

This project is for educational purposes as part of the 10 Academy training program.





