# Working with info on a new pizza restaurant

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)

print("We currently have " + str(num_two_dollar_slices) + " types of pizza slices with a cost of $2.")

num_pizzas = len(prices)

print("\nWe sell " + str(num_pizzas) + " different kinds of pizza!\n")

pizza_and_prices = []

# 2D list of toppings and prices
for i in range(len(toppings)):
  pizza_and_prices.append([prices[i], toppings[i]])

print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()
print(pizza_and_prices)

pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)