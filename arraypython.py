from array import * 
a =array( "i" , [1,2,3,434,423,6]) 
# print(a.buffer_info())
# print(a.reverse())
# print(type(a) , id(a))
for i in a :
    print("the value of array at index" ,i,"is:-", i)
# print(id(3))
newa= array(a.typecode,(a*a for a in a))

for i in newa:
    print(newa)