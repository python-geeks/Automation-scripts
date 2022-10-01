

file=open("text.txt") 

print(file.read())

print(file.read(6))

print(file.readline())
print(file.readline())
print(file.readline())


line=file.readline()
while(line!=""):
     print(line)
     line=file.readline()
    
print(file.readlines())
for line in file.readlines():
     print(line)

file.close()

with open("text.txt",'r') as reader:
    x=(reader.readlines())  
    print(x)
    x=x[::-1]
    print(x)
    with open("text.txt",'w') as writer:
        for line in x:
            writer.write(line)
    


