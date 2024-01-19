Q1
for i in range(1,11):
    print(i)
using while loop
program 1: Print first 10 natural numbers
i = 1
while i <= 10:
    print(i)
    i += 1


row = 5
for i in range( 1,row +1):
    print(i)
    for j in range( 1,i + 1):
        print(j, end=' ')
        print("")

Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Q3
# 
start=25
end=50
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if(num % i)==0:
                break
    else:
        print(num)

Q4
for i in range(2,21,2):
    print(i)




# Q5
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if(i>500):
        break
    elif(i>150):
        continue
    elif(i%5==0):
     print(i)


# # Q6
list1 = "shubham"
# reverse list
a = reversed(list1)
# iterate reversed list
for i in a:
    print(i)


# Q7
for i in range(-10,-2):
    print(i)


Q8
for i in range(5):
    print(i)
print("done!")    



Q9

n = 5
p=int(input("eneter the number"))
print(p)
for i in range(2,p+1):
    n=n+i
print("the sum is :",n)




Q10
fruit_list = ["Apple", "Banana"]

print(f' {fruit_list}')

new_fruit ="orange"

fruit_list.append(new_fruit)

print(f'Updated Fruits List {fruit_list}')





s=["APPELE , BANANA"]
print(f'{s}')
b="orange"
s.append(b)
print(f'{s}')
