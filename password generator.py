import random
import string

def generate_password(length=12, letters=True, values=True, symbols=True):

    characters = ""
    if letters:
        characters += string.ascii_letters
    if values:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("At least one character type.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def user_preferences():
    length = int(input("Enter the desired password length : "))
    letters = input("Include letters? (yes/no) : ").lower() == 'yes' 
    values = input("Include numbers? (yes/no) : ").lower() == 'yes' 
    symbols = input("Include symbols? (yes/no) : ").lower() == 'yes'
    return length, letters, values, symbols

def main():
    print("Welcome to the Password Generator!")
    length, letters, values, symbols = user_preferences()
    password = generate_password(length, letters, values, symbols)
    print(f"\nGenerated Password : {password}")

if __name__ == "__main__":
    main()