import math
from flask import render_template, request

def calcular():
    try:
        num1 = float(request.form["num1"])
        operacao = request.form["operacao"]

        if operacao == "sqrt":
            if num1 < 0:
                return render_template("calculadora.html", etapas="Erro: Não existe raiz real de número negativo.", resultados="Erro")
            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"
                return render_template("calculadora.html", etapas=etapas, resultados=resultado)

        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template("calculadora.html", etapas="Informe o segundo número para esta operação.", resultados="Erro")
        
        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"
        elif operacao == "/":
            if num2 == 0:
                return render_template("calculadora.html", etapas="Erro: Divisão por zero não é permitida.", resultados="Erro")
            resultado = num1 / num2
            etapas = f"{num1} / {num2} = {resultado}"
        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} elevado a {num2} = {resultado}"
        elif operacao == "log":
            if num1 <= 0 or num2 <= 0 or num2 == 1:
                return render_template("calculadora.html", etapas="Erro: Base deve ser >0 e ≠1. Logaritmando deve ser >0.", resultados="Erro")
            resultado = math.log(num1, num2)
            etapas = f"Log de {num1} na base {num2} = {resultado}"
        else:
            return render_template("calculadora.html", etapas="Operação inválida.", resultados="Erro")

        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    except ValueError:
        return render_template("calculadora.html", etapas="Erro: Por favor, digite apenas números válidos.", resultados="Erro")
