print("hello world")


print ("hello shubham ji,\"nice to meet u\",we will meet again")#scape squiance character (\)
print("shubham varshney is great")# varshney ji ka rola hai 
#elvAish bhai ke agge koi bol sakta hai kya 
print("bhupendra jogi ")
print("hey",6,7,sep="~",end="009\n")
print (" aditya bhai ka system hai ")


a=7
b=7
print (a+b)
print("the type of a is " ,type(a))
c=complex(5,7)
d=67
print (c-d)
print("the type of c is ", type(c))
list = [6,2.3],[36,8.9],["apple","bannana"]
print(list)
tuple =("chita,lion,panchi")
print(tuple)
dict2 = {"name":"sakshi", "age":18,"talent":100}

print(2+3)
print(2-3)
print(2*3)
print(2%3)
print(2/3)
print(2//3)
print(2**4)
n=15
m=7
print("the additon of",n,"and",m,"is",22)
print("the division of ",n,"and",m,"is",2.1)
print("the exponential of ",n,"and",m,"is",15**7)
print("the modules of is",n,"and",m,"is",15%7)
print("the floor division of",n,"and",m,"is",15//7)
print("the value of ",n,"+",m,"is",n+m)
print("the value of ",n ,"%",m,"is",n%m)
print("the value of ",n ,"//",m,"is:",n//m)



a="5"
b=4
print(int(a)+b)
#implicit function
a=6.9
b=6
print(a+b)
print(a-b)





b=input()
print("hello", 89 )
x=input()
y=input()
print(float(x)+int(y))
a=input()
h=input()
print("the modules of first and secound number is",int(a)%int(h))
#we learn in leacture 10 about input and input output are in string formate so if we want an integer so we have to convert it sing the int coomand






print('hello world')
print("elvish bhai ke agge koi bol sakta  hai kya aeee elvish bhai\"thara bhai jogindar")
print('''shubham
varsheny ji
hum pe to hai hi nooo''')

print('''name kya hai
bhupendra jogi 
us me kaha kaha gaye ho
us me bhot jagah gaya hu 
name batayaa
bhupendra jogi''')

name="shubham"
print("lets use a for loop\n")
for character in name:print(character)#lopping through string 

a="shu"
print(a[1])#Accessing character for string 
#in leacture 11 we study about string 





name="shubham,aditya"
print(name[0:7])#slicing string #(we always use square bracket [])# including 0 but not 7
# print(len(name))#length of string 
# animal=("sher")
# print("sher is a king of jungle",len(animal), "and he is vegetarian sher  ")
print(len(name))
print(name[:])
print(name[:9])#pythone automatically start from 0 if we dont put 0 
print(name[0:len(name)-4])
print(name[0:-4])#pythone automatically subtract in the length and give outuput f remaning value
print(name[-2:-4])#14-2,14-4=12:10- which doest'make a sense higher to lower 
print( name[-2:-1])#14-2,14-1-12:13 this is  right 


# # rstrip 
s="shhubham,!!!!!!!! harry"
sh="!!!!!!shubham"#not 
print(s.rstrip("!"))#only strip trialling!  not leading !
print(s.upper())
print(s.lower())
print(s.replace("shubham","shubham varshney"))
print(s.split(" "))#split use for make list and space in double court(" ")
shubhamvlog=("my self Shubham varsheny i am iT branch student ")
print(shubhamvlog.capitalize())
print(len(s))
print(s.center(4))
print(len(s.center(4)))#center
print(s.count("shubham"))#pair=1
b="shubham !!!!! varshney!!!"
print(b.endswith("!!!"))#it tell about the string end with!!! or not (!)Exclamation mark sign
c="snake is python"
print(c.endswith("snake",0,5))#we can also us evariable in endswith 
print(c.endswith("python",4,6))
