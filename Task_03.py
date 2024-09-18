import re

def check_password_complexity(password):
    strength = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'digit': False,
        'special_char': False
    }

    # Check if password length is at least 8 characters
    if len(password) >= 8:
        strength['length'] = True

    # Check for uppercase characters
    if re.search(r'[A-Z]', password):
        strength['uppercase'] = True

    # Check for lowercase characters
    if re.search(r'[a-z]', password):
        strength['lowercase'] = True

    # Check for digits
    if re.search(r'\d', password):
        strength['digit'] = True

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength['special_char'] = True

    # Determine overall strength
    criteria_met = sum(strength.values())
    
    if criteria_met == 5:
        return "Strong password!"
    elif 3 <= criteria_met < 5:
        return "Moderate password. Consider adding more complexity."
    else:
        return "Weak password. Please improve the password by including uppercase, lowercase, numbers, and special characters."

def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ")
    feedback = check_password_complexity(password)
    print("Password strength:", feedback)

if __name__ == "__main__":
    main()