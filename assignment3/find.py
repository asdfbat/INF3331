import sys
import os

def find_files(name, path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if name in filename:
                print dirpath + "/" + filename

find_files(sys.argv[1], sys.argv[2])
