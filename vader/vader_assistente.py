from tkinter import *
import json
import sounddevice as sd
import speech_recognition as sr
import wavio as wv



#abre json
with open("info_feriados.json") as jsonFile:
    dados = json.load(jsonFile)
feriado_1_janeiro = dados['feriado_1_janeiro']
razao_1_janeiro = dados['razao_1_janeiro']
origem_1_janeiro = dados['origem_1_janeiro']
feriado_21_abril = dados['feriado_21_abril']
razao_21_abril = dados['razao_21_abril']
origem_21_abril = dados['origem_21_abril']
feriado_1_maio = dados['feriado_1_maio']
razao_1_maio = dados['razao_1_maio']
origem_1_maio = dados['origem_1_maio']
feriado_12_outubro = dados['feriado_12_outubro']
razao_12_outubro = dados['razao_12_outubro']
origem_12_outubro = dados['origem_12_outubro']
feriado_2_novembro = dados['feriado_2_novembro']
razao_2_novembro = dados['razao_2_novembro']
origem_2_novembro = dados['origem_2_novembro']
feriado_25_dezembro = dados['feriado_25_dezembro']
razao_25_dezembro = dados['razao_25_dezembro']
origem_25_dezembro = dados['origem_25_dezembro']


def ia():
    # Importando arquivos de voz
    filename = "minhavoz.wav"
    falaia = "falaia.mp3"

    # Declarar globalmente a variável
    global says

    # Função de gravar áudio para reconhecimento.
    def grava():
        freq = 48000  # frequência
        duration = 7  # Duração de cada gravação
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        print('Estou te ouvindo, pode falar!')
        sd.wait()
        wv.write("minhavoz.wav", recording, freq, sampwidth=2)
        print('Certo! Processando...')

    while True:
        grava()

        # Iniciando o reconhecimento de fala
        r = sr.Recognizer()

        try:
            with sr.AudioFile(filename) as source:
                # "Escutando" o arquivo
                audio_data = r.record(source)
                # Convertendo de audio para texto
                says = r.recognize_google(audio_data, language='pt-BR')
                # Escrevendo o que foi dito.
                print('Você falou: ' + says.lower())
                texto = says.lower()

                # JANEIRO 01
                if 'dia primeiro.de janeiro' in texto:
                    print(f'Dia 1º de janeiro, {feriado_1_janeiro}')

                elif 'razão para comemorar o ano novo' in texto:
                    print(f'O motivo pelo qual o feriado é comemorado é: {razao_1_janeiro}')

                elif 'conte-me mais sobre o feriado do ano novo' in texto:
                    print(f'Certo, uma breve história: {origem_1_janeiro}')

                # ABRIL 21
                elif 'dia 21 de abril' in texto:
                    print(f'Dia 21 de abril, {feriado_21_abril}')
                    # fala(f'Dia 21 de abril, {feriado_21_abril}')

                elif 'razão para comemorar o dia de tiradentes' in texto:
                    print(f'O motivo pelo qual o feriado é comemorado é: {razao_21_abril}')

                elif 'conte-me mais sobre o feriado de tiradentes' in texto:
                    print(f'Certo, uma breve história: {origem_21_abril}')

                # MAIO 01
                elif 'dia primeiro.de maio' in texto:
                    print(f'Dia primeiro de maio, {feriado_1_maio}')

                elif 'razão para comemorar o dia do trabalho' in texto:
                    print(f'O motivo pelo qual o feriado é comemorado é: {razao_1_maio}')

                elif 'conte-me mais sobre o feriado do trabalho' in texto:
                    print(f'Certo, uma breve história: {origem_1_maio}')

                # OUTUBRO 12
                elif ' dia 12 de outubro' in texto:
                    print(f'Dia 12 de outubro, {feriado_12_outubro}')

                elif 'razão para comemorar o dia da nossa senhora' in texto:
                    print(f'O motivo pelo qual o feriado é comemorado é: {razao_12_outubro}')

                elif 'conte-me mais sobre o feriado da nossa senhora' in texto:
                    print(f'Certo, uma breve história: {origem_12_outubro}')

                # NOVEMBRO 02
                elif 'dia 2 de novembro' in texto:
                    print(f'Dia 2 de novembro, {feriado_2_novembro}')

                elif 'razão para comemorar o dia de finados' in texto:
                    print(f'O motivo pelo qual o feriado é comemorado é: {razao_2_novembro}')

                elif 'conte-me mais sobre o feriado de finados' in texto:
                    print(f'Certo, uma breve história: {origem_2_novembro}')

                # DEZEMBRO 25
                elif 'dia 25 de dezembro' in texto:
                    print(f'Dia 25 de dezembro, {feriado_25_dezembro}')

                elif 'razão para comemorar o natal' in texto:
                    print(f'O motivo pelo qual o feriado é comemorado é: {razao_25_dezembro}')

                elif 'conte-me mais sobre o feriado de natal' in texto:
                    print(f'Certo, uma breve história: {origem_25_dezembro}')

        # Se ocorrer algum erro, retornará:
        except Exception as e:
            print('Este comando não é válido!')


window = Tk()
window.title('Vader - Assistente Virtual')
photo = PhotoImage(file=r"/home/davi/vader_talking.gif")
photo_image = photo.subsample(3, 3)
Button(window, text='Clique em mim!', image=photo_image, compound=LEFT, command=ia).pack(side=TOP)

mainloop()
