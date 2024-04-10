def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password is too short"

    # Check complexity
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{};:'\"\\|,.<>/?`~" for char in password)

    if not (has_uppercase and has_lowercase and has_digit and has_special):
        return "Weak: Password lacks complexity"

    # Check commonality
    common_passwords = [
        "password", "123456", "qwerty", "abc123", "letmein", "admin", "welcome",
        "passw0rd", "password1", "12345678", "monkey", "1234567", "123456789",
        "iloveyou", "football", "12345", "123123", "1234567890", "password123",
        "qwerty123", "login", "admin123", "starwars", "1234", "test", "superman"
    ]
    if password.lower() in common_passwords:
        return "Weak: Commonly used password"

    return "Strong: Password meets all criteria"

# Test the function
password_input = input("Enter your password: ")
result = check_password_strength(password_input)
print(result)

