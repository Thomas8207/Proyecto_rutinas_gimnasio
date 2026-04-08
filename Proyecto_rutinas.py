class Ejercicio:
    def __init__(self, nombre, grupo_muscular, series, repeticiones):
        self.nombre = nombre
        self.grupo_muscular = grupo_muscular
        self.series = series
        self.repeticiones = repeticiones

    def mostrar_detalle(self):
        return f"{self.nombre} - {self.series}x{self.repeticiones} ({self.grupo_muscular})"


class DiaEntrenamiento:
    def __init__(self, nombre_dia):
        self.nombre_dia = nombre_dia
        self.ejercicios = []

    def agregar_ejercicio(self, ejercicio):
        self.ejercicios.append(ejercicio)

    def mostrar_ejercicios(self):
        print(f"\n--- {self.nombre_dia} ---")
        for ejercicio in self.ejercicios:
            print(ejercicio.mostrar_detalle())
class Usuario:
    def __init__(self, nombre: str, edad: int, peso: float, objetivo: str, nivel: str, dias_disponibles: int):

        if edad <= 0 or peso <= 0:
            raise ValueError("Edad y peso deben ser valores positivos")

        self.nombre: str = nombre
        self.edad: int = edad
        self.peso: float = peso
        self.objetivo: str = objetivo
        self.nivel: str = nivel
        self.dias_disponibles: int = dias_disponibles

    def __str__(self):
        return f"Usuario: {self.nombre} | Objetivo: {self.objetivo}"
        
      
