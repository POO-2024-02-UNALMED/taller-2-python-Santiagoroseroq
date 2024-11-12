class Asiento:
  def __init__(self, color, precio, registro):
      self.color = color
      self.precio = precio
      self.registro = registro

  def cambiarColor(self, cadena):
      if cadena in ['blanco', 'verde', 'rojo', 'amarillo', 'negro']:
          self.color = cadena

class Motor:
  def __init__(self, numeroCilindros, tipo, registro):
      self.numeroCilindros = numeroCilindros
      self.tipo = tipo
      self.registro = registro

  def cambiarRegistro(self, numero):
      if isinstance(numero, int):
          self.registro = numero

  def asignarTipo(self, cadena):
      if cadena in ['electrico','gasolina']:
          self.tipo = cadena

class Auto:
  cantidadCreados = 0
  def __init__(self, modelo, precio, asientos, marca, motor, registro):
      self.modelo = modelo
      self.precio = precio
      self.asientos = asientos
      self.marca = marca
      self.motor = motor
      self.registro = registro

  def cantidadAsientos(self):
      cantidad = 0
      for asiento in self.asientos:
          if isinstance(asiento, Asiento):
              cantidad += 1
      return cantidad

  def verificarIntegridad(self):
      registroMotor = self.motor.registro
      if registroMotor != self.registro:
          return 'Las piezas no son originales'
      for asiento in self.asientos:
          if isinstance(asiento, Asiento) and asiento.registro != self.registro:
              return 'Las piezas no son originales'
      return 'Auto original'


            



