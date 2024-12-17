import mysql.connector

class GerenciadorBancoDados:
    def __init__(self, user, password, host):
        self.config = {
            'user': user,
            'password': password,
            'host': host,
        }
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(**self.config)

            if self.connection.is_connected():
                print('Conexão estabelecida com sucesso!')
                self.cursor = self.connection.cursor()

        except mysql.connector.Error as error:
            print('Erro ao conectar ao banco de dados: {}'.format(error))

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print('Conexão fechada.')

    def criar_banco_dados(self, nome_database):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_database}")
            print(f'Banco de dados "{nome_database}" criado com sucesso!')

        except mysql.connector.Error as error:
            print('Erro ao criar o banco de dados: {}'.format(error))

    def selecionar_banco_dados(self, nome_database):
        try:
            self.cursor.execute(f"USE {nome_database}")
            print(f'Banco de dados "{nome_database}" selecionado!')

        except mysql.connector.Error as error:
            print('Erro ao selecionar o banco de dados: {}'.format(error))

    def criar_tabela_objetos(self):
        try:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS objetos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                endereco VARCHAR(100)
            )
            '''
            self.cursor.execute(create_table_query)
            print('Tabela de funcionários criada com sucesso!')

        except mysql.connector.Error as error:
            print('Erro ao criar a tabela de funcionários: {}'.format(error))

    def rastrear_objeto(self, item):
        try:
            search_query = '''
            SELECT * FROM objetos 
            WHERE nome = %s;
            '''
            self.cursor.execute(search_query, (item,))
            resultados = self.cursor.fetchall()
            
            if resultados:
                print("Objetos encontrados:")
                for resultado in resultados:
                    print(resultado)
            else:
                print("Nenhum objeto encontrado com o nome:", item)

        except mysql.connector.Error as error:
            print('Erro ao buscar o objeto: {}'.format(error))

     

    def inserir_objetos(self, objetos):
        try:
            insert_query = '''
            INSERT INTO objetos (nome, endereco) VALUES (%s, %s)
            '''
            self.cursor.executemany(insert_query, objetos)
            self.connection.commit()
            print('Inserção de funcionários concluída.')

        except mysql.connector.Error as error:
            print('Erro ao inserir funcionários: {}'.format(error))

    def listar_objetos(self):
        try:
            select_query = '''
            SELECT * FROM objetos
            '''
            self.cursor.execute(select_query)

            print('\nLista de funcionários:')
            for funcionario in self.cursor.fetchall():
                print(funcionario)

        except mysql.connector.Error as error:
            print('Erro ao listar funcionários: {}'.format(error))


# Exemplo de utilização da classe GerenciadorBancoDados
gerenciador = GerenciadorBancoDados('User_Do_Banco', 'Senha_Do_Banco', 'localhost')
gerenciador.conectar()
gerenciador.criar_banco_dados('fun')
gerenciador.selecionar_banco_dados('fun')
gerenciador.criar_tabela_objetos()

# Inserindo objetos e suas respectivas localizações
objetos = [
    ('Roupas', 'Rio do Sul'),
    ('celular', 'Ituporanga'),
    ('Notbook', 'Imbuia'),
    ('Roupas', 'Lontras'),
    ('Notbook', 'Rio do Sul'),
    ('Notbook', 'Agronomica'),
    ('celular', 'Laurentino')
]
gerenciador.inserir_objetos(objetos)

gerenciador.rastrear_objeto("celular")

# Listando os objetos
gerenciador.listar_objetos()

gerenciador.desconectar()