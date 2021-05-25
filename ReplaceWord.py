from colorama import *
init()

inp = input("Enter file name with extention : ")
while(1):
    try :
        fin=open(inp,'rt')
        oldword = input("Enter old word  : ")
        newword = input("Enter new word : ")
        data =fin.read()
        data = data.replace(oldword , newword)
        fin.close()
        fin=open(inp,'wt')
        fin.write(data)
        fin.close()
        print (Back.GREEN+'\nDone !')
    except :
    	print (Back.RED+' File not found !')
    	break
