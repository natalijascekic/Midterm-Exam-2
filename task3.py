"""
===================   TASK 3  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

#rekurzivno sumirati niz

def lista(brojevi):
    lista = 0
    for i in brojevi:
        lista = lista + i
    return lista

def main():

    niz = lista([9,3,5,7,9])
    print("Suma je:", niz)

    pass

if __name__ == "__main__":
    main()