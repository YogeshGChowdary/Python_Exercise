#### Love Calculator #####
# if no. of char matches between name and word "true" = first value of percentage
# if no. of char matches between name and word "love" = second value of percentage

name1 = input('enter name of person1: ')
name2 = input('enter name of person2: ')

name = (name1 + name2).lower()

characters_to_count_true = ['t', 'r', 'u', 'e']

count_true = 0
for i in name:
    if i in characters_to_count_true:
        count_true += 1
true = str(count_true)

characters_to_count_love = ['l', 'o', 'v', 'e']

count_love = 0
for i in name:
    if i in characters_to_count_love:
        count_love += 1
love = str(count_love)

print("Final score is: ", true+love)