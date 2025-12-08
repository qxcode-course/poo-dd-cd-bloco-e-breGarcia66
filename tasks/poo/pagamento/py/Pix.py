from Pagamento import Pagamento;

# Criando subclasse Pix
class Pix(Pagamento):

  # Construtor
  def __init__(self,
               valor: float,
               descricao: str,
               chave: str,
               banco: str):
    super().__init__(valor, descricao);
    self.__chave: str = chave;
    self.__banco: str = banco; 
  # Fim Construtor

  # Métodos de acesso
  @property
  def chave(self) -> str:
    return self.__chave;

  @property
  def banco(self) -> str:
    return self.__banco;
  # Fim métodos de acesso

  # Métodos do objeto
  def processar(self):
    self.valor = 0;
    self.descricao = '';
    
    print(f'PIX enviado via {self.banco} usando chave {self.chave}');
    return;
  # Fim métodos do objeto
# Fim subclasse Pix