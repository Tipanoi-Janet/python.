
# Write a Python program that takes a
# list of strings as input and outputs the
# number of times each string appears in the list, using
# # a dictionary
strings = ['janet', 'hannah', 'joy', 'wiky', 'jacint', 'kim',]
start = {}
for string in strings:
    if string in start:
        start[string] += 1
    else:
        start[string] = 1
for string, start in start.items():
    print(string, start)
# Write a Python program that takes a
# list of numbers as input and outputs the median of the numbers
def lists_number(num):
    sorted_list=sorted(num)
    lists_lenghth=len(num)
    mid_index = lists_lenghth// 2
    if lists_lenghth % 2 == 0:
        return (sorted_list[mid_index-1] + sorted_list[mid_index]) / 2
    else:
        return sorted_list[mid_index]
input_list = [5,9,0,7,65,10]
output = lists_number(input_list)
print(output)


#Write a Python program that takes a list of numbers as input and outputs the second largest number in the list using conditional statements and a for loop.
def list_Of_numbers(place):
place="Nairobi"
place1=revearsed(place)
if place==place1:

     print(f"{place} is a palindrome")
 else:
      print(f"{place} is not a palindrome")

#Write a Python program that takes a year as input and determines if it is a leap year.
year=2020

 if year%4==0:
     print(f"leap {year}")
 
 else :(f"not leap {year}")
