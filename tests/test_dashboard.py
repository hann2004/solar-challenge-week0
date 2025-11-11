import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from app.utils import get_metric_units, create_summary_stats

def test_get_metric_units():
    """Test that metric units are returned correctly"""
    assert get_metric_units('GHI') == 'W/m²'
    assert get_metric_units('Tamb') == '°C'
    assert get_metric_units('WS') == 'm/s'
    assert get_metric_units('Unknown') == ''
    print("✓ Metric units test passed!")

def test_create_summary_stats():
    """Test summary statistics creation"""
    # Create sample data
    sample_data = {
        'TestCountry': pd.DataFrame({
            'GHI': [100, 200, 300],
            'Tamb': [25, 30, 35]
        })
    }
    
    summary_df = create_summary_stats(sample_data, metrics=['GHI', 'Tamb'])
    
    assert 'Country' in summary_df.columns
    assert 'GHI_mean' in summary_df.columns
    assert 'Tamb_mean' in summary_df.columns
    assert len(summary_df) == 1
    print("✓ Summary stats test passed!")

if __name__ == "__main__":
    test_get_metric_units()
    test_create_summary_stats()
    print("All dashboard tests passed!")