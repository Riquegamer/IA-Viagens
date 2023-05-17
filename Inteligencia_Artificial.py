import sqlite3 as sql
from sklearn import tree

dB = sql.connect('IA_BD.db') # Conectando com o banco de dados

cursor = dB.cursor() # Criando Um cursor para realizar as querrys no banco de dados

cursor.execute("SELECT * FROM Viajantes") # Importando os dados da tabela viajantes do banco de dados
data = cursor.fetchall() # Atribuindo os dados da tabela viajantes a uma varivel

covid = 0 # Definindo um valor para covid
saudavel = 1 # Definindo um valor para saudavel 
caro = 2 # Definindo um valor para passagems caras
barato = 3 # Definindo um valor para passagems baratas

viagem = 4 # Definindo um valor para pretenção de viagem
casa = 5 # Criando um valor para sem pretenção de viagem

preco = 0 # Criando uma variavel responsável pelo preço da viagem pós analiise de dados
saude = 0 # Criando uma variavel responsável pelo saude do usuário pós analiise de dados

# Variaveis respondaveis pelo treinamento da IA
x = [[covid, barato], [saudavel, barato], [saudavel, caro], [covid, caro]] 
y = [casa, viagem, casa, casa]

clf = tree.DecisionTreeClassifier()  # Instanciando uma arvore de classificação
clf = clf.fit(x, y)  # Treinando a IA

for row in data: # Fazendo a analise dos dados de cada usuário separadamente
    lista = list(row) # Convertendo tupla em lista
    if float(lista[3]) < ((float(lista[2]) * 30) / 100): # Se o valor da passágem for menor do que 30% do salário da pessoa defina a passagem como barata
        preco = 4
    else:
        preco = caro

    if lista[4] == "covid": # Se a pessoa não está com covid defina a pessoa como saúdavel 
        saude = covid
    elif lista[4] == "saudável":
        saude = saudavel

    if clf.predict([[saude, preco]]) == viagem: 
        print(lista[1]+" vai viajar ")
    elif clf.predict([[saude, preco]]) == casa:
        print(lista[1]+" vai ficar em casa ")
