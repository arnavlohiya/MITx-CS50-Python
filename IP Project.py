#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as m
print('Welcome To The General Knowledge Test!')
print('Please enter the following details carefully.')
report=[]
count=0
wrong=0
name=str(input('Please enter your full name:'))
print('For answers that require names, make sure you type the full name with the correct spelling.\nGoodluck!')
ans1=float(input('Q1) Which year was Gandhi Ji born in?'))
if(ans1==1869):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')
ans2= float(input('Q2) In which year did the kargil war take place?'))
if(ans2==1999):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')    
ans3=str(input('Q3) Who was the first female Prime Minister of India?'))
if(ans3.upper()=='INDIRA GANDHI' or ans3.upper()=='INDIRA'): 
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')
ans4= float(input('Q4) Answer the following: (120+90-22)/2?'))
if(ans4==94):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')
ans5= str(input('Q5) Who is the wealthiest individual living on Earth?'))
if(ans5.upper()=='ELON MUSK' or ans5.upper()=='ELON' or ans5.upper()=='MUSK'):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')
ans6= str(input('Q6) Who is the captain of the Indian mens cricket team '))
if(ans6.upper()=='ROHIT SHARMA' or ans6.upper()=='ROHIT' ):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')    
ans7= float(input('Q7) How many zeroes are there in Hundred crores?'))
if(ans7==9):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')

ans8= float(input('Q8) How many hydrogen atoms are there in glucose?'))
if(ans8==12):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')

ans9= str(input('Q9) True or False: The strongest metal on earth is Tungsten?'))
if(ans9.upper()=='TRUE'):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Current Score->\t\t',count,'correct and',wrong,'wrong')

ans10= str(input('Q10) What is Sachin Tendulkar\'s middle name?'))
if(ans10.upper()=='RAMESH'):
   print('Correct,next')
   count+=1
   report.append('Correct')
else: 
   print('Wrong, next')
   wrong+=1
   report.append('Wrong')
print('Thank you for attempting the questionnaire')
correct=str(count*5)
mydb=m.connect(host="localhost",user="root",password="arnavlohiya",database='family')

mycursor=mydb.cursor()
mycursor.execute('use family')
mycursor.execute('create table if not exists project2 (Name varchar(30) primary key, Score varchar(3))')
mycursor.execute('insert into project2 values("'+name+'","'+correct+'")')
   
print('--------------------')
print('--------------------')
print('--------------------')
print('1. Final Score\n2. Graphical representation of score\n3. Tabular format of scores\n4. Feedback\n5. Show Leaders board\n6. Exit')
print('--------------------')
print('--------------------')
print('--------------------')
search=float(input('Enter your choice:'))
print('--------------------')
print('--------------------')
print('--------------------')
while(search<=6 and search>=1):
   if(search==1): 
       print('Final Score:\t',count,'correct and',wrong,'wrong')
       srch=float(input('Enter your choice:'))
       search=srch
       print("-------------")
       print("-------------")
       print("-------------")
   elif(search==2):
       plt.plot(np.arange(1,11),report,'og',ls="-",markeredgecolor='k',markersize=8)
       plt.xlabel('Question Numbers')
       plt.ylabel('Correct or wrong')
       plt.xticks([1,2,3,4,5,6,7,8,9,10])
       plt.show()
       srch=float(input('Enter your choice:'))
       search=srch
       print("-------------")
       print("-------------")
       print("-------------")
   elif(search==3):
       detrep=pd.Series(report,index=[np.arange(1,11)])
       print(detrep)
       srch=float(input('Enter your choice:'))
       search=srch
       print("-------------")
       print("-------------")
       print("-------------")

   elif(search==4):
       if(count<3):print('Very bad')
       elif(count>=3 and count<7): print('You can do better!')
       elif(count>=7 and count<10): print("Excellent performance!")
       elif(count==10):print('PERFECT.')
       srch=float(input('Enter your choice:'))
       search=srch
       print("-------------")
       print("-------------")
       print("-------------")
   elif (search==5):
       print('The top 3 Scores:')
       highscore=pd.read_sql('select *from project2 order by score desc limit 3',mydb)
       print(highscore)
       srch=float(input('Enter your choice:'))
       search=srch
       print("-------------")
       print("-------------")
       print("-------------")
   elif(search==6):
       print('Thank you')
       break
mydb.commit()


# In[ ]:





# In[ ]:




