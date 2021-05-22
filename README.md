# Super Useful Notion CLI

|                |                                                                                      |
| -------------- | ------------------------------------------------------------------------------------:|
| Language       | [Python 3.8](https://www.python.org/ "Python's Homepage")                            |
| External API   | [Notion API](https://developers.notion.com/reference/intro "Notion's API reference") |

Uma _command line interface_ (CLI) **SUPER ÚTIL** para quem usa Notion,
oferecendo formas simples e fáceis de criar páginas nas suas tabelas. 

> Brincadeira - na verdade essa CLI ainda não é TÃO  útil assim - por enquanto
> ela apenas te permite criar páginas de ata em um database do Notion (mas de 
uma forma bem irada, lhe garanto)

## 1. O que essa CLI faz afinal?
No momento ela está configurada apenas para criar Atas automaticamente em uma tabela do Notion de sua
preferência.

Este é um exemplo de database de atas no notion:
![Tabela com o título "Atas de Chapter" no Notion](https://github.com/dehatanes/super-useful-notion-cli/blob/main/doc_assets/notion_database_example.png)

E este é um exemplo da `cli` rodando e criando uma nova ata (adicionando um novo item nessa tabela):
![Video da cli funcionando](https://github.com/dehatanes/super-useful-notion-cli/blob/main/doc_assets/working_cli_video.gif)

## 2. Setup
####  First things first
Antes de mais nada, para configurar essa `cli` você precisa:
1. Clonar esse projeto no seu computador
2. Possuir `python 3.8` e `pip` instalados na sua máquina. Se não possuir, ainda
 você pode instalá-los [pelo website oficial da linguagem](https://www.python.org/ "Python's Homepage")
3. Ter uma conta no [Notion](https://www.notion.so/).
4. Configurar uma nova integração no seu workspace do notion. Você pode fazer isso
usando [esse tutorial do Notion](https://developers.notion.com/docs/getting-started).
  - PS: Esse tutorial vai te ensinar a pegar um `token` para integração e a pegar o 
  `id de databases`. Vamos usar ambos posteriormente, então guarda eles com carinho. 

#### Instalando dependências 
Uma vez que o projeto está instalado no seu computador, vá para a pasta dele no terminal
e instale as dependências do projeto usando o comando:
```
pip3 install -r requirements.txt
``` 

### Configurando variáveis de ambiente
Para a `cli` funcionar, você precisa adicionar algumas variáveis de ambiente no seu terminal.
Para isso rode os comandos a seguir alterando o que está depois de `=` por seus respectivos valores:
- Troque `<your_notion_api_key>` pelo token que você recebe ao [configurar uma nova integração no Notion](https://developers.notion.com/docs/getting-started).
- Troque `<your_notion_database_id>` pelo id do "database de atas" que você deseja inserir a nova ata criada pela cli.
- Troque `your_notion_template_page_id>` pelo id de uma página que tem o conteúdo que você quer usar de
template e copiar para a nova página que criar (É opcional, na ausência desse valor, sua página será criada em branco).
```bash
export NOTION_API_KEY=<your_notion_api_key>
export NOTION_DATABASE_ID=<your_notion_database_id>
export NOTION_TEMPLATE_PAGE_ID=<your_notion_template_page_id>  # this one is optional
```

## 3. Como usar
Para usar basta estar na pasta do projeto e rodar o comando:
```bash
python3 -m super_useful_cli.main 
```
E esperar a mágica acontecer :) 

## 4. Referências legais para fazer algo parecido
- [Notion API - Getting Started](https://developers.notion.com/docs/getting-started)
- [Notion API - Official Docs](https://developers.notion.com/reference/intro)
- [Building Beautiful Command Line Interfaces with Python](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df)

---
Made with :heart: by @dehatanes
