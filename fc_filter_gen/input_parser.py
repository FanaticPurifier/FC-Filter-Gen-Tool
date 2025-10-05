def parse_trade_list(raw_text):
    """
    Parses a multi-line, column-based string of player trade data.

    Args:
        raw_text (str): The raw text input copied from the web page.

    Returns:
        A list of tuples, where each tuple is (player_name, buy_price).
    """
    parsed_trades = []
    lines = raw_text.strip().splitlines()

    # We skip the header row (the first line) by slicing the list.
    for i, line in enumerate(lines[1:], 2): # Start enumeration at line 2 for logging
        if not line.strip():
            continue

        # split() with no arguments handles varying amounts of whitespace (spaces/tabs)
        parts = line.split()

        # A valid line should have at least 7 columns based on your example
        if len(parts) < 7:
            print(f"Warning: Skipping malformed line #{i}: Not enough columns.")
            continue
        
        # The player name is the first part.
        name = parts[0].strip()
        
        try:
            # The 'Rec. Buy Price' is the 5th column (index 4).
            # We must remove commas before converting to an integer.
            price_str = parts[4].replace(',', '')
            price = int(price_str)
            parsed_trades.append((name, price))
        except (ValueError, IndexError):
            print(f"Warning: Skipping line #{i} due to invalid price or format.")

    return parsed_trades

# --- Test Block ---
if __name__ == "__main__":
    sample_input = """
PlayerTrading Type	Current Price	Suggested at	Rec. Buy Price	Rec. Sell Price	Risk	Est. Profit
Hemp	Fodder	9,000	05/10/25,23:21	8,800	12,750	2.53 %	3,312
Buhl	Fodder	6,000	05/10/25,23:21	5,800	8,200	4.16 %	1,990
Reiten	Fodder	12,250	05/10/25,23:21	11,750	16,000	5.62 %	3,450
    """

    print("--- Parsing Sample Input ---")
    trades = parse_trade_list(sample_input)

    if trades:
        print("Parsed trades successfully:")
        for name, price in trades:
            print(f"  - Name: '{name}', Rec. Buy Price: {price}")
    else:
        print("No valid trades were parsed.")