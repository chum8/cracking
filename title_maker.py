import os, sys

# some default values
dft_error = "Something went wrong.  Exiting!"
dft_naming_convention = "titled_"
dft_success = "Operation completed!  Exiting."
dft_welcome = "Welcome to Title Maker, copyright (c) 2019 chum8!"

# return a new file name to write results to
def name_new_file(f_name):
    return dft_naming_convention + f_name

# get list from a file
def get_list(f_name):
    temp = []
    with open(f_name) as f:
        for line in f:
            temp.append(line.title())
    return temp

# write a list to a file, line by line
def write_file(f_name, t_list):
    with open(f_name, "w+") as f:
        for item in t_list:
            f.write(item)

# print a welcome message
def display_welcome(f_name1, f_name2):
    print(dft_welcome)
    print("Attempting to convert list from file")
    print(f_name1)
    print("and write to file")
    print(f_name2)

# print a warning
def display_warning():
    print(dft_welcome)
    print("You must specify a file name to use with this program.")
    print("i.e.")
    print("\tpython3 title_maker.py /usr/share/wordlists/somefile.txt")
    print("exiting.")

if len(sys.argv) < 2:
    display_warning()
    sys.exit()
else:
    try:
        f_name1 = sys.argv[1]
        f_name2 = name_new_file(f_name1)
        display_welcome(f_name1, f_name2)
        t_list = get_list(f_name1)
        write_file(f_name2, t_list)
        print(dft_success)
        sys.exit()
    except:
        print(dft_error)
        sys.exit()
