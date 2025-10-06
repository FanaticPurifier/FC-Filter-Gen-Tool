# We need to import the function we want to test.
from fc_filter_gen.input_parser import parse_trade_list

def test_parse_valid_input():
    """
    Tests that the parser correctly processes a mix of valid, invalid,
    and empty lines.
    """
    sample_input = """
Lavelle
Add to Portfolio
Promo Trading
52,000 
05/10/25,22:21
45,500
52,000
3.21 %
3,900
Stanway
Add to Portfolio
Promo Trading
18,250 
05/10/25,22:21
16,000
18,250
3.28 %
1,337 
    """

    # The expected output after parsing
    expected = [
        ('Lavelle', 52000),
        ('Stanway', 18250),
    ]

    # The actual result from our function
    result = parse_trade_list(sample_input)

    # Pytest uses simple 'assert' statements for checks.
    # If the assertion is false, the test fails.

    assert result == expected

def test_incomplete_block():
    sample_input = """
Lavelle
Add to Portfolio
Promo Trading
52,000
05/10/25,22:21
45,500
"""  # Only 6 lines, should be skipped
    result = parse_trade_list(sample_input)
    assert result == []

def test_invalid_price():
    sample_input = """
Lavelle
Add to Portfolio
Promo Trading
not_a_number
05/10/25,22:21
45,500
52,000
3.21 %
3,900
"""
    result = parse_trade_list(sample_input)
    assert result == []

def test_empty_input():
    sample_input = """
    """
    result = parse_trade_list(sample_input)
    assert result == []

def test_extra_whitespace():
    sample_input = """
  Lavelle  
Add to Portfolio
Promo Trading
  52,000   
05/10/25,22:21
45,500
52,000
3.21 %
3,900
  Stanway
Add to Portfolio
Promo Trading
18,250
05/10/25,22:21
16,000
18,250
3.28 %
1,337
    """
    expected = [
        ('Lavelle', 52000),
        ('Stanway', 18250),
    ]
    result = parse_trade_list(sample_input)
    assert result == expected

def test_parse_and_map_trades():
    from fc_filter_gen.input_parser import parse_and_map_trades
    from fc_filter_gen.data_mapper import DataMapper
    import tempfile, os

    # Create a temporary player_id_mapping.csv
    csv_content = "Name,ID\nLavelle,101\nStanway,102\n"
    fd, path = tempfile.mkstemp(suffix='.csv')
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(csv_content)
    data_mapper = DataMapper(path)

    sample_input = """
Lavelle
Add to Portfolio
Promo Trading
52,000
05/10/25,22:21
45,500
52,000
3.21 %
3,900
Stanway
Add to Portfolio
Promo Trading
18,250
05/10/25,22:21
16,000
18,250
3.28 %
1,337
    """
    expected = [
        ('Lavelle', '101', 52000),
        ('Stanway', '102', 18250),
    ]
    result = parse_and_map_trades(sample_input, data_mapper)
    assert result == expected
    os.remove(path)