from maya import cmds
import pymel.core as pm
#clear history.
#pm.scriptEditorInfo(clearHistory=True)
def search_poly_count(return_long_name = False, return_tri = False):
    sel = cmds.ls(sl=True, l=True)
    #variables.
    poly_count_dict = {}

    if len(sel) == 0:
        sel = cmds.ls(typ="mesh", l=True)
        #total.
        total_poly_count = cmds.polyEvaluate(sel, f=True)
        #each.
        print("\n=============Result================\n")
        for each in sel:
            if return_tri == True:
                each_poly_count = cmds.polyEvaluate(each, f=True, t=True)
                poly_count_dict[each] = each_poly_count["face"]
                short_name = each.split("|")[-1]
                print("---------start bar----------\n")
                if return_long_name == False:        
                    print("Geo name : %s\n"%(short_name))
                else:
                    print("Full Geo name : %s\n"%(each))
                print("Poly face count : %s"%(each_poly_count["face"]))
                if each_poly_count["triangle"] > 0:
                    print("There are triangles in this mesh....\nPoly Triangle Count : %s"%(each_poly_count["triangle"]))
                else:
                    print("There is no triangles in this mesh...")
                print("---------end bar----------\n")
            else:
                each_poly_count = cmds.polyEvaluate(each, f=True)
                poly_count_dict[each] = each_poly_count
                short_name = each.split("|")[-1]
                print("---------start bar----------\n")
                if return_long_name == False:        
                    print("Geo name : %s\n"%(short_name))
                else:
                    print("Full Geo name : %s\n"%(each))
                print("Poly face count : %s"%(each_poly_count))
                print("---------end bar----------\n")   
        print("There are %s poly counts in total."%(total_poly_count))    

    elif len(sel) == 1:
        if return_tri == True:
            polyCount = cmds.polyEvaluate(sel[0], f=True, t=True)
            print("\n=============Result================\n")
            print("---------start bar----------\n")
            short_name = sel[0].split("|")[-1]
            if return_long_name == False:          
                print("Geo name : %s\n"%(short_name))
            else:
                print("Full Geo name : %s\n"%(sel[0]))
            print("Poly face count : %s"%(polyCount["face"]))
            if polyCount["triangle"] > 0:
                print("There are triangles in this mesh....\nPoly Triangle Count : %s"%(polyCount["triangle"]))
            else:
                print("There is no triangles in this mesh...")
            print("---------end bar----------\n")
        else: 
            polyCount = cmds.polyEvaluate(sel[0], f=True)
            print("\n=============Result================\n")
            print("---------start bar----------\n")
            short_name = sel[0].split("|")[-1]
            if return_long_name == False:          
                print("Geo name : %s\n"%(short_name))
            else:
                print("Full Geo name : %s\n"%(sel[0]))
            print("Poly face count : %s"%(polyCount))
            print("---------end bar----------\n")

    else:
        if return_tri == True:
            #total.
            total_poly_count = cmds.polyEvaluate(sel, f=True)
            #each.
            print("\n=============Result================\n")
            for each in sel:
                each_poly_count = cmds.polyEvaluate(each, f=True, t=True)
                poly_count_dict[each] = each_poly_count["face"]
                short_name = each.split("|")[-1]
                print("---------start bar----------\n")        
                if return_long_name == False:  
                    print("Geo name : %s\n"%(short_name))
                else:
                    print("Full Geo name : %s\n"%(each))
                print("Poly face count : %s"%(each_poly_count["face"]))
                if each_poly_count["triangle"] > 0:
                    print("There are triangles in this mesh....\nPoly Triangle Count : %s"%(each_poly_count["triangle"]))
                else:
                    print("There is no triangles in this mesh...")
            print("---------end bar----------\n")
        else:
            #total.
            total_poly_count = cmds.polyEvaluate(sel, f=True)
            #each.
            print("\n=============Result================\n")
            for each in sel:
                each_poly_count = cmds.polyEvaluate(each, f=True)
                poly_count_dict[each] = each_poly_count
                short_name = each.split("|")[-1]
                print("---------start bar----------\n")        
                if return_long_name == False:  
                    print("Geo name : %s\n"%(short_name))
                else:
                    print("Full Geo name : %s\n"%(each))
                print("Poly face count : %s"%(each_poly_count))
                print("---------end bar----------\n")  
        print("There are %s poly counts in total."%(total_poly_count))    

    return poly_count_dict
search_poly_count(return_long_name = True, return_tri = True)
