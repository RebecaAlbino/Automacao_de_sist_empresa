# Passo a passo
# Passo 1 - Entrar no Sistema da Empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar -> pyautogui.press
# apertar -> pyautogui.hotkey
# rolar -> pyautogui.scroll
import pyautogui
import time

pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("chome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)
# Passo 2 - Fazer Login

pyautogui.click(x=438, y=393)
pyautogui.write("emailficticio2024.gmail.com")
pyautogui.press("tab")
pyautogui.write("senha exemplo")
pyautogui.click(x=666, y=558)
time.sleep(1)

# Passo 3 - Importar a tabela  com banco de dados

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 - Cadastrar banco de dados

for linha in tabela.index:
    #Pegar posição do campo
    pyautogui.click(x=479, y=259)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # escrever no campo
    pyautogui.write(str(codigo))
    #passar para o proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # = "1"
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

#enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")
# dar scroll de tudo pra cima
    pyautogui.scroll(1000)
# Passo 5 - Repetir o processo até o fim dos dados

