import pandas as pd
import os

def test_notebook_exists():
    # Checks if EDA notebook is in the right place
    notebook_path = "notebooks/01_exploratory_data_analysis.ipynb"
    assert os.path.exists(notebook_path) == True

def test_data_column_logic():
    # A simple logic test to ensure pytest is working
    sample_data = {'date': ['2020-01-01', '2020-01-02']}
    df = pd.DataFrame(sample_data)
    assert 'date' in df.columns