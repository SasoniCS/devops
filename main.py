import psycopg2

try:
    #Conexão banco de dados
    connection = psycopg2.connect(
        user='',
        password='',
        host='', 
        port='',
        database=''
    )
except (Exception, psycopg2.errors) as e:
    print(f'Erro ao conectar no banco de dados. {e}')