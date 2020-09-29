from matplotlib import pyplot

def saveMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    # Mostrando os dados e a grade
    text = f'Overshoot: {malha.overshoot}%'
    pyplot.text(0.5, 0.3, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
    pyplot.grid(True)

    # Salvando a figura
    pyplot.savefig(f'img/{malha.legenda}.png')

def saveMalhas(arrayMalha):

    # Adicionando todas as malhas no plot
    for malha in arrayMalha:
        pyplot.plot(malha.resposta, label=f'{malha.legenda}')
        pyplot.legend()    

    # Salvando todas as malhas passadas
    pyplot.grid(True)
    pyplot.savefig('img/malhas.png')

def plotMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    # Mostrando os dados e a grade
    if malha.tempo_acomodacao != 0:
        pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao, c='black', alpha = 0.8)	
        pyplot.annotate(f'x = {malha.tempo_acomodacao}\ny = {malha.valor_acomodacao}', (malha.tempo_acomodacao, malha.valor_acomodacao))	
        text = f'{malha.overshoot}\nValor de acomodação: {malha.valor_acomodacao}\nTempo de acomodação: {malha.tempo_acomodacao}s'
    else:
        text = f'Overshoot: {malha.overshoot}%\nErro: {malha.erroRegimePermanente}'
        
    pyplot.text(0.5, 0.3, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
    pyplot.grid(True)

    # Mostrando a malha
    pyplot.grid(True)
    pyplot.show()

def plotMalhas(arrayMalha):

    # Adicionando todas as malhas no plot
    for malha in arrayMalha:
        pyplot.plot(malha.resposta, label=f'{malha.legenda}')
        pyplot.legend()

    # Mostrando todas as malhas passadas
    pyplot.grid(True)
    pyplot.show()

def plotAndSaveMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    # Mostrando os dados e a grade
    text = f'Overshoot: {malha.overshoot}%'
    pyplot.text(0.5, 0.3, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
    pyplot.grid(True)

    # Mostrando a malha
    pyplot.grid(True)
    pyplot.savefig(f'img/{malha.legenda}.png')
    pyplot.show()

def plotAndSaveMalhas(arrayMalha):

    # Adicionando todas as malhas no plot
    for malha in arrayMalha:
        pyplot.plot(malha.resposta, label=f'{malha.legenda}')
        pyplot.legend()

    # Mostrando todas as malhas passadas
    pyplot.grid(True)
    pyplot.savefig('img/malhas.png')
    pyplot.show()