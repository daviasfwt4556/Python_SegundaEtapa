from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Atividade 5 - Login</title>
        </head>
        <body>
            <h2>Pagina de Login</h2>
            <form method="POST">
                <label>Nome:</label><br>
                <input type="text" name="usuario" placeholder="Insere o teu nome"><br><br>
                
                <label>Senha (Matricula):</label><br>
                <input type="password" name="senha" placeholder="Insere a tua matricula"><br><br>
                
                <button type="submit">Entrar</button>
            </form>
        </body>
        </html>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario.lower() == 'davi' and senha == '123456':
        return f"<h1>Bem-vindo, {usuario.capitalize()}! Acesso autorizado gata 🎉.</h1>"
    else:
        return "<h1>Você é tão  irrelevante que nem tem login kkkkkkkkk</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True, port=5001)