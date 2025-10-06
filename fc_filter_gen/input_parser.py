def parse_trade_list(raw_text):
    parsed_trades = []
    lines = [line for line in raw_text.strip().splitlines() if line.strip()]
    
    # Each player block is 9 lines
    for i in range(0, len(lines), 9):
        block = lines[i:i+9]
        if len(block) < 9:
            print(f"Warning: Skipping incomplete block starting at line {i+1}.")
            continue
        name = block[0].strip()
        price_str = block[3].replace(',', '').strip()
        try:
            price = int(price_str)
            parsed_trades.append((name, price))
        except ValueError:
            print(f"Warning: Skipping block for '{name}' due to invalid price '{block[3]}'.")
    return parsed_trades