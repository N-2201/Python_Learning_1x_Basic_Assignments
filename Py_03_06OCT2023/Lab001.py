# Get input from the user
n = int(input("Enter a number: \n"))

# Print the table using an f-string
print(f"{n} x 1 = {n * 1}")
print(f"{n} x 2 = {n * 2}")
print(f"{n} x 3 = {n * 3}")
print(f"{n} x 4 = {n * 4}")
print(f"{n} x 5 = {n * 5}")
print(f"{n} x 6 = {n * 6}")
print(f"{n} x 7 = {n * 7}")
print(f"{n} x 8 = {n * 8}")
print(f"{n} x 9 = {n * 9}")
print(f"{n} x 10 = {n * 10}")

#print the table using for loop
print("\nPrint the table using for loop")
for x in range(1,11):
    print(f"{n} x {x} = {n * x}")



