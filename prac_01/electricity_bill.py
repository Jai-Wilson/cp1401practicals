

print("Electricity bill estimator")

cents=float(input("Enter cents per kWh: "))
daily_use=float(input("Enter daily use in kWh: "))
days=float(input("Enter number of billing days: "))
bill= (cents * daily_use * days) / 100

print("Your bill is ", bill)