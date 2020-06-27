#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# b() - in this first function call, we tell the member variable 'a' to have effect on global variable 'a' 
#       through the use of keyword global.
#     - we assign the value returned by the function call c(a) to a, which will be 2 (0 + 2).
#     - value of a = 2.
# b() - we again call function c(a) and assign it to a which will be 4 (2 + 2).
#     - value of a = 4.
# b() - we again call function c(a) and assign it to a which will be 6 (4 + 2).
#     - value of a = 6.
# a  - the value of a is now 6 which will be the output.

# ## Question 2

# In[ ]:


#  function fileLength takes the fullname with extension as argument
def fileLength(fileName):
    
#   append fileName with aboslute path to get full path
    fullpath = "C:\\Users\\prav3\\Documents\\" + fileName
    
    try:
#       opening file in read mode 
        file = open(fullpath, 'r')
#       initializing count variable to keep track of lines 
        count = 0
#       loop
        for line in file:
            count += 1
        print(count)          
    except FileNotFoundError:
#       custom error message
        print('File '+ fileName+  ' not found.')

fileLength('currencies.txt')
fileLength('currenciessss.txt')


# ## Question 3

# In[ ]:


class Marsupial:
    items = []
    
    def __init__(self, item=None):
        self.items = item or []
    def put_in_pouch(self, item):
        self.items.append(item)
    def pouch_contents(self):
        return self.items

m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')

m.pouch_contents()


# In[ ]:


class Kangaroo(Marsupial):
    
    def __init__(self, xCoord=0, yCoord=0):
        self.x = xCoord
        self.y = yCoord
        
    def __str__(self):
        return "I am a Kangaroo located at coordinates({},{})".format(self.x,self.y)
    
    def jump(self, xCoord=0, yCoord =0):
        self.x += xCoord
        self.y += yCoord
        
k = Kangaroo(0,0)

print(k)


# In[ ]:


k.put_in_pouch('apple')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')

k.pouch_contents()


# In[ ]:


k.jump(1,0)
k.jump(1,0)
k.jump(1,0)

print(k)


# ## Question 4

# In[ ]:


class Mortgage(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        labelLoanAmount =Label(self,
                                    relief = FLAT,
                                    padx=10,
                                     pady=10,
                                    width=5,
                                    text= 'Loan Amount:')
        labelLoanAmount.grid(row=1, column=0, columnspan=4, sticky=W+E)

        entryLoanAmount= Entry(self)
        entryLoanAmount.grid(row=1, column=4, columnspan=4, sticky=W+E)


        labelInterestRate =Label(self,
                            relief = FLAT,
                            padx=15,
                            text= 'Interest Rate:')
        labelInterestRate.grid(row=2, column=0, columnspan=4, sticky=W+E)

        entryInterestRate= Entry(self)
        entryInterestRate.grid(row=2, column=4, columnspan=4, sticky=W+E)


        labelLoanTerms =Label(self,
                            relief = FLAT,
                            padx=15,
                            text= 'Loan Terms:')
        labelLoanTerms.grid(row=3, column=0, columnspan=4, sticky=W+E)

        entryLoanTerms= Entry(self)
        entryLoanTerms.grid(row=3, column=4, columnspan=4, sticky=W+E)


        buttonComputeMortage =Button(self,
                            relief = GROOVE,
                            padx=15,
                            text= 'Compute Mortgage')
        buttonComputeMortage.grid(row=4, column=0, columnspan=4, sticky=W+E)
        entryComputeMortage= Entry(self)
        entryComputeMortage.grid(row=4, column=4, columnspan=4, sticky=W+E)


# In[ ]:


class Calculator(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        
       
        entryLoanAmount= Entry(self)
        entryLoanAmount.grid(row=0, column=0, columnspan=4,pady =15, sticky=W+E)
        
        numbers = [['MC',  'M+', 'M-', 'MR'],
           ['C', '\u221A','x\u00b2','+'],
           ['7','8','9','-'],
           ['4', '5','6','*'],
           ['1','2', '3', '/'],
           ['0', '.', '+-', '=']
          ]
        for r in range(6):
            for c in range(4):
                button= Button(self,
                            relief = GROOVE,
                            padx=10,
                             pady=10,
                            width=5,
                            text= numbers[r][c])
                button.grid(row=r+1, column=c)


# In[ ]:


from tkinter import *
root = Tk()

mortgage = Mortgage(root)
mortgage.pack(side=LEFT)

calculator = Calculator(root)
calculator.pack(side=RIGHT)


root.mainloop()


# ## Question 5

# In[ ]:



    def collatez(number):
   try:
       num = abs(int(number))
           
       if num == 1:
           print(num)
           
       #x/2 if even
       elif num%2 == 0:
           print(num)
           num = int(num / 2)
           collatez(num)

       #3x+1 if odd
       else:
           print(num)
           num = int((3 * num) + 1)
           collatez(num)
    
   except ValueError:
       # Handle the exception
       print('Please enter an integer')
  
    collatez(20)

   


# ## Question 6

# In[ ]:


#this is the string that we'll display to the user
a=''

def binary(number):
    try:
#     we changing the value from inside of the function
        global a
#     changing the input to number even though user enters negative
        num = abs(int(number))
    
#     if the number is 0
        if num == 0:
#         if the supplied parm was 0, we just return it
            if not a:
                print(0)
#         if the value of a is not empty, it means user enter value > 0, 
#            so we displya the reverse of string
            else:
                print(a[::-1])
       
        else:
#           concatenate the quotient from the operation which will be in 1 & 0s, duh
            a += str(num%2)
#           floor divison
            binary(num//2)
                        
    except ValueError:
        print("please enter an integer")
        
binary(9)



# inspired by this code....
# def dec2bin(n): 110100
#     if n < 0:
#         'Must be a positive integer'
#     elif n == 0:
#         return '0'
#     else:
#         return dec2bin(n//2) + str(n%2)

# dec2bin(3)


# ## Question 7

# In[ ]:


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    recordh1 = False
    def __init__(self):
        HTMLParser.__init__(self)
        self.record = False
        self.recordName=''

    def handle_starttag(self, tag, attrs):
        if tag == 'h1' or tag=='h2' or tag=='h3' or tag=='h4' or tag=='h5' or tag=='h6':
            self.record = True
            self.recordName = tag
    def handle_endtag(self, tag):
        self.record= False

    def handle_data(self, data):
        if self.record:
            if self.recordName == 'h1':
                print (data)
            elif self.recordName == 'h2':
                print('\t{}'.format(data))
            elif self.recordName == 'h3':
                print('\t\t{}'.format(data))
            elif self.recordName == 'h4':
                print('\t\t\t{}'.format(data))
            elif self.recordName == 'h5':
                print('\t\t\t\t{}'.format(data))
            elif self.recordName == 'h6':
                print('\t\t\t\t\t{}'.format(data))
                    


# In[ ]:


fullpath = 'C:\\Users\\prav3\\Documents\\wc3.html'
content = ''
try:
#   opening file in read mode 
    infile = open(fullpath, 'r')
    content = infile.read()   
    infile.close()
except FileNotFoundError:
#   custom error message
    print('File '+ fileName+  ' not found.')

parser = MyHTMLParser()
parser.feed(content)


# ## Question 8

# In[ ]:


from urllib.request import *
from html.parser import *


def analyze(url, depth, indent):
    content = urlopen(url).read().decode()
    collector = Collector(url,depth)
    collector.feed(content)
    urls=collector.getLinks()

    print("{}{}".format(indent * ' ', url))
    for link in urls:
        if depth > 0:
            webdir(link, depth - 1, indent + + 4)
    
    return urls


# In[ ]:


from urllib.parse import urljoin
from html.parser import HTMLParser
class Collector(HTMLParser):
    
    def __init__(self, url,depth):
        HTMLParser.__init__(self)
        self.url = url
        self.depth = depth
        self.links=[]
        self.count = 0


    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute =  urljoin(self.url, attr[1])
                    if(absolute[:4] == 'http'):
                        if (self.depth > self.count):
                            self.links.append(absolute)
                            self.count = self.count + 1
           
    
    def getLinks(self):
        return self.links


# In[ ]:


visited = set()
def webdir(url, depth, indent):
    
    global visited
    visited.add(url)
    
    links =  analyze(url,depth, indent)
    
    for link in links:
        if link not in visited:
            try:
                crawl1(link,depth,indent)
            except:
                pass


webdir('https://www.w3.org/TR/html401/struct/links.html',3,1)


# ## Question 9

# In[ ]:


get_ipython().run_cell_magic('!', '', 'pip install --trusted-host pypi.org ipython-sql')


# In[ ]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[ ]:


get_ipython().run_line_magic('sql', 'sqlite://')


# In[ ]:


get_ipython().run_cell_magic('sql', '', "CREATE TABLE WEATHER(City varchar(50),Country varchar(50), Season VARCHAR(50), Temperature float, Rainfall float);\nINSERT INTO WEATHER VALUES('Mumbai','India', 'Winter', 24.8, 5.9);\nINSERT INTO WEATHER VALUES('Mumbai','India', 'Spring', 28.4, 16.2);\nINSERT INTO WEATHER VALUES('Mumbai','India', 'Summer', 27.9, 1549.4);\nINSERT INTO WEATHER VALUES('Mumbai','India', 'Fall', 27.6, 346.0);\nINSERT INTO WEATHER VALUES('London','United Kingdom', 'Winter', 4.2, 207.7);\nINSERT INTO WEATHER VALUES('London','United Kingdom', 'Spring', 8.3, 169.6);\nINSERT INTO WEATHER VALUES('London','United Kingdom', 'Summer', 15.7, 157.0);\nINSERT INTO WEATHER VALUES('London','United Kingdom', 'Fall', 10.4, 218.5);\nINSERT INTO WEATHER VALUES('Cairo','Egypt', 'Winter', 13.6, 16.5);\nINSERT INTO WEATHER VALUES('Cairo','Egypt', 'Spring', 20.7, 6.5);\nINSERT INTO WEATHER VALUES('Cairo','Egypt', 'Summer', 27.7, 0.1);\nINSERT INTO WEATHER VALUES('Cairo','Egypt', 'Fall', 22.2, 4.5);")


# ### a) All the temperature data. 
# 

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT Temperature from WEATHER;')


# ### b) All the cities, but without repetition.

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT City from WEATHER;')


# ### c) All the records for India.

# In[ ]:


get_ipython().run_cell_magic('sql', '', "SELECT  * from WEATHER WHERE Country='India';")


# ### d) All the Fall records.

# In[ ]:


get_ipython().run_cell_magic('sql', '', "SELECT  * from WEATHER WHERE Season='Fall';")


# ### e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters. 

# In[ ]:


get_ipython().run_cell_magic('sql', '', "SELECT  City, Country, Season\nfrom WEATHER \nWHERE  Rainfall > 400 AND Rainfall < 200;\nWHERE Rainfall >= '200' \nAND rainfall <= '400';\n")


# ### f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.
# 

# In[ ]:


get_ipython().run_cell_magic('sql', '', "\nSELECT  City, Country\nfrom WEATHER\nWHERE Temperature >= '20'\nORDER by Temperature ASC;")


# ### g) The total annual rainfall for Cairo. 
# 

# In[ ]:


get_ipython().run_cell_magic('sql', '', "SELECT SUM(Rainfall)\nFROM WEATHER\nWHERE City='Cairo';")


# ### h) The total rainfall for each season.
# 

# In[ ]:


get_ipython().run_cell_magic('sql', '', '\n\nSELECT Season, SUM(Rainfall)\nFROM WEATHER\nGROUP BY Season;')


# ## Question 10

# ### 10.a

# In[ ]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words = [word.upper() for word in words]
words


# ### 10.b

# In[ ]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words = [word.lower() for word in words]
words


# ### 10.c

# In[ ]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words = [len(word) for word in words]
words


# ### 10.d

# In[ ]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words = [ (word.upper(),word.lower(),len(word)) for word in words]
words


# ### 10.e

# In[ ]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words = [word for word in words if len(word) >= 4]
words

