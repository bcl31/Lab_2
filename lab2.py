# this program set was written by James Laidlaw, lab H21.
# this is a simple Caesar cipher program
# the program asks the user for the name of a text file in the same folder as the program conatining a correctly formatted message
# the program then pull the information from that folder, and uses it to decrypt the message inside
# finally, the program prints the decrypted message

def main():

    # get filename from user
    filename = get_input_file()

    # pull information from raw file and clean into usable format
    raw_message, shift = pull_from_file(filename)

    # decode the cleaned raw message
    decrypted_message = decrypt(raw_message, shift)

    # output decrypted message
    print(decrypted_message)


# prompts the user to input the name of the file they wish to be decrypted, if the file is not a valid .txt format, notifies the user and asks them
# again
def get_input_file():
    # ask the user for filename
    filename = input("Please enter the full name of the text file: ")

    # if the file is invalid, re-ask the user for filenames until it is valid
    while filename[-4:] != ".txt":
        filename = input("Invalid filename extension. Please re-enter the input filename: ")

    return filename


# filename is a string containing the full name of the file information is to be pulled from

# opens the file specified in filename, finds the decryption key and message, cleans leading and trailing whitespace from the message, then returns
# both the message and the key in message, key format
def pull_from_file(filename):
    # pull information from file
    file = open(filename, "r")
    shift = int(file.readline())
    raw_message = file.readline()
    file.close()

    # clean information into usable format
    raw_message = raw_message.strip()
    raw_message = raw_message.lower()

    return raw_message, shift


# encrypted is a string containing an encrypted message
# key is an int indicating the amount of shift each letter needs to be moved by in order to decrypt the message

# decrypts the message found in encrypted by shifting every letter in the message key entries backwards in the alphabet.
def decrypt(encrypted, key):
    # establish alphabet for reference and an empty  lkist to store the progress on the decrypted message
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = []

    # go through each character in the encrypted message, appending them to decrypted. if they are a letter, shift them by key first.
    for item in encrypted:
        if item.isalpha():
            index = alphabet.find(item)
            index -= key
            index = index % len(alphabet)
            item = alphabet[index]
        decrypted.append(item)
    decrypted = "".join(decrypted)
    return decrypted


main()
