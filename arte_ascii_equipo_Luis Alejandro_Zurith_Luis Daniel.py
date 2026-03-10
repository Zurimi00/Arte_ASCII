"""
Generador de Arte ASCII Animado
Proyecto de Animación

Equipo:
- Estudiante 1: [Luis Alejandro Ambriz Cordero] - Menú y Patrones Geométricos
- Estudiante 2: [Nombre] - Generadores de Texto Artístico
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
    """
    Genera un banner con el texto ingresado.

    Args:
        texto (str): Texto a convertir en banner
    """
    # TODO: Implementar banner grande
    # Opción simple: crear un marco alrededor del texto
    # Opción avanzada: convertir cada letra a ASCII art grande

    # Ejemplo simple:
    # ╔══════════════════════╗
    # ║                      ║
    # ║     HOLA MUNDO       ║
    # ║                      ║
    # ╚══════════════════════╝

    pass  # Reemplazar con su código


def marco_decorativo(texto, estilo):
    """
    Crea un marco decorativo alrededor del texto.

    Args:
        texto (str): Texto a enmarcar
        estilo (int): Tipo de estilo (1, 2, o 3)
    """
    # TODO: Implementar diferentes estilos de marcos
    # Estilo 1: Simple con ═ ║
    # Estilo 2: Doble con bordes decorativos
    # Estilo 3: Con asteriscos o caracteres especiales

    # Caracteres útiles:
    # ═ ║ ╔ ╗ ╚ ╝ (estilo 1)
    # ★ ☆ (estilo 2)
    # * # @ (estilo 3)

    pass  # Reemplazar con su código


def tabla_multiplicar_visual(numero):
    """
    Genera una tabla de multiplicar con formato visual atractivo.

    Args:
        numero (int): Número para generar la tabla (1-10)
    """
    # TODO: Implementar tabla decorada
    # - Crear encabezado decorativo
    # - Generar tabla del 1 al 10
    # - Alinear números correctamente
    # - Cerrar con pie decorativo

    # Ejemplo:
    # ╔════════════════════════╗
    # ║  TABLA DEL 5           ║
    # ╠════════════════════════╣
    # ║  5 x  1 =  5           ║
    # ║  5 x  2 = 10           ║
    # ║  ...                   ║
    # ╚════════════════════════╝

    pass  # Reemplazar con su código


def menu_texto_artistico():
    """Menú para generadores de texto artístico"""
    print("\n--- GENERADORES DE TEXTO ---")
    print("1. Crear Banner")
    print("2. Marco Decorativo")
    print("3. Tabla de Multiplicar")
    print("4. Volver al menú principal")

    # TODO: Implementar lógica del menú

    pass  # Reemplazar con su código


# ============================================
# SECCIÓN 4: ANIMACIONES (Estudiante 3: Missa)
# ============================================

def crear_retraso(duracion):
    """
    Crea un retraso usando un loop vacío.
    Ajustado para procesadores rápidos (Apple M1).
    """
    # Factor de 2,000,000 para que la animación sea visible al ojo humano
    for _ in range(duracion * 2000000):
        pass


def barra_progreso():
    """Muestra una barra de progreso animada"""
    print("\n📦 Iniciando descarga de recursos...")
    ancho_barra = 20

    for i in range(101):
        # Cálculo de bloques llenos (█) y vacíos (-)
        lleno = int((i / 100) * ancho_barra)
        vacio = ancho_barra - lleno

        # \r mueve el cursor al inicio de la línea para sobrescribir
        barra = "█" * lleno + "-" * vacio
        print(f"\rProgreso: [{barra}] {i}%", end="")

        crear_retraso(1)

    print("\n\n✅ ¡Proceso finalizado con éxito!")
    # Se integra con la función de historial del Estudiante 1
    agregar_al_historial("Animación", "Barra de progreso ejecutada")


def animacion_texto_movil():
    """Anima un cohete moviéndose de izquierda a derecha"""
    objeto = "🚀"
    espacios_maximos = 35

    print("\n🚀 Preparando lanzamiento:")
    for i in range(espacios_maximos):
        # Multiplicamos el string de espacio " " por el índice i para mover el objeto
        print(f"\r{' ' * i}{objeto}", end="")
        crear_retraso(3)
    for i in range(espacios_maximos):
        # Multiplicamos el string de espacio " " por el índice i para mover el objeto
        print(f"\r{' ' * i}{objeto}", end="")
        crear_retraso(3)

        # --- LÍNEA 294 (Nueva) ---
    print(" 💥 ¡BOOM! 💥")

    print("\n\n✨ ¡oh no el cohete choco con un asteroide .")
    agregar_al_historial("Animación", "Lanzamiento de cohete móvil")


def menu_animaciones():
    """Menú interactivo exclusivo para la sección de animaciones"""
    while True:
        print("\n" + "•" * 30)
        print("      SISTEMA DE ANIMACIONES")
        print("•" * 30)
        print("1. Ejecutar Barra de Progreso")
        print("2. Iniciar Animación de Cohete")
        print("3. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            barra_progreso()
        elif opcion == "2":
            animacion_texto_movil()
        elif opcion == "3":
            print("Saliendo de la sección de animaciones...")
            break
        else:
            print("❌ Error: Opción invalida vuelve a ponerlo .")


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