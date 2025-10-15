import logging
import unittest
from datetime import datetime
import os

# Configuração inicial do logging
def configurar_logging(nome_arquivo='logs/aplicacao.log', nivel=logging.DEBUG):
    """
    Configura o sistema de logging com saída para console e arquivo.
    
    Args:
        nome_arquivo (str): Nome do arquivo de log
        nivel (int): Nível de severidade do log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Criação do logger principal
    logger = logging.getLogger('Aplicacao')
    logger.setLevel(nivel)
    
    # Formato do log
    formato = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(nivel)
    console_handler.setFormatter(formato)
    
    # Handler para arquivo
    arquivo_handler = logging.FileHandler(nome_arquivo)
    arquivo_handler.setLevel(nivel)
    arquivo_handler.setFormatter(formato)
    
    # Remove handlers duplicados, se existirem
    logger.handlers.clear()
    
    # Adiciona os handlers ao logger
    logger.addHandler(console_handler)
    logger.addHandler(arquivo_handler)
    
    return logger

# Exemplo de classe que utiliza logging
class ProcessadorDados:
    def __init__(self, logger):
        self.logger = logger
    
    def processar_dados(self, dados):
        """
        Processa uma lista de dados e registra logs para cada etapa.
        
        Args:
            dados (list): Lista de números a serem processados
        Returns:
            float: Média dos dados
        """
        self.logger.info("Iniciando processamento de dados")
        
        try:
            if not dados:
                self.logger.warning("Lista de dados vazia")
                return 0.0
                
            soma = 0
            for i, valor in enumerate(dados):
                self.logger.debug(f"Processando valor {valor} na posição {i}")
                if not isinstance(valor, (int, float)):
                    self.logger.error(f"Valor inválido encontrado: {valor}")
                    raise ValueError(f"Valor inválido: {valor}")
                soma += valor
            
            media = soma / len(dados)
            self.logger.info(f"Processamento concluído. Média calculada: {media}")
            return media
            
        except Exception as e:
            self.logger.critical(f"Erro crítico no processamento: {str(e)}")
            raise

# Testes unitários para o sistema de logging
class TesteProcessadorDados(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente de teste antes de cada teste.
        """
        # Configura um logger temporário para testes
        self.logger = configurar_logging('logs/teste.log', logging.DEBUG)
        self.processador = ProcessadorDados(self.logger)
        
        # Captura logs para verificação
        self.log_capturado = []
        def capturar_log(record):
            self.log_capturado.append(record.getMessage())
        self.logger.handlers[0].emit = capturar_log
        
    def test_processamento_sucesso(self):
        """
        Testa o processamento de dados válidos.
        """
        dados = [1, 2, 3, 4, 5]
        resultado = self.processador.processar_dados(dados)
        self.assertEqual(resultado, 3.0)
        self.assertIn("Iniciando processamento de dados", self.log_capturado)
        self.assertIn("Processamento concluído. Média calculada: 3.0", self.log_capturado)
        
    def test_lista_vazia(self):
        """
        Testa o comportamento com lista vazia.
        """
        resultado = self.processador.processar_dados([])
        self.assertEqual(resultado, 0.0)
        self.assertIn("Lista de dados vazia", self.log_capturado)
        
    def test_dados_invalidos(self):
        """
        Testa o comportamento com dados inválidos.
        """
        dados = [1, 2, "invalido", 4]
        with self.assertRaises(ValueError):
            self.processador.processar_dados(dados)
        self.assertIn("Valor inválido encontrado: invalido", self.log_capturado)

if __name__ == '__main__':
    # Configura o logging
    logger = configurar_logging()
    
    # Exemplo de uso
    processador = ProcessadorDados(logger)
    try:
        dados = [10, 20, 30, 40, 50]
        resultado = processador.processar_dados(dados)
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Erro: {e}")
    
    # Executa os testes
    unittest.main(argv=[''], exit=False)