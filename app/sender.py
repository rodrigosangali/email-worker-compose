from bottle import route, run, request

#atende a rota raiz para o metodo post
@route('/', method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    return 'Mensagem enfileirada ! Assunto: {} Mensagem {}'.format(assunto, mensagem)

# verifica se é o arquivo principal
if __name__ == '__main__':
    #disponibiliza o serviço(onde tem a action no html)
    run(host='0.0.0.0', port=8080, debug=True)