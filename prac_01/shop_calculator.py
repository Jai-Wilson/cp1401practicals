

number_of_items = int(input("How many items do you have today? "))
while number_of_items <= 0:
    print("That is an invalid amount")
    print()
    number_of_items = int(input("How many items do you have today? "))
prices = []

for i in range (0, number_of_items, 1):
    item_value = float(input('Enter price of item: $'))
    prices.append(item_value)

cost = sum(prices)

if cost > 100:
    cost = cost * 0.9

print("The price of ", number_of_items, " items is ", cost)
