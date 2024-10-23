print("**************************************************")
print("*                                                *")
print("*          🌟 Welcome to the Tip Calculator! 🌟          *")
print("*                                                *")
print("**************************************************")

def get_bill_details():
    bill = float(input("Enter your bill: "))
    tip_percentage = int(input("Enter your tip percentage: "))
    people = int(input("How many people to split the bill: "))
    return bill, tip_percentage, people

def calculate_tip(bill, tip_percentage):
    return bill * (tip_percentage / 100)

def calculate_each_share(bill, tip, people):
    return (bill + tip) / people

def print_final_amount(each_share):
    print(f"\nEach of you should pay: ${each_share:.2f}")

print("\nLet's start calculating your bill!")
while True:
    bill, tip_percentage, people = get_bill_details()
    tip = calculate_tip(bill, tip_percentage)
    each_share = calculate_each_share(bill, tip, people)
    print_final_amount(each_share)

    more_calculations = input("\nWould you like to calculate another tip? Type Yes or No: ").lower()
    if more_calculations != "yes":
        break

print("\nThank you for using the Tip Calculator! Have a great day!")
