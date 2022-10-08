class Gastos:
    """En esta clase solo se ingresa el gasto como tal"""
    def __init__(self, name, amount):
        self.nombre = name
        self.monto = amount

    def __repr__(self):
        return str(self.__dict__)
