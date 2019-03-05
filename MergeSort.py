#HarveyGW
#Mergesort

def mergesort(mergelist):
  if len(mergelist) > 1:
    mid = len(mergelist) //2 #Sets the midpoint
    lefthalf = mergelist[:mid] #Takes all of the numbers to the left of the defined midpoint
    righthalf = mergelist[mid:] #Takes all of the numbers to the right of the defined midpoint
    mergesort(lefthalf) #Merges the left side back together
    mergesort(righthalf) #Merges the right side back together
    i = 0 #Sets i,j,k variables to 0
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] < righthalf[j]: #If right half is bigger than left half, mergelist[k] becomes the same as lefthalf[i], then adds 1 to i 
        mergelist[k] = lefthalf[i]
        i += 1
      else:
        mergelist[k] = righthalf[j] #Else sets mergelist[k] to righthalf[j], adds 1 to j
        j += 1 #END WHILE
      k += 1 #Adds 1 to k
    while i < len(lefthalf):
      mergelist[k] = lefthalf[i] #Makes mergelist[k] = lefthalf[i], adds 1 to i, adds 1 to k
      i += 1
      k += 1
    while j < len(righthalf):
      mergelist[k] = righthalf[j] #Makes mergelist[k] = righthalf[j], adds 1 to j, adds 1 to k
      j+=1
      k+=1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Main Program
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
mergelist = input("Enter the list of numbers: ").split() #Asks for the list of integers and splits them
for i in range(0, len(mergelist)): #These two lines make it so any number can be used
  mergelist[i] = int(mergelist[i])
mergesort(mergelist) #Mergesorts the list
print(mergelist) #Prints the new list
