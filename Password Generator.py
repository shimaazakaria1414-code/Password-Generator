import random
import string

def get_password_length():

    length=int(input("\nEnter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
        return
    
    return length


def get_user_choices():
    num_choice =input("\nDo you want numbers in your password (Y/N)?").upper()
    sym_choice = input("\nDo you want symbols in your password (Y/N)?").upper() 
    return num_choice,sym_choice


def build_character_pool(length,num_choice,sym_choice):

    generated_password = []
    
    num = string.digits
    char_up = string.ascii_uppercase
    char_low = string.ascii_lowercase
    symbol = string.punctuation

    password= char_up+ char_low
    
    if num_choice == "Y":
        password += num
        generated_password.append(random.choice(num))

    if sym_choice == "Y":
        password += symbol
        generated_password.append(random.choice(symbol))

    while len(generated_password) < length:
        generated_password.append(random.choice(password))

    return generated_password
  

def generate_password(generated_password):

    random.shuffle(generated_password)
    print("\nGenerated Password:", "".join(generated_password))


def main():

    length= get_password_length()

    if length is None:
        return

    num_choice,sym_choice=get_user_choices()
    generated_password = build_character_pool(
        length,
        num_choice,
        sym_choice)

    generate_password(generated_password)
    

if __name__ == "__main__":
    main()
