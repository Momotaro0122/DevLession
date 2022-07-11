'''
CreateShaderMachine
Description:Create custom textures & shaders. 
Author: Chia Xin Lin 
Created: 18 Jun 2022
Last Updated: 25 Jun 2022 - Martin Lee
Usuage - Type in the proper input and create custom shder from it! 
'''
####
##Modules.
import maya.cmds as mc
from functools import partial

####
##Core.
class CreateShaderMachine:
    ##Instance Variables.
    Create_Arnold_Shader = partial(mc.shadingNode, 'aiStandardSurface', asShader=True)
    Create_Custom_Texture = partial(mc.shadingNode, 'file', asTexture=True)
    Create_Place2d_Texture = partial(mc.shadingNode, 'place2dTexture', asUtility=True)    
    ##__init__.
    def __init__(self, main_name="", texture_Suffix = '_CO', tex_attr = ".outColor", mshader_attr = ".baseColor"):
        ##Variables.
        self.texture_suffix_list = ('_CO', '_RG')
        self.place_2d_texture = main_name + "Place2d"
        self.main_name = main_name
        self.shader_name = self.main_name + "_SD"
        self.result_dict = {}
        self.texture_Suffix = str(texture_Suffix)
        self.tex_attr = tex_attr
        self.mshader_attr = mshader_attr
        self.main_shader = self.create_shader()
        self.create_texture = self.create_texture(self.main_name+self.texture_Suffix)
        self.place_2d_texture = self.create_place2d_texture()
        self.main_shader_info = [self.main_shader, self.main_shader+self.mshader_attr]
        self.create_texture_info = [self.create_texture, self.create_texture+self.tex_attr]
        self.data = (("main_shader",self.main_shader), ("texture", self.create_texture), ("place_2d_texture",self.place_2d_texture))
        print("init done...")

    def create_shader(self):
        """
        Try to build main shader
        """
        # self.main_shader = self.Create_Arnold_Shader(name = self.shader_name + "_SD")
        self.main_shader = CreateShaderMachine.Create_Arnold_Shader(name = self.shader_name)
        print("Create shader done...")
        return self.main_shader

    def create_texture(self, suffix):
        """
        Create custom texture.
        """
        #! self.custom_texture = self.Create_Custom_Texture(name=self.shader_name + suffix)
        # [chiaxin] Not need to save texture name here, because we will return it immedicately.
        texture = CreateShaderMachine.Create_Custom_Texture(name = suffix)
        print("Create texture done...")
        return texture

    def create_place2d_texture(self):
        """
        Create place2d texture.
        """
        place_2d_texture = self.Create_Place2d_Texture(name = self.main_name + "_Place2d")
        print("Create place2d done...")
        return place_2d_texture

    def connect_place2d_texture(self, main_shader_info, create_texture_info, place_2d_texture):
        """
        Connect place2d and others.
        """
        create_texture = create_texture_info[0] 
        create_texture_attr = create_texture_info[-1]
        main_shader_attr = main_shader_info[-1]
        mc.defaultNavigation(connectToExisting=True, source=place_2d_texture, destination=create_texture)
        mc.connectAttr(create_texture_attr, main_shader_attr)
        print("Connect done...")

    ##Run function.
    def do_it(self):
        """
        Main funtion & give the result.
        """
        self.connect_place2d_texture(self.main_shader_info, self.create_texture_info, self.place_2d_texture)
        print("Final stage done...")
        self.result_dict = {key: value for (key, value) in self.data}
        print("\n===================Start===================")
        print("\nBoom! %s have just created!!!"%(self.main_shader))
        print("\nHere are your result details...")
        for key, value in self.result_dict.items():
            print("\n%s = %s"%(key, value))
        print("\n===================End=====================")
        return self.result_dict


name = "ttt"
create_shader_machine = CreateShaderMachine(name)
shader = create_shader_machine.do_it()


