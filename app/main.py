import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Add src to path to import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from visualization.plotter import SolarDataVisualizer

# Page configuration
st.set_page_config(
    page_title="Solar Farm Analysis Dashboard",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
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
st.markdown("Compare solar potential across Benin, SierraLeone, and Togo")

# Sidebar for controls
st.sidebar.title("Dashboard Controls")
st.sidebar.markdown("Customize the analysis below:")

# Country selection
selected_countries = st.sidebar.multiselect(
    "Select Countries:",
    ["Benin", "SierraLeone", "Togo"],
    default=["Benin", "SierraLeone", "Togo"]
)

# Metric selection
selected_metric = st.sidebar.selectbox(
    "Select Solar Metric:",
    ["GHI", "DNI", "DHI", "Tamb", "WS"]
)

# Load data function
@st.cache_data
def load_country_data(country_name):
    """Load cleaned data for a country with caching for performance"""
    try:
        file_path = f"data/{country_name.lower().replace(' ', '_')}_clean.csv"
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error loading data for {country_name}: {e}")
        return None

def main():
    # Load data for selected countries
    country_data = {}
    for country in selected_countries:
        df = load_country_data(country)
        if df is not None:
            country_data[country] = df
    
    if not country_data:
        st.error("No data loaded. Please check if cleaned CSV files exist in the data/ directory.")
        return
    
    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"{selected_metric} Distribution Comparison")
        
        # Create boxplot
        fig, ax = plt.subplots(figsize=(10, 6))
        data_to_plot = []
        valid_countries = []
        
        for country, df in country_data.items():
            if selected_metric in df.columns:
                data_to_plot.append(df[selected_metric].dropna())
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
        for country, df in country_data.items():
            if selected_metric in df.columns:
                metric_data = df[selected_metric].dropna()
                
                st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
                st.markdown(f"**{country}**")
                st.metric(
                    label=f"Average {selected_metric}",
                    value=f"{metric_data.mean():.1f}",
                    delta=f"Std: {metric_data.std():.1f}"
                )
                st.markdown(f'</div>', unsafe_allow_html=True)
                st.write("")  # Add some space
    
    # Summary table
    st.subheader("Country Comparison Summary")
    
    summary_data = []
    for country, df in country_data.items():
        country_stats = {'Country': country}
        
        key_metrics = ['GHI', 'DNI', 'DHI', 'Tamb', 'WS']
        for metric in key_metrics:
            if metric in df.columns:
                country_stats[f'{metric}_mean'] = df[metric].mean()
                country_stats[f'{metric}_median'] = df[metric].median()
        
        summary_data.append(country_stats)
    
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)
    
    # Recommendations section
    st.subheader("🌍 Strategic Recommendations")
    
    if 'GHI' in summary_df.columns:
        # Find country with highest GHI
        best_country = summary_df.loc[summary_df['GHI_mean'].idxmax(), 'Country']
        st.success(f"**Primary Investment Recommendation**: {best_country} shows the highest average GHI, making it the most promising location for solar farm development.")
    
    st.info("""
    **Considerations for Site Selection:**
    - Higher GHI values indicate better overall solar potential
    - Lower standard deviation means more predictable energy generation
    - Consider local infrastructure, regulations, and costs
    - Environmental factors and community impact
    """)

if __name__ == "__main__":
    main()