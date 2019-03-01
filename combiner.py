import os, sys

# some default values
dft_error = "Something went wrong.  Exiting!"
dft_success = "Operation completed!  Exiting."
dft_name_word = "Combined_"
dft_welcome = "Welcome to Combiner word list tool, copyright (c) 2019 chum8!"
dft_pct_stop = 100

# get list from a file
def get_list(f_name):
    temp = []
    with open(f_name) as f:
        for line in f:
            temp.append(line)
    return temp

# write a list to a file, line by line
def write_file(f_name, t_list):
    with open(f_name, "w+") as f:
        for item in t_list:
            f.write(item)

def combine(t_list1, t_list2, f_name):
    with open(dft_name_word + f_name, "w+") as f:
        pct100 = len(t_list1)
        i = 1
        p = 0
        for item1 in t_list1:
            if (i / pct100) * 100 == dft_pct_stop:
                p += dft_pct_stop
                i = 1
                c = input(str(p) + "% complete.  Continue? (yN)")
                if c != 'y':
                    sys.exit()
                    break
            for item2 in t_list2:
                f.write(item1.rstrip()+item2.rstrip()+'\n')
            i = i + 1

# print a welcome message
def display_welcome(f_name1, f_name2):
    print(dft_welcome)
    print("Attempting to combine wordlist from file")
    print(f_name1)
    print("with wordlist from file")
    print(f_name2)

# print a warning
def display_warning():
    print(dft_welcome)
    print("You must specify exactly two file names to use with this program.")
    print("i.e.")
    print("\tpython3 combiner.py /usr/share/wordlists/firstfile.txt /usr/share/wordlists/secondfile.txt")
    print("exiting.")

if len(sys.argv) < 3:
    display_warning()
    sys.exit()
else:
    if 1 == 1: #try:
        f_name1 = sys.argv[1]
        f_name2 = sys.argv[2]
        display_welcome(f_name1, f_name2)
        t_list1 = get_list(f_name1)
        t_list2 = get_list(f_name2)
        t_list_final = combine(t_list1, t_list2, f_name2)
        print(dft_success)
        sys.exit()
    else: #except:
        print(dft_error)
        sys.exit()
