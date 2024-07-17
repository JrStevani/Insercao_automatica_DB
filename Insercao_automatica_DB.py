import mysql.connector
import json
from os import path, listdir

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_animes'
)
cursor = conn.cursor()

# Cria a tabela 'animes' se ela não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS animes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    linguagem VARCHAR(10),
    generos JSON NOT NULL,
    imagem VARCHAR(255) NOT NULL,
    temporada_episodios JSON NOT NULL
)
''')

# Lista dos tipos de gêneros
list_genero = ['dublado', 'legendado']
c = 0

# Itera sobre os tipos de gêneros
for tipo in list_genero:
    diretorio = f'.\\Resultado\\{tipo}\\Animes'
    
    # Verifica se o diretório existe
    if path.exists(diretorio):
        diretorios_encontrados = []

        # Lista os diretórios dentro do diretório principal
        for item in listdir(diretorio):
            if path.isdir(path.join(diretorio, item)):
                diretorios_encontrados.append(item)
        
        # Itera sobre os diretórios encontrados
        for anime in diretorios_encontrados:
            lista = []
            caminho = f'{diretorio}\\{anime}\\{anime}-episodios.json'
            
            # Verifica se o arquivo JSON do anime existe
            if path.exists(caminho):
                with open(caminho, 'r') as arc:
                    anime_data = json.load(arc)
                print(f'[OK] - {anime}')

                # Converte as listas de gêneros e episódios em JSON
                generos_json = json.dumps(anime_data["generos"])
                temporadas_episodios_json = json.dumps(anime_data["temporadas_episodios"])

                # Insere os dados do anime na tabela 'animes'
                cursor.execute('''
                INSERT INTO animes (nome, descricao, linguagem, generos, imagem, temporada_episodios)
                VALUES (%s, %s, %s, %s, %s, %s)
                ''', (anime_data["nome"], anime_data["descricao"], tipo, generos_json, anime_data["imagem"],
                      temporadas_episodios_json))
                c += 1

                # Confirma a inserção no banco de dados
                conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
print(f'Total de animes: {c}')
