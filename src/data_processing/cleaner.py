import pandas as pd
import numpy as np
from pathlib import Path

class DataCleaner:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        
    def load_data(self):
        """Load the raw data from CSV"""
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"Data loaded successfully. Shape: {self.df.shape}")
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def handle_missing_values(self, threshold=0.05):
        """Handle missing values in the dataset"""
        if self.df is None:
            print("No data loaded. Call load_data() first.")
            return
        
        # Report missing values
        missing_report = self.df.isna().sum() / len(self.df)
        print("Missing values report:")
        print(missing_report[missing_report > 0])
        
        # Drop columns with more than threshold missing values
        cols_to_drop = missing_report[missing_report > threshold].index
        if len(cols_to_drop) > 0:
            print(f"Dropping columns: {list(cols_to_drop)}")
            self.df = self.df.drop(columns=cols_to_drop)
        
        # Impute remaining missing values with median for numeric columns
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        
        print(f"After cleaning - Shape: {self.df.shape}")
    
    def detect_outliers_zscore(self, columns, threshold=3):
        """Detect outliers using Z-score method"""
        outlier_mask = pd.Series([False] * len(self.df))
        
        for col in columns:
            if col in self.df.columns:
                z_scores = np.abs((self.df[col] - self.df[col].mean()) / self.df[col].std())
                outlier_mask = outlier_mask | (z_scores > threshold)
        
        outlier_count = outlier_mask.sum()
        print(f"Detected {outlier_count} outliers ({outlier_count/len(self.df)*100:.2f}%)")
        return outlier_mask
    
    def save_cleaned_data(self, output_path):
        """Save cleaned data to CSV"""
        if self.df is not None:
            self.df.to_csv(output_path, index=False)
            print(f"Cleaned data saved to: {output_path}")
        else:
            print("No data to save. Please load and clean data first.")

def clean_country_data(country_name):
    """Helper function to clean data for a specific country"""
    input_path = f"data/{country_name}.csv"
    output_path = f"data/{country_name}_clean.csv"
    
    if not Path(input_path).exists():
        print(f"Raw data file not found: {input_path}")
        return
    
    cleaner = DataCleaner(input_path)
    if cleaner.load_data():
        cleaner.handle_missing_values()
        
        # Define key columns for outlier detection
        key_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
        available_columns = [col for col in key_columns if col in cleaner.df.columns]
        outlier_mask = cleaner.detect_outliers_zscore(available_columns)
        
        cleaner.df = cleaner.df[~outlier_mask]
        
        cleaner.save_cleaned_data(output_path)

if __name__ == "__main__":
    countries = ['benin', 'sierra_leone', 'togo']
    for country in countries:
        print(f"\nCleaning data for {country}...")
        clean_country_data(country)