"""
This program is complete however it has a bug in it. When
a user put in "0.0028" which is correct, the program would
still output false. So if we added rounding and comparing rounded
version of two floats it should fix the problem. 
"""
# Amount of food and number of people
tons_of_food = 0.07
num_people = 25

# Determine how much food each person gets
tons_of_food_per_person = tons_of_food / num_people
print tons_of_food_per_person

# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take? "))
if round(tons_taken, 5)  == round(tons_of_food_per_person, 5):
    print "Good job, you took the right amount of food!"
else:
    print "You took the wrong amount of food!"