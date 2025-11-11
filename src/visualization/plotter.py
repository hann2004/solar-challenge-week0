import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

class SolarDataVisualizer:
    def __init__(self):
        self.country_data = {}
        plt.style.use('default')
        
    def load_country_data(self, country_name, data_path):
        """Load cleaned data for a country"""
        try:
            df = pd.read_csv(data_path)
            self.country_data[country_name] = df
            print(f"Loaded data for {country_name}: {df.shape}")
            return True
        except Exception as e:
            print(f"Error loading {country_name}: {e}")
            return False
    
    def create_comparison_boxplots(self, metrics=None):
        """Create boxplots comparing countries for different metrics"""
        if metrics is None:
            metrics = ['GHI', 'DNI', 'DHI']
        
        fig, axes = plt.subplots(1, len(metrics), figsize=(15, 5))
        if len(metrics) == 1:
            axes = [axes]
        
        for i, metric in enumerate(metrics):
            data_to_plot = []
            country_names = []
            
            for country, df in self.country_data.items():
                if metric in df.columns:
                    data_to_plot.append(df[metric].dropna())
                    country_names.append(country)
            
            if data_to_plot:
                axes[i].boxplot(data_to_plot, labels=country_names)
                axes[i].set_title(f'{metric} Distribution by Country')
                axes[i].set_ylabel(f'{metric} (W/m²)')
                axes[i].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        return fig
    
    def create_summary_table(self):
        """Create a summary table of key metrics across countries"""
        summary_data = []
        
        for country, df in self.country_data.items():
            country_stats = {'Country': country}
            
            # Key solar metrics
            key_metrics = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS']
            
            for metric in key_metrics:
                if metric in df.columns:
                    country_stats[f'{metric}_mean'] = df[metric].mean()
                    country_stats[f'{metric}_median'] = df[metric].median()
                    country_stats[f'{metric}_std'] = df[metric].std()
            
            summary_data.append(country_stats)
        
        summary_df = pd.DataFrame(summary_data)
        return summary_df
    
    def save_plot(self, fig, filename):
        """Save plot to file"""
        plots_dir = Path("plots")
        plots_dir.mkdir(exist_ok=True)
        
        filepath = plots_dir / filename
        fig.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {filepath}")

def compare_all_countries():
    """Main function to compare all three countries"""
    visualizer = SolarDataVisualizer()
    
    # Load all country data
    countries = {
        'Benin': 'data/benin_clean.csv',
        'Sierra Leone': 'data/sierra_leone_clean.csv', 
        'Togo': 'data/togo_clean.csv'
    }
    
    for country, path in countries.items():
        if Path(path).exists():
            visualizer.load_country_data(country, path)
        else:
            print(f"File not found: {path}")
    
    if len(visualizer.country_data) >= 2:
        # Create comparison plots
        fig = visualizer.create_comparison_boxplots()
        visualizer.save_plot(fig, "country_comparison_boxplots.png")
        
        # Create summary table
        summary_df = visualizer.create_summary_table()
        print("\nSummary Statistics:")
        print(summary_df.to_string(index=False))
        
        # Save summary table
        summary_df.to_csv('data/country_comparison_summary.csv', index=False)
        print("\nSummary table saved to: data/country_comparison_summary.csv")
        
        return summary_df
    else:
        print("Need at least 2 countries with data for comparison")
        return None

if __name__ == "__main__":
    compare_all_countries()