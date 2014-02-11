from os import mkdir
from os import listdir
from shutil import move

# create 26 directories in the current dir, one for each letter of the alphabet
# loop through files in ./original_files, organize into previously created dir
# by alpha

# Create a directory for each letter of the alphabet

currdir = listdir(".")

for name in [chr(x) for x in range(97,123) if chr(x) not in currdir]:
    mkdir(name)

original_files = listdir("./original_files")

# Loop through files in original_files
for filename in original_files:
# Move it into the appropriate directory
    move("./original_files/"+filename,"./"+filename[0]+"/.")