from Animal import Animal;

# Criando classe Cachorro
class Cachorro(Animal):

  # Contrutor
  def __init__(self, nome: str):
    super().__init__(nome);
  #Fim construtor

  # Métodos do objeto
  def fazerSom(self):
    print('Au au!!!');

  def mover(self):
    print(f'O cachorro {self.nome} está se movendo pelo parque....');
  # Fim métodos do objeto
#Fim classe Cachorro