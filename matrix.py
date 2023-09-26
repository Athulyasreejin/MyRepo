import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
example_matrix = []  
print("Please give the entries row-wise:")  
  
for _ in range(n):   
    r = []  
    for __ in range(m): 
        r.append(input()) 
    example_matrix.append(r)  

for _ in range(n):  
    for __ in range(m):  
        print(example_matrix[_][__], end=" ")  
    print()  

str =''
for _ in range(m):  
    for __ in range(n):  
         str = str + example_matrix[__][_]
    

i = 0
while i<=(len(str)-1) and str[i].isalnum == False:
    i += 1

result = i

stringpart1main = str[:result+1]
stringpart2main = str[result+1:]

i = len(stringpart2main) - 1
while i>=0 and stringpart2main[i].isalnum() == False:
    i -= 1

result = i

stringpart1 = stringpart2main[:result+1]
stringpart2 = stringpart2main[result+1:]

s = re.sub('[^0-9a-zA-Z]+', ' ', stringpart1)

Finalstring = stringpart1main + s + stringpart2
print(Finalstring)