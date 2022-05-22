import os
os.system("title Cell2Code")
a=input("path:")
with open(a) as f:
    asd=f.readlines()
    f.close
for x in range(len(asd)):
    print(asd[x].replace(":","")[:17])
input()
