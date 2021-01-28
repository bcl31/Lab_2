# this program set was written by James Laidlaw, lab H21.
# this is a simple Caesar cipher program
# TODO add more description

def get_input_file():
    raw_name = input("Please enter the full name of the text file: \n")
    if raw_name[-4:] == ".txt":
        return raw_name
    else:
        print("Error, the entered name is not a valid .txt format file")
        return get_input_file()


get_input_file()
