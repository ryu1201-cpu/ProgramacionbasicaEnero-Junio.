#Problema 55

tipo = input("¿Crear lista de números o texto? (numeros/texto): ").lower()
lista = []
while True:
    print("\nOpciones:")
    print("1. Agregar valores")
    print("2. Eliminar valores")
    print("3. Ordenar lista directamente")
    print("4. Ordenar lista generando nueva")
    print("5. Verificar elemento y mostrar índices")
    print("6. Calcular estadísticas (solo números)")
    print("7. Salir")
    op = int(input("Elige una opción: "))
    
    if op == 1:
        valor = input("Ingresa el valor a agregar: ")
        if tipo == "numeros":
            try:
                valor = float(valor)
            except ValueError:
                print("Valor no es un número válido")
                continue
        lista.append(valor)
        print("Valor agregado")
    
    elif op == 2:
        sub_op = input("¿Eliminar por índice o valor? (indice/valor): ").lower()
        if sub_op == "indice":
            idx = int(input("Ingresa el índice: "))
            if 0 <= idx < len(lista):
                lista.pop(idx)
                print("Valor eliminado")
            else:
                print("Índice inválido")
        else:
            valor = input("Ingresa el valor a eliminar: ")
            if tipo == "numeros":
                try:
                    valor = float(valor)
                except ValueError:
                    print("Valor no es un número válido")
                    continue
            if valor in lista:
                lista.remove(valor)
                print("Valor eliminado")
            else:
                print("Valor no encontrado")
    
    elif op == 3:
        lista.sort()
        print("Lista ordenada directamente:", lista)
    
    elif op == 4:
        lista_nueva = sorted(lista)
        print("Nueva lista ordenada:", lista_nueva)
        print("Lista original:", lista)
    
    elif op == 5:
        valor = input("Ingresa el elemento a verificar: ")
        if tipo == "numeros":
            try:
                valor = float(valor)
            except ValueError:
                print("Valor no es un número válido")
                continue
        indices = [i for i, elem in enumerate(lista) if elem == valor]
        if indices:
            print(f"Elemento encontrado en los índices: {indices}")
        else:
            print("Elemento no encontrado")
    
    elif op == 6:
        if tipo == "numeros" and lista:
            maximo = max(lista)
            minimo = min(lista)
            suma = sum(lista)
            promedio = suma / len(lista)
            print(f"Máximo: {maximo}, Mínimo: {minimo}, Suma: {suma}, Promedio: {promedio:.2f}")
        else:
            print("Opción solo válida para listas numéricas no vacías")
    
    elif op == 7:
        print("Saliendo...")
        break
    
    else:
        print("Opción inválida")
