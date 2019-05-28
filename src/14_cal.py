"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
# function that takes in a variable number of arguments
## if no argument, return current calendar month
## if 1 argument, assume it's a month and year = current year
## if 2 arguments, assume it's month and year
## if any other combination, print error message
# def wutDate(a=datetime.currentmonth, b=datetime.currentyear):
#    if a and b are valid date and month, return the calendar for a, b
      # else print ("Please pass a valid month or a valid month and valid year to this function")
      # quit()