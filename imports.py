from random import choice

people = {'John': {'id': 1, 'age': '37', 'sex': 'Male'},
          'Marie': {'id': 2, 'age': '42', 'sex': 'Female'},
          'Jane': {'id': 3, 'age': '30', 'sex': 'Female'}}


nums = [1,2,3,4,5,6,7,8]

print(choice(nums))
print(choice(list(people.items())))



