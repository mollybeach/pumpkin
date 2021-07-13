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


#we dont need to put student.py because it automatically gets .py 
#make sure in same directory
from student import Student
class Person(Student):
    pass #too avoid error 
p1 = Person()
print(p1.name) #inherits every single thing 

#Python Shell 
#Python Interpretor or the Python Shell
# python shell is automatically installed whenever you install python on your computer 
#IDLE Shell 
#small enviroment python shell is just a small enviroment where i can easily test some code 

#in the python shell: 
print('hope you are enjoying this tutorial ')
name = 'Tim'
print(name)
#you can also print the name without even writing print it automatically prints it out 
#>>> name 
#'Tim'
#>>>
#thats just when your testing out in your shell you cannot use on main editor

for letter in 'Tim':
	print(letter)

	
T
i
m


 class Person();'''

'''
#Building a Simple Login and SIgn Up System with Python

#how to build basic python program thats getting user input and if statement 
print('create account now')

username = input('Create new username :')
password = input('Create new password : ')
print('Your account has been created successfully please enter your credentials again to login ')
print('Login now here: \n')

username2 = input('Enter username : ')
password2 = input('Enter password : ')

if username == username2 and password == password2:
    print('Logged in successfully')
else: 
    print('Login failed')


#Modules 
#Modules in Python
# Modules basically allow get the fucntion class or everything present in another file it allows you to implement it 
#and use those same funtions in a file or project 
#very very versatile very widely used in Python everybody uses modules 

### in mondule .py
###def say_hi():
#### print(say_hi)

import module_ex

module_ex.say_hi()

#now module_ex is starting as a modue for my file 
#module or libray 
#modules are hosted online 
#looking for module specific task


#implement PIP

#pip used to install external modules from the web to your local PC 
#go online search for moduels 
#lets go to pypi lets install django-deep-seralizer 0.1.3
#pip install django-deep-serializer
'''
#Django is a Python Web Framework 
#concepts you need to start building your own projects using Django
#With Django  
#web applications with django without westing any time lets get straight to the video
#intro install
#url routing and django apps 
#django template languge 
#sending data to template file 
#building a word coutner in django
#get post in django
#static files in django
#introduction to django mdoels
#django admin panel and manipulation
#user registration in django
#user login and logout iout in django
#dynamic roating in django
#postfresql setup

#now you can see that we have django installede for each django project you 
# want to have some particlar packages just for only that your project is stored in so 
#its just like a mini envorment wehre you can access everything 
#just for your project not for your entire computer 
#i also have a different django version just for a specific reason for each proejct 
#what we need to do is create a virtual ennvirment 
#it's like a little box where everything your project is stored in it's just like a mini envorment where you
#can access everything 


#you need to install a virtual enviroment on your computer 
#use the one that i recommend
#is Anaconda 
#but for this simple tutoral lets use a simplier one 
#called Virtual env wrapper 
#pip install virtualenvwrapper 
#mac have to type pip3 
#windows just pip 
'''

Create virtual environments for python with conda


How to set up a virtual environments using conda for the Anaconda Python distribution
A virtual environment is a named, isolated, working copy of Python that that maintains its own files, directories, and paths so that you can work with specific versions of libraries or Python itself without affecting other Python projects. Virtual environmets make it easy to cleanly separate different projects and avoid problems with different dependencies and version requiremetns across components. The conda command is the preferred interface for managing intstallations and virtual environments with the Anaconda Python distribution. If you have a vanilla Python installation or other Python distribution see virtualenv

Outline
Check conda is installed and available
Update conda if necessary
Create a virtual environment
Activate a virtual environment
Install additional python packages
Deactivate a virtual environment
Delete a virtual environment
Jargon

link to PATH,

Requirements
Anaconda Python distribution installed and accessible
1. Check conda is installed and in your PATH
Open a terminal client.
Enter conda -V into the terminal command line and press enter.
If conda is installed you should see somehting like the following.
$ conda -V
conda 3.7.0
2. Check conda is up to date
In the terminal client enter
conda update conda


Upadate any packages if necessary by typing y to proceed.
3. Create a virtual environment for your project

In the terminal client enter the following where yourenvname is the name you want to call your environment, and replace x.x with the Python version you wish to use. (To see a list of available python versions first, type conda search "^python$" and press enter.)


conda create -n yourenvname python=x.x anaconda



Press y to proceed. This will install the Python version and all the associated anaconda packaged libraries at “path_to_your_anaconda_location/anaconda/envs/yourenvname”


4. Activate your virtual environment.
To activate or switch into your virtual environment, simply type the following where yourenvname is the name you gave to your environement at creation.


source activate yourenvname


Activating a conda environment modifies the PATH and shell variables to point to the specific isolated Python set-up you created. The command prompt will change to indicate which conda environemnt you are currently in by prepending (yourenvname). To see a list of all your environments, use the command conda info -e.
5. Install additional Python packages to a virtual environment.
To install additional packages only to your virtual environment, enter the following command where yourenvname is the name of your environemnt, and [package] is the name of the package you wish to install. Failure to specify “-n yourenvname” will install the package to the root Python installation.
conda install -n yourenvname [package]
6. Deactivate your virtual environment.
To end a session in the current environment, enter the following. There is no need to specify the envname - which ever is currently active will be deactivated, and the PATH and shell variables will be returned to normal.
source deactivate
6. Delete a no longer needed virtual environment
To delete a conda environment, enter the following, where yourenvname is the name of the environment you wish to delete.
conda remove -n yourenvname -all
Related info
The conda offical documentation can be found here.

@cammerschooner

eResearch cookbook - 2 minute recipes for scientists
eResearch cookbook - 2 minute recipes for scientists
your-email@domain.com
 jekyll
 jekyllrb
A template for capturing task recipes for repeatable scientific practices in a consistent format and hosted in a centralised online repository
'''

# $ conda create -n yourenvname python=x.x anaconda
#  $ conda activate p_virtual_env
# (base) mollybeach@Mollys-MacBook-Air ~ % conda activate p_virtual_env
# (p_virtual_env) mollybeach@Mollys-MacBook-Air ~ % pip install django                      (install everything you need in new project including python version )
# (p_virtual_env) mollybeach@Mollys-MacBook-Air 2018 % cd zigzag                              (change to the wanted directed as u can see on the left it still remains in the virtual enviroment
# (p_virtual_env) mollybeach@Mollys-MacBook-Air zigzag % django-admin startproject myapp      (make sure to include the app/project you want after startproject space appname
# open your project in vscode (directory in vs code)
#you will see that theres manage.py already there leave it alone and also init asgi 
# settings install apps 
# url 
# #wsgi 
# manage


#to deactivate our project all we ha e to do is type conda deactivate in terminal
# conda deactivate --> no longer in virtual enviroment 

#now open terminal from inside vscode from inside project file 
#now to activate virtual enviroment there all you have to do is type 

# (base) mollybeach@Mollys-MacBook-Air myapp % source activate p_virtual_env
#(p_virtual_env) mollybeach@Mollys-MacBook-Air myapp % 


#URL Routing and Django App

# The root directory of the Django project is the being in the directory that includes the manage.py file 

#create an app thats when we use manage.py 
#----> in terminal in vscode
#python 

#use the right intrepetator in vs code to get django errors to go away in vs code 
#https://hruthiktechtips.wordpress.com/2021/02/19/report-missing-module-source/


'''
in urls.py : 
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index')

in app.py : 

from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1> hey, Welcome </h1>')
    
    
    '''
#then we're going to run our project in terminal $ python manage.py runserver 
# after $python manage.py migrating to apply migration 
# the text : 'hey welcome ' was seen on localhost server : http://127.0.0.1:8000/

#IF NOT WORKING
#from django.urls import path, include <- add this to line 17
# #if local host isnt open and is stuck on the django template and isn't showing hey welcome 
#path('', include('myapp.urls) #if local host isnt opening add this line here 



#we want to add more 
#configure django to see our html files 
# in our root directory (where manage.py is s sibling ) we are going to create a folder called templates 
#in that folder we are going to store all our html files 
#we need to tell django where our templates folder is 
#so we go into settings.py scroll down to TEMPLETES = 'DIRS' : [BASE_DIR, 'templates']
#now django knows where to look for html files 
#create new html file in #templates folder 
# go to view.py 
#change def index(request):
#   return HttpResponse('<h1> hey, Welcome </h1>')
#to 
# def index(request): 
#return render(request, 'index.html') 

#just quit and reload the server 
# working properly 
#current html is static 
#dynamic data 
# set a variable 
# name = 'John
''' 
    name = 'Patrick'
    return render(request, 'index.html', {'name': name})  #this , curly brace after index html 
    #is like a dictionary send variable to html file 
    #in html file change <p>Welcome , John/p>
    #to 
    # <p>Welcome , {{name}}/p>
    # now thisPatrick is coming from the backend 
    can also have something like 

    name = user.name 

    #return HttpResponse('<h1> hey, Welcome </h1>')
    name = 'Patrick'
    return render(request, 'index.html', {'name': name})  #this , curly brace after index html 
    #is like a dictionary send variable to html file 
    #in html file change <p>Welcome , John/p>
    #to <p>Welcome , {{name}}/p>
    can also have user.name='Patrick'

    
    '''

#after restarting the server it works again 
#building a word counter in django

#create form in html
#see that when u submit it is sent to the url 

#create another URL to counter 
#create another URL to send the data to so go to urls.py

#go to urlpatterns = []
# add another path 
#path('counter', views.counter, name='counter')
# path('counter', views.counter, name='counter') #at the moment we dont have any function called 
#view.counter so lets go create that so go into the views.py 

#in views .py underneath the def index(request ) return blah blah 
#create new function 
#def counter(request):
#   return render(request,'counter.html')
#and go into templates and create new html file 
#counter .html
#then in the form method of the index.html <form method='' action='counter'
# in view.py in new function  words = request.GET['words']
#setting new vairables setting request .get 
#we are setting it to .GET['words] because that is the name we gave the particular text area 
#in views.py: 
#def counter(request):
#   words = request.GET['words']
#   amount_of_words = len(words.split())
#   return render(request, 'counter.html', {'amount' : amount_of_words})
# in counter.html 
#The amount of words is {{amount}}
# it's working even tho .GET and .split weren't highlighting correctly that due to the intpretator guess should ignore
#working properly 
#http://127.0.0.1:8000/counter?words=hi+my+name+is+molly+
# says The amount of words is 5
#what if we want the url to not be so lengthy what if we want it to just be /counter 
#talk about that more in the next part 

# get requests vs post request  in django 
#the reason it is so lengthly is because in the <form method='' the type of method 
#we left blank there's only two possible types GET and POST  
#the GET method is when we are not passing not safe infomation or personal information 
#because it is going to show in the URL 
#but if we use post method more safe prevents attacks 
#if i put method = '' or dont put method='' in form it automatically uses a get method 
#now change to POST
#it says Forbidden because post is more safe 
#CSRF verification failed Cross Size Request Forgery it's like an attack 
#CSRF token prevents attack 
#so we need to add a CSRF token in Django for it to work 
#  <form method="POST" action='counter'> 
#       {% csrf_token %}
#</form>
# very easy we just have to add this 
#errror still coming up MultiValueDictKeyError at /counter
#we're getting this error because right in view.py  you'll see ->  words = request.GET['words']
# when we need .POST
#now it is working the URL is clear 

#Static Files in Django 
#any external file in 
#CSS image we have tell where 
#create new folder called static 
#put in settings.py
#import os  gets a specific operating system 


#go down to underneath STATIC_URL = '/static'

#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#and then in static create style.css
#then we link stylesheet at top of html file 
#  <link rel="stylesheet" type="text/css" href="../static/styles.css">
#the video said it wasnt working but it is for me he said to do it like :

#  <link rel="stylesheet" type="text/css" href='{% static 'style.css' %}'>
#after changing it to this i got an error it said 
#TemplateSyntaxError at /
#Invalid block tag on line 8: 'static'. Did you forget to register or load this tag?
#load it by : adding this to the top of the html file  {% load static %}
#{% load static %}
#<!DOCTYPE html>
#<html lang="en">


#now it working 

#free html temple 


#bootstrap made 
#get free html file move it into templates from one page 
# and also move the assests into the static file too 


#introduction  to Django Models Models get data base SQL
#model view SQL not single 
# model database 
# view templete 
# instead of using SQL we use classes in python to view our databse 
#classes and inhereitence 


#go to Models.py
# create  Models.py it i didnt see it 

'''write this : 
from django.db import models 

#create your models here 

class Feature:
    id : int 
    name : str
    details : str  
    '''
#and then in views 

'''def index(request):
    

    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our Service is Very Quicky '
    
    return render(request, 'index.html', {'feature': feature1}) 
    '''
#<link href="{% static "assets/vendor/aos/aos.css" %}"  rel="stylesheet"  >
#<img src="{% static "assets/img/about-video.jpg" %}" class="img-fluid" alt="">
# after changing all the href and src in index.html to static then 
#on line 101 in index.html add : 
#  <h4 class="title"><a href="">{{feature.name}}</a></h4> 
# then restart the server and it should say 
# fast in one of the cards 

# and it does congrats 

#reloaded the page and it works for the rest 



