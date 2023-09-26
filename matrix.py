# n = int(input("Enter the number of rows: "))
import re

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         odd_num = (i-1)*i + (j*2 - 1)
#         print(odd_num, end=" ")
#     print()

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
example_matrix = []  
print("Please give the entries row-wise:")  
  
# For user input  
for _ in range(n):  # This for loop is to arrange rows  
    r = []  
    for __ in range(m):  # This for loop is to arrange columns  
        r.append(input()) 
    example_matrix.append(r)  

  
# Printing the matrix given by user  
for _ in range(n):  
    for __ in range(m):  
        print(example_matrix[_][__], end=" ")  
    print()  

str =''
for _ in range(m):  
    for __ in range(n):  
         str = str + example_matrix[__][_]
         #print(str)

#print(str)

i = 0
while str[i].isalnum() == False:
    i += 1

result = i - 1

stringpart1main = str[:result+1]
stringpart2main = str[result+1:]



i = len(stringpart2main) - 1
while stringpart2main[i].isalnum() == False:
    i -= 1

result = i


stringpart1 = stringpart2main[:result+1]
stringpart2 = stringpart2main[result+1:]



# for element in range(0, len(str)):
#     print(str[element])

# filter(str.isalnum, str)
# clean_string = filter(lambda x: x.isalnum(), str)
# clean_string = "".join(clean_string)

# print(clean_string)

s = re.sub('[^0-9a-zA-Z]+', ' ', stringpart1)


Finalstring = stringpart1main + s + stringpart2
print(Finalstring)