from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text("RA"), sg.Input(key='senha')],
    [sg.Button('Entrar')],
    [sg.Text(size=(40, 1), key='mensagem')]
]

janela = sg.Window('Tela de login', layout)

banco_de_dados = {
    "joão": "1234",
    "paulo": "5522",
    "carol": "7733",
    "julia": "7896",
    "gustavo": "5913",
    "geovana": "9753",
    "pedro": "2469",
    "marcos": "7070",
    "amanda": "5427",
    "tiago": "1421"
}

def verificar_login(usuario, senha):
    return usuario in banco_de_dados and senha == banco_de_dados[usuario]

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if verificar_login(valores['usuario'], valores['senha']):
            janela['mensagem'].update('Acesso liberado', text_color='green')
        else:
            janela['mensagem'].update('Nome ou RA incorretos', text_color='red')

janela.close()