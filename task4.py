"""
===================   TASK 4  ====================
* Name: Merge Sort
*
* Write a function that will implement merge sort
* algorithm. Generate list of 1000 random integer
* numbers and sort the list using your function.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

def merge(niz1,niz2):

    zbirni = []
    duzina1 = len(niz1)
    duzina2 = len(niz2)

    i = 0
    j = 0

    while i < duzina1 and j < duzina2:
        if niz1[i] < niz2[j]:
            zbirni.append(niz1[i])
            i += 1
        else:
            zbirni.append(niz2[j])
            j += 1

    while i < duzina1:
        zbirni.append(niz1[i])
        i += 1

    while j < duzina2:
        zbirni.append(niz2[j])
        j += 1

    return zbirni

def merge_sort(niz):

    duzina = len(niz)

    if duzina == 1:
        return niz

    mid = duzina // 2

    lijevi = niz[:mid]
    desni = niz[mid:]

    lijevi = merge_sort(lijevi)
    desni = merge_sort(desni)

    return merge(lijevi,desni)

def main():
    niz = []
    for i in range(1000):
        niz.append(randint(0, 1000))
    merge_sort = merge_sort(niz)
    print(merge_sort)


if __name__ == "__main__":
    main()














