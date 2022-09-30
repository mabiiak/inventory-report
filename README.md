# Boas-vindas ao projeto Inventory Reports

  Projeto feito durante o curso de desenvolvimento web na trybe.

  No projeto passado você implementou algumas funções que faziam leitura e escrita de arquivos `JSON` e `CSV`, correto?

  Neste projeto foi implementado um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

  Esses dados de estoque poderão ser obtidos de diversas fontes:

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

## Habilidades:
  - Aplicar conceitos de Orientação a Objetos em Python;
  
  - Aplicar padrões de projeto;
  
  - Leitura e escrita de arquivos (XML, CSV, JSON).

# Desenvolvimento
<details>
  <summary>
    <h3>
      Antes de começar a desenvolver
    </h3>
    </summary>

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:mabiiak/inventory-report.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `inventory-report`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Crie uma branch a partir da branch `master`

  - Verifique que você está na branch `master`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `master`
    - Exemplo: `git checkout master`
  - Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
    - Exemplo: `git checkout -b nome-inventory-report`

  5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

  - Verifique que as mudanças ainda não estão no _stage_
    - Exemplo: `git status` (deve aparecer listada a pasta _joaozinho_ em vermelho)
  - Adicione o novo arquivo ao _stage_ do Git
    - Exemplo:
      - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
      - `git status` (deve aparecer listado o arquivo _joaozinho/README.md_ em verde)
  - Faça o `commit` inicial
    - Exemplo:
      - `git commit -m 'descrição do commit'` (fazendo o primeiro commit)
      - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

  6. Adicione a sua branch com o novo `commit` ao repositório remoto

  - Usando o exemplo anterior: `git push -u origin nome-inventory-report`

  7. Crie um novo `Pull Request` _(PR)_

  - Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/mabiiak/inventory-report/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
  - Coloque um título para a sua _Pull Request_
    - Exemplo: _"Cria tela de busca"_
  - Clique no botão verde _"Create pull request"_
  - Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
  - **Não se preocupe em preencher mais nada por enquanto!**
  - Volte até a [página de _Pull Requests_ do repositório](https://github.com/mabiiak/inventory-report/pulls) e confira que o seu _Pull Request_ está criado

</details>

<details>
  <summary><strong> Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>Docker</strong></summary>
  Caso queria executar os seus testes de projeto via `Docker-compose`, substituindo o ambiente virtual, execute o comando:

  ```bash
  docker-compose run --rm inventory pytest
  ```
</details>

<details>
  <summary><strong> Arquivos com os dados de entrada</strong></summary><br />
  Três formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Confira o exemplo de formato eles:
  
  <strong>Arquivos CSV</strong>
  Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
[
  {
    "id":1,
    "nome_do_produto":"Borracha",
    "nome_da_empresa":"Papelaria Solar",
    "data_de_fabricacao":"2021-07-04",
    "data_de_validade":"2029-02-09",
    "numero_de_serie":"FR48",
    "instrucoes_de_armazenamento":"Ao abrigo de luz solar"
  }
]
```

<strong>Arquivos XML</strong>
Os arquivos **XML** seguem o seguinte modelo:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>Microfone</nome_do_produto>
    <nome_da_empresa>Tecno Uau LTDA</nome_da_empresa>
    <data_de_fabricacao>2021-10-27</data_de_fabricacao>
    <data_de_validade>2032-08-31</data_de_validade>
    <numero_de_serie>MT08</numero_de_serie>
    <instrucoes_de_armazenamento>Longe de fonte de calor</instrucoes_de_armazenamento>
  </record>
</dataset>
```
</details>

# Requisitos

    ✅ 1 - Testar o construtor/inicializador do objeto Produto

    ✅ 2 - Testar o relatório individual do produto

    ✅ 3 - Gerar a versão simplificada do relatório

    ✅ 4 - Gerar a versão completa do relatório

    ✅ 5 - Gere os relatórios através de um arquivo CSV

    ✅ 6 - Gere os relatórios através de um arquivo JSON

    ✅ 7 - Gere os relatórios através de um arquivo XML

    ✅ 8 - Organizar o código de importação com o padrão Strategy

    ❌ 9 - Testar a geração de uma versão do relatório em cores

# Bônus

    ❌ 10 - Criar uma classe `InventoryIterator`

        - 10.1 - Será validado que a instancia de InventoryRefactor é iterável (Iterable)

        - 10.2 - Será validado que é possível iterar o primeiro item da lista usando csv

        - 10.3 - Será validado que é possível iterar o primeiro item da lista usando json

        - 10.4 - Será validado que é possível iterar o primeiro item da lista usando xml

        - 10.5 - Será validado que é possível receber duas fontes de dados sem sobrescrita

        - 10.6 - Será validado que não é possível enviar arquivo inválido

    ❌ 11 - Preencha a função `main` no módulo `inventory_report/main.py`

        - 11.1 - Será validado se pelo comando é possível importar um arquivo csv simples

        - 11.2 - Será validado se pelo comando é possível importar um arquivo csv completo

        - 11.3 - Será validado se pelo comando é possível importar um arquivo json simples

        - 11.4 - Será validado se pelo comando é possível importar um arquivo json completo

        - 11.5 - Será validado se pelo comando é possível importar um arquivo xml simples

        - 11.6 - Será validado se pelo comando é possível importar um arquivo xml completo

        - 11.7 - Será validado se houverem argumentos faltantes será retornando um erro
