#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Check the Python Version
import sys
print ("WELCOME VER")
print(sys.version)


# In[5]:


#Type of 12 
type(12)


# In[6]:


#Type of 2.14 
type(2.14)


# In[7]:


# Type of "Hello, Python 101!" 
type("Hello, Python 101!")


# In[9]:


# Print the type of -1
type(-1)


# In[11]:


# Print the type of 4
type(4) 


# In[12]:


# Print the type of 0
type(0)


# In[13]:


# Print the type of 1.0
type(1.0) # Notice that 1 is an int, and 1.0 is a float


# In[14]:


#Print the type of 0.5
type(0.5)


# In[15]:


# System settings about float type
sys.float_info


# In[16]:


# Addition operation expression
43 + 60 + 16 + 41


# In[17]:


# Subtraction operation expression
50 - 60


# In[18]:


# Mathematical expression 
30 + 2 * 60


# In[21]:


# Sample List
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]


# In[25]:


# Overwrite variable with new value
x = x / 60
x


# In[26]:


# Name the variables meaningfully

total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min


# In[27]:


# Name the variables meaningfully

total_hours = total_min / 60 # Total length of albums in hours
total_hours


# In[28]:


# Complicate expression
total_hours = (43 + 42 + 57) / 60 # Total hours in a single expres sion
total_hours


# In[8]:


# Create your first tuple
tuple1 = ("disco",10,1.2 )
tuple1


# In[9]:


# Print the type of the tuple you created
type(tuple1)


# In[10]:


# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])


# In[11]:


# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))


# In[12]:


# Use negative index to get the value of the last element
tuple1[-1]


# In[13]:


# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
tuple2


# In[15]:


# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock",                            "R&B", "progressive rock", "disco")
genres_tuple


# In[16]:


# Create a list
L = ["Michael Jackson", 10.1, 1982]
L


# In[17]:


# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3] )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2] )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1] )


# In[18]:


# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L


# In[19]:


# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)


# In[21]:


# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2] 
B= A
print('A:', A)
print('B:', B)


# In[22]:


print('B[0]:', B[0]) 
A[0] = "hard rock"
print('B[0]:', B[0])


# In[23]:


# Write your code below and press Shift+Enter to execute
a_list = [1, 'hello', [1,2,3], True]
a_list


# In[24]:


# Write your code below and press Shift+Enter to execute
a_list[1]


# In[25]:


# Write your code below and press Shift+Enter to execute
a_list[1:4]


# In[41]:


# Write your code below and press Shift+Enter to execute
A=[1,'a']
B=[2,1,'d']
C=A+B
C


# In[35]:


# Question sample dictionary
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic


# In[36]:


# Write your code below and press Shift+Enter to execute
soundtrack_dic.keys() # The Keys are "The Bodyguard" and "Saturday Night Fever"


# In[37]:


# Write your code below and press Shift+Enter to execute
soundtrack_dic.values()  # The values are '1992'and '1977'


# In[47]:


# Write your code below and press Shift+Enter to execute
SetX = {'rap','house', 'electronic music', 'rap'}
print(SetX)

listY = ['rap','house', 'electronic music', 'rap']
SetY = set(listY)
print(SetY)

SetZ = set(['rap','house', 'electronic music', 'rap'])
print(SetZ)


# In[48]:


# Write your code below and press Shift+Enter to execute
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print(sum(A))
print(sum(B))


# In[49]:


# Write your code below and press Shift+Enter to execute

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
album_set3


# In[50]:


# Write your code below and press Shift+Enter to execute
album_set1.issubset(album_set3)


# In[54]:


# Condition statement example 

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


# In[55]:


# Condition statement example
album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")


# In[56]:


# Condition statement example 

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")
print('do something..')


# In[57]:


# Else statement example

age = 8
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
print("move on")


# In[58]:


# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
            print(dates[i])


# In[59]:


# Example of for loop 

for i in range(0, 8):
    print(i)


# In[61]:


# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares): 
    print(i, square)


# In[62]:


# Write your code below and press Shift+Enter to execute
for i in range(-4, 5):
    print(i)


# In[63]:


# Write your code below and press Shift+Enter to execute 
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] 
for Genre in Genres:
    print(Genre)


# In[64]:


# Write your code below and press Shift+Enter to execute
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6): 
    Rating = PlayListRatings[i]
    print(Rating)
    i=i+1


# In[68]:


#  function that divides the first input by the second input:
def divide(a,b):
    c=a/b
    return c
c=divide(10,5)
print("function that divides the first input by the second input:",c)


# In[70]:


# the con function we defined before be used to add to integers or strings?
con("python","programming")
con(2,3)

