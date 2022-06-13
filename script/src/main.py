import sys
import traceback
from utility import *

FUNCTIONS = {
    'generate_thumbnail' : generate_thumbnail,
    'extract_and_gifify' : extract_and_gifify,
    'extract' : extract_certain_scene,
    'gif_composer' : gifify_certain_scene
}

def main():
    argv = sys.argv
    if len(argv) < 4:
        print('Too little arguments were given', sys.stderr) 
        return
    func = FUNCTIONS.get(argv[1], generate_thumbnail)
    func(in_filename=argv[2], out_filename=argv[3])

if __name__ == '__main__':
    try:
        main()
    except:
        sys.stderr.write(traceback.format_exc())
        exit(1)