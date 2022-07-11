'''
    texture_finder.py
        Create custom textures & shaders. 

    Usage : 
        Search all texture the .ma file

    Author: Martin Lee

    Created: 03 July 2022

    Last Updated: 
        03 July 2022 - Martin Lee
'''
import sys
import re
import time

def count_spend_time(function_pointer):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function_pointer(*args, **kwargs)
        spend_time = time.time() - start_time
        print("Spend time : {:0.4f} sec".format(spend_time))
        return result
    return wrapper 

@count_spend_time
def find_texture(maya_file):
    '''
    [::args::]
        maya_file: string - A maya file want to parse.
    [::return::]
        list - Texture strings.
    '''
    textures = []
    with open(maya_file, 'r') as file_search:
        content = file_search.readlines()
    for line in content:
        matcher = re.match(r'^createNode file -n "(.*)";', line)
        if matcher:
            textures.append(matcher.groups()[0])
    print("Done ... \n {} texture(s) have been found.".format(len(textures)))
    return textures

if __name__ == '__main__':
    maya_file = sys.argv[1]
    results = find_texture(maya_file)
    print("\n".join(results))

