i = int(input("Introduce cantidad de numeros a realizar kaprekar: "))
for l in range(i):

    tab = []
    loop = 'loop'
# La lista tab va a contener los números ingresados.
# La variable loop va ser para una mejor redacción.

    def asc(n):
    # Ordena los dígitos en forma ascendente...
        return int(''.join(sorted(str(n))))

    def desc(n):
    # ...Ordena los dígitos de forma descendente
        return int(''.join(sorted(str(n))[::-1]))
    print(f"Ciclo: {l+1} ")
    n = input("Introduce un numero de 4 dígitos: ")
    n = int(n)

    if n>999 and n<10000:#Tiene que ser un número de 4 cifras.
        print("\nCargando...", str(n) + ":")


        while True:
    # Itera el programa, asignando la diferencia entre los valores.
            print(desc(n), "-", asc(n), " =", desc(n)-asc(n))
            n = desc(n) - asc(n)

            if n not in tab:
        # Chequea si el numero aparece en tab o no, si no aparece lo agrega.
                tab.append(n)
            else:

                if tab.index(n) == len(tab)-1:
        # Si éste se encuentra al último, es una constante Kaprekar.
                    tab = []
                    tab.append(n)
                    loop = 'constante'
                else:
        
                    tab = tab[tab.index(n):]
            

            break

        print('Kaprekar', loop, 'resultado:', tab)
 
    else:
        print("Número no válido")


