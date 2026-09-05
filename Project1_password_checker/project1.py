with open("100k-most-used-passwords-NCSC.txt", "r") as file:
    common_passwords = set(line.strip() for line in file)
while True:
    password = input("Enter your password: ")
 
    if password in common_passwords:
        strength = "Very Weak (Common password)"
        print("Password strength:", strength)
    else:

        has_digit = False
        for char in password:
            if char .isdigit():
                has_digit = True
        

        has_upper = False
        has_symbol = False
        symbols = "!@#$%^&*()-+?_=,<>/"
        for char in password:
            if char .isupper():
                has_upper = True
            if char in symbols:
                has_symbol = True
        

        score = 0 
        if len(password) >= 12:
            score += 1
        if len(password) >= 8:
            score += 1
        if has_digit:
            score += 1
        if has_upper:
            score += 1
        if has_symbol:
            score += 1

        if len(password) < 8:
            strength = "Very Weak"
        elif score == 5:
            strength = "Very Strong"
        elif score == 4:
            strength = "Strong"
        elif score == 3:
                strength = "Medium"
        elif score == 2:
            strength = "Weak"
        else:
            strength = "Very Weak"
        print("Password strength:", strength)

    again = input("Check another Password? (yes/no): ")
    if again.lower() != "yes":
        break


