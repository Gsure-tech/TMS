def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.254

    # return f"{feet} feet and {inches} inches is equal to {meters} meters."
    return {"feet": feet, "inches": inches}
