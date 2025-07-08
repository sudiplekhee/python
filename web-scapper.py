land_units = {
    # Terai system
    "bigha": 72900,
    "katha": 3645,
    "dhur": 182.25,

    # Hill system
    "ropani": 5476,
    "aana": 342.25,
    "paisa": 85.56,
    "daam": 21.39,

    # Standard units
    "sqft": 1,
    "sqm": 10.7639  # 1 m² = 10.7639 ft²
}

def convert_land_area(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in land_units or to_unit not in land_units:
        return "Invalid unit"

    # Convert from source to square feet
    sqft = value * land_units[from_unit]

    # Convert from square feet to target unit
    result = sqft / land_units[to_unit]
    return result

# Example Usage
value = float(input("Enter land area value: "))
from_unit = input("From unit (e.g. katha, ropani, sqm): ").strip()
to_unit = input("To unit (e.g. sqft, dhur, aana): ").strip()

output = convert_land_area(value, from_unit, to_unit)
print(f"{value} {from_unit} = {output:.4f} {to_unit}")
