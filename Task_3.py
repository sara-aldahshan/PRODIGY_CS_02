def PassChecker(password):
    strength = 0
    feedback = []

    # Check for minimum length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append('Password must be at least 8 characters.')

    # Check for uppercase letters
    if any(letter.isupper() for letter in password):
        strength += 1
    else:
        feedback.append('Password must contain uppercase letters.')

    # Check for lowercase letters
    if any(letter.islower() for letter in password):
        strength += 1
    else:
        feedback.append('Password must contain lowercase letters.')

    # Check for digits
    if any(letter.isdigit() for letter in password):
        strength += 1
    else:
        feedback.append('Password must contain numbers.')

    # Check for special characters
    if any(not letter.isalnum() for letter in password):
        strength += 1
    else:
        feedback.append('Password must contain special characters.')

    # Determine password strength
    if strength == 5:
        result = "Strong"
        feedback.append("Accepted. Your password is strong!")
    elif strength == 4:
        result = "Medium"
        feedback.append("Make it stronger. Your password is medium!")
    else:
        result = "Weak"
        feedback.append("Make it stronger. Your password is weak!")

    return result, feedback


password = input("Enter your password: ")
strength, feedback = PassChecker(password)
print("Password Strength: " + strength)
print("=============================")
for line in feedback:
    print(line)
