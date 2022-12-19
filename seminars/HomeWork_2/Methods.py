def create_list(num):
    list=[]
    for i in range(-num,num+1):
        list.append(i)
    return list

def rndm(list):
    l=len(list)-1
    for i in range(0,len(list)//2):
        list[i],list[l-i]=list[l-i],list[i]
    return list
    
def factorial(n):
    if n < 1:
        return 1
    else:
        returnNumber = n * factorial(n - 1) 
        print(returnNumber, end=" ")
        return returnNumber
