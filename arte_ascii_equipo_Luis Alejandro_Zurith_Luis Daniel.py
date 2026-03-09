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

def triangulo(altura):
    """
    Genera un triángulo de asteriscos de altura especificada.

    Args:
        altura (int): Número de filas del triángulo
    """
    # TODO: Implementar
    # Usar un loop for con range(1, altura + 1)
    # Cada fila debe tener i asteriscos
    # Ejemplo: si altura=5
    # *
    # **
    # ***
    # ****
    # *****

    pass  # Reemplazar con su código


def cuadrado(lado):
    """
    Genera un cuadrado con bordes de tamaño especificado.

    Args:
        lado (int): Tamaño del lado del cuadrado
    """
    # TODO: Implementar
    # - Primera fila: todos asteriscos o símbolos
    # - Filas del medio: símbolo, espacios, símbolo
    # - Última fila: todos asteriscos o símbolos
    # Ejemplo: cuadrado(5)
    # *****
    # *   *
    # *   *
    # *   *
    # *****

    pass  # Reemplazar con su código


def piramide(altura):
    """
    Genera una pirámide centrada de altura especificada.

    Args:
        altura (int): Número de filas de la pirámide
    """
    # TODO: Implementar
    # Cada fila debe:
    # - Tener espacios al inicio para centrar: (altura - i) espacios
    # - Tener asteriscos: 2*i - 1 asteriscos
    # Ejemplo: piramide(5)
    #     *
    #    ***
    #   *****
    #  *******
    # *********

    pass  # Reemplazar con su código


def menu_patrones():
    """Menú para seleccionar patrones geométricos"""
    print("\n--- PATRONES GEOMÉTRICOS ---")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Pirámide")
    print("4. Volver al menú principal")

    # TODO: Implementar lógica del menú
    # - Solicitar opción al usuario
    # - Pedir tamaño del patrón
    # - Llamar a la función correspondiente
    # - Preguntar si desea ver otro patrón

    pass  # Reemplazar con su código


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