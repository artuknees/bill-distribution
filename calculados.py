import json
from gastos import Gastos

class Calculados:
    """Esta clase hace todos los calculos que requiere el programa"""
    def __init__(self):
        self.block = []
        self.consumidores = []
        self.monto = 0

    def cargar_gasto(self,bloque):
        self.block.append(bloque)
    
    def cargar_consumidor(self,nombre):
        self.consumidores.append(nombre)

    def cargar_monto(self,monto):
        self.monto = self.monto + monto

    def load_data(self):
            try:
                with open('gastos.txt', mode = 'r') as f: 
                    file_content = f.readlines()
                    
                    bloques = json.loads(file_content[0][:-1])
                    bloques_actualizados = []
                    for bloque in bloques:
                        bloque_actualizado = Gastos(bloque['nombre'],bloque['monto'])
                        bloques_actualizados.append(bloque_actualizado)
                    self.block = bloques_actualizados
                    print(self.block)
                    print('te falta cargar los nombres por separado y los montos totales')
                    print('tambien te falta intentar cargar siempre que haya un archivo')
                    # open_transactions = json.loads(file_content[1])
                    # updated_transactions = []
                    # for tx in open_transactions:
                    #     updated_transaction = Transaction(tx['sender'],tx['recipient'],tx['signature'],tx['amount'])
                    #     updated_transactions.append(updated_transaction)
                    # self.__open_transactions = updated_transactions
            except (IOError , IndexError ): #to handle not existing file or empty file
                pass
            finally:
                print('Cleanup') #not necessary


    def guardar_datos(self):
        try:
            with open('gastos.txt', mode = 'w') as f: 
                bloque_grabable = [bloque.__dict__ for bloque in self.block]
                nombre_grabable = [nombre for nombre in self.consumidores]
                total_grabable = self.monto
                f.write(json.dumps(bloque_grabable))
                f.write('\n')
                f.write(json.dumps(nombre_grabable))
                f.write('\n')
                f.write(json.dumps(total_grabable))

        except IOError:
            print('Saving failed')