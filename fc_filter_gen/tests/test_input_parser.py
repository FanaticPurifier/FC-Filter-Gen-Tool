# We need to import the function we want to test.
from fc_filter_gen.input_parser import parse_trade_list

def test_parse_valid_and_invalid_lines():
    """
    Tests that the parser correctly processes a mix of valid, invalid,
    and empty lines.
    """
    sample_input = """
PlayerTrading Type	Current Price	Suggested at	Rec. Buy Price	Rec. Sell Price
Hemp	Fodder	9,000	05/10/25,23:21	8,800	12,750
Buhl	Fodder	6,000	05/10/25,23:21	5,800	8,200

Reiten	Fodder	12,250	05/10/25,23:21	11,750	16,000
Invalid Line With No Price
Smith	Fodder	1,000	...	9o0	1,500 
    """

    # The expected output after parsing
    expected = [
        ('Hemp', 8800),
        ('Buhl', 5800),
        ('Reiten', 11750),
    ]

    # The actual result from our function
    result = parse_trade_list(sample_input)

    # Pytest uses simple 'assert' statements for checks.
    # If the assertion is false, the test fails.
    assert result == expected