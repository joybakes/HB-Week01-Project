from os import mkdir
from os import listdir
# create 26 directories in the current dir, one for each letter of the alphabet
# loop through files in ./original_files, organize into previously created dir
# by alpha

# Create a directory for each letter of the alphabet

currdir = listdir(".")

for name in [chr(x) for x in range(97,123) if chr(x) not in currdir]:
    mkdir(name)

