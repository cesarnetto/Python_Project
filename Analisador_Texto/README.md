# Analisador de Texto

### Info:

Programa analisa um texto fornecido pelo usuário, conta o número de palavras (independentemente se há repetição ou não), a quantidade de cada palavra e a quantidade de cada letra. Ignora letras maiúsculas e minúsculas ao contar letras (ou seja, transforma tudo para minúsculas). Tratamento para pontuação e espaço ao contar palavras.

### Aplicação:

Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve imprimir:

```
Contagem de palavras: 8
Frequência de palavras: Counter({'Olá': 2, 'mundo': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1})
Frequência de letras: Counter({' ': 7, 'e': 6, 'o': 4, 't': 4, 'm': 3, 'n': 3, 'l': 2, 'á': 2, 'u': 2, 's': 2, 'd': 1, 'é': 1, 'v': 1, 'a': 1})
```

### Documentações

- https://docs.python.org/pt-br/3/library/string.html
- https://docs.python.org/pt-br/3/library/stdtypes.html?highlight=translate#str.maketrans
- https://docs.python.org/pt-br/3/library/stdtypes.html?highlight=translate#str.translate