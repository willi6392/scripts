#------------------------------------------------------------------------------------------------#
#
#   Syntax for replace() method
#       str.replace(old, new[, max])
#  
#   Parameters
#       old − This is old substring to be replaced.
#
#       new − This is new substring, which would replace old substring.
#   
#       max − If this optional argument max is given, only the first count occurrences are replaced.
#------------------------------------------------------------------------------------------------#

# Code example
text1 = """This xxx a string example....cool!"""
text2 = "this xxx xxx the second string example. If the optional argument max is given, only the first count occurrences are replaced....Very Cool!!!"

# This replaceing everything
print(text1.replace("xxx", "is"))

# This is a optional argument that, only the first count occurrences are replaced
print(text2.replace("xxx", "is", 1)) 