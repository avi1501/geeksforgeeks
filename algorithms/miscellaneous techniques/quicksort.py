def quicksort(sequence):
    length=len(sequence)
    if length<2:
        return sequence
    pivot=sequence.pop(length//2)
    lower=[]
    higher=[]
    for i in sequence:
        if i>pivot:
            higher.append(i)
        else :
            lower.append(i)
    return quicksort(lower)+[pivot]+quicksort(higher)
a=[20,30,80,46,52,11]
print(quicksort(a))