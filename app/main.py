import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import tempfile


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from visualization.plotter import SolarDataVisualizer

# Page configuration
st.set_page_config(
    page_title="Solar Farm Analysis Dashboard",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">☀️ Solar Farm Analysis Dashboard</h1>', unsafe_allow_html=True)
st.markdown("Compare solar potential across Benin, Sierra Leone, and Togo")

# File upload section
st.sidebar.title("📁 Data Upload")
st.sidebar.markdown("Upload your cleaned CSV files:")

uploaded_files = {}
countries = ['Benin', 'Sierra Leone', 'Togo']

for country in countries:
    uploaded_file = st.sidebar.file_uploader(
        f"{country} data", 
        type=['csv'],
        key=f"upload_{country}"
    )
    if uploaded_file is not None:
        uploaded_files[country] = uploaded_file

# Load data function
@st.cache_data
def load_uploaded_data(uploaded_file):
    """Load data from uploaded file"""
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None

def main():
    if not uploaded_files:
        st.warning("👆 Please upload cleaned CSV files for analysis using the file uploaders in the sidebar.")
        st.info("""
        **Required files:**
        - Benin: `benin_clean.csv`
        - Sierra Leone: `sierra_leone_clean.csv`
        - Togo: `togo_clean.csv`
        
        These are the cleaned files you created in Task 2.
        """)
        return

    # Load data for selected countries
    country_data = {}
    for country, uploaded_file in uploaded_files.items():
        df = load_uploaded_data(uploaded_file)
        if df is not None:
            country_data[country] = df
            st.sidebar.success(f"✅ {country} data loaded")

    if not country_data:
        st.error("No valid data loaded. Please check your CSV files.")
        return

    # Rest of your dashboard code continues here...
    # [Keep all your existing visualization code from the previous version]
    
    # Country selection
    selected_countries = st.sidebar.multiselect(
        "Select Countries to Compare:",
        list(country_data.keys()),
        default=list(country_data.keys())
    )

    # Metric selection
    selected_metric = st.sidebar.selectbox(
        "Select Solar Metric:",
        ["GHI", "DNI", "DHI", "Tamb", "WS"]
    )

    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"{selected_metric} Distribution Comparison")
        
        # Create boxplot
        fig, ax = plt.subplots(figsize=(10, 6))
        data_to_plot = []
        valid_countries = []
        
        for country in selected_countries:
            if country in country_data and selected_metric in country_data[country].columns:
                data_to_plot.append(country_data[country][selected_metric].dropna())
                valid_countries.append(country)
        
        if data_to_plot:
            ax.boxplot(data_to_plot, labels=valid_countries)
            ax.set_title(f'{selected_metric} Distribution by Country')
            
            # Set y-axis label based on metric
            if selected_metric in ['GHI', 'DNI', 'DHI']:
                ax.set_ylabel(f'{selected_metric} (W/m²)')
            elif selected_metric == 'Tamb':
                ax.set_ylabel('Temperature (°C)')
            elif selected_metric == 'WS':
                ax.set_ylabel('Wind Speed (m/s)')
            else:
                ax.set_ylabel(selected_metric)
                
            plt.xticks(rotation=45)
            st.pyplot(fig)
        else:
            st.warning(f"Metric '{selected_metric}' not found in selected countries' data.")
    
    with col2:
        st.subheader("Key Metrics")
        
        # Calculate and display key statistics
        for country in selected_countries:
            if country in country_data and selected_metric in country_data[country].columns:
                metric_data = country_data[country][selected_metric].dropna()
                
                st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
                st.markdown(f"**{country}**")
                st.metric(
                    label=f"Average {selected_metric}",
                    value=f"{metric_data.mean():.1f}",
                    delta=f"Std: {metric_data.std():.1f}"
                )
                st.markdown(f'</div>', unsafe_allow_html=True)
                st.write("")  # Add some space

    # Summary table and recommendations...
    # [Include the rest of your existing dashboard code]

if __name__ == "__main__":
    main()