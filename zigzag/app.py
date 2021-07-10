'''
#variables
name = input('Input You Name: ' )
age = int(input('Input Your Age: '))
print('Your name is ' + name + 'and you are ' + age + 'years old')

#input 
from math import * # from math import everything 
num = sqrt(2) #so we can use the sqrt

#methods
bin(334)

#replace
sentence = input('Enter your sentence: ')
print('Your sentence is ' + sentence)
word1 = input('Enter the word to replace: ')
word2 = input('Enter the word to replace it with: ')
print(sentence.replace(word1, word2))

#lists
countries = ['United Kingdom', 'Ghana', 'Nigeria', 'Australia', 'New Zealand']
print(countries[1:]) #from index one to the end
print(countries[1:4]) #from start up until but not including end
countries[0] = 'United States'
countries[3] = 'Canada'
print(countries[-2]) #negative from the back 
print(len(countries))
print(type(countries[2]))

#list methods 
list1 = [1, 2, 3, 4, 5]
list2= ['banana', 'apples',  'mango', 'orange', 'cherry']
list1.extend(list2) #join 1 with 2
print(list1)
list2.append('blueberry') #append adds to the end of the list 
print(list2)
list2.insert(1, 'pineapple') # insert pineapple string at index 1
print(list2)
list2.remove('banana') #removes banana string in list 2 
print(list2)
list2.clear() #empties the list just going to be empty list 
print(list2.index('mango')) #finds index of mango
print(list2.count('mango')) #find how many times mango appears in the list 
list3 = [4, 3, 5, 1, 2] 
list3.sort() #sort list in accesending order 
print(list3) 
list3.reverse() #reverse the list 
print(list3) #print order in reverse 
list4 = list3.copy() #makes a copy of list 3 and assigns it to the variable list 4 
print(list4) 
list4.pop() #remove the last value of the list now only has 4 values 
del list2[0] #deletes the first index from list another way of deleting an item in a list
del list2 #deletes the entire list not the same as clear it now does not exist 

#tuples

#used to store mutiples items in a variable very simialar to lists but there are some basic differences 
#tuples are immutable you cant change any value in a tuple
three_numbers = (1, 2, 3) #when we write a tuple we use number bracket not square bracket 
print(three_numbers)
print(three_numbers[0]) #prints1
three_numbers[1] = 23 #this will run an error because tuples does not support it thats the basic difference between a list and a tuple
#tuples allow repeatition repeat of the same value (1,2,3,1) 
print(len(three_numbers)) #gives length
#and you can do type 
#and you can use various data types 

#tuple constructor 
tup = tuple((1, 'Home', True, 3, 1))
string = ('home','land', 'earth')
boo = (True, False, True)
print(tup) #(1, 'Home', True, 3, 1) prints normally for the constructor 
#you want to use tuples when you have a value you don't want to change 

#functions 
#code that preform a particular task
#indentation is very important one indentation is 4 spaces 
#back space is out of the function 
def greetings(name):
    print('Welcome user ' +name)
greetings('Molly') #have to call the function outside of the function
#we can also pass in other data type for ex number 
#greetings(34) #TypeError: can only concatenate str (not 'int') to str
#convert int to a string str(name)
def greetings1(name):
    print('Welcome user ' +str(name))
greetings1(34)
#multiple parameters 
def greetings2(name, name2):
    print('Welcome user ' + name +' and ' + name2)
greetings2('Molly', 'Alisha')
#if we have an unknown amount of parameters that will be input 
def greetings3(*names):
    print('Welcome ' + names)
greetings3('David', 'Molly', 'Maggie', 'Alisha') #TypeError: can only concatenate str (not 'tuple') to str

def greetings4(*names):
    print('Welcome ' + names[1])
greetings4('David', 'Molly', 'Maggie', 'Alisha') #prints the 1st index 

def welcome(name, age):
    print('Welcome' +name+ '.you are ' + str(age)+' years old')
welcome('John', 27) #this is the same 
welcome(name ='John', age = 27) #as calling it like this 
def welcome_input (name, age):
    print('Welcome' +name+ '.you are ' + str(age)+' years old')
name = input('Enter your name : ')
age = input('Enter your age : ') 
welcome_input(name, age)

#return statement 
#just used to get a response from the task being executed in a function 

def add_numbers(num1, num2):
    return num1+num2
num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number: '))
print(add_numbers(num1, num2)) #this concationates it 8020 we need to put int(input())


#if statements
#just gives python a condition 
a = 2
b = 3
if a > b: 
    print(str(a + 'is greater than ' + b))
if a == b:
    print('a = b')
#string
c= 'lol'
d = 'lol'
if c == d: 
    print('a is equals to b')
e = True
if e != True:
    print('a is True')

f= 4
g = 3
if f>=g:
    print('f equals g')
elif f == 4:
    print('f equals 4')
elif f == 4 and g > 3 :
    print('f is 4 and greater than 3 ')
elif f == 4 or g< 3 :
    print('f is 4 or g is 3 one of these conditions is true ')
else: 
    print('g not equals f')
value = input('Input a value : ' )
if type(value) == str: 
    print(value +' is a stinrg ')
elif type(value) == int:
    print(value +' is a  int')
elif type(value) == list:  
    print(value +' is a list ')
    print('We dont know the data type' )
#dictionary 
#key value pair
#changable
#no duplicates 

dict= {
    'key1': ['hellow', 'how', 'are'],
    'key2': 2,
    'key3': 3,
}

print(dict['key1'][2])
#while loop
i = 1
while i < 6 or i==6:
    print(i)
    i+=1

#for loop
list = ['abc', 'def', 'hij']

for item in list:
    #print(item)
    if item =='def':
        break
    print(item)


#loop through range of numbers
for x in range(10):
    print(x)
else:
    print('finished looping ')

#2D list Nested Loop

my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for item in my_list:
    for row in item:
        print(row)

#comments single line 
#''' ''' multi line

#building a basic calculaor 

def add_numbers(num1, num2, op):
    if op=='+':
        return  'The addition is', num1+num2
    elif op=='-':
        return 'The subtraction is',  num1-num2
    elif op=='*':
        return  'The multiplication is' , num1*num2
    elif op=='/':
        return 'The division is',  abs(num1/num2)
    else:
        return 'not an operator'
    #return num1+num2
num1 = int(input('Enter first number : ' ))
num2 = int(input('Enter second number: ' ))
op = input('Enter operator:  ' )

print(add_numbers(num1, num2, op))


#try except
#exception here except value error 


try: 
    x = int(input('Input an interger :' ))
    print(x)
except:
    print('something went wrong please enter an integer' )


#value error
try: 
    x = int(input('Input an interger :' ))
    print(x)
except ValueError:
    print('Value not an integer' )
else: print('nothing went wrong')

#finally
try: 
    x = int(input('Input an interger :' ))
    print(x)
except ValueError:
    print('Value not an integer' )
finally: print('try except finished went wrong')

#reading files
#if its in the same folder you write it like this :open('message.txt', 'r') #read file
open('message.txt', 'r') #read file
open('message.txt', 'w') #write file
open('message.txt', 'a') #append add to the end of the file 
open('message.txt', 'r+w') #reading and writing

#if we open the file we should close the file

#message_file = open('message.txt', 'r') #relative path 
message_file = open('/Users/mollybeach/Documents/code/2018/zigzag/message.txt', 'r') #absolute path root path 
def execute():
    #print(message_file.readable()) #check if file is readable going to return a boolean value true or false 
    #print(message_file.readline()) #prints a line 
    # print(message_file.readline()) #post same method again print second line from the txt file 
    #print(message_file.readlines()) #prints all lines in a list 
    #print(message_file.readlines()[0]) #print the first line 
    #interesting when i put 270 and 271 both uncommented it: IndexError list index out of range
    #return message_file.readline()
#for loop in reading files     
    for line in message_file.readlines():
        print(line)
execute()


message_file.close() #close file 

#writing files 

#message_file = open('message.txt', 'w') #open file 
#message_file.write('This is the new text') #write file 
#it ruins everything because it over wrote 

#but if we create a new file in the absolute path 
#message_file = open('/Users/mollybeach/Documents/code/2018/zigzag/docs/new_message.txt', 'w')  #absolute path 
#message_file.write('hello u r ') #write into new file 
#message_file.close() #close file 

#creating new file with the relative path
message_file = open('new_relative_message.txt', 'w') #open  & write file 
message_file.write('hello u r ') #write into new file 
message_file.close() #close file 

#append file

message_file = open('new_relative_message.txt', 'a') #open & append file 
message_file.write('\n inserted a new line') #write into new file 
message_file.close() #close file 

#writing to another python file 

message_file = open('new_app.py', 'w') #write /create new python  file 
message_file.write('print(\'this is a new file\')')#write into new python file we have to use the backslash to write code 
message_file.close() #close file 

when you enter the path of a  python file in terminal it prints the contents : 
mollybeach@Mollys-MacBook-Air zigzag % /opt/homebrew/bin/python3 /Users/mollybeach/Documents/code/2018/zigzag/new_app.py
this is a new file
mollybeach@Mollys-MacBook-Air zigzag % 



#classes and objects
#python object oriented 
#feature python
#classes is a constructor of objects various objects 
class Myclass:
    x = 5
p1 = Myclass() #if we want to intialize an object to our class so we go like this 
print(p1.x)

#init function allows us to intilizate different values in our class 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 87)#if we want to intialize an object to our class so we go like this 
print(p1.name)
print(p1.age) 

#input classes 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
name = input('Enter your name : ')
age = input('Enter your age : ')
p1 = Person(name, age)#if we want to intialize an object to our class so we go like this 
print(p1.name)
print(p1.age) 

#delete 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 13)
del p1.age 
print(p1.name) #will still work
print(p1.age) #wont work

#del pl 
#print(p1) 


#pass
#if we're creating a class and we dont know what to put in it for now 
#we can use something called pass 
#it allows us to by pass any error 
class Person:
    pass


p1 = Person('John', 13)
del p1.age 
print(p1.name) #will still work
print(p1.age) #wont work
'''

#we dont need to put student.py because it automatically gets .py 
#make sure in same directory
from student import Student
class Person(Student):
    pass #too avoid error 
p1 = Person()
print(p1.name) #inherits every single thing 