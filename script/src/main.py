import sys
from utility import *

FUNCTIONS = {
    'generate_thumbnail' : generate_thumbnail,
    'extract_images' : extract_images,
    'extract_and_gifify' : extract_and_gifify
}

def main():
    argv = sys.argv
    if len(argv) < 4:
        print('Too little arguments were given', sys.stderr) 
        return
    func = FUNCTIONS.get(argv[1])
    func(in_filename=argv[2], out_filename=argv[3])

if __name__ == '__main__':
    try:
        main()
    except:
        print("Input file was not found")