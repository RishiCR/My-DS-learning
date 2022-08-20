#!/usr/bin/env python
# coding: utf-8
Q1.Write a Python program to convert kilometers to miles?
# In[26]:


a=float(input("Enter the Value in kilometers to convert it to miles ?"))

b=a* 0.62137119

print("The value n miles is :",round(b,2))


# Q2.Write a Python program to convert Celsius to Fahrenheit?

# In[12]:


celsius=float(input("enter the value of Celsius : "))
Fahrenheit=(celsius*1.8)+32
print("the value in Fahrenheit is : ",round(Fahrenheit,2))

Q3.Write a Python program to display calendar?
# In[17]:


import calendar
 
yy = int(input("enter Year "))
mm = int(input("enter Month "))
 
# display the calendar
print(calendar.month(yy, mm))

Q4.Write a Python program to solve quadratic equation?

# In[28]:


import math 
  
  
# function for finding roots
def equationroots( a, b, c): 
  
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    # checking condition for discriminant
    if dis > 0: 
        print(" real and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 
        

equationroots(10, -50, 40)      

Q5.Write a Python program to swap two variables without temp variable?
# In[30]:


a=int(input("Enter the 1st value"))
b=int(input("Enter the 2nd value"))
print("the value of 1st before swapped is",a,"the value of 2nd before swapped is ",b)
a,b=b,a

print("The value of 1st after swapped is ",a,"The value of 2nd after swapped is",b)


# In[ ]:




