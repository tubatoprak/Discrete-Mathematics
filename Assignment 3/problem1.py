
def reflexive(R, R2):
    for a in R2:
        if [a,a] not in R:
            return False
        R.remove([a,a])	     
    return True

def symmetric(R, R2):
    for a, b in R:
        if [b, a] not in R :
            return False
    return True

def prints(R, R2):
    for a, b in R:
        ths.write("({},{}) ".format(a,b))

def antisymmetric(R,R2):
    for a, b in R:
        if [a,b] in R and [b,a] in R and a != b:
        	return False
    return True

def transitive(R, R2):
    for a in R2:
        for b in R2:
            if [a, b] in R:
                for c in R2:
                    if [b, c] in R and [a, c] not in R:
                        return False                 
    return True
if __name__ == "__main__":
    ths = open("exampleoutput.txt", "w")
   # ths.write("ornek metin"),
    file = open("input.txt","r")
    list_index = int(file.readline())
    satir = ''
    R1=[]
    R2=[]
    tmp=[]
    temp = []
    boskume=[]
    while True:
        satir = file.readline().replace(',','')
        for i in range(len(satir)-1):
            temp.append(satir[i])
        R2.append(temp)
        temp=[]
        list_index-=1
        while list_index >= 0:
	        #line by line
	        satir = file.readline()
	        boskume.append(satir[0])
	        boskume.append(satir[2])
	        tmp.append(boskume)        
	        list_index -= 1
	        boskume=[]
	     
        list_index = file.readline()
        R1.append(tmp)
        tmp=[]
        if list_index != '\n':
	        list_index = int(list_index)
        else:
	        break
        i = 0
        deneme = []
    for x,y in zip(R1,R2):
        ths.write("n")
        ths.write("\n")
        if True == reflexive(x,y):
            if True == antisymmetric(x,y):
                if True == transitive(x,y):
                    ths.write("POSET: ")
                else :
                    ths.write("NOT POSET: ")
            else :
                ths.write("NOT POSET: ")
        else :
            ths.write("NOT POSET : ")       
        prints(x,y)   
        ths.write("\n")
        reflexive(x,y)
        #print(R1)
    ths.close()

            