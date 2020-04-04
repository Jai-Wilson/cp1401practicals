

tariffs = {'TARIFF_11': 0.244618, 'TARIFF_31': 0.136928}
a= 0.244618
b=0.136928
print("Electricity bill estimator")

finished = False
tariff = int(input('What tariff are you using? TARIFF_'))
tariff_index = 'TARIFF_' + str(tariff)
while not finished:
    if tariff_index in tariffs.keys():
        finished = True
    else:
        print("Not valid")
        tariff = input('What tariff are you using? TARIFF_')
used_tariff = tariffs[tariff_index]
daily_use=float(input("Enter daily use in kWh: "))
days=float(input("Enter number of billing days: "))
bill= (tariff * daily_use * days) / 100

print("Your bill is ", bill)