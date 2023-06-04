import pymysql

class produto: 
    def conexao(self):
        con= pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="loja_de_produtos"
        )
        return con
    def cadastrar(self, codigo, nome, preco, quantidade):

        conexao = self.conexao()
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade= quantidade

        comando= "Insert into produto values(%s, %s, %s, %s)"

        valores = (codigo, nome, preco, quantidade)

        consulta = conexao.cursor()

        consulta.execute(comando, valores)

        conexao.commit()

        print(consulta.rowcount, "linhas inseridas com sucesso\n")

        conexao.close()

    def consultar (self):

        conexao = self.conexao()

        comando = "select * from produto"

        consulta = conexao.cursor()

        consulta.execute(comando)

        resultado = consulta.fetchall()

        print("Tabela PRODUTOS ========================")

        cont=0
        for perc in resultado:
             cont+=1
             print(f"Código: {perc[0]}\t Nome: {perc[1]}\t Preço {perc[2]}\t Quantidade: {perc[3]}\n")

        print ("PRODUTOS CADASTRADOS =================\n")
        print(f"Há{cont} produtos cadastrados.\n")
        print("=========================================")
    
    def deletar(self,codigo):
        self.codigo = codigo
        conexao= self.conexao()

        comando="Delete from produto where codigo =%s"

        consulta = conexao.cursor()

        consulta.execute(comando, self.codigo)

        conexao.commit()

        if consulta.rowcount == 0:
            print("Erro: nenhum item foi deletado")
        elif consulta.rowcount > 0:
            print(consulta.rowcount, "Linhas excluidas com sucesso!")

        conexao.close()

