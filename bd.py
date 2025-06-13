from usuario import *
class bd():
    _instancia = None
    def __init__(self):
        """Inicializa la base de datos con un diccionario vacío"""
        self.listaPedidos = {}
        self.listaUsuarios = {}
        self.idContadorUsuarios = 1



    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def agregarPedido(self, pedido):
        """Guarda un pedido en la base de datos usando su ID como clave"""
        if not hasattr(pedido, 'getidPedido'):
            #raise ValueError("El objeto no parece ser un Pedido válido")
            return 0
        self.listaPedidos[pedido.getidPedido()] = pedido
        return 1
    def recuperarPedido(self, idPedido):
        """Devuelve el pedido correspondiente al ID proporcionado"""
        if idPedido not in self.listaPedidos:
            #raise KeyError(f"No existe un pedido con ID {idPedido}")
            return 0
        return self.listaPedidos[idPedido]

    def mostrarPedidos(self):
        """Muestra los IDs de todos los pedidos almacenados"""
        if not self.listaPedidos:
            print("No hay pedidos registrados")
            return

        print("Pedidos almacenados:")
        for id_pedido in self.listaPedidos:
            print(f"- ID: {id_pedido} \t estado : {self.listaPedidos[id_pedido].estado}")

    def mostrarPedidosUsuario(self,idUsuario):
        """Muestra los IDs de todos los pedidos almacenados"""
        if not self.listaPedidos:
            print("No hay pedidos registrados")
            return

        print("Pedidos almacenados:")
        for id_pedido in self.listaPedidos:
            rec = self.listaPedidos[id_pedido]
            if(idUsuario == rec.getidUsuario()):
                print(f"- ID: {id_pedido} \t estado : {self.listaPedidos[id_pedido].estado} \t precio : {self.listaPedidos[id_pedido].gettotalReal()}")
    #esto es como para simular guardar usuarios en la "base de datos"
    #es mas que nada para que sea global
    def nuevoUsuario(self,nombre, direccion, tipoCliente):
        nuevo = usuario(self.idContadorUsuarios,nombre,direccion, tipoCliente)
        self.idContadorUsuarios = self.idContadorUsuarios + 1
        self.listaUsuarios[nuevo.getidUsuario()] = nuevo
        return self.idContadorUsuarios-1

    def buscarUsuario(self,idUsuario):
        if idUsuario in self.listaUsuarios:
            return self.listaUsuarios[idUsuario]
        else:
            print(f"No hay usuario registrado en la base de datos con la id: {idUsuario} ")
            return 0
