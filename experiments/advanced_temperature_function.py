def advanced_temperature_function(temperature):
    if temperature > 25:
        result = "Hot"
    if 15 >= temperature >= 25:
        result = "Warm"
    if temperature < 15:
        result = "Cold"
    return result
