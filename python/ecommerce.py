import sqlite3
import pandas as pd

# Criar o banco no mesmo local do script
conexao = sqlite3.connect("ecommerce.db")

# Carregar CSVs
clientes = pd.read_csv(r"C:\Users\leticia\Downloads\projeto e-commerce\python\clientes.csv")
produtos = pd.read_csv(r"C:\Users\leticia\Downloads\projeto e-commerce\python\produtos.csv")
pedidos = pd.read_csv(r"C:\Users\leticia\Downloads\projeto e-commerce\python\pedidos.csv")


# Criar tabelas
clientes.to_sql("clientes", conexao, if_exists="replace", index=False)
produtos.to_sql("produtos", conexao, if_exists="replace", index=False)
pedidos.to_sql("pedidos", conexao, if_exists="replace", index=False)

print("Banco criado e dados inseridos!")
conexao.close()
