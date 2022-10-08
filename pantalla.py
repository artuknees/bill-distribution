from gastos import Gastos
from calculados import Calculados

class Pantalla:
    """Este archivo funciona de interfaz de usuario"""
    def __init__(self):
        self.calculados = Calculados()

    def get_user_choice(self):
        print('-' * 100)
        user_input=input('Tu elección: ')
        return user_input
    
    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('-' * 100)
            print('Elija que desea hacer')
            print('1: Añadir gasto')
            print('2: Añadir personas')
            print('3: Ver el monto total gastado')
            print('4: Ver participantes')
            print('5: Calcular distribuciones')
            print('6: Guardar los datos en un archivo')
            print('7: Cargar datos de un archivo')
            print('q: Salir')
            user_choice = self.get_user_choice()

            if user_choice == '1':
                nombre = input('Ingresar el nombre: ')
                cantidad = float(input('Ingresar el gasto: '))
                bloque = Gastos(nombre,cantidad)
                self.calculados.cargar_gasto(bloque)
                self.calculados.cargar_consumidor(nombre)
                self.calculados.cargar_monto(cantidad)
                print('bloque cargado:', self.calculados.block[-1])
                print('bloque total:', self.calculados.block)

            elif user_choice == '2':
                nombre = input('Ingresar el nombre: ')
                bloque = Gastos(nombre,0)
                self.calculados.cargar_gasto(bloque)
                self.calculados.cargar_consumidor(nombre)
                print('bloque cargado:', self.calculados.block[-1])
                print('bloque total:', self.calculados.block)

            elif user_choice == '3':
                print('Total gastado: $ {}'.format(self.calculados.monto))
            elif user_choice == '4':
                print('Los participantes son:')
                for el in self.calculados.consumidores:
                    print(el)
            elif user_choice == '5':
                distribuido = self.calculados.monto/len(self.calculados.block)

                for block in self.calculados.block:
                    if (distribuido)-block.monto < 0:
                        print('{} recibe $ {:.0f}'.format((block.nombre),(-((distribuido)-block.monto))))
                    elif (distribuido)-block.monto > 0:
                        print('{} pone $ {:.0f}'.format((block.nombre),((distribuido)-block.monto)))
                    else:
                        print(block.nombre , 'no pone ni recibe mas dinero')
            elif user_choice == '6':
                self.calculados.guardar_datos()
            elif user_choice == '7':
                self.calculados.load_data()
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print ('Elegí un valor posible.')
        else:
            print('Saliendo...')    
        print ('Hecho!')

inicio = Pantalla()
inicio.listen_for_input()