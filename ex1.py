from os import mkdir, listdir
from shutil import move

# create 26 directories in the current dir, one for each letter of the alphabet
# loop through files in ./original_files, organize into previously created dir
# by alpha

# Create a directory for each letter of the alphabet
[mkdir(chr(x)) for x in range(97,123) if chr(x) not in listdir(".")]


# Loop through files in original_files, Move it into the appropriate directory
[move("./original_files/"+filename,"./"+filename[0]+"/.") for filename in listdir("./original_files")]

