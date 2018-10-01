# Show data with functools
from functools import reduce

# create data list
data =[1,2,3,4,6,7]

#define function to act like reduce 
def myreduce(data):
    mydata =1
    for x in data:
        mydata =mydata*x
    else:
        return mydata

# print final value as out put        
print(myreduce(data))

# function for calculation
myfuction =lambda x,y:x*y

# in-build reduce funtion use 
reduce(myfuction,data)

