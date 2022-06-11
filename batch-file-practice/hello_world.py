#
# Please completed this python script just display hello, World
#
'''
hellow_world.py
Description:Practice for batch file. 
Show: None
Rig System: None
Author: Martin Lee
Created: 6 Jun 2022
Last Updated: 6 Jun 2022 - Martin Lee
Usuage - Input content for the print statement. 
'''
#Modules.
import sys

#Functions.
class Hellow:
    def __init__(self, content):        
            self.content = content

    def hellow_func(self):
        if isinstance(self.content, str):
            print("Hello, World & %s!!"%(self.content))
        else:
            print("Input type must be string...")
            return None
        

content = sys.argv[-1]
H = Hellow(str(content))
H.hellow_func()


