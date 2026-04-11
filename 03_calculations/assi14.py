'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0'''

cost_price,selling_price= map(float,input("Enter Cost Price and Selling Price (use comma to separate) :").split(","))
if(cost_price>selling_price):
 loss = cost_price-selling_price
 print("Loss% :",cost_price(loss/100))
