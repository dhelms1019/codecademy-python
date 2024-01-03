# Data for a imaginary hair salon

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Determining average price of haircuts...
total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)

print("Average Haircut Price: $" + str(round(average_price, 2)) + "\n")

# Cutting all haircut prices by $5...
new_prices = [price - 5 for price in prices]
print(new_prices)

# Examining revenue...
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("\nTotal Revenue: $" + str(round(total_revenue, 2)))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: $" + str(round(average_daily_revenue, 2)))

# Advertising haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]

print("\nAvailable Haircuts Under $30:")
print(cuts_under_30)


