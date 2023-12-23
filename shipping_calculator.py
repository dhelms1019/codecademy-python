weight = 4.8
cost = 0

# Ground Shipping
if weight <= 2:
  cost = round(20 + (weight * 1.5), 2)
elif weight <= 6:
  cost = round(20 + (weight * 3), 2)
elif weight <= 10:
  cost = round(20 + (weight * 4), 2)
else:
  cost = round(20 + (weight * 4.75), 2)

print("Ground Shipping cost based on weight of " + str(weight) + " pounds: " + str(cost))

# Ground Shipping Premium
premium_cost = 125
print("Ground Shipping Premium cost: " + str(premium_cost))

# Drone Shipping
if weight <= 2:
  cost = round(weight * 4.5, 2)
elif weight <= 6:
  cost = round(weight * 9, 2)
elif weight <= 10:
  cost = round(weight * 12, 2)
else:
  cost = round(weight * 14.25, 2)

print("Drone Shipping cost based on weight of " + str(weight) + " pounds: " + str(cost))