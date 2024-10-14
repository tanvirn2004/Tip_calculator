print("**************************************************")
print("*                                                *")
print("*          🌟 Welcome to the Tip Calculator! 🌟          *")
print("*                                                *")
print("**************************************************")

bill = float(input("Enter your bill: "))
tip_percentage = int(input("Enter your tip percentage: "))
persone = int(input("How many to split the bill :"))
tip = bill * (tip_percentage/100)
each_bill = (bill + tip)/persone
print(f"Each of you should pay {each_bill:.2f}")