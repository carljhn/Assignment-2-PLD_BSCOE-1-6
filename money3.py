money = int(input("You have an amount of: "))
apl_prc = int(input("An apple costs: "))
max_apl = int(money/apl_prc)
total = (max_apl * apl_prc)
change = (money - total)
print(f"You can buy {max_apl} apples and your change is {change} pesos.")