alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
from art import logo
print(logo)

print("Welcome to ceasar cipher decryption !!!")

def ceaser_decryption(start_text,shift_amount,cipher_direction):
    end_text = ""
    if direction=="decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")

should_end = False
while  not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" )
    text = input("Type your message:").lower()
    shift = int(input("type the shift number:"))

    ceaser_decryption(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again .otherwise Type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
