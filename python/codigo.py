# Passo a passo do projeto
# Passo 1: Entrar no sistemaa empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo5:Repetir o cadastro para todos os produtos
import pyautogui
import time

#pyautogui.write -> escrever o texto
#pyautogui.press -> apertar um tecla
#pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE=0.3

#abrir o microsoft edge
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")

#entrar no link
link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar o site carregar
time.sleep(2)

# Passo 2: Fazer login
pyautogui.click(x=735, y=544)
pyautogui.write("martins@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")

pyautogui.click(x=723, y=674)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de dados de produtos
import pandas as pd

tabela=pd.read_csv("projetos.csv")
print(tabela)


# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=811, y=350)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
#Preencher os campos
 # pegar da tabela o valor do campo que a gente quer preencher

    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim