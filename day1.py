
val = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    val1 = int(input())
 
    val.append(val1) # adding the element
     
print('List Before Sorting ',val)
val.sort(reverse=True)
print('List In Descending Order ',val)