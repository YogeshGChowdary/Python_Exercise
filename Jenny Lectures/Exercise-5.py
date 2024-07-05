# #How many days, weeks, months we have left to live until 90 years old
# input = your current age
# output = you have a days, b weeks and c months left
# --- 1year = 365days, 1year = 52weeks, 1year = 12months

age = int(input("Enter your age: "))

years_left = 90-age
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

print("you have", days_left, 'days', weeks_left, 'weeks', 'and', months_left, )

