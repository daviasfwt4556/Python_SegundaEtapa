from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def atividade_jinja():
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Atividade Jinja</title>
    </head>
    <body>
        <h2>1 e 2 - Mensagem, Nome e Idade</h2>
        <p>Olá, {{ nome }}.</p>
        <p>Idade demonstrada: {{ idade }} anos.</p>


        <h2>3 - Dados do Utilizador (Dicionario)</h2>
        <p>Nome: {{ usuario.nome }}</p>
        <p>Email: {{ usuario.email }}</p>


        <h2>4 - Lista de Alunos</h2>
        <ul>
        {% for aluno in alunos %}
            <li>{{ loop.index }} - {{ aluno }}</li>
        {% endfor %}
        </ul>


        <h2>5 - Validação de Nota</h2>
        <p>Nota final: {{ nota }}</p>
        <p>Resultado: 
        {% if nota >= 7 %}
            <strong>Aprovado</strong>
        {% else %}
            <strong>Reprovado</strong>
        {% endif %}
        </p>
    </body>
    </html>
    """
    
    return render_template_string(
        template,
        nome="Davi",
        idade=18,
        usuario={"nome": "Ana", "email": "ana@email.com"},
        alunos=["Bernardo", "Caio", "Clarice", "Davi Augusto", "Luanny", "Lucas"],
        nota=8.5
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
