#Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.

Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
s = sum(stock[fruit] * prices[fruit] for fruit in stock.keys())