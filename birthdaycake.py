

def birthday_cake(candle_list):
    if not isinstance(candle_list, list):
        return 0

    if len(candle_list) == 0:
        return 0
    max_height = max(candle_list)
    amount = candle_list.count(max_height)
    return amount  