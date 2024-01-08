def custom_round(number, decimal_places):
    factor = 10 ** decimal_places
    rounded_number = int(number * factor + 0.5) / factor
    return rounded_number