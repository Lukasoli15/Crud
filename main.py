# CRIAÇÃO DE OPERAÇÕES CRUD
import sqlite3 
conexao = sqlite3.connect("banco.db")

def menu():
    opcao = 1
    while(opcao != 9):
        print("----- MENU -----")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Deletar")
        print("5. Pesquisar")
        print("9. Sair ")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            cadastro()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        elif opcao == 5:
            pesquisar()
        
# CADASTRO DA NOTA FISCAL
def cadastro():
    id = int(input("Código: "))
    empresa = input("Nome da empresa: ")
    cnpj = float(input("Cnpj: "))
    mercadoria = input("Mercadoria: ")
    valor = float(input("Valor: "))
    imposto = float(input("Imposto: "))
    total = valor + imposto

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO fiscal(id, empresa, cnpj, mercadoria, valor, imposto, total) VALUES(?, ?, ?, ?, ?, ?, ?)", (id, empresa, cnpj, mercadoria, valor, imposto, total))
    conexao.commit()
    conexao.close()


# LISTAR NOTAS 

def listar():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM fiscal")
    resultado = cursor.fetchall()
    conexao.close()
    
    for linha in resultado:
        print("id:", linha[0])
        print("Empresa: ", linha[1])
        print("cnpj: ", linha[2])
        print("mercadoria:",linha[3])
        print("valor:", linha[4])
        print("imposto:", linha[5])
        print("total: ", linha[6])

# ATUALIZAR OS DADOS FISCAIS - UPDATE TEM QUE SER FEITO COM AS VARIAVEIS ORIGINAIS PARA UMA SUBSTITUIÇÃO DE NOVAS VARIÁVEIS
def atualizar():
    id = int(input("Id da nota: "))
    Nova_empresa = input("Nova empresa: ")
    Novo_cnpj = float(input("Novo Cnpj: "))
    Nova_mercadoria = input("Nova mercadoria: ")
    Novo_valor = float(input("Novo valor: "))
    Novo_imposto = float(input("Novo imposto: "))
    No_total = Novo_valor + Novo_imposto

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE fiscal SET empresa=?, cnpj=?, mercadoria=?, valor=?, imposto=?, total=? WHERE id=?",(Nova_empresa, Novo_cnpj, Nova_mercadoria, Novo_valor, Novo_imposto, No_total, id))
    conexao.commit()
    conexao.close()

# DELETAR ALGUMA NOTA FISCAL PELO ID 
def deletar():
    id = int(input("Código a ser excluido: "))
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM fiscal WHERE id=?",(id,))
    conexao.commit()
    conexao.close()

# PESQUISAR PRODUTO A PARTIR DA EMPRESA
def pesquisar():
    pesquisa = input("Qual nota deseja encontrar? ")
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    pesquisa = "%" + pesquisa + "%"
    cursor.execute("SELECT * FROM fiscal WHERE empresa=?;",(pesquisa,))
    resultado = cursor.fetchall()
    conexao.close()
    print(resultado)
    return resultado

menu()
