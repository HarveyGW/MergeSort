#HarveyGW
#Mergesort
import colorama
import sys
from time import sleep
from colorama import Fore
print (Fore.)
def mergesort(mergelist):
  if len(mergelist) > 1:
    mid = len(mergelist) // 2
    lefthalf = mergelist[:mid]
    righthalf = mergelist[mid:]
    mergesort(lefthalf)
    mergesort(righthalf)
    i = 0
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] < righthalf[j]:
        mergelist[k] = lefthalf[i]
        i += 1
      else:
        mergelist[k] = righthalf[j]
        j += 1
      k += 1
    while i < len(lefthalf):
      mergelist[k] = lefthalf[i]
      i += 1
      k += 1
    while j < len(righthalf):
      mergelist[k] = righthalf[j]
      j+=1
      k+=1
print(Fore.WHITE)
mergelist = raw_input("Enter the list of numbers: ").split()
for i in range(0, len(mergelist)):
  mergelist[i] = int(mergelist[i])
wait = 'Working on it....'
for char in wait:
  sleep(0.1)
  sys.stderr.write(Fore.YELLOW + char)
mergesort(mergelist)
print(Fore.GREEN)
print(mergelist) 
