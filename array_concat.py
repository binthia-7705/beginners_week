import numpy as np

a=[1,2,3,4,5]
b=[6,7,8,9,10]

#Using + operator
join=a+b
print(join)

#Using extend() method
copy_a=a.copy()
copy_a.extend(b)
print(copy_a)

#Using append() method
copy_a1=a.copy()
copy_a1.append(b)
print(copy_a1)

#Using concatenate() method of numpy
join4=np.concatenate((np.array(a),np.array(b)))
print(join4)

#Using append() method of numpy
join5=np.append(np.array(a),np.array(b))
print(join5)
