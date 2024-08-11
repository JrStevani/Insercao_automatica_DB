# Insercao_automatica_DB

<a href="https://jrstevani.github.io/Insercao_automatica_DB/" target="_blank">Projéto detalhado</a>

<strong>Descrição do Projeto</strong>

Este projeto em Python tem como objetivo conectar-se a um banco de dados MySQL para armazenar informações detalhadas sobre animes. As principais funcionalidades e passos do código incluem:

1. <strong>Conexão ao Banco de Dados:</strong> O código estabelece uma conexão com o banco de dados MySQL chamado `db_animes`.

2. <strong>Criação da Tabela animes:</strong> Se a tabela `animes` não existir, o código cria a tabela com as seguintes colunas:
   - id: Um identificador único auto-incremental.
   - nome: Nome do anime.
   - descricao: Descrição do anime.
   - Linguagem: Linguagem do anime (dublado ou legendado).
   - generos: Gêneros do anime, armazenados como JSON.
   - imagem: Caminho da imagem do anime.
   - temporada_episodios: Informações das temporadas e episódios, armazenadas como JSON.

3. <strong>Leitura e Inserção de Dados:</strong> O código percorre dois diretórios (`dublado` e `legendado`) para ler arquivos JSON contendo informações dos animes. Para cada anime, os dados são extraídos e inseridos na tabela `animes` no banco de dados. 

4. <strong>Confirmação e Fechamento:</strong> Após a inserção dos dados, a transação é confirmada (commit) e a conexão com o banco de dados é fechada. No final, é exibido o total de animes inseridos.

 Detalhes Técnicos

- <strong>Bibliotecas Utilizadas:</strong>
  - mysql.connector para a conexão com o banco de dados MySQL.
  - json para manipulação de dados JSON.
  - os para manipulação de diretórios e arquivos.

- <strong>Estrutura de Diretórios e Arquivos:</strong>
  - Diretórios `.\Resultado\dublado\Animes` e `.\Resultado\legendado\Animes` contêm subdiretórios para cada anime.
  - Cada subdiretório contém um arquivo JSON chamado `<nome_do_anime>-episodios.json` com as informações do anime.


