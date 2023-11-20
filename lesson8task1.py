# A simple function.

# Create a simple function called favorite_movie, 
# which takes a string containing the name of your favorite movie. 
# The function should then print "My favorite movie is named {name}".

def favorite_movie(your_movie):
    print(f"My favorite movie is named {your_movie}")

user_ans = input("Enter your favorite movie: ")
favorite_movie(user_ans)