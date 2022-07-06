'''
CreateShaderMachine
Description:Create custom textures & shaders. 
Author: Martin Lee
Created: 03 July 2022
Last Updated: 03 July 2022 - Martin Lee
Usuage - Search all texture the .ma file.  
'''
##Modules.
import re
import time
##Core.
def count_spend_time(function_pointer):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function_pointer(*args, **kwargs)
        spend_time = time.time() - start_time
        print("Spend time : {} sec".format(spend_time))
        return result
    return wrapper 

@count_spend_time
def find_texture(maya_file):
    match_list = []
    with open(maya_file, 'r') as file_search:
        content = file_search.readlines()        
    for i in content:
        match = re.match(r'createNode file -n "([[a-zA-Z]*.*ViewportProxy)";', i)
        if match:
            match_list.append(match.groups()[0])
        else:
            pass
    print("\n\nSearching done....\nFind {} texture in total".format(len(match_list)))
    return match_list

maya_file = "E:\my script\my python\lession4\maya_files\guitar.ma"
result_list = find_texture(maya_file)
print(result_list)

