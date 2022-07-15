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
class Hellow():
    def __init__(self):
        #self.content = content
        pass

    def run(self):
        """
            This method's responsibility is check out argument and call self.hellow_func
        """
        args = sys.argv[:]
        if len(args) > 1:
            first_argument = args[1]
            self.hellow_func(first_argument)

    def hellow_func(self, content):
        if isinstance(content, str):
            # Original code :
            # print("Hello, World & %s!!"%(self.content))
            # Fixed :
            # You can use old string pattern format,
            # But in convention, added space in left and right side of "%" is more better.
            # And if depended argument not over than 1, Not need add parentheses.
            print("Hello, World & %s!!" % content)
            # Or
            print("Hello, World {}!!".format(content))
            # Python 3 new string format capture feature :
            print(f"Hello, World {content}")
        else:
            print("Input type must be string...")
            # return None
            # In this case is execute failed, I recommand return empty string better than None.
            # Because you not defined return value if successful.
            # When we call this method, 
            # the better way is tell caller the function is successful or failed after call.
            return ""
        # If successful, return content!
        return content

if __name__ == '__main__':
    # Because sys.argv could be get in class's method, so not need get it from outside!
    # content = sys.argv[-1]
    # In convention, the local variable is lower-case name.
    h = Hellow()
    #H.hellow_func()
    h.run()


