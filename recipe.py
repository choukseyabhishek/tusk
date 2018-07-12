""" SECOND_CODE"""
import re
R = re.compile("PSL")
S1 = "PSLaaaaa Welcome to aaaaa.PSL persistent......"
S2 = "aaaa PSL Welcome to aaaaa.persistent......."
print("hii")
if R.match(S1):
    print("Match Found")
else:
    print("Match Not Found")
print("hello") 
print("hello world") 
