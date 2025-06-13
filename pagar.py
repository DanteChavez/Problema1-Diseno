from abc import ABC, abstractmethod
import time

class pagar(ABC):
    @abstractmethod
    def procesarPago(self, monto, idUsuario):
        pass

class transferencia(pagar):
    def procesarPago(self, monto, usuario):

        print(f"Procesando transferencia de {monto} para el usuario {usuario}")
        r = input("continuar? \n0 : si\n1 : no\n")
        while(r != "0" and r != "1"):
            r = input("continuar? \n0 : si\n1 : no\n")
        if r == "0":
            r = print("Numero de cuenta a transferir: 554.545.987")
            r = input("Haga click cuando haya completado el pago\n")
            print("Verificando su transferencia")
            time.sleep(1.5)
            print("Pago Procesado")
            return 1
        else:
            return 0

class Tarjeta(pagar):
    def procesarPago(self, monto, usuario):
        print(f"Procesando pago con tarjeta de {monto} para el usuario {usuario}")
        r = input("continuar? \n0 : si\n1 : no\n")
        while(r != "0" and r != "1"):
            r = input("continuar? \n0 : si\n1 : no\n")
        if r == "0":
            r = print("Ingrese numero de tarjeta")
            r = input("\n")
            print("Procesando...")
            time.sleep(1.5)
            print("Pago Procesado")
            return 1
        else:
            return 0

class Cripto(pagar):
    def procesarPago(self, monto, usuario):
        print(f"Procesando pago con cripto de {monto} para el usuario {usuario}")
        r = input("continuar? \n0 : si\n1 : no\n")
        while(r != "0" and r != "1"):
            r = input("continuar? \n0 : si\n1 : no\n")
        if r == "0":
            r = print("Numero de billetera virtual: \t 6575455fa56f1a6a51a65d1d6")
            r = input("Haga click cuando haya completado el pago\n")
            print("Verificando su transferencia")
            time.sleep(1.5)
            print("Pago Procesado")
            return 1
        else:
            return 0

class Entrega(pagar):
    def procesarPago(self, monto, usuario):
        print(f"Usted {usuario} pagara {monto} al momento de la entrega")
        r = input("confirmar? \n0 : si\n1 : no\n")
        while(r != "0" and r != "1"):
            r = input("continuar? \n0 : si\n1 : no\n")
        if r == "0":
            return 1
        else:
            return 0


class FabricaDePagos(ABC):
    @abstractmethod
    def crearMetodoPago(self) -> pagar:
        pass


class Fabricatransferencia(FabricaDePagos):
    def crearMetodoPago(self) -> pagar:
        return transferencia()

class FabricaTarjeta(FabricaDePagos):
    def crearMetodoPago(self) -> pagar:
        return Tarjeta()

class FabricaCripto(FabricaDePagos):
    def crearMetodoPago(self) -> pagar:
        return Cripto()

class FabricaEntrega(FabricaDePagos):
    def crearMetodoPago(self) -> pagar:
        return Entrega()

#Funcion de uso
def procesarPago(fabrica: FabricaDePagos, monto, idUsuario):
    metodoPagar = fabrica.crearMetodoPago()
    resultado = metodoPagar.procesarPago(monto, idUsuario)
    return resultado


def verdad(entrada):
    if entrada:
        print("pago completado")
    else:
        print("pago no completado")

#Pago por Transferencia
fabricaTransferencia = Fabricatransferencia()
resultado = (procesarPago(fabricaTransferencia, 5000, "Dante"))









"""
#Pago con Tarjeta
fabrica_tarjeta = FabricaTarjeta()
verdad(procesarPago(fabrica_tarjeta, 75.25, "user456"))

#Pago con Cripto
fabrica_cripto = FabricaCripto()
verdad(procesarPago(fabrica_cripto, 200.00, "user789"))

#=== Pago contra Entrega
fabrica_entrega = FabricaEntrega()
verdad(procesarPago(fabrica_entrega, 50.00, "user101"))
"""
