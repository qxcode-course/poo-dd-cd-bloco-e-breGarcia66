from Pagamento import Pagamento;

# Criando subclasse CartaoCredito
class CartaoCredito(Pagamento):
  
  # Construtor
  def __init__(self,
               valor: float,
               descricao: str,
               numero: str,
               nomeTitular: str,
               limiteDisponivel: float):
    super().__init__(valor, descricao);
    self.__numero: str = numero;
    self.__nomeTitular: str = nomeTitular;
    self.__limiteDisponivel: float = limiteDisponivel;
  # Fim construtor

  # Métodos de acesso
  @property
  def numero(self) -> str:
    return self.__numero;

  @property
  def nomeTitular(self) -> str:
    return self.__nomeTitular;

  @property
  def limiteDisponivel(self) -> float:
    return self.__limiteDisponivel;
  # Fim métodos de acesso

  # Métodos mutantes
  @limiteDisponivel.setter
  def limiteDisponivel(self, valor: float):
    self.__limiteDisponivel = valor;
  # Fim métodos mutantes

  # Métodos de objeto
  def processar(self):
    if self.valor > self.limiteDisponivel:
      print(f'Erro: Limite insuficiente no cartão {self.numero}');
      return;

    self.limiteDisponivel -= self.valor;
    self.valor = 0;
    self.descricao = '';

    print(f'Pagamento aprovado no cartão {self.nomeTitular}. Limite restante: {self.limiteDisponivel:.2f}');
    return;

  # Fim métodos do objeto
# Fim subclasse pagamento