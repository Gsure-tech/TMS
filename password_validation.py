def strength(password):
    result = []

    pass_strength = False
    if len(password) >= 8:
        pass_strength = True
    result.append(pass_strength)

    for i in password:
        password_capital = False
        if i.isupper():
            password_capital = True
    result.append(password_capital)

    for i in password:
        password_digit = False
        if i.isdigit():
            password_digit = True
    result.append(password_digit)

    if all(result):
        final_result = "Strong Password"
    else:
        final_result = "Weak Password"

    return final_result




