def crypt(message, shift, reverse):
    crypt_message = []

    if reverse:
        shift = -shift

    for char in message:

        if not str.isalpha(char):
            crypt_message.append(char)
        elif str.isupper(char):
            crypt_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            crypt_message.append(crypt_char)
        else:
            crypt_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            crypt_message.append(crypt_char)

    return ''.join(crypt_message)

def menu():
    print('Please choose an option below:')
    print('1. Encrypt a message')
    print('2. Decrypt a message')
    print()

def main():
    menu()
    user_choice = int(input('Please enter either a 1 or a 2: '))
    message = input('Please enter a message: ')
    shift = int(input('Please enter a shift: '))

    if user_choice == 1:
       print('The encrypted message is:', crypt(message, shift, False))
    else:
        print('The decrypted message is:', crypt(message, shift, True))

main()