#This is a python program that sorts the pens in a pouch based on the remaining ink(cm) in ascending order using bubble sort

#This function is for sorting the pens in ascending order
def bubblesort(pens):
    l=[]
    for key,value in pens.items():
        l.append([key,value])

    for i in range(len(l)):
        for j in range (0,len(l)-i-1):
            if l[j][1]>l[j+1][1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return dict(l)

#This function is for accepting the pen names along with amount of ink left
def inputing():
    pen={}
    n=int(input("Enter the no: of pens in the pouch: "))
    for i in range(n):
        key=input("Enter the pen name: ")
        value=float(input("Enter the amount of remaining ink(cm): "))
        pen[key]=value
    return pen

#This is the main program
pens=inputing()
pens_sorted=bubblesort(pens)
print("The pens in ascending order is :")
for key,value in pens_sorted.items():
    print(f"{key}: {value}")



