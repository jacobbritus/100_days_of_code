# welcome, total_bill, tip? 10 12 15, split?, calculation
print("Welcome to the tip calculator!")
total_bill = float(input("How much was the the total bill?\n$"))
tip = int(input("What percentage would you like to tip?\n%"))
split = int(input("With how many people would you like to split the bill?\n"))

print(f"Each person will pay ${round((total_bill+total_bill*(tip/100)) / split, 2)}!")