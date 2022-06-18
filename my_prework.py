#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of 
# the function. The first line of the code has been defined as below.

def hello_name():
    name = input("Please enter your name: ")
    print("Hello " + name + "!")

hello_name()


#Question 2
#Write a python function, first_odds that prints the odd numbers from 
# 1-100 and returns nothing

def first_odds():
    odds = list(range(1,101,2))
    for number in odds:
        print(number)

first_odds()


#Question 3
#Please write a Python function, max_num_in_list to return the max 
#number of a given list. The first line of the code has been defined 
# as below.

def max_num_in_list(a_list):
    print(max(a_list))

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_num_in_list(digits)


#Question 4
#Write a function to return if the given year is a leap year. A leap 
# year is divisible by 4, but not divisible by 100, unless it is also 
# divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
#first condition is year divisible by (%) 4
    #second condition divisible by (%) 100
        #third condition is divisible by (%) 400
    if (a_year % 4) == 0:
        if (a_year % 100) == 0:
            if (a_year % 400) == 0:
                return True #met all 3 conditions so true / leap year
            else:
                return False #did not meet all conditions so F /not LY
        else:
            return True #meets two conditions of divisible by 4 and 
                        #not 100 so leap year and true
    else:
        return False # failed first test condition so not a leap year 
                     #and false

Determination_of_leapyear = is_leap_year(2020)  #2020 is a known leap
print(Determination_of_leapyear)


#Question 5
#Write a function to check to see if all numbers in list are 
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive 
# numbers, but [1,2,4,5] are not consecutive numbers. The return 
# should be boolean Type.


# Python3 Program to Create list 
# with integers within given range 
  
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
      
# Driver Code
lst = [2, 3, 1, 4, 5]
print(is_consecutive(lst))

#This approach uses sorted() function of Python. We compare the sorted 
# list with list of range of minimum and maximum integer of the list 
# and return it.

#Sort one copy of a list (sort function) to put it in sequential order 
# so it will be able to match another list that is generated based on 
# a range whose start and end points are set by the smallest (min 
# function) through the largest(max function) + 1. item of the 
# unsorted list.  That creates a list identical to the sorted copy and 
# when compared using == the return is true. 
