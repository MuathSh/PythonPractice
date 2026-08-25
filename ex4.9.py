#Default Argument Values
def f(a, L=5): #any thing we put after the L= , dosen't matter because it is just a workaround so we use a new list every time
    if L == 5:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(1, f(2, f(2))))
