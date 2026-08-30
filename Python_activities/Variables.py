#Create two variables, length and width, then print their values.
#Update the value of the width variable and print the new value.

length = 3
width = 4

print("\033[1;34mlength=\033[1;31m",length, "\033[1;34mwidth=\033[1;31m", width)

width = width + 10
print("\033[1;32mUpdated width value:\033[0m")

print("\033[1;34mlength=\033[1;31m",length, "\033[1;34mwidth=\033[1;31m", width)
