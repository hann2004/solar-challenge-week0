import pandas as pd
import streamlit as st
from pathlib import Path

@st.cache_data
def load_all_country_data():
    """Load cleaned data for all available countries"""
    countries = {
        'Benin': 'data/benin_clean.csv',
        'Sierra Leone': 'data/sierraleone_clean.csv',
        'Togo': 'data/togo_clean.csv'
    }
    
    country_data = {}
    for country_name, file_path in countries.items():
        try:
            if Path(file_path).exists():
                df = pd.read_csv(file_path)
                country_data[country_name] = df
                st.success(f"Loaded {country_name} data: {df.shape}")
            else:
                st.warning(f"⚠️ File not found: {file_path}")
        except Exception as e:
            st.error(f"❌ Error loading {country_name}: {e}")
    
    return country_data

def get_metric_units(metric):
    """Return appropriate units for each metric"""
    units = {
        'GHI': 'W/m²',
        'DNI': 'W/m²', 
        'DHI': 'W/m²',
        'Tamb': '°C',
        'WS': 'm/s',
        'RH': '%',
        'BP': 'hPa'
    }
    return units.get(metric, '')

def create_summary_stats(country_data, metrics=None):
    """Create summary statistics for selected metrics"""
    if metrics is None:
        metrics = ['GHI', 'DNI', 'DHI', 'Tamb', 'WS']
    
    summary_data = []
    for country_name, df in country_data.items():
        country_stats = {'Country': country_name}
        
        for metric in metrics:
            if metric in df.columns:
                data = df[metric].dropna()
                country_stats[f'{metric}_mean'] = data.mean()
                country_stats[f'{metric}_median'] = data.median()
                country_stats[f'{metric}_std'] = data.std()
                country_stats[f'{metric}_min'] = data.min()
                country_stats[f'{metric}_max'] = data.max()
        
        summary_data.append(country_stats)
    
    return pd.DataFrame(summary_data)

def get_country_recommendations(summary_df):
    """Generate investment recommendations based on data"""
    recommendations = []
    
    if 'GHI_mean' in summary_df.columns:
        best_ghi_country = summary_df.loc[summary_df['GHI_mean'].idxmax(), 'Country']
        best_ghi_value = summary_df['GHI_mean'].max()
        recommendations.append(f"**🏆 Top Solar Potential**: {best_ghi_country} (Average GHI: {best_ghi_value:.1f} W/m²)")
    
    if 'GHI_std' in summary_df.columns:
        most_consistent_country = summary_df.loc[summary_df['GHI_std'].idxmin(), 'Country']
        consistency_value = summary_df['GHI_std'].min()
        recommendations.append(f"**📊 Most Consistent**: {most_consistent_country} (GHI Std: {consistency_value:.1f} W/m²)")
    
    return recommendations