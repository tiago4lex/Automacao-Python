# Passo 1: Abrir o sistema da empresa
#     Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
# Passo 2: Fazer login no Sistema
# Passo 3: Importar a base de dados dos produtos
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até acabar todos os produtos


import pyautogui
import time
import pandas

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# abrir navegador
pyautogui.press("winleft")
pyautogui.write("edge")
pyautogui.press("enter")

# acessar site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  
pyautogui.press("enter")

time.sleep(3)

# fazer login
pyautogui.click(x=600, y=450, clicks=1)
pyautogui.write("email@email")
pyautogui.press("tab")
pyautogui.write("senha1234")
pyautogui.press("tab")
pyautogui.press("enter")

# importar base de dados dos produtos
tabela = pandas.read_csv("C:/Users/Tiago/Documents/PROJETOS/Automação Python/produtos.csv")
print(tabela)
time.sleep(2)

# cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=600, y=300, clicks=1)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
        
    pyautogui.press("tab")
    
    pyautogui.press("enter")

    pyautogui.press("page_up")
