total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter expense:\n")))
total = sum(expenses)
print("You expent $",total,sep='')