#define string of input 
inputvalue ='acadgild'
#list comprehensions to save to other 
value =[a.upper() for a in inputvalue]
print(value)

input1 =['x','y','z']
value = [x*y for x in input1 for y in range(1,5)]
print(value)

input1 =['x','y','z']
value = [x*y for x in range(1,5) for y in input1]
print(value)

input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))

input_list = [2,3,4,5]
result = [[item+num for item in input_list] for num in range(0,4)]
print("[2,3,4] =>" +  str(result))

input_list =[1,2,3]
result =[(b,a) for a in input_list for b in input_list]
print("[2,3,4] =>" +  str(result))
    
