#[Medium] Improve the password strength checker

def check_password(password):
    if len(password) < 8:
        return "Weak"
    return "Strong"