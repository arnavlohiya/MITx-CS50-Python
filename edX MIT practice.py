#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s=str(input("Enter the string"))
L=len(s)
a=0
count=0


while a<L:
    if (s[a]=="a"):
        count+=1
    elif (s[a]=="e"):
        count+=1
    elif (s[a]=="i"):
        count+=1
    elif (s[a]=="o"):
        count+=1
    elif (s[a]=="u"):
        count+=1
    a+=1
print(count)
print(L)


# In[ ]:


s='myname'
if (s[1] in ['a','e','i','o','u']):
    print('hello')
else: print('none')


# In[ ]:


import numpy as np
print(np.arange(5))


# In[ ]:


happy= int(input("Enter your integer:"))
if happy>2:
    print('hello world')


# In[ ]:


sq=int(input('Enter number:'))
a=0
num=sq
while sq!=0:
    a+=num
    sq-=1
print(a)


# In[ ]:


for l in 'arnav lohiya':
    print(l)


# In[ ]:


str1='hello'
print('llo' in str1)


# In[ ]:


str1[1:12]


# In[ ]:


end=2
count=0
for num in range(end+1):
    count+=num
    end=0
print(count)
print(end)


# In[ ]:


a=str(input('enter:'))
print(a)


# In[ ]:


a=1341294845234
if str(345) in str(a):print('yes')
else: print('no')


# In[ ]:


low=0
high=100
mid=(low+high)/2
numguesses=0
print("Please think of a number between 0 and 100!")
while mid<100:
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    a=input('Is your secret number '+str(int(mid))+'?')
    
    if a=="h":
        high=int(mid)
        mid=(high+low)/2
    elif a=="l":
        low=int(mid)
        mid=(high+low)/2
    elif a=="c":
        answer=str(mid)
        print("Game over. Your secret number was: "+answer)
        break
    else: print("Sorry, I did not understand your input.")



# In[ ]:





# In[ ]:


a=str(50)


# In[ ]:


print(a)


# In[ ]:


def is_even(i):
    print("hello")
    return i%2==0


# In[ ]:


print(is_even(98))


# In[ ]:


x=18
def f(x):
    x=x+100
    print(x)
f(13)


# In[ ]:


a=a+1
print(a)


# In[ ]:


def h(x):
    a='avd'
    x=x+1
    x+1+32
    return x
print(h(2))


# In[ ]:


h(x)


# In[ ]:


s=' ARNAV LaIA!!'
t="arnav lohiya!!!"
s.capitalize()


# In[ ]:


s.isupper()


# In[ ]:


t.islower()


# In[ ]:


t.find("yash")


# In[ ]:


4%6


# In[ ]:


def gcdRecur(a,b):
    gcd=''
    if a==0:
        gcd=b
        return gcd
    elif b==0:
        gcd=a
        return gcd
    #elif a==b:
        #return a
    
    if a>b:
        factor=b
    else: 
        factor=a
        
    remainder= a%b
    a= gcdRecur(remainder,factor)
    print(gcd)


# In[ ]:


print("start")
gcdRecur(9,12)


# In[ ]:


s="Arnav"
s[1]


# In[ ]:


"a"<"b"


# In[ ]:


5/2


# In[ ]:


def isIn(char, aStr):
    length= len(aStr)
    low=0
    high= length
    mid=(high+low)//2
    
    if length==0:
        return False
    elif char== aStr[mid]:
        return True
    elif length==1: 
        return False
    elif char<aStr[mid]:
        return isIn(char, aStr[:mid])
    elif char>aStr[mid]:
        return isIn(char, aStr[mid:])
        
    


# In[ ]:


print(isIn("x",""))


# In[ ]:


#Banking code, introduction to computer science MIT course; problem set 2.
month=0
balance=3329
annualInterestRate=0.20
monthlyInterestRate=annualInterestRate/12
monthlyPaymentRate=0.04

while month<12:
    rem_balance= (balance-305)*(1+monthlyInterestRate)
    month+=1
    balance=rem_balance
print("Remaining balance:",round(rem_balance,2))


# In[ ]:


# question 2, problem set 2
month=0
balance=301
k=0
b=balance
annualInterestRate=0.2
monthlyInterestRate=annualInterestRate/12
while k<b:
    month=0
    while month<12:
        rem_balance=(balance-k)*(1+monthlyInterestRate)
        month+=1
        balance=rem_balance
    if rem_balance<=0:
        print(k)
        break
    else: 
        k+=10
        
    
print('working')


# In[ ]:


#####not this one

#k=1
balance=3329
high=balance
low=0
mid=(high+low)/2
annualInterestRate=0.20
monthlyInterestRate=annualInterestRate/12

def remBalanceAfter12Months(x): # x has the value of fixed amount to be payed
    month=0
    balance=3329
    while month<12:
        rem_balance=(balance-x)*(1+monthlyInterestRate)
        month+=1
        balance=round(rem_balance,2)
    return rem_balance

a=0
while a<high:
    if remBalanceAfter12Months(a)==0:
        print(remBalanceAfter12Months(123))
    else:
        a+=0.001

    
print("working")


# In[ ]:


print('h')


# In[ ]:


balance=3329

bal=balance
annualInterestRate= 0.2
monthlyInterest=annualInterestRate/12
monthlyInterestRate=monthlyInterest+1
for fixed_payment in range(0,bal,10):
    balance=bal
    for month in range(1,13):
        rem_balance= (balance-fixed_payment)*round(monthlyInterestRate,3)
        balance=rem_balance
        print(balance,fixed_payment,month)
    
    if round(balance,2)<0:
        print(balance)
        print("Lowest Payment",fixed_payment)
        break
    
print('working')


# In[ ]:


#given:
balance=320000
bal=balance
annualInterestRate=0.2
##
monthlyInterestRate=(annualInterestRate/12) +1
low=balance/12
high=(balance*(monthlyInterestRate**12))/12.0
mid=(high+low)/2


while mid<bal:
    balance=bal
    balance_two=bal
    for a in range(1,13):
        rem_balance=(balance-mid)*monthlyInterestRate
        rem_balance_two=(balance_two-(mid-0.01))*monthlyInterestRate
        balance=rem_balance
        balance_two=rem_balance_two
        
    
    if balance>0:
        low=mid
        mid=(high+low)/2
    elif (balance<=0 and balance_two<=0):
        high=mid
        mid=(high+low)/2
    elif (balance<=0 and balance_two>0):
        print("Lowest Payment:", round(mid,2))
        break
    else:
        print("no value found, sorry")


# In[ ]:


low=0
high=100
mid=(low+high)/2
numguesses=0
print("Please think of a number between 0 and 100!")
while mid<100:
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    a=input('Is your secret number '+str(int(mid))+'?')
    
    if a=="h":
        high=int(mid)
        mid=(high+low)/2
    elif a=="l":
        low=int(mid)
        mid=(high+low)/2
    elif a=="c":
        answer=str(mid)
        print("Game over. Your secret number was: "+answer)
        break
    else: print("Sorry, I did not understand your input.")



# In[ ]:


print('hi')


# In[ ]:


print("asd")
print('as')


# In[ ]:


tup=(1,2,3,"arnav","lohiya")
num=()
words=()

for x in tup:
    if x%1==0:
        num+=(x,)
    else:
        words+=(x,)
    print(num)
print(words)


# In[ ]:


new=[10,20,30]
for a in new:
    k=0
    while k<len(new):
        a+=a
        new[k]=a
print(new)
print('working')


# In[1]:


print('hello')


# In[2]:


lis=[0,10,20,30,4]
lis.sort


# In[3]:


lis.remove(30)


# In[20]:


b=['x','y','z','a']
b.sort()
b


# In[28]:


b.reverse()
b.sort()
b


# In[24]:





# In[65]:


listA=[100,0,1,4,7]
listA.extend([4, 1, 6, 3, 4])


# In[66]:


listA.count(4)


# In[67]:


listA


# In[68]:


listA.index(1)


# In[69]:


listA.pop(4)


# In[87]:


listA


# In[88]:


listA.reverse()
listA


# In[89]:


listA.sort(reverse=True)


# In[90]:


print(listA)


# In[1]:


a=[2,2,3,4]
b=a
a==b


# In[2]:


a is b


# In[3]:


a is not b


# In[7]:


a=[1,2,3]
b=a
a==b


# In[8]:


cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
        dList.append(num)
cList == dList


# In[10]:


print(cList)


# In[33]:


print(dList)
dList[0::2]


# In[12]:


cList is dList


# In[14]:


type(dList)


# In[16]:


abs(-2)


# In[32]:


a=[]
for elem in map(min,[1,2,-4,-1,2,-3],[10,203,102,-90,9123,-1212]):
    print(elem)
    a.append(elem)
print(a)


# In[22]:


3/2


# In[47]:


animals={'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
'c' in animals


# In[44]:


del(animals['b'])


# In[45]:


animals


# In[49]:


len(animals.values())


# In[50]:


animals


# In[55]:


animals.key('baboon')


# In[59]:


import string
string.ascii_lowercase


# In[1]:


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    a=''
    for letters in secretWord:
        if letters in lettersGuessed:
            a=a+letters
        else:
            a=a+ ' _'
    return a



secretWord='arnav'
lettersGuessed=[]
def hangman(secretWord):
    import string
    
    global availableLetters
    availableLetters= string.ascii_lowercase
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+ ' letters long')
    print('-----------')
    guesses_left=8
    while guesses_left>0:
        print('You have '+str(guesses_left)+' guesses left')
        print('Available letters: '+str(availableLetters))
        guess_word= input('Please guess a letter: ')
        
        if guess_word in lettersGuessed:
            print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord,lettersGuessed))
        elif guess_word in secretWord:
            lettersGuessed.append(guess_word)
            print('Good guess: '+ getGuessedWord(secretWord,lettersGuessed))
        
        elif guess_word not in secretWord:
            print('Oops! That letter is not in my word: '+getGuessedWord(secretWord,lettersGuessed))
            guesses_left-=1
        if isWordGuessed(secretWord,lettersGuessed):
            print('-----------')
            print('Congratulations, you won!')
            break
            
        a=''
        for letter in availableLetters:
            if guess_word!=letter:
                a+=letter
        availableLetters=a
        
    
    if guesses_left==0:
        print('-----------')
        print('Sorry, you ran out of guesses. The word was '+secretWord)
        
        
hangman('Computer')


# In[3]:





# In[3]:


print(availableLetters)


# In[3]:


l=[1,2,3,4]
a=l


# In[5]:


print(a,l)


# In[6]:


a.append(l)


# In[7]:


print(a)


# In[8]:


print(l)


# In[26]:


def test(a):
    print(a)
    return 3/1>1


# In[27]:


val=test('arnav')


# In[28]:


print(val)


# In[23]:


print(int(5/2)==5//2)


# In[24]:


a=3>1


# In[25]:


print(a)


# In[33]:


if 'a' in "lohyia" and 2!=3:
    print('hell')


# In[37]:


for a in {1:'a',2:'b',3:'c'}:
    print({1:'a',2:'b',3:'c'}[a])


# In[47]:


# computing the factorial of any given number

def factorial(given_number):
    while given_number>0:
        if given_number==1:
            return 1
        else:
            return given_number* factorial(given_number-1)
    if given_number==0:
        return 0
        

    


# In[51]:


factorial(2
         )


# In[72]:


#computing the fibonacci sequence of a given factor
def fib(n):
    
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# In[96]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[10,20,30,40])
plt.show()


# In[98]:


from matplotlib.pyplot import *
plot([1,2,3],[10,20,30])


# In[78]:


def rev(s):
    if len(s)==1: 
        return s
    else:
        return s[-1]+ rev(s[:-1])
    
    


# In[89]:


word='ananana'
if rev(word)=='ananana':
    print('the word',word,'is a palindrome')


# In[91]:


from numpy import*
print(arange(5))


# In[93]:


import numpy as np
print(np.arange(5))


# In[109]:


s='arnavLohiyaL'
print(s.replace('arnav','yash'))


# In[111]:


bb=('arnav',)
print(bb)


# In[120]:


for letter in 'arnav':
    print(letter)


# In[128]:


listt=[1,2,3,4,'a','b','c','d']
listt.append([0,1])


# In[129]:


print(listt)


# In[130]:


listt.extend([0,6])


# In[131]:


print(listt)


# In[143]:


#converting a string to a list
string_name='ArnavxLohiyaxisxthexbest'

print(list(string_name))


# In[144]:


string_name.split('x')


# In[150]:


listt=['arnav','arnav','moksha']
" loves ".join(listt)


# In[155]:


sorted(listt)
print(listt)
listt.sort()
print(listt)


# In[159]:



print(listt.reverse())


# In[160]:


listt


# In[161]:


#The greatest common divisor of two positive integers is the largest integer
#that divides each of them without remainder

def gcdRecur(a,b):
    if b==0:
        return a
    else:
        return gcdRecur(b, a%b)
    


# In[164]:


gcdRecur(8,8)


# In[175]:


from math import *
def polysum(n,s):
    area=(0.25*n*(s**2))/(tan(pi/n))
    perimeter=n*s
    sq_perimeter=perimeter**2
    return round(area+sq_perimeter,4)   # returns the sum of area and the square of the polygon's perimeter, rounded to 4 decimal places


# In[176]:


polysum(10,2)


# In[170]:


pi


# In[178]:


n=10
tan(n)


# In[180]:


x='pi'
y='pie'

x,y=y,x
print(y)


# In[208]:


def fun(x):
    if x==1:
        print('before')
    break


# In[206]:


print('after')
    print('function working after execution of break statement')


# In[16]:


lis=[1,2,3,4]
lis.insert(0,12)
print(lis)


# In[45]:


L=[[1,2,3],[1,2,3]]
def deep_reverse(L):
    newL=L[:]
    for elt_one in newL:
        a=[]
        for elt in elt_one:
            
            a.insert(0,elt)
        L.insert(0,a)
        del(L[-1])
    print(L)
    


# In[46]:


deep_reverse([[1,20,3],[10,20,30]])


# In[1]:


def dict_invert(d):
    a=[]

    new_d={}
    for el in d.values():#[10,20,20]
        new_val=[]
    
        for a in sorted(d):#[1,2,3]
            if d[a]==el:
                new_val.append(a)
    
        new_d[el]=new_val
    


# In[3]:


dd={1:10,2:20,5:40,4:40}
dict_invert(dd)


# In[5]:


def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0]+s2[0] + helpLaceStrings(s1[1:],s2[1:],out)
    return helpLaceStrings(s1, s2, '')


# In[6]:


laceStringsRecur('arnav','lohiya')


# In[70]:


def f(s):
    return 'a' in s

def satisfiesF(L):
    alist=L[:]
    for a in alist:               
        if f(a)==False:
            L.remove(a)
    return len(L)    


# In[75]:


L=["a",'arnv','c','a','b','ba','cdd','aaa']
print(satisfiesF(L))
print(L)


# In[72]:


lis


# In[64]:


lis.remove('c')


# In[17]:


myl=[10,20,30]

print(int('1')+3)


# In[ ]:





# In[124]:


from datetime import *
try:
    a=int(input('Enter an integer:'))
    b=int(input('Enter an integer:'))
    print(a/b)

except ValueError:
    print('11')

#else:
#    print('executing else statement')
#    print('The tenth multiple of the given integer is:',a*10)

finally:
    print('executing finally statement')
    print(datetime.now().strftime("%H:%M"))


# In[34]:


a=int(input('Enter an integer:'))
print('The tenth multiple of the given integer is:',a*10)


# In[87]:


def func(L1,L2):
    assert len(L1)==len(L2)
    print(L1,L2)


# In[109]:


def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        try: 
            raise Exception('This is an error')
            
        finally:
            print('lets see')


# In[121]:


def fancy_divide(list_of_numbers, index):
    try:
        try:
            print('ok')
            a/0
            print('ok2')
        finally:
            print('went through finally clause')
            denom = list_of_numbers[index]
#            for i in range(len(list_of_numbers)):
#               list_of_numbers[i] /= 0
            list_of_numbers[20]
    except Exception as ex:
        print(ex)


# In[122]:


fancy_divide([0,2,4], 0)


# In[92]:


list_of_numbers=[0,2,4]
index=2
try:
        print('ok')
        raise Exception("0")
        print('ok2')
        
finally:
        print('went through finally clause')
        denom = list_of_numbers[index]
        for i in range(len(list_of_numbers)):
            list_of_numbers[i] /= 1
        print('lo')
        


# In[159]:


def f():
    a=[]
    for e in map(abs,[10,20,-21,-232]):
        a.append(e)
    return a


# In[162]:


[abs(item) for item in [10,20,30]]


# In[165]:


for item in map(abs,[10,-20,30]):
    print(item)


# In[ ]:





# In[167]:


d={'a':2,'b':4}
d['b']


# In[170]:


hand={'a':6,'b':3,'c':1}
hande=hand.copy()
hande


# In[174]:


wordList=['apple','bat','tan','loss']
if 'bat' in wordList:
    print('ok')
else:
    print('not ok')


# In[177]:


hand.get('h',0)


# In[ ]:


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed. displayHand(hand)
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    total_score=0
    while (len(hand)!=0):
        print('Current Hand:',displayHand(hand))
        user_input=input('Enter word, or a "." to indicate that you are finished: ')
        if user_input=='.':
            print("Run out of letters. Total score:", total_score)
        else:
            if isValidWord(user_input, hand, wordList):
                total_score+=getWordScore(user_input,n)
                print(word, "earned",getWordScore(user_input,n), 'points. Total:',total_score, "points")
                hand=updateHand(hand,user_input)
      
                
            
        



# In[191]:


def di():
    print('a b c d')
    print()
di()


# In[193]:


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()  


# In[199]:


displayHand({'a': 1, 'c': 1, 'e': 1, 'h': 1, 'o': 1,'t': 1,'y':1})


# In[26]:


print('Hello', end = " ")
print('world', end="?")
print('!')


# In[5]:


class Animal(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print(name,age)
    def funx(self):
        print(self.name*5,self.age*5)
        
        
class cat(Animal):
    def __str__(self):
        return 'youre looking at a cat'
        
        


# In[6]:


a=cat('angel',2)


# In[7]:


print(a)


# In[8]:


type(a)


# In[36]:


import random

print(random.randrange(0,5,3))


# In[39]:


[1,2,3,4,5,6][::2]


# In[44]:


print('\')')


# In[61]:


aa='hei my nam arna'


# In[62]:


' '.join(aa)


# In[63]:


myTuple = ("John", "Peter", "Vicky")

x = " ".join(aa)

print(x)


# In[83]:


def gt(n):
    while True:
        yield n+1
        n=n+1


# In[84]:


a=gt(3)


# In[89]:


a.__next__()


# In[1]:


import string


def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert 0<=shift<=26,'Please enter a valid shift input'
        dict_keys=string.ascii_lowercase+string.ascii_uppercase
        _dict_={}
        count=0
        dict_values=string.ascii_lowercase[n:]+string.ascii_lowercase[:n]+string.ascii_uppercase[n:]+string.ascii_uppercase[:n]
        for letter in dict_keys:
            _dict_[letter]=dict_values[count]
            count+=1
        return _dict_
        
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_text=''
        encrypt_dict=build_shift_dict(self,shift)
        for letter in self.message_text:
            try:
                shifted_text+=encrypt_dict[letter]
            except:
                shifted_text+=letter
        return shifted_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        pass #delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        pass #delete this line and replace with your code here

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass #delete this line and replace with your code here

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
b


# In[90]:


import string
string.ascii_uppercase


# In[107]:


vl
def build_shift_dict(self,shift):
    assert 0<=shift<=26,'Please enter a valid shift input'
    dict_keys=string.ascii_lowercase+string.ascii_uppercase
    _dict_={}
    count=0
    dict_values=string.ascii_lowercase[n:]+string.ascii_lowercase[:n]+string.ascii_uppercase[n:]+string.ascii_uppercase[:n]
    for letter in dict_keys:
        _dict_[letter]=dict_values[count]
        count+=1
    return _dict_

a=build_shift_dict(4)
print(a)


# In[ ]:


class parent(object):
    def __init__(self,n):
        self.n=n
    def plus(self, n):
        return n+n
    
    
class child(parent):
    def __init__(self,n):
        parent.__init__(self,n)
    def minus(self,nn):
        return nn*10
    
og=child(5)
    


# In[114]:


og.plus(8)


# In[2]:


abcd=[1]
print(abcd[:-1])


# In[25]:


one="arnav"
two='lohiya'
print(one,two)


# In[27]:


#from math import pi
print(pi)


# In[ ]:


#bogo sort
import random
def ssort(list_n):
    a=list_n[0]
    for element in list_n:
        if element >=a:
            a=element
        elif element<a:
            return False
        return True
a=[9,2,4,76,2,4,5]
while ssort(a):
    random.shuffle(a)


# In[ ]:


print(a)


# In[9]:


a=[9,2,4,76,2,4,5]
a.sort()
print(a)
is_sorted(a)


# In[10]:


n=[1,2,4,5]

def y():
    for element in n:
        yield element
        


# In[7]:


def genPrimes():
    n=[2]
    next_element=3
    yield 2
    while True:
        count=0
        for element in n:
            
            
            if (next_element%element!=0):
                count+=1
                
        if count==len(n):
            n.append(next_element)
            
            yield next_element
            next_element+=1
            
        else:
            next_element+=1
            
            
        
        
        


# In[8]:


a=genPrimes()


# In[9]:


a.__next__()


# In[10]:


a.__next__()


# In[11]:


a.__next__()


# In[14]:


a.__next__()


# In[ ]:





# In[137]:


def aas():
    n1=0
    n2=1
    yield n1
    while True:
        yield n2
        n1,n2=n2,n1+n2
        
    
        
    


# In[143]:


ob=aas()


# In[144]:



dic={}
for a in range(10):
    val=ob.__next__()
    
    dic[a]=val
    


# In[145]:


dic


# In[160]:


b=[1,9,1,4,19]
for a in b:
    if a==10:
        print('hi')
        break
else:
    
    print(a,'not equal to ten.')
    
print(a)


# In[158]:


print('work')


# In[179]:


lis=[1,2,3,4,5]
a=iter(lis)
a.__next__()


# In[180]:


list(a)


# In[182]:


p={'a':22,"b":55}
p['a']=1
p['a']


# In[183]:


def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    summed_val=1
    counter=2
    while True:
        if summed_val==k:
            return True
        elif summed_val>k:
            return False
        else:
            summed_val+=counter
            counter+=1
        
        


# In[185]:


a=is_triangular(11)
print(a)


# In[17]:


L=[3, 2, -1, 2, 7]
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    
    #function to calculate sum of longest run of elements in increasing order
    def incCount(L):
        incList=[]
        maxLen=0
        maxel=[]
        data=[]
        
        for el in range(len(L)):
        
            if el==0:
                incList.append(L[el])
            elif L[el]>=L[el-1]:
                #numOfElement+=1
                incList.append(L[el])
                        
            else:
                data.append(incList)
                incList=[L[el]]
        
        data.append(incList)  
    
        for el in data:
            if len(el)>maxLen:
                maxLen=len(el)
                maxel=el
        print(maxel)
        print(data)  
        print(sum(maxel))
        return (sum(maxel),L.index(maxel[0]),maxLen)

            
            
    def decCount(L):
        incList=[]
        maxLen=0
        maxel=[]
        data=[]
        
        for el in range(len(L)):
        
            if el==0:
                incList.append(L[el])
            elif L[el]<=L[el-1]:
                #numOfElement+=1
                incList.append(L[el])
                        
            else:
                data.append(incList)
                incList=[L[el]]
        
        data.append(incList)  
    
        for el in data:
            if len(el)>maxLen:
                maxLen=len(el)
                maxel=el
        
        return (sum(maxel),L.index(maxel[0]),maxLen)       

    a=incCount(L)
    b=decCount(L)
    if a[2]==b[2]:
        if a[1]>b[1]:
            return(b[0])
        else:
            return(a[0])
    elif a[2]>b[2]:
        return(a[0])
    else:
        return(b[0])
    
    

a=longest_run(L)
print(a)


# In[8]:


L=[1,2,3,4,5,6,7,8,9]
#function to calculate sum of longest run of elements in increasing order
def incCount(L):
    incList=[]
    maxLen=0
    maxel=[]
    data=[]
        
    for el in range(len(L)):
        
        if el==0:
            incList.append(L[el])
        elif L[el]>=L[el-1]:
            #numOfElement+=1
            incList.append(L[el])
                        
        else:
            data.append(incList)
            incList=[L[el]]
        
    data.append(incList)  
    
    for el in data:
        if len(el)>maxLen:
            maxLen=len(el)
            maxel=el
            
    return (sum(maxel),L.index(maxel[0]),maxLen)

            
            
def decCount(L):
    incList=[]
    maxLen=0
    maxel=[]
    data=[]
        
    for el in range(len(L)):
        
        if el==0:
            incList.append(L[el])
        elif L[el]<=L[el-1]:
            #numOfElement+=1
            incList.append(L[el])
                    
        else:
            data.append(incList)
            incList=[L[el]]
        
    data.append(incList)  
    
    for el in data:
        if len(el)>maxLen:
            maxLen=len(el)
            maxel=el
            
    return (sum(maxel),L.index(maxel[0]),maxLen)       

a=incCount(L)
b=decCount(L)
if a[2]==b[2]:
    if a[1]>b[1]:
        print(a)
    else:
        print(a)
elif a[2]>b[2]:
    print(a[0])
else:
    print(b[0])


# In[210]:


print(incList)


# In[23]:


def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    key_code={}
    decoded=''
    for index in range(len(map_from)):
        key_code[map_from[index]]=map_to[index]
    for letter in code:
        decoded+=key_code[letter]
    return (key_code,decoded)


print(cipher("abcd", "dcba", "dab"))


# In[22]:


a={'a':1,'b':2}

b='arnav'
len(b)


# In[28]:


class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name,'says: It is obvious that '+self.name+' says '+ stuff
    
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

ae.say('hello')


# In[30]:


stuff='hello'
name='arnav'
print('It is obvious that ',name,' says ', stuff)


# In[8]:


for a in range(0,10,2):
    print(a)


# In[2]:


print('a')


# In[46]:


class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.coll=[]
        
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.count3=0
        for a in range(0,len(self.coll),2):
            if self.coll[a]==str(k):
                self.count3+=1
                self.coll[a+1]=str(v)
                
        if self.count3==0:
            self.coll.extend([str(k),str(v)])
        
        
    def getval(self, k):
        """ k, immutable object  """
        self.count=0
        for a in range(0,len(self.coll),2):
            if self.coll[a]==str(k):
                self.count+=1
                return self.coll[a+1]
        if self.count==0:
            
            raise KeyError('KeyError successfully raised')
        
    def delete(self, k):
        """ k, immutable object """  
        self.count2=0
        for a in range(0,len(self.coll),2):
            if self.coll[a]==str(k):
                self.count2+=1
                self.coll=self.coll[0:a]+self.coll[a+2:]
                break
        if self.count2==0:
            raise KeyError('KeyError successfully raised')
    def getc(self):
        return self.coll

d1=myDict()
d1.assign(1,4)
d1.assign(4,4)
d1.assign(8,4)
print(d1.getval(1))
print(d1.getval(4))
print(d1.getval(8))
print(d1.getc())
d1.delete(4)
print(d1.getval(1))
print(d1.getval(8))


# In[5]:


s='arnav'
s+=str(1)+str(2)
s


# In[13]:


for a in range(0,6,2):
    print(a)

 #   raise Exception('KeyError successfully raised')


# In[23]:


raise Exception('ho')


# In[49]:


import pylab as plt
plt.plot([1,2,3,4],[1,2,3,4])
plt.show()


# In[58]:


class Fruit(object):
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color

    
apple=Fruit('Apple','RED')
apple.get_name()
apple.get_color()


# In[61]:


"arnav lohiya" in "My name is arnav lohiya"


# In[71]:


aword=1
def fun():
    print(aword)
l=fun()


# In[84]:


import datetime as dt

a=dt.datetime(2022,5,17)
print(a.now("yy:mm:dd"))


# In[ ]:




