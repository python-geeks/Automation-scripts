# Python Program to auto-delete old docker images
"""
    Rules:
   
    1. All images with 'latest' tag would not be touched.
    2. For a particular repository, the tag with the highest number would be preserved.
    3. A provision is made to add exception images which would be never stopped.

"""

import subprocess as sp
import re
import operator, itertools

class DeleteImage:
    
    def __init__(self):
        self.imgList = []
        self.hashList = []
        

# Storing All the Docker Image Details Found on the System to a File
    def getAll(self):
        file = open("temp.txt","r+")
        file.truncate(0)
        sp.run("sudo docker image list --format '{{.Repository}}~{{.Tag}}' >> temp.txt", shell=True , capture_output=True)
        file.close()
        

#Add other exceptions here
    def isExcluded(self , tag):              
        
        reg = r"alpine|buster|slim|latest"  #Excluding all the images with Alpine, Buster, Slim & Latest Tags
        m = re.search(reg, tag)
        if m != None:
             return 0        
        return 1
    
# Loading data from the File to the Python program       
    def loadAll(self):
        f = open("temp.txt", "r")
        
        for line in f:
            line = line.rstrip("\n")
            image = line.split('~')
            if self.isExcluded(image[1]): 
                
                regex = r"^(((\d+\.)?(\d+\.)?(\*|\d+)))(\-(dev|stage|prod))*$"        
                match = re.search(regex, image[1])
                
                imgDict = { 'Repository':image[0] , 'Tag': match.group(2) }
                self.imgList.append(imgDict)      
        f.close()
        
        
    def manData(self):       
        key = operator.itemgetter('Repository')
        b = [{'Repository': x, 'Tag': [d['Tag'] for d in y]} 
        for x, y in itertools.groupby(sorted(self.imgList, key=key), key=key)]
        
        self.imgList.clear()
        self.imgList = b.copy()

        
# Sorting Tags according to the Version Numbers    
    def sortTag(self):
                
        for img in self.imgList:                
            temp = img['Tag'].copy()            
            
            for n, i in enumerate(img['Tag']):
                img['Tag'][n] = int(i.replace('.', ''))
            
            maxLen = len(str(max(abs(x) for x in img['Tag'])))            
            templateString = '{:<0' + str(maxLen) + '}'            
            finalList = []
            
            for n, i in enumerate(img['Tag']):
                finalList.append(templateString.format(i))
                
            for i in range(0 , len(img['Tag'])):
                hashMap = { 'TagsManipulated': finalList[i] , 'TagsOriginal': temp[i] }
                self.hashList.append(hashMap)
                
            finalList.sort()
                            
            img['Tag'].clear()
            img['Tag'].extend(finalList[:-1])            
        
        print(self.hashList)        
        print (self.imgList)        
        
    
    def hashFunc(self , tag):        
        for hashMap in self.hashList:
            if tag == hashMap['TagsManipulated']:
                t = hashMap['TagsOriginal']
                break
            else:
                t = 'Error in Manipulation'            
        return t
    
# Running the Docker RMI Command to Delete the Older Versions
    def removeImage(self):        
        for img in self.imgList:            
            if img['Tag']:
                for tag in img['Tag']:
                    val = self.hashFunc(tag)
                    imageURL = img['Repository'] + ":" + val
                    print ("Deleting Image : " + imageURL )
                    sp.run("sudo docker rmi " + imageURL, shell=True , capture_output=True)
            
# Main Function
if __name__ == "__main__":
    
    docker = DeleteImage()
    docker.getAll()    
    docker.loadAll()    
    docker.manData()    
    docker.sortTag()    
    docker.removeImage()