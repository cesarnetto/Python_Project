# 🤖 Automação de Processos com Python

Projeto desenvolvido durante a aula de automação utilizando Python, com o objetivo de automatizar tarefas repetitivas, manipular dados e gerar um relatório de vendas de forma automática.

## 📚 O que aprendi

Durante esta aula foram abordados os seguintes conceitos:

- Automatização de tarefas utilizando **PyAutoGUI**;
- Controle do teclado e do mouse por código;
- Abertura de programas e navegação entre aplicações;
- Manipulação de planilhas Excel com **Pandas**;
- Cálculo de indicadores a partir dos dados;
- Geração e envio automático de e-mails;
- Utilização do **Pyperclip** para copiar textos longos sem perda de formatação;
- Controle de tempo de execução utilizando `time.sleep()`.

## 🛠️ Tecnologias utilizadas

- Python 3
- PyAutoGUI
- Pandas
- OpenPyXL
- Pyperclip

## 📌 Fluxo da automação

1. Abre o navegador.
2. Acessa o sistema.
3. Baixa a planilha de vendas.
4. Lê os dados da planilha.
5. Calcula:
   - Faturamento total;
   - Quantidade de produtos vendidos.
6. Abre o Gmail.
7. Envia automaticamente o relatório por e-mail.

## 📍 Ferramenta para descobrir posições da tela

Como as coordenadas do mouse variam de computador para computador, utilize o código abaixo para descobrir a posição exata onde deseja clicar.

```python
import pyautogui
import time

time.sleep(5)  # Tempo para posicionar o mouse
print(pyautogui.position())
```

Após executar o script, posicione o cursor sobre o local desejado e aguarde 5 segundos. As coordenadas serão exibidas no terminal e poderão ser utilizadas com:

```python
pyautogui.click(x=0, y=0)
```

## 📦 Instalação

Instale as dependências com:

```bash
pip install pyautogui pandas openpyxl pyperclip
```

## ⚠️ Observação

As coordenadas utilizadas no projeto foram obtidas na minha máquina. Caso execute a automação em outro computador, será necessário capturar novamente as posições do mouse utilizando a ferramenta acima.