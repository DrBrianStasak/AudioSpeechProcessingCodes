# FILE MATCH GETTER - Brian Stasak 2019 v0
# This will look at a list of files and copy only these selected files over to a designated directory
# This script is useful when a directory has a large number of files and you only require specific ones

import os
import shutil
import re
                      
# Directories Needed; directory (where raw files are); directoryout (where files specific files are copied)
directory = '/YOURFILEINPUTDIRECTORY/'
directoryout = '/YOURFILEOUTPUTDIRECTORY/'

# Load text file list (contains list of specific files wanted)
file_list = open('/YOURFILEDIRECTORY/Files_Getter_List.txt')

# initialise an empty master lookup
data = []

# for each line in the files wanted; removes possible \n indicator
for line in file_list:
    line = line.strip('\n')
    print(line)
    data.append(line)
    
file_list.close()

# This should match the number copied over in the end (unless some raw files are missing from list)
length = len(data)
print(length, "Total Files in List\n")
count = 1

# Looks in directory; count shows how many files present
# This prints processed file index, iposition in directory, and file name
# iposition is where the file is located numerically in processed order (not alphabetised)

for filename in os.listdir(directory):
    for i in range(length):
        #print(data[i])
        if filename == data[i]:
            print(count, i, filename)
            count = count + 1
            iposition = str(i)
            newfilename = (directory+'/'+filename)
            destfilename = (directoryout+filename)
            #destfilename = (directoryout+iposition+'_'+filename) # use this line if directory indices order is important (re-labels)
            #print(newfilename)
            shutil.copy(newfilename,destfilename)
            
