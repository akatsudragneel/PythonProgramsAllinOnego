#INSERTION SORT

array=[]

n=int(input("Enter the number of elements you want to sort: "))
print("Enter the array values one by one: ")
for i in range(0, n):
    a=int(input())
    array.append(a)

for i in range(1, len(array)):
    key = array[i] 
    j = i-1
    while j >=0 and key < array[j] : 
        array[j+1] = array[j] 
        j -= 1
    array[j+1] = key 
    print(array)
print(array)
