import properties
class FileOp:
    def writeFile(self,contents):
        
        file = open(properties.file_name,'w')
        file.write(contents)
        file.close()
    
    def readFile(self):
        
        file = open(properties.file_name,'r')
        contents = file.read()
        file.close()
        
        return contents
