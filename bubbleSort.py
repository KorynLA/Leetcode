#!/usr/bin/python

def countSwaps(a):
  arrSize=len(a)
  swapped=0
  for i in range(0, arrSize):
    for j in range(0, arrSize-1):
      #if prev value is larger than next, swap!
      if a[j] > a[j+1]:
        temp=a[j]
        a[j]=a[j+1]
        a[j+1]=temp
        swapped=swapped+1
  #required print statements
  print("Array is sorted in", swapped, "swaps.")
  print ("First Element:", a[0])
  print("Last Element:", a[arrSize-1])
  
a=[1,2,3]
countSwaps(a)
