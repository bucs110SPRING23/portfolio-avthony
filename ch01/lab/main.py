import random

#Part A
weeks = 16
print(weeks,type(weeks))
classes = 5
print(classes,type(classes))
tuition = 15000
print(tuition,type(tuition))
classes_per_week = 11
print(classes_per_week,type(classes_per_week))
cost_per_week = ((tuition/classes)/weeks)
print(cost_per_week,type(cost_per_week))
print("cost per week:", cost_per_week)
cost_per_class = (cost_per_week/classes_per_week)
print(cost_per_class,type(cost_per_class))
print("cost per class:",cost_per_class)

#part B
mylist = ["Hello",4.5,13,"What?","Goodbye"]
random_choice = random.choice(mylist)
print(random_choice)
