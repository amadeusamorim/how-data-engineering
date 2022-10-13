# HOW BOOTCAMPS - ENGENHARIA DE DADOS

A ideia dessa pasta é agrupar todos os conhecimentos adquiridos durante as aulas e com os códigos hands-on dos projetos ensinados pelos facilitadores.

## 🧑🏻‍💻 DESCRITIVOS DAS PASTAS E PROJETOS

* **A001 (Fundamentos da Engenharia de dados)**: O objetivo do exercício contido na pasta é de compreender a dinâmica inicial de um Engenheiro de Dados, extraindo dados de um site e realizando os procedimentos necessários para inseri-los num dataframe.
  * *main.py*: A proposta do desafio é coletar dados dos sorteios da Lotofácil e levantar informações relativas à:
    * Quais números mais sorteados e menos sorteados?
    * Quais combinações de números pares e ímpares e primos saem por sorteio?

    🎯 Atingindo os **objetivos**:
    * Criar um ambiente virtual.
    * Ler um arquivo de dados para um dataframe.
    * Tratar a informação recebida.
    * Selecionar os dados necessários.
    * Extrair informações dos dados (em `html`).
    * Analisar os dados.
    * Automatizar o processo.
  
    📖 **Bibliotecas** utilizadas: `requests`, `pandas` e `collections`.

* **A002 (Fundamentos da Ingestão de dados)**: A ideia do módulo é entender o funcionamento de APIs e requests, tratando erros e fazendo retentativas, criar logs, utilizar o Chrome Inspect, buscando dados através dessa inspeção.
  * *main.py*: A ideia do exercício/desafio é entender como funciona uma API e que tipo de direcionamento pode ser feito com os dados extraídos. A API utilizada foi de conversão de moedas.
    🎯 Atingindo os **objetivos**:
    * Criar um ambiente virtual.
    * Coletar dados utilizando API.
    * Retornar dados necessários (abstração).
    * Tratar erros com `try` e `except`.
    * Utilizar decoradores e tratar erros por meio do `on_exception` da biblioteca `backoff`.
    * Criar logs para acompanhamento dos dados ingeridos.

    📖 **Bibliotecas** utilizadas: `requests`, `json`, `backoff`, `random` e `logging`.
  
  * *podcast.py*: Extrair todos os episódios de podcast do site *portalcafebrasil* e inserir num dataframe com colunas de nome e descrição.
    🎯 Atingindo os **objetivos**:
    * Coletar dados do site.
    * Utilizar o `BeautifulSoup` para extrair informações de html do site.
    * Utilizar o Google Inspect.
    * Criar logs para acompanhamento dos dados ingeridos.
    * Criar dataframe e inserir os dados extraídos do site.
    * Salvar o arquivo em .csv.

    📖 **Bibliotecas** utilizadas: `requests`, `bs4`, `logging` e `pandas`.

   * *imoveis.py*: Extrair os 9.500 apartamentos para venda mais atualizados de João Pessoa do site Viva Real e inserir as informações num dataframe.
    🎯 Atingindo os **objetivos**:
      * Coletar dados do site.
      * Utilizar o Google Inspect.
      * Utilizar o `Thunder Client` (extensão do VSCode) para organizar informações extraídas do retorno da API.
      * Utilizar o `BeautifulSoup` dentro da minha funçõa para retirar informações do html extraído pelo `Thunder Client`.
      * Evitar timeout de requisições.
      * Criar dataframe e inserir os dados extraídos do site.
      * Salvar o arquivo em .csv.

    📖 **Bibliotecas** utilizadas: `os`, `wsgiref.validate`, `pyparsing`, `requests`, `bs4`, `pandas`, `wcwidth`, `json` e `time`.

*🚧 Em atualização 🚧*
