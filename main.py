import math

MIN_PASSWORD_LENGTH=8
"""calculate the strength of the password"""
def get_password_strength(p_score):
    if p_score <= 2:
        return "Weak"
    elif 3 <= p_score <= 4:
        return "Medium"
    elif p_score >= 5:
        return "Strong"

"""check each quality of the password"""
def check_length(pass_word):
    return len(pass_word) >= MIN_PASSWORD_LENGTH

def check_uppercase(pass_word):
    return any(char.isupper() for char in pass_word)

def check_lowercase(pass_word):
    return any(char.islower() for char in pass_word)

def check_numbers(pass_word):
    return any(char.isdigit() for char in pass_word)

def check_symbols(pass_word):
    return any(not char.isalnum() and not char.isspace() for char in pass_word)

"""check each score of the password"""
def calculate_strength(pass_word):
    score = 0
    if check_length(pass_word):
        score += 1
    if check_uppercase(pass_word):
        score += 1
    if check_lowercase(pass_word):
        score += 1
    if check_numbers(pass_word):
        score += 1
    if check_symbols(pass_word):
        score += 1
    return score

"""generate the suggestions for passwords"""
def generate_suggestions(pass_word):
    suggestions = []
    if not check_length(pass_word):
        suggestions.append("-Increase password length")
    if not check_uppercase(pass_word):
        suggestions.append("-Add uppercase")
    if not check_lowercase(pass_word):
        suggestions.append("-Add lowercase")
    if not check_numbers(pass_word):
        suggestions.append("-Add numbers")
    if not check_symbols(pass_word):
        suggestions.append("-Add symbols")
    return suggestions

def check_common_password(pass_word):
    password=pass_word.lower()
    with open("common_passwords.txt", "r") as file:
        common_password = [line.lower().strip() for line in file.readlines()]
        return password in common_password
def calculate_entropy(pass_word):
    length=len(pass_word)
    charset=0
    if check_uppercase(pass_word):
        charset+=26
    if check_lowercase(pass_word):
        charset+=26
    if check_numbers(pass_word):
        charset+=10
    if check_symbols(pass_word):
        charset+=32
    if charset==0:
        charset=1
    entropy=length*math.log2(charset)
    return entropy
def entropy_rating(entropy_score):
    if entropy_score<28:
        return "Very Weak"
    elif 28<=entropy_score<=35:
        return "Weak"
    elif 36<=entropy_score<=59:
        return "Reasonable"
    elif 60<=entropy_score<=127:
        return "Strong"
    else:
        return "Very Strong"

def estimate_crack_time(entropy_score):
    guesses_per_second = 1_000_000_000
    crack_time=2**entropy_score/guesses_per_second
    return crack_time




"""Main function"""
def main():
    user_password = input("Enter password: ")

    while len(user_password.strip()) < 1:
        print("Password cannot be empty.")
        print("Please enter a valid password.")
        user_password = input("Enter password: ")
    print("""========================
PASSWORD ANALYSIS REPORT
========================
        """)
    if check_common_password(user_password):
        print("Warning!!:   Password is common!")

    final_score = calculate_strength(user_password)
    entropy_score=calculate_entropy(user_password)
    crack_time=estimate_crack_time(entropy_score)
    print(f"Password Score : {final_score}/5")
    print(f"Strength       : {get_password_strength(final_score)}")
    print(f"Entropy Score  : {entropy_score:.2f} bits")
    print(f"Entropy Rating : {entropy_rating(entropy_score)}")

    suggestions = generate_suggestions(user_password)
    if suggestions:
        print()
        print("Suggestions:")
        for suggestion in suggestions:
            print(suggestion)
    else:
        print()
        print("""Excellent password.
No suggestions needed.""")
    print("========================")
if __name__ == "__main__":
    main()



