import types
lista=[1,[2,3,4,[5,6,7,[8,9,10]]]]
def função(b, contador):
    for a in b:
        if type(a)==int:
            print((contador * " ") + (str(a)))
        else:
            função(a, contador + 4)
função(lista, 0)