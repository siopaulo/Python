from functions import square
# or just import functions -- but I'd have to add function to the square function: "function.square(i)"
for i in range(10):
    print(f"The square of {i} is {square(i)}")