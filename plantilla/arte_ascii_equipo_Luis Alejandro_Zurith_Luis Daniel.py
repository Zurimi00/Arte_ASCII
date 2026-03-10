"""
Generador de Arte ASCII Animado
Proyecto de Animación

Equipo:
- Estudiante 1: [Luis Alejandro Ambriz Cordero] - Menú y Patrones Geométricos
- Estudiante 2: [Zurith Anelis Fierros Garcia] - Generadores de Texto Artístico
- Estudiante 3: [Nombre] - Animaciones

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""
import os
from datetime import datetime

# ============================================
# SECCIÓN 1: MENÚ PRINCIPAL (Estudiante 1)
# ============================================
# Variable para el historial
historial = []

# Función para verificar entradas
def validar_numero(mensaje):
    while True:
        try: return float(input(f"  {mensaje}"))
        except ValueError: print(" X  Error: Ingrese un número válido.")

#Menu con todas las opciones y opciones de historial
def mostrar_menu_principal():
    """Muestra el menú de la galería de arte ASCII"""
    print("\n" + "="*60)
    print("     🎨 GALERÍA DE ARTE ASCII v1.0 🎨")
    print("     Creado por: [Nombres del equipo]")
    print("="*60)
    print("\nGALERÍA:")
    print("1. Patrones Geométricos")
    print("2. Generador de Banner")
    print("3. Marcos Decorativos")
    print("4. Animaciones")
    print("5. Tabla de Multiplicar Visual")
    print("6. Mostrar historial")
    print("7. Borrar historial")
    print("8. Salir")
    print("-"*60)

# GESTIÓN Y ARCHIVOS

#Por el momento el historial solo guarda la categoria y descripcion base de las operaciones de figuras basicas
#No tengo ni la menor idea de como guardar las figuras
def agregar_al_historial(categoria, descripcion):
    global historial
    fecha_hora = datetime.now().strftime("%H:%M:%S")
    # Formato: Hora, Categoria que se eligío, Descripción
    entrada = f"[{fecha_hora}] {categoria}: {descripcion}"
    historial.append(entrada)
    # Almacenar solo las últimas 10 operaciones
    if len(historial) > 10: historial.pop(0)

def mostrar_historial():
    print("\n" + "HISTORIAL RECIENTE " * 2)
    if not historial:
        print("   > El historial está vacío.")
    else:
        for i, registro in enumerate(historial, 1):
            print(f"  {i}. {registro}")

def guardar_historial_archivo():
    if not os.path.exists("datos"): os.makedirs("datos")
    # Guardar historial en archivo al salir
    with open("datos/historial.txt", "w") as archivo:
        for linea in historial: archivo.write(linea + "\n")

def cargar_historial_archivo():
    global historial
    # Cargar historial al iniciar si existe
    if os.path.exists("datos/historial.txt"):
        with open("datos/historial.txt", "r") as archivo:
            historial.extend([linea.strip() for linea in archivo])
            if len(historial) > 10:
                historial[:] = historial[-10:]

def borrar_historial():
  global historial
  #Dar la opción al usuario de borrar el historial, se repite hasta que se ingrese una opcion valida
  while True:
    try:
      opcion_borrar_historial = int(input("Seguro que quieres borrar el historial?\n1 = SI\n2 = NO\n"))

      if opcion_borrar_historial == 1:
        #Esto limpia el historial de la memoria
        historial.clear()
        if os.path.exists("datos/historial.txt"):
          with open("datos/historial.txt", "w") as archivo:
            archivo.write("")  # Vacía el archivo si es que existe
        print("✅ Historial borrado correctamente.")
        return
      elif opcion_borrar_historial == 2:
        #Esto vuelve al menu principal si se decide que no
        return
        #Se imprime si se elige una opcion invalida con numero entero
      else:
        print("Elige una de las opciones validas")
        #Se imprime si se elige una letra como opcion
    except ValueError:
      print("Error: Debes ingresar un número entero")

# ============================================
# SECCIÓN 2: PATRONES GEOMÉTRICOS (Estudiante 1)
# ============================================

#Genera un triangulo de asteriscos con una altura dada
def triangulo(altura):
    for i in range(1, altura + 1):
        print('*' * i)
    pass

#Genera un cuadrado con un espacio en blanco en el interior
def cuadrado(lado):
    for i in range(lado):
        for j in range(lado):
            # Imprime los asterisco en los bordes y deja un espacio en blanco en el interior
            if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        #Salto de linea el final de cada ciclo
        print()
    pass

#Genera una piramede centrada de asteriscos con una altura dada
def piramide(altura):
    for i in range(1, altura + 1):
      Espacios = " " * (altura - i)
      Asteriscos = "*" * (2 * i - 1)
      print(Espacios + Asteriscos)
    pass


#Menu para seleccionar patrones geométricos
def menu_patrones():
    while True:
            print("\n--- PATRONES GEOMÉTRICOS ---")
            print("1. Triángulo")
            print("2. Cuadrado")
            print("3. Pirámide")
            print("4. Volver al menú principal")
            opcion_patrones = input("\nSeleccione una opción (1-4): ")
            if opcion_patrones == "4":
                return
            val = int(validar_numero("\nDe que tamaño quiere su figura?: ")) #Se vuelve un int para no tener problemas
            if opcion_patrones == "1":
                triangulo(val)
                agregar_al_historial("Patrón Geométrico", f"Triangulo de tamaño {val}")
            elif opcion_patrones == "2":
                cuadrado(val)
                agregar_al_historial("Patrón Geométrico", f"Cuadrado de tamaño {val}")
            elif opcion_patrones == "3":
                piramide(val)
                agregar_al_historial("Patrón Geométrico", f"Piramide de tamaño {val}")
            else:
                print("Elige una de las opciones validas")

    pass

# ============================================
# SECCIÓN 3: TEXTO ARTÍSTICO (Estudiante 2)
# ============================================

def generar_banner(texto):
    ancho = len (texto) + 4

    # Construcción del marco
    print("╔" + "═" * ancho + "╗")
    print("║" + " " * ancho + "║")
    print(f"║  {texto}  ║")  # El texto con dos espacios de margen a cada lado
    print("║" + " " * ancho + "║")
    print("╚" + "═" * ancho + "╝")
pass
    


def marco_decorativo(texto, estilo):
    """
    Crea un marco decorativo alrededor del texto.
    """
    ancho = len(texto ) + 4  
    if estilo ==1:
        #estilo simple
        print("╔" + "═" * ancho + "╗")
        print("║" + " " * ancho + "║")
        print(f"║  {texto}  ║")
        print("║" + " " * ancho + "║")
        print("╚" + "═" * ancho + "╝")
    elif estilo ==2:
        #estilo con estrellas
        borde = "★" * (ancho + 2)
        print(borde)
        print(f"★ {texto.center(ancho)} ★")
        print(borde)

    elif estilo ==3:
        #estilo con asteriscos y arrobas 
        borde = "@" + "*" * ancho + "@"
        print(borde)
        print(f"* {texto.center(ancho)} *")
        print(borde)
    else:
        print("Estilo no válido. Por favor seleccione 1, 2 o 3.")
        print(texto)
    pass


def tabla_multiplicar_visual(numero):
    """
    Genera una tabla de multiplicar con formato visual atractivo.
    """
    #Encabezado
    titulo = f"Tabla del {numero}"
    ancho = 20
    print("╔" + "═" * ancho + "╗")
    print(f"║ {titulo.center(ancho - 2)} ║")
    print("╠" + "═" * ancho + "╣")
    #Generar tabla y aliniado
    for i in range(1, 11):
        resultado = numero * i
        #Usamos f-strings para alinnear
        linea = f"{numero} x {i:2} = {resultado:2}"
        print(f"║ {linea.ljust(ancho-2)} ║")
        #Cerrar pie decorativo
    print("╚" + "═" * ancho + "╝")

def menu_texto_artistico():
   while True:
        print("\n--- GENERADORES DE TEXTO ARTÍSTICO ---")
        print("1. Crear Banner")
        print("2. Marco Decorativo")
        print("3. Tabla de Multiplicar")
        print("4. Volver al menú principal")

        opcion_principal = input("\nSeleccione una opción (1-4): ")


        if opcion_principal == "1":
            texto = input("Ingrese el texto para su banner: ")
            generar_banner(texto)
            agregar_al_historial("Texto Artístico", f"Banner: {texto}")
            input("\nPresione Enter para continuar...")

        elif opcion_principal == "2":
            texto = input("Ingrese el texto para el marco: ")
            print("Seleccione un estilo:")
            print("1. Simple  2. Estrellas  3. Asteriscos/Arrobas")
            estilo = int(validar_numero("Estilo: ", 1, 3)) # Usando tu validador
            marco_decorativo(texto, estilo)
            agregar_al_historial("Texto Artístico", f"Marco estilo {estilo}")
            input("\nPresione Enter para continuar...")

        elif opcion_principal == "3":
            # Usamos tu función validar_numero para asegurar que sea entre 1 y 10
            numero = int(validar_numero("Ingrese un número para la tabla (1-10): ", 1, 10))
            tabla_multiplicar_visual(numero)
            agregar_al_historial("Texto Artístico", f"Tabla del {numero}")
            input("\nPresione Enter para continuar...")

        elif opcion_principal == "4": # Re-added to correctly handle returning to main menu
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

pass




# ============================================
# SECCIÓN 4: ANIMACIONES (Estudiante 3)
# ============================================

def crear_retraso(duracion):
    """
    Crea un retraso usando un loop vacío.

    Args:
        duracion (int): Factor de duración (más alto = más lento)
    """
    # TODO: Implementar retraso
    # Usar un loop for que no haga nada
    # Ejemplo: for _ in range(duracion * 100000):
    #              pass

    pass  # Reemplazar con su código


def barra_progreso():
    """Muestra una barra de progreso animada"""
    # TODO: Implementar barra de progreso
    # - Usar un loop de 0 a 100
    # - En cada iteración, mostrar la barra actualizada
    # - Usar caracteres como █ ■ o # para la barra llena
    # - Usar - o espacio para la parte vacía
    # - Mostrar el porcentaje

    # Ejemplo de salida:
    # Procesando...
    # [■■■■■■■■■■----------] 50%
    # [■■■■■■■■■■■■■■■■----] 80%
    # [■■■■■■■■■■■■■■■■■■■■] 100% ¡Completo!

    # Pista: usar end="\r" en print para sobrescribir la misma línea

    pass  # Reemplazar con su código


def animacion_texto_movil():
    """Anima un texto moviéndose de izquierda a derecha"""
    # TODO: Implementar animación de texto
    # - Definir el texto a animar
    # - Usar un loop para cada posición
    # - En cada iteración, imprimir espacios + texto
    # - Incrementar los espacios para simular movimiento
    # - Limpiar la línea anterior con \r

    # Ejemplo:
    # ☆                (frame 1)
    #  ☆               (frame 2)
    #   ☆              (frame 3)
    # ...

    pass  # Reemplazar con su código


def menu_animaciones():
    """Menú para animaciones"""
    print("\n--- ANIMACIONES ---")
    print("1. Barra de Progreso")
    print("2. Texto en Movimiento")
    print("3. Volver al menú principal")

    # TODO: Implementar lógica del menú

    pass  # Reemplazar con su código


# ============================================
# FUNCIONES AUXILIARES
# ============================================

def limpiar_pantalla_simple():
    """Imprime líneas en blanco para simular limpieza de pantalla"""
    # No usamos os.system() porque no está en los módulos 1-6
    print("\n" * 50)


def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔════════════════════════════════════════════════════════════╗")
    print("║           ¡Bienvenido a la Galería de Arte ASCII!         ║")
    print("║                                                            ║")
    print("║    Donde la creatividad se encuentra con la programación  ║")
    print("╚════════════════════════════════════════════════════════════╝")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_patrones()
        elif opcion == "2":
            print("\n--- GENERADOR DE BANNER ---")
            # TODO: Solicitar texto y generar banner
            pass
        elif opcion == "3":
            menu_texto_artistico()
        elif opcion == "4":
            menu_animaciones()
        elif opcion == "5":
            print("\n--- TABLA DE MULTIPLICAR VISUAL ---")
            # TODO: Solicitar número y generar tabla
            pass
        elif opcion == "6":
            print("\n" + "="*60)
            print("  ¡Gracias por visitar la Galería de Arte ASCII!")
            print("  Creado con ❤️  y código por: [Nombres del equipo]")
            print("="*60)
            continuar = False
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

        if continuar and opcion != "6":
            pausar()

    print("\nPrograma terminado. ¡Hasta pronto! 🎨")


# Punto de entrada del programa
if __name__ == "__main__":
    main()