import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data_processing.cleaner import DataCleaner
import pandas as pd
import numpy as np

def test_data_cleaner_initialization():
    """Test that DataCleaner initializes correctly"""
    cleaner = DataCleaner("dummy_path.csv")
    assert cleaner.data_path == "dummy_path.csv"
    assert cleaner.df is None
    print("✓ DataCleaner initialization test passed!")

def test_missing_value_handling():
    """Test missing value handling with sample data"""
    # Create sample data with missing values
    sample_data = pd.DataFrame({
        'GHI': [100, 200, np.nan, 400, 500],
        'DNI': [50, np.nan, np.nan, 200, 250],
        'Tamb': [25, 30, 35, 40, 45]
    })
    
    # This is just a basic test - we'll test the actual functionality later
    print("✓ Missing value handling test structure ready!")
    
if __name__ == "__main__":
    test_data_cleaner_initialization()
    test_missing_value_handling()
    print("All basic tests passed!")