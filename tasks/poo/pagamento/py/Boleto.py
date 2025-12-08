from Pagamento import Pagamento;

# Criando subclasse Boleto
class Boleto(Pagamento):

  # Construtor
  def __init__(self,
              valor: float,
              descricao: str,
              codigoDeBarra: str,
              dataVencimento: str):
    super().__init__(valor, descricao);
    self.__codigoDeBarra: str = codigoDeBarra;
    self.__dataVencimento: str = dataVencimento;
  # Fim constutor

  # Métodos de acesso
  @property
  def codigoDeBarra(self) -> str:
    return self.__codigoDeBarra;

  @property
  def dataVencimento(self) -> str:
    return self.__dataVencimento;
  # Fim métodos de acesso 

  # Métodos do objeto
  def processar(self):
    print('Boleto gerado. Aguardando pagamento...');
  # Fim métodos do objeto
# Fim subclasse Boleto