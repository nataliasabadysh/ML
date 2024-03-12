# Shopping

phone = 1299.99
mac = 3199.29
subs = 122.40

sum_amount = phone + mac + subs # 4621.679999999999


dollars = int(sum_amount)
cents = round((sum_amount - dollars) * 100)

print(f"Dollars: {dollars} Cents: {cents}")
