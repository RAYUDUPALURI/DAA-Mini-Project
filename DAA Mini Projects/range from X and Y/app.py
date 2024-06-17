X = int(input("Enter the starting integer (X): "))
Y = int(input("Enter the ending integer (Y): "))

for number in range(X, Y + 1):
    print(number)

my_range = list(range(X, Y + 1))
print(my_range)
