from Animal import Animal;

# Criando classe Urso
class Urso(Animal):

  # Construtor
  def __init__(self, nome: str):
    super().__init__(nome);
  # Fim construtor

  # Métodos do objeto
  def fazerSom(self):
    print('Uuuaaaarrrrrhhhh!!!');

  def mover(self):
    print(f'O urso {self.nome} está se movendo impoderado pela escura floresta...');
  #Fim métodos do objeto
# Fim classe Urso