arquivo = open('Alunos.txt', 'r')
linhas = arquivo.readlines()
del linhas[:4]

#criar indicadores
qtde_anuncio = 0
qtde_org = 0
qtde_yt_org = 0
qtde_igfb_org = 0
qtde_site_org = 0

#percorrer o arquivo
for linha in linhas:
    email, origem = linha.split(',')
    if '_org' in origem:
        qtde_org += 1
        if 'hashtag_yt_org' in origem:
            qtde_yt_org += 1
        if 'hashtag_site_org' in origem:
            qtde_site_org += 1
        if 'hashtag_ig_org' in origem or 'hashtag_igfb_org' in origem:
            qtde_igfb_org += 1
    else:
        qtde_anuncio += 1
    
    
#fechar arquivo
arquivo.close()


with open('Indicadores.txt', 'w') as arquivo_indicadores:
    arquivo_indicadores.write('Quantidade Anuncio: {}\n'.format(qtde_anuncio))
    arquivo_indicadores.write('Quantidade Orgânico: {}\n'.format(qtde_org))
    arquivo_indicadores.write('Quantidade Youtube: {}\n'.format(qtde_yt_org))
    arquivo_indicadores.write('Quantidade Instagram: {}\n'.format(qtde_igfb_org))
    arquivo_indicadores.write('Quantidade Site: {}\n'.format(qtde_site_org))
print('Fim do Código')