import json
import unicodedata

def strip_accents(text):
    if not isinstance(text, str):
        return text
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

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

def load_player_data(player_data_path="fc_filter_gen/player_data.json"):
    with open(player_data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def robust_player_match(name, data_mapper, player_data_list):
    name_norm = strip_accents(name).lower()
    # Try DataMapper first
    matches = data_mapper.search_by_name(name)
    if matches:
        return matches[0]
    # Try player_data.json fields
    for pdata in player_data_list:
        for field in ['name', 'firstName', 'lastName', 'commonName']:
            field_value = pdata.get(field, '')
            field_norm = strip_accents(str(field_value)).lower()
            if name_norm in field_norm:
                # Return the original, accented version from player_data.json
                return {
                    'Name': pdata.get('name', None),
                    'ID': str(pdata.get('id', None)),
                    'firstName': pdata.get('firstName', None),
                    'lastName': pdata.get('lastName', None),
                    'commonName': pdata.get('commonName', ""),
                    'rating': pdata.get('rating', None)
                }
    return None

def parse_and_map_trades(raw_text, data_mapper, player_data_path="fc_filter_gen/player_data.json"):
    """
    Parses the input and robustly maps each name to its full name, ID, and extra fields using DataMapper and player_data.json.
    Returns a list of dicts: {full_name, id, buy_price, firstName, lastName, commonName, rating}
    """
    parsed_trades = parse_trade_list(raw_text)
    player_data_list = load_player_data(player_data_path)
    player_data_by_id = {str(p['id']): p for p in player_data_list}
    mapped_trades = []
    for name, buy_price in parsed_trades:
        match = robust_player_match(name, data_mapper, player_data_list)
        if match:
            full_name = match.get('Name', name)
            player_id = match.get('ID', None)
            pdata = player_data_by_id.get(str(player_id), match)
            mapped_trades.append({
                'full_name': full_name,  # always accented from mapping/data
                'id': player_id,
                'buy_price': buy_price,
                'firstName': pdata.get('firstName', None),
                'lastName': pdata.get('lastName', None),
                'commonName': pdata.get('commonName', ""),
                'rating': pdata.get('rating', None)
            })
        else:
            mapped_trades.append({
                'full_name': name,
                'id': None,
                'buy_price': buy_price,
                'firstName': None,
                'lastName': None,
                'commonName': "",
                'rating': None
            })
    return mapped_trades