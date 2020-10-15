import calendar
import datetime 
import random


#     two digits for month
#     two digits for day
#     and four digits for the year


hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute 

h =hour 
m =minute
x = 12

if h < x: 
    print ("It is ",h,m,"AM","Hello and Good Morning") 
elif h < (x+6): 
    print ("It is ",h,m,"PM","Hello and Good Afternoon") 
else: 
    print ("It is ",h,m,"PM","Hello and Good Evening") 

i = int(input("Enter the month in number:  ",))
d = int(input("Enter the date: ",))
y = int(input("Enter the year: ",))
print()
print(f"{i}/{d}/{y}")
r = x - i
print()
print("and there are",r,"remaining months:")
print("\n----Current Month----\n")
print(calendar.month(y, i, w=1, l=2,))
print("---------------------")
print("""\n*Remaining Calendar""")
Cal = calendar.TextCalendar(calendar.MONDAY)

i = i + 1
while i<=x:

  Cal.prmonth(y,i,w=1,l=2)
  print("\n",)
  i+=1
  
print("          ",y+1,"Happy New Year")