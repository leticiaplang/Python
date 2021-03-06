  
"""
DATA: 30/03/2021

Projeto: Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
input year, output boolean

------------------------------------------------------------------------------------------------
def is_leap(year):
    leap = (year%4==0 and year%100!=0) or (year%100==0 and year%400==0)
    return leap
year = int(input())
print(is_leap(year))

------------------------------------------------------------------------------------------------


DATA: 16/04/2021
Refatorado o projeto diminuindo 1 linha de código e adequando PEP8. 
"""

def is_leap(year):
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)
    return leap

print(is_leap(int(input())))
