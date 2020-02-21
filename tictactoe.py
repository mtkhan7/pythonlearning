# Activty 4 - grid for nots and crosses

space1 = "x"
space2 = "o"
space3 = ""
space4 = "o"
space5 = "x"
space6 = "o"
space7 = "x"
space8 = ""
space9 = ""

print("    |    |    ")
print("  {} |  {} |  {} ".format(space1, space2, space3))
print("    |    |    ")
print("--------------")
print("    |    |    ")
print("  {} |  {} |  {} ".format(space4, space5, space6))
print("    |    |    ")
print("--------------")
print("    |    |    ")
print("  {} |  {}  | {}  ".format(space7, space8, space9))
print("    |    |    ")

if(space1 == "x" and space2 =="x" and space3 =="x"): 
    print("crosses win")
elif(space1 =="o" and space2 =="o" and space3=="o"):
    print("nots win")
else:
    print("try again")

