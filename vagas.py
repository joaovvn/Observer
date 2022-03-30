from abc import ABCMeta, abstractclassmethod

class Notificar(metaclass = ABCMeta):
  @abstractclassmethod
  def notificar(self):
    pass

class Veiculo:
  def __init__(self, carro, local, vaga):
    self.carro = carro
    self.local = local
    self.vaga = vaga

  def notificacao(self):
    return f'{self.carro} atualmente ocupa a vaga {self.vaga} no {self.local}!'

class Enviar(Notificar):
  def __init__(self, veiculo):
    self.veiculo = veiculo

  def notificar(self):
    return f'Seu {self.veiculo.notificacao()}'