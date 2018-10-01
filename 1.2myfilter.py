# create data list
data =[1,2,3,4,6,7]

#define function to act like reduce 
def myfilter(functionfilter, data):
    mydata =[]
    for x in data:
        if functionfilter(x):
            mydata.append(x)
    else:
        return mydata

# function value to check the filter 
def functionfilter(x):
    return x>2

print(myfilter(functionfilter,data))