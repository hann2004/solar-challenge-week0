import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.visualization.plotter import SolarDataVisualizer
import pandas as pd

def test_visualizer_initialization():
    """Test that SolarDataVisualizer initializes correctly"""
    visualizer = SolarDataVisualizer()
    assert visualizer.country_data == {}
    print("✓ SolarDataVisualizer initialization test passed!")

def test_summary_table_structure():
    """Test summary table creation with sample data"""
    visualizer = SolarDataVisualizer()
    
    # Create sample data for testing
    sample_data = pd.DataFrame({
        'GHI': [100, 200, 300],
        'DNI': [50, 100, 150], 
        'Tamb': [25, 30, 35]
    })
    
    visualizer.country_data['TestCountry'] = sample_data
    summary_df = visualizer.create_summary_table()
    
    # Check if summary table has expected structure
    assert 'Country' in summary_df.columns
    assert 'GHI_mean' in summary_df.columns
    print("✓ Summary table structure test passed!")

if __name__ == "__main__":
    test_visualizer_initialization()
    test_summary_table_structure()
    print("All visualization tests passed!")