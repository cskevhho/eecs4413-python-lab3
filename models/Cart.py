@staticmethod
def validate_input(no_items: int, price: float, tax: float) -> str:
    if no_items <= 0:
        return "Number of items must be a positive integer."
    if price <= 0:
        return "Price must be a positive number."
    if tax <= 0 or tax > 100:
        return "Tax rate must be between 0 and 100"
    return None  # null


@staticmethod  # decorator indicates that this is a static method, don't need to call class.
def calculate_total(
    no_items: int, price: float, tax: float
) -> float:  # type hinting, not forced, -> float means return float
    validation_error = validate_input(no_items, price, tax)

    if validation_error != None:
        raise ValueError(validation_error)

    total = float(no_items * price * (1 + tax / 100))
    return total
