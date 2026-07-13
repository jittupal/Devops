import os
import sys

def count_files_with_extension(directory, extension):
    file_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_count += 1
    
    return file_count
        
count = count_files_with_extension("count_files/test1", "txt")

print(f"The number of files is {count} in the directory and sub-folder")