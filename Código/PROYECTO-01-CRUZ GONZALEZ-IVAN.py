from lifestore_file import lifestore_searches #importar la lista que contiene los datos de búsqueda de los productos
from lifestore_file import lifestore_sales #importar la lista que contiene las ventas
from lifestore_file import lifestore_products #importar la lista de productos

#Lista de administradores del sistema
usuarios_lifestore = [["admin","adminlifestore"],["ivanocho","iv4n0ch0"],["root","12345root"]]
#declaración de la variable que controla el flujo del sistema en general
salir = False
#variable para validar al usuario en el sistema
usuario_valido = False
#ciclo que permite validar usuarios para inciar el sistema (ciclo principal)
while usuario_valido == False and salir == False:
    print("\nBienvenidos al sistema LifeStore")
    usuario = input("Escriba su nombre de usuario: ") #variable que recibe el nombre de usuario
    password = input("Escriba su contraseña: ") #variable que recibe la contraseña
    for user_pass in usuarios_lifestore: #ciclo para validar al usuario y contraseña en la listas de usuarios válidos
        if user_pass[0] == usuario and user_pass[1] == password:
            usuario_valido = True
            break
    if usuario_valido == True: #Si el usuario y el password son correctos, el usuario puede ingresar al sistema
        while salir == False: #inicio del While principal
            #Se imprime el menú principal de opciones
            print("\nSeleccione la opción deseada:")
            print("1) Productos más vendidos y productos rezagados")
            print("2) Productos por reseña en el servicio")
            print("3) Totales")
            print("4) Salir")
            opcion = input("\nTeclear la opción: ") #Se pide que ingrese una opción válida
            if opcion == "4": #Si la opción es Salir
                opcion_valida = False #variable que valida si la opción seleccionada es correcta
                while opcion_valida == False: #ciclo que verifica si el usuario desea salir del sistema
                    salida = input("\n¿Estás seguro que deseas salir? (S/N): ")
                    if (salida == "S") or (salida == "s"):
                        salir = True
                        opcion_valida = True
                    elif (salida == "N") or (salida == "n"):
                        salir = False
                        opcion_valida = True
                    else:
                        print("\n¡opción incorrecta!")

            elif opcion == "1": #Productos más vendidos y productos rezagados
                menu_principal = False
                opcion_valida = False
                while menu_principal == False and opcion_valida == False: #mientras no regrese al menú principal o la opción no sea la correcta
                    print("\na)  50 productos con mayores ventas")
                    print("b) 100 productos con mayores búsquedas")
                    print("c)  50 productos con menores ventas por categoría")
                    print("d) 100 productos con menores búsquedas por categoría")
                    print("e) Regresar al menú principal")
                    opcion= input("\nTeclear la opción: ")

                    if opcion == "a" or opcion == "A": #50 productos con mayores ventas
                        lifestore_50_most_sales = [] #Lista que contendrá los 50 productos más vendidos
                        for producto_catalogo in lifestore_products: #ciclo para recorrer el catálogo de productos
                            vendidos = 0 #variable que llevará el conteo de productos vendidos
                            monto_vendido = 0 #variable que llevará la suma en monto de lo vendido
                            for producto_venta in lifestore_sales: #ciclo para recorrer el listado de ventas
                                if producto_catalogo[0] == producto_venta[1]: #si las claves de producto coinciden, cuenta como vendido
                                    vendidos += 1
                                    monto_vendido += producto_catalogo[2]
                            lifestore_50_most_sales.append([producto_catalogo[0],producto_catalogo[1],vendidos, producto_catalogo[4], monto_vendido]) #agrega el item calculado a la lista
                        #ordenar de mayor a menor venta
                        #a continuación, se tiene el código para ordenar por inserción. Este código se replica a lo largo de la implementación del sistema.
                        #el algoritmo para ordenar es el de insersión mediante recorrido de la lista
                        n = len(lifestore_50_most_sales)          #calcula la longitud de la lista
                        for i in range(1, n):                     #ciclo para recorrer la lista
                            valor = lifestore_50_most_sales[i][2] #variable que guarda el valor a comparar
                            aux =  lifestore_50_most_sales[i]     #variable auxiliar para guardar el registro a comparar
                            j = i                                 #el índice j se iguala a la posición actual del índice i
                            #mientras el índice j sea mayor que cero y el valor actual de la lista en la posición j-1 sea menor que el valor comparado
                            while j > 0 and lifestore_50_most_sales[j-1][2] < valor:
                                lifestore_50_most_sales[j] = lifestore_50_most_sales[j-1] #mueve el registro de la posición j a la j-1
                                j -=1                                                     #decrementa el índice j
                            lifestore_50_most_sales[j] = aux #actualiza la posición j de la lista con el valor del registro auxiliar
                        #termina de ordenar la lista mediante el recorrido de la misma
                        lifestore_50_most_sales = lifestore_50_most_sales[0:50] #limita la lista a los 50 primeros items (inclusive si su número de ventas es 0)
                        i = 1 #variable que lleva el conteo de productos en el listado
                        monto_total_vendido = 0 #variable que llevará la suma del monto total de los 50 productos
                        stock_total_restante = 0 #variable que llevará la suma del stock  total restante
                        stock_total_vendido = 0#variable que llevará la suma del stock total vendido
                        for mas_vendidos in lifestore_50_most_sales: #ciclo para imprimir la lista
                            #si el valor es igual a cero (o sea, no hay registro alguno de venta) entonces, desplegar
                            #el resto de elementos ya no tiene razón de ser y por lo tanto, se debe de truncar el desplegado
                            if mas_vendidos[2] == 0:
                                break
                            print("\nProducto No. ", i)
                            print("Id: ", mas_vendidos[0])
                            print("Producto: ", mas_vendidos[1])
                            print("Vendidos: ", mas_vendidos[2])
                            print("Monto vendido: ", mas_vendidos[4])
                            print("Stock: ", mas_vendidos[3])
                            print("-----------------------------------------------------------------------------------------")
                            i += 1
                            monto_total_vendido += mas_vendidos[4]
                            stock_total_restante += mas_vendidos[3]
                            stock_total_vendido += mas_vendidos[2]
                        print("\nValor total de las ventas: ", monto_total_vendido)
                        print("Stock total restante: ", stock_total_restante)
                        print("Stock total vendido: ", stock_total_vendido)
                        print("++++++++++++++++++++++++++++++++++++")

                    elif opcion == "b" or opcion == "B": #100 productos con mayores búsquedas
                        lifestore_100_most_search = [] #lista que contendrá los 100 productos con mayores búsquedas
                        for producto_catalogo in lifestore_products: #ciclo para recorrer el catálogo de productos
                            search = 0 #variable que cuenta cuántas veces aparece en una búsqueda
                            for producto_buscado in lifestore_searches: #ciclo para recorrer el listado de búsquedas
                                if producto_catalogo[0] == producto_buscado[1]: #si las claves de producto coinciden, cuenta una búsqueda
                                    search += 1
                            lifestore_100_most_search.append([producto_catalogo[0],producto_catalogo[1],search, producto_catalogo[4]]) #agrega el item calculado a la lista
                        #ordenar de mayor a menor
                        n = len(lifestore_100_most_search) #calcula la longitud de la lista
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_100_most_search[i][2]
                            aux =  lifestore_100_most_search[i]
                            j = i
                            while j > 0 and lifestore_100_most_search[j-1][2] < valor:
                                lifestore_100_most_search[j] = lifestore_100_most_search[j-1]
                                j -=1
                            lifestore_100_most_search[j] = aux
                        #fin del ciclo para ordenar
                        lifestore_100_most_search = lifestore_100_most_search[0:100] #trunca la lista a los primeros 100 elementos
                        i = 1 #variable para llevar el conteo de productos en la lista de reporte
                        for mas_buscados in lifestore_100_most_search: #ciclo para imprimir la lista
                            #si el valor es igual a cero (o sea, no hay registro alguno de búsqueda) entonces, desplegar
                            #el resto de elementos ya no tiene razón de ser y por lo tanto, se debe de truncar el desplegado
                            if mas_buscados[2] == 0:
                                break
                            print("\nProducto No. ",i)
                            print("Id: ", mas_buscados[0])
                            print("Producto: ", mas_buscados[1])
                            print("No.de búsquedas: ", mas_buscados[2])
                            print("Stock: ", mas_buscados[3])
                            print("-----------------------------------------------------------------------------------------")
                            i += 1
                        print("++++++++++++++++++++++++++++++++++++")

                    elif opcion == "c" or opcion == "C": #50 productos menos vendidos por categoría
                        lifestore_50_less_sales_by_c = [] #Lista que contendrá los 50 productos menos vendidos ordenados por categoría
                        for producto_catalogo in lifestore_products: #ciclo para recorrer el catálogo de productos
                            vendidos = 0 #variable para contar el número de productos vendidos
                            monto_menos_vendidos = 0 #variable asigna el precio unitario del producto
                            for producto_venta in lifestore_sales: #ciclo para recorrer el listado de ventas
                                if producto_catalogo[0] == producto_venta[1]: #si las claves de producto coinciden, cuenta como venta
                                    vendidos += 1
                            monto_menos_vendidos = producto_catalogo[2]
                            #agrega el item calculado a la lista
                            lifestore_50_less_sales_by_c.append([producto_catalogo[0],producto_catalogo[1],producto_catalogo[3], vendidos,producto_catalogo[4], monto_menos_vendidos])
                        #ordenar por menor venta
                        n = len(lifestore_50_less_sales_by_c) #calcula la longitud de la lista
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_50_less_sales_by_c[i][3]
                            aux =  lifestore_50_less_sales_by_c[i]
                            j = i
                            while j > 0 and lifestore_50_less_sales_by_c[j-1][3] > valor:
                                lifestore_50_less_sales_by_c[j] = lifestore_50_less_sales_by_c[j-1]
                                j -=1
                            lifestore_50_less_sales_by_c[j] = aux
                        lifestore_50_less_sales_by_c = lifestore_50_less_sales_by_c[0:50] #Trunca la lista a los 50 primeros elementos
                        #ordenar por cada categoría
                        n = len(lifestore_50_less_sales_by_c) #calcula la longitud de la lista
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_50_less_sales_by_c[i][2]
                            aux =  lifestore_50_less_sales_by_c[i]
                            j = i
                            while j > 0 and lifestore_50_less_sales_by_c[j-1][2] > valor:
                                lifestore_50_less_sales_by_c[j] = lifestore_50_less_sales_by_c[j-1]
                                j -=1
                            lifestore_50_less_sales_by_c[j] = aux
                        cambio = "" #variable que compara si existe un cambio de categoría durante el recorrido para imprimir
                        i = 1 #variable que lleva el conteo de productos en el listado
                        subtotales = False #variable que controla la impresión de subtotales por categoría
                        total_stock = 0 #variable que lleva la suma total del stock de los 50 productos menos vendidos
                        total_monto = 0 #variable que lleva la suma total del monto equivalente del stock
                        for menos_vendidos_x_c in lifestore_50_less_sales_by_c: #ciclo para imprimir la lista por categoría
                            #si existe un cambio de categoría durante el despliegue, imprime un separador para indicar el cambio
                            if cambio != menos_vendidos_x_c[2]:
                                if subtotales == True:
                                    print("\nTotal en stock de esta categoría: ", stock_menos_vendidos_x_cat)
                                    print("Valor del stock en esta categoría: ", monto_menos_vendidos_x_cat)
                                    total_stock += stock_menos_vendidos_x_cat
                                    total_monto += monto_menos_vendidos_x_cat
                                print("-----------------------------------------------------------------------------------------")
                                print(menos_vendidos_x_c[2])
                                print("-----------------------------------------------------------------------------------------")
                                cambio = menos_vendidos_x_c[2]
                                monto_menos_vendidos_x_cat = 0 #variable que llevará la suma del monto de productos no vendidos por cat
                                stock_menos_vendidos_x_cat = 0 #variable que llevará la suma del stock de productos menos vendidos por categoría
                                subtotales = True
                            print("\nProducto No: ", i)
                            print("Id: ",menos_vendidos_x_c[0])
                            print("Producto: ",menos_vendidos_x_c[1])
                            print("Ventas: ", menos_vendidos_x_c[3])
                            print("Stock: ", menos_vendidos_x_c[4])
                            monto_menos_vendidos_x_cat += menos_vendidos_x_c[5] * menos_vendidos_x_c[4]
                            stock_menos_vendidos_x_cat += menos_vendidos_x_c[4]
                            i += 1
                        print("\nTotal en stock de esta categoría: ", stock_menos_vendidos_x_cat)
                        print("Valor del stock de esta categoría: ", monto_menos_vendidos_x_cat)
                        print("\n++++++++++++++++++++++++++++++++++++")
                        total_stock += stock_menos_vendidos_x_cat
                        total_monto += monto_menos_vendidos_x_cat
                        print("Stock total del listado: ", total_stock)
                        print("Valor del stock del listado: ", total_monto)

                    elif opcion == "d" or opcion == "D": #100 productos con menores búsquedas
                        lifestore_100_less_search_by_c = [] #lista que contendrá los 100 productos con menores búsquedas
                        for producto_catalogo in lifestore_products: #ciclo para recorrer el catálogo de productos
                            search = 0 #variable que lleva el conteo de búsquedas
                            for producto_buscado in lifestore_searches: #ciclo para recorrer el listado de búsquedas
                                if producto_catalogo[0] == producto_buscado[1]: #si las claves de producto coinciden, cuenta como búsqueda
                                    search += 1
                            lifestore_100_less_search_by_c.append([producto_catalogo[0],producto_catalogo[1],producto_catalogo[3],search,producto_catalogo[4]]) #agrega el item calculado a la lista
                        #ordenar de menor a mayor
                        n = len(lifestore_100_less_search_by_c) #calcula la longitud de la lista
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_100_less_search_by_c[i][3]
                            aux   = lifestore_100_less_search_by_c[i]
                            j = i
                            while j > 0 and lifestore_100_less_search_by_c[j-1][3] > valor:
                                lifestore_100_less_search_by_c[j] = lifestore_100_less_search_by_c[j-1]
                                j -=1
                            lifestore_100_less_search_by_c[j] = aux
                        lifestore_100_less_search_by_c = lifestore_100_less_search_by_c[0:100]
                        #y luego, ordenar por categoría
                        n = len(lifestore_100_less_search_by_c) #calcula la longitud de la lista
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_100_less_search_by_c[i][2]
                            aux =  lifestore_100_less_search_by_c[i]
                            j = i
                            while j > 0 and lifestore_100_less_search_by_c[j-1][2] > valor:
                                lifestore_100_less_search_by_c[j] = lifestore_100_less_search_by_c[j-1]
                                j -=1
                            lifestore_100_less_search_by_c[j] = aux
                        cambio = "" #variable para detectar un cambio de categoría durante la impresión
                        i = 1
                        for menos_buscados_x_c in lifestore_100_less_search_by_c: #ciclo para imprimir la lista por categoría
                            if cambio != menos_buscados_x_c[2]: #si hay un cambio de categoría, imprimir separación de bloque
                                print("-----------------------------------------------------------------------------------------")
                                print(menos_buscados_x_c[2])
                                print("-----------------------------------------------------------------------------------------")
                                cambio = menos_buscados_x_c[2]
                            print("\nProducto No: ", i)
                            print("Id: ",menos_buscados_x_c[0])
                            print("Producto: ",menos_buscados_x_c[1])
                            print("Búsquedas: ", menos_buscados_x_c[3])
                            print("Stock: ", menos_buscados_x_c[4])
                            i += 1
                        print("++++++++++++++++++++++++++++++++++++")

                    elif opcion == "e" or opcion == "E": #volver al menú principal
                        menu_principal = True
                        opcion_valida = True
                    else:
                        print("\n¡opción incorrecta!")

            elif opcion == "2": #Productos por reseña en el servicio
                menu_principal = False
                opcion_valida = False
                while menu_principal == False and opcion_valida == False: #mientras entre al menú o la opción tecleada no sea válida
                    print("\na)  20 productos con mejores reseñas")
                    print("b)  20 productos con peores reseñas")
                    print("c) Regresar al menú principal")
                    opcion= input("\nTeclear la opción: ")

                    if opcion == "a" or opcion == "A": #20 productos con mejores reseñas
                        lifestore_20_best_score = [] #Lista que contendrá los 20 productos con mejor reseña
                        for producto_catalogo in lifestore_products: #ciclo para recorrer el catálogo de productos
                            score = 0 #variable que cuenta el score de reseña del producto
                            no_productos = 0 #variable que cuenta el número de productos
                            devoluciones = 0 #variable que cuenta el número de devolucioness
                            for producto_venta in lifestore_sales: #ciclo para recorrer el listado de ventas
                                if producto_catalogo[0] == producto_venta[1]: #si las claves de producto coinciden, suma el score de reseña
                                    if producto_venta[4] == 1: #si el producto tiene una devolución, contar la devolución
                                        devoluciones += 1
                                    score += producto_venta[2] #suma el score de reseña
                                    no_productos += 1 #suma la cantidad de productos
                            if no_productos == 0: #si el número de productos es cero, el cálculo del score de reseñas es cero (para evitar la división entre cero)
                                lifestore_20_best_score.append([producto_catalogo[0],producto_catalogo[1],0,devoluciones,producto_catalogo[4]]) #agrega el item calculado a la lista
                            else: #de otro modo, se calcula la división sin problema
                                lifestore_20_best_score.append([producto_catalogo[0],producto_catalogo[1],score/no_productos,devoluciones,producto_catalogo[4]]) #agrega el item calculado a la lista

                        #ordenar lista de productos de mejor a peor reseña
                        n = len(lifestore_20_best_score) #calcula la longitud de la lista
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_20_best_score[i][2]
                            aux =  lifestore_20_best_score[i]
                            j = i
                            while j > 0 and lifestore_20_best_score[j-1][2] < valor:
                                lifestore_20_best_score[j] = lifestore_20_best_score[j-1]
                                j -=1
                            lifestore_20_best_score[j] = aux
                        #luego, ordena de menor a mayor número de devoluciones
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_20_best_score[i][3]
                            aux =  lifestore_20_best_score[i]
                            j = i
                            while j > 0 and lifestore_20_best_score[j-1][3] > valor:
                                lifestore_20_best_score[j] = lifestore_20_best_score[j-1]
                                j -=1
                            lifestore_20_best_score[j] = aux
                        lifestore_20_best_score = lifestore_20_best_score[0:20] #limita la lista a los 20 primeros elementos
                        i = 1 #variable para contar el número de productos listados
                        for mejor_reseña in lifestore_20_best_score: #ciclo para imprimir la lista
                            if mejor_reseña[2] == 0: #sí los productos tienen score 0, no tiene sentido que aparezcan en la lista
                                break
                            print("\nProducto No. ", i)
                            print("Id: ", mejor_reseña[0])
                            print("Producto: ", mejor_reseña[1])
                            print("Rate de reseñas: ", mejor_reseña[2])
                            print("Devoluciones: ", mejor_reseña[3])
                            print("Stock: ", mejor_reseña[4])
                            print("-----------------------------------------------------------------------------------------")
                            i += 1
                        print("++++++++++++++++++++++++++++++++++++")

                    elif opcion == "b" or opcion == "B":
                        lifestore_20_worst_score = [] #Lista que contendrá los 20 productos con peor reseña
                        for producto_catalogo in lifestore_products: #ciclo para recorrer el catálogo de productos
                            score = 0 #variable que sumará el score
                            no_productos = 0 #variable que contará el número de productos
                            devoluciones = 0 #variable que contará el número de devoluciones
                            for producto_venta in lifestore_sales: #ciclo para recorrer el listado de ventas
                                if producto_catalogo[0] == producto_venta[1]: #si las claves de producto coinciden, suma el score
                                    if producto_venta[4] == 1: #si el producto tiene decolución, se cuentan las devoluciones
                                        devoluciones += 1
                                    score += producto_venta[2]
                                    no_productos += 1
                            #si el conteo de productos fue cero, se pone a cero el promedio del score para evitar división por cero
                            if no_productos == 0:
                                lifestore_20_worst_score.append([producto_catalogo[0],producto_catalogo[1],0,devoluciones,producto_catalogo[4]])
                            else:
                                lifestore_20_worst_score.append([producto_catalogo[0],producto_catalogo[1],score/no_productos,devoluciones,producto_catalogo[4]])

                        #ordenar de peor a mejor reseña
                        n = len(lifestore_20_worst_score) #calcula la longitud de la lista
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_20_worst_score[i][2]
                            aux =  lifestore_20_worst_score[i]
                            j = i
                            while j > 0 and lifestore_20_worst_score[j-1][2] > valor:
                                lifestore_20_worst_score[j] = lifestore_20_worst_score[j-1]
                                j -=1
                            lifestore_20_worst_score[j] = aux
                        #y luego, ordena de mayor a menor devoluciones
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = lifestore_20_worst_score[i][3]
                            aux =  lifestore_20_worst_score[i]
                            j = i
                            while j > 0 and lifestore_20_worst_score[j-1][3] < valor:
                                lifestore_20_worst_score[j] = lifestore_20_worst_score[j-1]
                                j -=1
                            lifestore_20_worst_score[j] = aux
                        lifestore_20_worst_score = lifestore_20_worst_score[0:20] #limita la lista a los 50 primeros elementos
                        i = 1 #variable para contar el número de productos de la lista
                        for peor_reseña in lifestore_20_worst_score: #ciclo para imprimir la lista
                            print("\nProducto No. ", i)
                            print("Id: ", peor_reseña[0])
                            print("Producto: ", peor_reseña[1])
                            print("Rate de reseñas: ", peor_reseña[2])
                            print("Devoluciones: ", peor_reseña[3])
                            print("Stock: ", peor_reseña[4])
                            print("-----------------------------------------------------------------------------------------")
                            i += 1
                        print("++++++++++++++++++++++++++++++++++++")

                    elif opcion == "c" or opcion == "C": #si la opción es regresar al menú principal
                        menu_principal = True
                        opcion_valida = True
                    else:
                        print("\n¡opción incorrecta!")

            elif opcion == "3": #opción para mostrar el menú de ventas por mes y año
                menu_principal = False
                opcion_valida = False
                while menu_principal == False and opcion_valida == False: #mientras entre al menú o la opción tecleada sea inválida
                    print("\na)  Total de ingresos y ventas promedio mensuales")
                    print("b)  Total anual y meses con más ventas al año")
                    print("c) Regresar al menú principal")
                    opcion= input("\nTeclear la opción: ")
                    #inicia el cálculo por mes
                    total_sales_month = [] #lista que contendrá los totales por mes
                    #variables para sumar las ventas por mes del producto
                    vent_en = vent_feb = vent_mar = vent_abr = vent_may = vent_jun = 0
                    vent_jul = vent_ago = vent_sep = vent_oct = vent_nov = vent_dic = 0
                    #variables para sumar la cantidad de productos vendidos en el mes
                    vendido_en = vendido_feb = vendido_mar = vendido_abr = vendido_may = vendido_jun = 0
                    vendido_jul = vendido_ago = vendido_sep = vendido_oct = vendido_nov = vendido_dic = 0
                    for producto_catalogo in lifestore_products: #ciclo para recorrer el listado de productos
                        for producto_venta in lifestore_sales: #ciclo para recorrer el listado de ventas
                            #si el producto coincide con el registro de venta y el año corresponde a 2020
                            if producto_catalogo[0] == producto_venta[1] and int(producto_venta[3][6:10]) == 2020:
                                #si el producto no tiene devolución, entonces se suma al total de venta del mes correspondiente
                                if producto_venta[4] != 1:
                                    #si el mes corresponde a enero, suma la venta a enero y cuenta la venta
                                    if int(producto_venta[3][3:5]) == 1:
                                        vent_en += producto_catalogo[2]
                                        vendido_en +=1
                                    #si el mes corresponde a febrero, suma la venta a febrero y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 2:
                                        vent_feb += producto_catalogo[2]
                                        vendido_feb += 1
                                    #si el mes corresponde a marzo, suma la venta a marzo y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 3:
                                        vent_mar += producto_catalogo[2]
                                        vendido_mar += 1
                                    #si el mes corresponde a abril, suma la venta a abril y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 4:
                                        vent_abr += producto_catalogo[2]
                                        vendido_abr += 1
                                    #si el mes corresponde a mayo, suma la venta a mayo y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 5:
                                        vent_may += producto_catalogo[2]
                                        vendido_may += 1
                                    #si el mes corresponde a junio, suma la venta a junio y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 6:
                                        vent_jun += producto_catalogo[2]
                                        vendido_jun += 1
                                    #si el mes corresponde a julio, suma la venta a julio y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 7:
                                        vent_jul += producto_catalogo[2]
                                        vendido_jul += 1
                                    #si el mes corresponde a agosto, suma la venta a agosto y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 8:
                                        vent_ago += producto_catalogo[2]
                                        vendido_ago += 1
                                    #si el mes corresponde a septiembre, suma la venta a septiembre y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 9:
                                        vent_sep += producto_catalogo[2]
                                        vendido_sep += 1
                                    #si el mes corresponde a octubre, suma la venta a octubre y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 10:
                                        vent_oct += producto_catalogo[2]
                                        vendido_oct += 1
                                    #si el mes corresponde a noviembre, suma la venta a noviembre y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 11:
                                        vent_nov += producto_catalogo[2]
                                        vendido_nov += 1
                                    #si el mes corresponde a diciembre, suma la venta a diciembre y cuenta la venta
                                    elif int(producto_venta[3][3:5]) == 12:
                                        vent_dic += producto_catalogo[2]
                                        vendido_dic += 1
                    #validar si las ventas no fueron cero, para evitar la división por cero en el cálculo del promedio
                    #e introducirlas en la lista correspondiente para posteriormente imprimirlas
                    if vendido_en == 0:
                        total_sales_month.append(['Enero',vent_en,0])
                    else:
                        total_sales_month.append(['Enero',vent_en,vent_en/vendido_en])
                    if vendido_feb == 0:
                        total_sales_month.append(['Febrero',vent_feb,0])
                    else:
                        total_sales_month.append(['Febrero',vent_feb,vent_feb/vendido_feb])
                    if vendido_mar == 0:
                        total_sales_month.append(['Marzo',vent_mar,0])
                    else:
                        total_sales_month.append(['Marzo',vent_mar,vent_mar/vendido_mar])
                    if vendido_abr == 0:
                        total_sales_month.append(['Abril',vent_abr,0])
                    else:
                        total_sales_month.append(['Abril',vent_abr,vent_abr/vendido_abr])
                    if vendido_may == 0:
                        total_sales_month.append(['Mayo',vent_may,0])
                    else:
                        total_sales_month.append(['Mayo',vent_may,vent_may/vendido_may])
                    if vendido_jun == 0:
                        total_sales_month.append(['Junio',vent_jun,0])
                    else:
                        total_sales_month.append(['Junio',vent_jun,vent_jun/vendido_jun])
                    if vendido_jul == 0:
                        total_sales_month.append(['Julio',vent_jul,0])
                    else:
                        total_sales_month.append(['Julio',vent_jul,vent_jul/vendido_jul])
                    if vendido_ago == 0:
                        total_sales_month.append(['Agosto',vent_ago,0])
                    else:
                        total_sales_month.append(['Agosto',vent_ago,vent_ago/vendido_ago])
                    if vendido_sep == 0:
                        total_sales_month.append(['Septiembre',vent_sep,0])
                    else:
                        total_sales_month.append(['Septiembre',vent_sep,vent_sep/vendido_sep])
                    if vendido_oct == 0:
                        total_sales_month.append(['Octubre',vent_oct,0])
                    else:
                        total_sales_month.append(['Octubre',vent_oct,vent_oct/vendido_oct])
                    if vendido_nov == 0:
                        total_sales_month.append(['Noviembre',vent_nov,0])
                    else:
                        total_sales_month.append(['Noviembre',vent_nov,vent_nov/vendido_nov])
                    if vendido_dic == 0:
                        total_sales_month.append(['Diciembre',vent_dic,0])
                    else:
                        total_sales_month.append(['Diciembre',vent_dic,vent_dic/vendido_dic])
                    if opcion == "a" or opcion == "A": #total de ingresos y venta mensual promedio
                        for ventas_mensuales_promedios in total_sales_month: #ciclo para imprimir la lista
                            print("\n++++++++++++++++++++++++++++++++++++")
                            print("Mes: ",ventas_mensuales_promedios[0] )
                            print("Venta mensual: ", ventas_mensuales_promedios[1])
                            print("Venta mensual promedio: ", ventas_mensuales_promedios[2])

                    elif opcion == "b" or opcion == "B": #total anual y meses con mayor número de ventas
                        venta_anual = vent_en + vent_feb + vent_mar + vent_abr + vent_may + vent_jun + vent_jul + vent_ago + vent_sep + vent_oct + vent_nov + vent_dic
                        #ordenar las ventas mensuales de mayor a menor
                        n = len(total_sales_month) #calcula la longitud de la lista
                        for i in range(1, n): #ciclo para recorrer la lista
                            valor = total_sales_month[i][1]
                            aux =  total_sales_month[i]
                            j = i
                            while j > 0 and total_sales_month[j-1][1] < valor:
                                total_sales_month[j] = total_sales_month[j-1]
                                j -=1
                            total_sales_month[j] = aux
                        #ciclo para imprimir la lista de ventas mensuales
                        for venta_mensual in total_sales_month:
                            #si la venta fue igual a cero, no tiene sentido seguir imprimiento elementos
                            if venta_mensual[1] == 0:
                                break
                            print("\n+++++++++++++++++++++++++++++++++++++++")
                            print("Mes: ", venta_mensual[0])
                            print("Monto de venta: ", venta_mensual[1])
                        print("\nTotal de ventas anuales: ", venta_anual)

                    elif opcion == "c" or opcion == "C": #regresar al menú principal
                        menu_principal = True
                        opcion_valida = True
                    else:
                        print("\n¡opción incorrecta!")
            else: #si se teclea una opción no válida desde el menú
                print("\n¡opción incorrecta!")

    else: #En caso de que el usuario y/o el password no sean correctos
        print("\nUsuario o password incorrecto.")
        opcion_valida_user_psw = False
        #mientras no sea válida la opción de sí o no
        while opcion_valida_user_psw == False:
            salida = input("\n¿Deseas intentar con otro usuario/password de nuevo? (S/N): ")
            if (salida == "S") or (salida == "s"): #sale de la iteración para preguntar por usuario y contraseña de nuevo
                opcion_valida_user_psw = True
            elif (salida == "N") or (salida == "n"): #sale del sistema
                opcion_valida_user_psw = True
                salir = True
            else:
                print("\n¡opción incorrecta!")
#fin del While que itera el sistema
