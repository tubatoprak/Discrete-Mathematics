def prints(R, R2):  #to print one of lists
    for a, b in R:
        ths.write("({},{}) ".format(a,b))  #print result

def reflexive(R, R2): 
    for a in R2:      # to control all elements
        if [a,a] not in R:
            ths.write("Reflexive: No,({} {}) is not found ".format(a,a))  #print result
            return False	     
    ths.write("Reflexive: Yes, all elements are present. ")  #message result
    return True

def symmetric(R, R2):
    for a, b in R:      # to control all pairs in R
        if [b, a] not in R :
            ths.write("Symmetric: No,({},{}) is not found whereas ({},{}) is found ".format(b,a,a,b))  #message result
            return False
    ths.write("Symmetric: Yes,Symmetrics of each pair are found")  #message result
    return True
	
def antisymmetric(R,R2):
    for a, b in R:  # to control all pairs in R
        if [a,b] in R and [b,a] in R and a != b: 
        	ths.write("Antisymmetric: No,({},{}) is found whereas ({},{}) is found ".format(b,a,a,b)) #print result
        	return False
    ths.write("Antisymmetric: Yes,all relations consist of reflexive relations") #print result

def transitive(R, R2):
    for a in R2:    # to control all element in R2
        for b in R2: # to control all elements in R2
            if [a, b] in R: # to control all pairs in R
                for c in R2:    # to control all element in R2
                    if [b, c] in R and [a, c] not in R:   #to check if transitive
                        ths.write("Transitive: No,({},{}) is not found whereas ({},{}) and  is found ({},{}) are found ".format(a,c,a,b,b,c))
                        return False
    ths.write("Transitive: Yes,all relations consist of reflexive and there is no other relation.")   #print result                 
    return True

if __name__ == "__main__":
    ths = open("exampleoutput.txt", "w")     #to open file 
   # ths.write("ornek metin"),
    file = open("input.txt","r")   #to write file
    list_index = int(file.readline())
    satir = ''
    R1=[]              #list of pairs
    R2=[]                  #list of element
    tmp=[]
    temp = []
    boskume=[]
    while True:                           #to list the entire file
        satir = file.readline().replace(',','')     #start to line by line
        for i in range(len(satir)-1):              #to seperate element
            temp.append(satir[i])
        R2.append(temp)                 #set element in  list named R2
        temp=[]
        list_index-=1
        while list_index >= 0:       # to escape comma
	        #line by line
	        satir = file.readline()
	        boskume.append(satir[0])      
	        boskume.append(satir[2])
	        tmp.append(boskume)        
	        list_index -= 1
	        boskume=[]
	     
        list_index = file.readline()
        R1.append(tmp)                             #set pairs in list named R1
        tmp=[]
        if list_index != '\n':
	        list_index = int(list_index)
        else:
	        break
        i = 0
    for x,y in zip(R1,R2):              #to read all lists
        ths.write("n")
        ths.write("\n")
        prints(x,y)            #go to fonction to print  all pairs
        ths.write("\n")
        reflexive(x,y)      #go to reflexive function to chechk wheter reflexive list 
        ths.write("\n")
        symmetric(x,y)      #go to symmetric function to chechk wheter symmetric list 
        ths.write("\n")
        antisymmetric(x,y)  #go to antisymmetric function to chechk wheter antisymmetric list 
        ths.write("\n")
        transitive(x,y)     #go to transitive function to chechk wheter transitive list 
        ths.write("\n")
    ths.close()             #close file 

            