# nested loop means a loop within a loop

for x in range(3):
    for y in range(1,10):
        print(y,end="")
    print()

rows = int(input("Enter no. of rows: "))
columns = int(input("Enter no. of columns: "))
symbol = input("Enter a symbol to use: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()


