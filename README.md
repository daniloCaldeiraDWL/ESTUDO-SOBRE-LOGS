# ESTUDO PRÁTICO DEDICADO AOS LOGS
Este projeto é unicamente voltado a um estudo prático para se trabalhar com logs. 

Autor: Danilo Martins Caldeira. 

## Biblioteca logging
Nosso estudo foca na biblioteca padrão logging, que é amplamente adotada pela comunidade Python. Apresentaremos detalhes de sua tragetória. 

A biblioteca logging é parte da biblioteca padrão do Python, não requer instalação adicional e é amplamente utilizada para gerenciar logs em aplicações Python. Ela suporta diferentes níveis de severidade (DEBUG, INFO, WARNING, ERROR, CRITICAL), formatadores personalizados e múltiplos destinos de saída (console, arquivo, etc.).

## Padrão para elaboração de uma linha de log
Existe um padrão amplamente aceito pela comunidade Python para o formato de uma linha de log, embora ele seja flexível e dependa das necessidades do projeto. A biblioteca logging do Python permite personalizar o formato, mas há convenções comuns baseadas em boas práticas e legibilidade. O formato de uma linha de log geralmente inclui:

- Timestamp: Data e hora do evento, para rastrear quando ocorreu.
- Nome do Logger: Identifica o componente ou módulo que gerou o log.
- Nível de Severidade: Indica a importância do evento (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- Mensagem: Descrição clara do evento ou ação.

Formato comum recomendado:
```%(asctime)s - %(name)s - %(levelname)s - %(message)s```

Exemplo:
- 2025-10-14 22:20:00 - Aplicacao - INFO - Iniciando processamento de dados
- 2025-10-14 22:20:00 - Aplicacao - DEBUG - Processando valor 10 na posição 0

Outros modelos podem seguir o padrão, como por exemplo:
- 2025-10-14 23:12:00 - Aplicacao - INFO - processador.py:25 - Iniciando processamento de dados


## Níveis de severidade
Os níveis de severidade indicam a importância do evento (DEBUG, INFO, WARNING, ERROR, CRITICAL). Podem ser:

- DEBUG: Detalhes do processo (ex.: valor sendo processado).
- INFO: Informações gerais (ex.: início e fim do processamento).
- WARNING: Avisos (ex.: lista vazia).
- ERROR: Erros recuperáveis (ex.: valor inválido).
- CRITICAL: Erros graves (ex.: falha no processamento).


## Boas Práticas para Controlar o Tamanho
O tamanho de um arquivo de log não tem um limite estrito imposto pela biblioteca logging do Python ou pelo sistema operacional Windows 11, mas o crescimento descontrolado de arquivos de log pode causar problemas como:

- Consumo de Disco: Arquivos de log muito grandes podem ocupar espaço significativo.
- Desempenho: Arquivos grandes podem tornar a escrita e a leitura mais lentas.
- Gerenciamento: Logs extensos dificultam a busca por informações específicas.

Para gerenciar o tamanho de arquivos de log, a biblioteca **logging** oferece handlers especializados, como RotatingFileHandler e TimedRotatingFileHandler, que **ajudam a limitar** o tamanho ou criar novos arquivos com base em critérios como tamanho ou tempo.

1. RotatingFileHandler: Divide o arquivo de log quando ele atinge um tamanho máximo (ex.: 10 MB). Mantém um número definido de arquivos de backup, substituindo os mais antigos. Ideal para limitar o espaço em disco.
2. TimedRotatingFileHandler: Cria novos arquivos de log com base em intervalos de tempo (ex.: diariamente, semanalmente). Útil para projetos onde logs são organizados por data.

### Sobre apagar arquivos de logs:
Arquivos de log podem (e muitas vezes devem) ser apagados periodicamente para evitar o acúmulo excessivo e liberar espaço em disco. No entanto, isso deve ser feito com cuidado para não perder informações críticas, especialmente em aplicações que requerem auditoria ou rastreamento.