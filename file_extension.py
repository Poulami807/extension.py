

fname=input("Input the file name: ")
dict={'C':'C','cpp':'C++','py':'python','java':'java'}
for i in range(0,len(fname)):
     if fname[i]=='.':
         extension=fname[i+1:]
         break
     
print("The extension of the file is: ",dict[extension])
         
    