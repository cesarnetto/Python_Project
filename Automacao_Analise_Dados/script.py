import pyautogui
import pandas
import pyperclip
import time

pyautogui.PAUSE = 0.5

# Entrar no sistema da empresa (link do drive)
pyautogui.press("win")
pyautogui.write("chrome") # abri o Chrome
pyautogui.press("enter")

time.sleep(2)

link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga" 
pyautogui.write(link) # digita o link do sistema
pyautogui.press("enter")
time.sleep(3)

# Navegar no sistema para encontrar a base de dados
pyautogui.click(x=1704, y=334, clicks=2)
time.sleep(3)

# Exportar a base de dados (baixar o arquivo)
pyautogui.click(x=1870, y=332) # seleciona o arquivo
time.sleep(2)
pyautogui.click(x=3226, y=330) # clica nos 3 pontos
time.sleep(3)
pyautogui.click(x=3007, y=430) # baixa o arquivo

time.sleep(4)

# Abrir a base de dados
caminho = r"C:\Users\Cesar Neto\Downloads\Vendas - Dez.xlsx"
tabela = pandas.read_excel(caminho)

# Visualizar as informações da base de dados
display(tabela)

# somar o faturamento de todos os produtos = somar a coluna de Valor Final
faturamento = tabela["Valor Final"].sum()
# somar a quantidade de produtos = somar a coluna de quantidade
qtde_produtos = tabela["Quantidade"].sum()

# abrir uma nova aba
pyautogui.hotkey("ctrl", "t")

# entrar no email
pyautogui.write("http://mail.google.com/")
pyautogui.press("enter")
time.sleep(8)

# clicar no botão escrever
pyautogui.click(x=1481, y=180)
time.sleep(6)

# Enviar o email
pyautogui.write("cesarnetto21@gmail.com")
pyautogui.press("tab") # seleciona o email
pyautogui.press("tab") # passar para o campo do assunto

# Assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Corpo do email
texto = f"""
Prezados,

Segue o relatório de vendas de hoje.

Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {qtde_produtos:,}

Qualquer dúvida estou à disposição.
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")


# Enviar o email
pyautogui.click(x=2666, y=1003)