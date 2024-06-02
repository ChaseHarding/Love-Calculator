#Welcome to the Love Calculator
#Below is the code users interact with on page load
print("The love calculator is calculating your score...")
name1 = input("What is your name?: ")
name2 = input("What is your partners name?: ")

#This is where the fun begins
combined_names = name1 + name2 
lower_names = combined_names.lower()

#lets check how many times the letters in 'true' appear
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

#storing this value in a new variable for the final answer
first_digit = t + r + u + e
