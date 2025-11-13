# Make a dictionary called 'price'.

prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}


# Make a second dictionary called 'stock'.

stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}


# Print price and stock for each fruit.

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]


# Calculate how much money you make if you sold all.

total = 0
for key in prices:
  money = prices[key] * stock[key]
  total += money

print total
