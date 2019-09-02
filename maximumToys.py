#!/usr/bin/python

# Complete the maximumToys function below.
def maximumToys(prices, k):
  #sort the prices
  prices.sort()
  counter=0
  #go through the items
  for item in prices:
    k=k-item
    #if the amount of money left is greater than 0, add that item
    if k > 0:
      counter+=1
    #else exit
    else:
      break
  return counter
  
toys=[1,12,3,5,6]
maximumToys(toys, 5)
