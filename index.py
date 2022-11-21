
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bem vindo ao Humanitar Dados'

@app.route('/buscar/<termo_de_busca>')
def buscar(termo_de_busca):
#    while True:
#        pagina_de_busca = pagina_padrao
#        pagina_de_busca = pagina_de_busca + 'voce digitou:'+termo_de_busca
    nome_de_busca = str(termo_de_busca)
    return f'Você digitou ${nome_De_busca}'
#        nome_de_busca = nome_de_busca.replace(' ','+')
#        resultado_da_busca = session.get('https://www.buscagrupos.com.br/grupo.php?p='+nome_de_busca+'&categoria=whatsapp') #'https://www.google.com/search?q=%22'+nome_de_busca+'%22+grupo%22whatsapp') #+site%3Achat.whatsapp.com')
#        texto = resultado_da_busca.html.texto
#        pagina_de_busca = pagina_de_busca + 'resultado bruto da busca:'+str(texto)
#        continue
#    return pagina_de_busca


#==========================================================
#        PROJETO PARA HUMANITAR
#==========================================================


#print('iniciando teste de capitura de dados da api da humanitar')
#print('iniciando execução')

#url_humanitar = 'https://humanitar.net/api/claudio/tempodeespera'
#api_tempo_de_espera = 'https://humanitar.net/api/controlador/waittime'

#html = os.popen('curl https://humanitar.net/api/claudio/tempodeespera').read()
#=========================
#import urllib.request, json
#with urllib.request.urlopen(api_tempo_de_espera) as url:
#    data = json.load(url)
#    print(data)
#=========================
#print('resultado: '+str(page))'''

'''
O que curl 56 recebeu o código HTTP 403 do proxy depois de conectar?
Ao receber uma resposta 403, o servidor está lhe dizendo :
“Sinto muito. Eu sei quem você é - eu acredito em quem você diz que é
- mas você simplesmente não tem permissão para acessar este recurso.
Talvez se você pedir gentilmente ao administrador do sistema, obtenha permissão.

'''

#print('fim da leitura da api da humanitar')