#HarveyGW
#Mergesort

def mergesort(mergelist):
  if len(mergelist) > 1:
    mid = len(mergelist) //2
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

mergelist = input("Enter the list of numbers: ").split()
mergesort(mergelist)
print(mergelist) 
