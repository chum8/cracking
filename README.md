# cracking
Python scripts for manipulating word lists to mount password cracking campaign.

# title_maker.py
Converts words to titled words.
usage: python3 title_maker.py <file>
crevice -> Crevice

# combiner.py
usage: python3 combiner.py <file1> <file2>
Combines words from two lists.

List 1
Dog
Cat
Mouse

List 2
Slow
Fast

Result
DogSlow
DogFast
CatSlow
CatFast
MouseSlow
MouseFast

# trimmer.py
usage: python3 trimmer.py <file> <n>
Removes words greater than length n from a list.

List
fabulous
tree
heaven

Result, removing words length 6 or greater
tree
