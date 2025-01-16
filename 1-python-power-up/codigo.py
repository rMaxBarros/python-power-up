# Biblioteca: automotiza tarefas 
# pyautogui: para automoção de tarefas.
# pip install pyautogui

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5 # Espera 1s a cada comando executado.

# pyautogui.click -> clicar
# pyautogui.hotkey("Ctrl", "C") -> atalho de teclado


# Passo 1: Abrir o sistema da empresa
#     Sistema:

# Abre o Iniciar do Windows
pyautogui.press("win")
# Abrir o Opera
pyautogui.write("Opera")
# Apertar enter
pyautogui.press("enter")

#Pausa para esperar o navegador abrir.
time.sleep(2)

# Abrir o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Pausa de 3s, pois pode ser que o site demore para carregar.
time.sleep(3)


# Passo 2: Fazer login
# Clicar na caixa de login
pyautogui.click(x=835, y=455)
# Escrever o email
pyautogui.write("email@email.com")
# Pressionar tab para passar para o campo de senha
pyautogui.press("tab")
# Digite senha
pyautogui.write("senha")
# Pressionar tab para passar para o botão de logar
pyautogui.press("tab")
pyautogui.press("enter")


# Passo 3: Importar a base de dados dos produtos

# Pacote para trabalhar com dados no python
# pip install pandas openpyxl

# Lendo o arquivo csv e armazenando na variável tabela
tabela = pandas.read_csv("produtos.csv")

print(tabela)


time.sleep(2)
# Passo 4: Cadastrar um produto

# Para cada item dentro de uma lista de itens, faça. O python chama as linhas de index
for linha in tabela.index: 

    pyautogui.click(x=867, y=306) # clica no primeiro campo
    # DICA: Sempre que for fazer operação pra vários itens, pensa sempre como será o processo pra UM.

    # CÓDIGO
    # .loc é entre [] porque em toda tabela é passada com valor, chave.
    codigo = tabela.loc[linha, "codigo"] # Pegando a informação da tabela
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # MARCA
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # TIPO
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # CATEGORIA
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) # Transformando o número em string
    pyautogui.press("tab")

    # PREÇO UNITÁRIO
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # CUSTO
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs) # Só vai preencher obs se tiver algum valor.
    pyautogui.press("tab")

    pyautogui.press("enter") # Apertar o botão de enviar.

    # Scroll da tela
    pyautogui.scroll(10000)

# Passo 5: Repetir o passo 4 até acabar todos os produtos


# nan: valor vazio em uma base de dados

# Exemplos:
    # pyautogui.press("win") -> Abre o Iniciar do Windows