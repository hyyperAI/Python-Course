# Taking input from 'input' tag is in string so we added int() to convert string into integer

bill = int(input("what's the total bill: "))
# getting total bill in form of int

tip = int(input('how many percent you would like to give as a tip : '))
# getting the amount of percent does the costumer wanted to give tip

people = int(input("total number of people: "))

tip_percent = float(tip / 100 * bill)
# total tip in bill , getting the total amount of tip's percent in bill

total_bill = float(tip_percent + bill)
# adding the tip to bill to get the total amount of bill

bill_each_ = float(total_bill / people)
# diving the bill into number of people

bill_each_person = round(bill_each_, 2)
# rounding the amount of bill

bill_per_person = '{:.2f}'.format(bill_each_person)
# actual way of using round function ,
# 2f indicate the actual value of rounding off, and any other is the syntax

print(f'total bill each person has to pay is : {bill_each_person}')
# telling every one the amount of bill
