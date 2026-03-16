import pytest 
from src.cleaner import parse_date, clean_row
from unittest.mock import MagicMock

# Test 1: Check if parse_date correctly handles good and bad dates
def test_parse_date():
    # Added '0' to the day (05) to match %Y-%m-%d strictly
    assert parse_date('2025-12-05') is not None
    assert parse_date('2025-12') is None
    assert parse_date('2025-13-5') is None
    
# Test 2: Check if clean_row removes rows with empty strings (nulls)
def test_null_remover():
    mock_writer = MagicMock()
    bad_row = ["John", "", "john@email.com"]
    
    result = clean_row(bad_row, mock_writer)
    assert result is None
    mock_writer.writerow.assert_called_with(bad_row)

# Test 3: Check if clean_row catches invalid dates automatically
def test_auto_date_validation():
    mock_writer = MagicMock()
    bad_date_row1 = ["John", "Doe", "john@email.com", "2024 05"]
    bad_date_row2 = ["John", "Doe", "john@email.com", "2024-05"]
    
    result1 = clean_row(bad_date_row1, mock_writer)
    result2 = clean_row(bad_date_row2, mock_writer)
    
    assert result1 is None
    assert result2 is None

    

    mock_writer.writerow.assert_called_with(bad_date_row2)
# Test 4: Check if dates are correctly standardized and rows are updated
def test_date_standardization():
    
    assert parse_date('2025/12/05') == '2025-12-05'
    assert parse_date('15-04-2024') == '2024-04-15'
    assert parse_date('05-20-2024') == '2024-05-20'

    
    mock_writer = MagicMock()
    messy_row = ["Sam", "G", "sam@test.com", "15/04/2024"]
    
    
    result = clean_row(messy_row, mock_writer, date_columns=4)
    
    
    assert result[3] == "2024-04-15"