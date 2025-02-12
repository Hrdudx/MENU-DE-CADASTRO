![unnamed](https://github.com/user-attachments/assets/bd3e2da9-6dce-4b75-9c72-45dca47d4e6b)


# Cadastro de Pessoas com Python e Flask 

Este projeto permite ao usuário inserir o nome e a idade de uma pessoa, armazenar essas informações na memória e exibi-las em uma lista. Ele utiliza o framework Flask para criar a interface web e gerenciar os dados.

## Funcionalidades

* **Cadastro de Pessoas:** Permite inserir o nome e a idade de uma pessoa através de um formulário.
* **Listagem de Pessoas:** Exibe uma lista com o nome e a idade de todas as pessoas cadastradas.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Flask:** Framework web para criação da interface e gerenciamento das rotas.
* **HTML:** Linguagem de marcação para estruturar as páginas web.
* **CSS:** Linguagem de estilo para estilizar as páginas web.

## Pré-requisitos

* Python 3.x instalado.
* Flask instalado: `pip install Flask`

## Instalação

1. Clone este repositório: `git clone https://github.com/seu-usuario/cadastro-pessoas-flask.git`
2. Acesse o diretório do projeto: `cd cadastro-pessoas-flask`

## Execução

1. Execute o arquivo `sistema.py`: `python sistema.py`
2. Abra o navegador e acesse `http://127.0.0.1:5000/`

## Estrutura do Projeto
static/style.css: Contém as regras de estilo CSS que controlam a aparência das páginas HTML. Define cores, fontes,布局 e outros aspectos visuais.

templates/index.html: Este arquivo HTML contém o formulário para o usuário inserir o nome e a idade da pessoa. Ele utiliza o método POST para enviar os dados para o servidor Flask.

templates/lista.html: Este arquivo HTML exibe a lista de pessoas cadastradas. Ele recebe os dados do servidor Flask e os exibe em uma tabela.

funcao.py: Este arquivo contém as funções que manipulam os dados. Ele define duas funções:

adicionar_pessoa(nome, idade): Adiciona uma nova pessoa à lista de pessoas cadastradas.
listar_pessoas(): Retorna a lista de todas as pessoas cadastradas.
sistema.py: Este arquivo é o coração da aplicação Flask. Ele é responsável por:

Inicializar o aplicativo Flask.
Definir as rotas da aplicação (URLs que o usuário pode acessar).
Renderizar os templates HTML.
Gerenciar o fluxo de dados entre o formulário, as funções de manipulação de dados e a exibição da lista.
