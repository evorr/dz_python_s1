#Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def logical(x,y,z):
    left = not(x or y or z)
    right = not x and not y and not z
    result = left == right
    return result

for x in range(2):
    for y in range (2):
        for z in range(2):
            print(f'x{x} y {y} z {z}')
            print(logical(x,y,z))