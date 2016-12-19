def QuickSort(Tablica,low,high):
  if high>low:
    p=partition(Tablica,low,high)
    QuickSort(Tablica,low,p-1)
    QuickSort(Tablica,p+1,high)
    
def partition(Tablica,low,high):
	divider=low
	pivot=high

	for i in range(low,high):
		if (Tablica[i]<Tablica[pivot]):
			Tablica[i], Tablica[divider] = Tablica[divider],Tablica[i]
			divider+=1
	Tablica[pivot], Tablica[divider]= Tablica[divider], Tablica[pivot]

	return divider

Tablica=[0, 2,3,4,2,1,212,1.5]
QuickSort(Tablica,0,len(Tablica)-1)
print (Tablica)