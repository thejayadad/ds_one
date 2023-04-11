

from array import * #bring in array

#<---------------------ARRAY's------------------------------>
#How to create an array
arr1 = array('i', [1,2,3,4,5,6]) #declare the type
arr2 = array('d', [1.6,2.5,8.5])
print(arr1)

print(arr2)

#How to insert a new value into the array
arr3 = array('i', [7,5,2,5,7])
print(arr3)
arr3.insert(5,7) #two parameters, i is the index and v is the value - Time complexity of O(1) at the end of the array
print(arr3)
arr3.insert(0,2)#insert in the beginning and - all elements move to the right - O(N) time at beginning of array
print(arr3)
arr3.insert(3,10)#insert middle of array
print(arr3)

#TRAVERSAL OPERATION
#print all items in array first to last
def traveral_array(array):
    for i in array:
        print(i)

traveral_array(arr1)

#ACCESSING VALUE IN ARRAY
def access_element(array, index): #<--Two arguments the array and index
    #if element not in array
    if index > len(array):
        print("index doesnt exist")
    else:
        print(array[index])

print("Accessing element")
access_element(arr1, 2)
access_element(arr1, 12)



#SEARCHING ITEMS IN ARRAY
arr4 = array('i', [4,5,6,7,8,8])
def search_array(array, value):
    for i in array:
        if i == value:
            return array.index(value) #<-- index comes from array model
        else:
            return f"Value {value} does not exist in this array"

print("Searching array")
print(arr4)
print(search_array(arr4, 4))