def check_password_strength(password):
    # Check if password meets minimum requirements

    has_length, has_upper, has_lower, has_digit, has_special = False, False, False, False, False

    special_chars = "!@#$%^&*()-_=+[]{}\\|;:'\",.<>/?"

    if len(password) > 7:
        has_length = True

    for char in password:
        
        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in special_chars:
            has_special = True

    if has_length and has_upper and has_lower and has_digit and has_special:
        return True

    else:
        return False