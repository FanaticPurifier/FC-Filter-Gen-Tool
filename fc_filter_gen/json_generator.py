import json
import copy

def generate_output_json(mapped_trades, template_path, output_path, player_data_path="fc_filter_gen/player_data.json"):
    """
    mapped_trades: list of dicts with keys: full_name, id, buy_price, firstName, lastName, commonName, rating
    template_path: path to template json
    output_path: path to write output json
    player_data_path: path to player data json
    """
    with open(template_path, 'r', encoding='utf-8') as f:
        template = json.load(f)


    # Buy filters
    buy_filters = {
        'device': template['filters'].get('device', False),
        'shared': template['filters'].get('shared', {})
    }
    # Bid filters
    bid_filters = {
        'device': template['filters'].get('device', False),
        'shared': template['filters'].get('shared', {})
    }

    for trade in mapped_trades:
        key = trade['lastName'].upper() if trade['lastName'] else trade['full_name'].upper()
        example_key = next((k for k in template['filters'] if k not in ['device','shared']), None)
        example_obj = template['filters'][example_key] if example_key else {}

        # Buy filter
        buy_obj = copy.deepcopy(example_obj)
        buy_obj['playerData']['id'] = int(trade['id']) if trade['id'] else None
        buy_obj['playerData']['firstName'] = trade['firstName']
        buy_obj['playerData']['lastName'] = trade['lastName']
        buy_obj['playerData']['commonName'] = trade['commonName'] if trade['commonName'] else ""
        buy_obj['playerData']['rating'] = trade['rating']
        buy_obj['baseSetting']['buySetting']['buyPrice'] = trade['buy_price']
        buy_obj['baseSetting']['buySetting']['bidPrice'] = 0
        buy_obj['baseSetting']['buySetting']['bidItemsExpiringIn'] = 3600
        buy_obj['criteria']['maskedDefId'] = int(trade['id']) if trade['id'] else -1
        buy_obj['criteria']['maxBuy'] = trade['buy_price']
        buy_obj['criteria']['maxBid'] = 0
        buy_obj['baseSetting']['sellSetting']['sellPrice'] = []
        buy_obj['baseSetting']['sellSetting']['moveToTransferList'] = True
        buy_filters[key] = buy_obj

        # Bid filter
        bid_obj = copy.deepcopy(example_obj)
        bid_obj['playerData']['id'] = int(trade['id']) if trade['id'] else None
        bid_obj['playerData']['firstName'] = trade['firstName']
        bid_obj['playerData']['lastName'] = trade['lastName']
        bid_obj['playerData']['commonName'] = trade['commonName'] if trade['commonName'] else ""
        bid_obj['playerData']['rating'] = trade['rating']
        bid_obj['baseSetting']['buySetting']['buyPrice'] = 0
        bid_obj['baseSetting']['buySetting']['bidPrice'] = trade['buy_price']
        bid_obj['baseSetting']['buySetting']['bidItemsExpiringIn'] = 480
        bid_obj['criteria']['maskedDefId'] = int(trade['id']) if trade['id'] else -1
        bid_obj['criteria']['maxBuy'] = 0
        bid_obj['criteria']['maxBid'] = trade['buy_price']
        bid_obj['baseSetting']['sellSetting']['sellPrice'] = []
        bid_obj['baseSetting']['sellSetting']['moveToTransferList'] = True
        bid_filters[key] = bid_obj

    # Write buy filters
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({'filters': buy_filters}, f, indent=4, ensure_ascii=False)

    # Write bid filters
    bid_output_path = output_path.replace('.json', '_bid.json')
    with open(bid_output_path, 'w', encoding='utf-8') as f:
        json.dump({'filters': bid_filters}, f, indent=4, ensure_ascii=False)
