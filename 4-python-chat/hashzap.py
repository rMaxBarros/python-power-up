# Tela inicial: 
    # Título: Hashzap
    # Botão: iniciar chat
        # Quando clicar no botão:
        # ele vai abrir um pop-out/modal/alerta
            # Título: Bem-vindo ao hashzap
            # Caixa de texto: Escreva seu nome no chat
            # Botão: Entrar no chat
                # Quando clicar no botão:
                # fechar o popup
                # Sumir com o título
                # Sumir com o botão iniciar chat
                    # Carregar o chat
                    # Carregar o campo de enviar mensagem: Digite sua mensagem
                    # Carregar o botão Enviar
                        # Quando clicar no botão enviar: Enviar a mensagem e limpa a caixa de mensagem.

# Instalações de ferramentas pra criar sites no Python: Flet
# Com o flet é possível criar o front e back, além de versão pra desktop e mobile.
# Comando: pip install flet

# datetime

# Etapa 1: importar o flet
import flet as ft

# Etapa 2: criar uma função principal para rodar o seu aplicativo
# Função principal
# pagina -> onde os elementos serão colocados.
def main(pagina):
    # Título
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)

    # websocket - tunel de comunicação entre dois usuários
    # Para criar a comunicação entre usuários, é necessário 3 coisas:
    # 1: Criar a função que vai ser executada pelo túnel de comunicação
    # Essa função é executada pra todo mundo.
    def enviar_mensagem_tunel(mensagem):
        # executar tudo o que eu quero que aconteça para todos os usuários que recebem a mensagem
        texto = ft.Text(mensagem) # Cria o texto na tela de todos os usuários
        chat.controls.append(texto) # Adiciona o texto na tela de todos os usuáriios
        pagina.update() # Atualiza a página de todos os usuários
        

    # O que vai acontecer no túnel:
    # Pega a mensagem enviada -> cria um texto da mensagem -> adiciona o texto no chat de todos os usuários -> atualiza o chat de todos os usuários
    # 2: criar o túnel
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
        # pubsub: nome do túnel que o flet dá ao túnel
        # explicando: pegando o aplicativo(pagina), criando o túnel de comunicação(pubsub) e sempre que alguma coisa for enviada no túnel (subscribe), execute a mensagem.


    # Adicionando as mensagens enviadas pro chat em forma de coluna, uma embaixo da outra.
    def enviar_mensagem(evento):
        # pegando o nome do usuário e o valor da mensagem escrita
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value

        # 3: Enviar a mensagem no túnel de comunicação
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
                # ANTES: criava o texto = ft.Text(f"{nome_usuario}: {texto_campo_mensagem}")
                # e adicionava no chat =  chat.controls.append(texto)
                # DEPOIS: envia a mensagem no túnel de comunicação.
        # Enviando a mensagem no túnel de comunicação:
        pagina.pubsub.send_all(mensagem)

        # Limpar a caixa de enviar mensagem
        campo_enviar_mensagem = ""
        pagina.update()

    # on_submit=enviar_mensagem: envia a mensagem com o enter.
    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", 
                                         on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # Mexer no visual da tela
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    # Os dois campos irão aparecer em forma de linha e não um embaixo do outro.

    # Criando um container de colunas onde ficarão as mensagens
    chat = ft.Column()

    def entrar_chat(evento):
        # fechar o popup
        popup.open = False

        # Sumir com o título
        pagina.remove(titulo)

        # Sumir com o botão iniciar chat
        pagina.remove(botao)

        # Carregar o chat
        pagina.add(chat)

        # Carregar o campo de enviar mensagem
        pagina.add(linha_enviar)
        # Carregar o botão enviar
        pagina.add(botao_enviar)

        # Adicionar no chat a mensagem que o usuário entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        # ANTES do túnel: texto_mensagem = ft.Text(f"{nome_usuario} entrou no chat")
                        # chat.controls.appen(texto_mensagem)
        pagina.pubsub.send_all(mensagem)

        pagina.update()


    # criar o popup
    titulo_popup = ft.Text("Bem-vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, 
                           content=caixa_nome, 
                           actions=[botao_popup])
    # Como actions está no plural, precisa passar uma lista de botões, mesmo que só tenha 1.

    # Sempre que associa uma função ao click de um botão, significa que a função obrigatoriamente recebe o evento de click do botão como parâmetro (não necessariamente ele vai ser usado. Mas precisa).
    # O que vai acontecer quando o usuário clicar no botão
    def abrir_popup(evento):
        # Colocar o popup na tela
        pagina.dialog = popup
        popup.open = True
        # Sempre que uma função atualiza algo visual na tela, precisa do update.
        pagina.update()

    # Botão Inicial
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    pagina.add(botao)

# Etapa 3: executar essa função com o flet
# Parâmetro view: muda a forma como o programa será exibido, como um "programa", no navegador, etc. 
ft.app(main, view=ft.WEB_BROWSER)
