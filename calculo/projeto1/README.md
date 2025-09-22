# Projeto: Calculadora de Derivada Numérica em Streamlit

Este projeto é uma aplicação web simples desenvolvida com Streamlit para calcular a derivada numérica de uma função matemática dada pelo usuário em um ponto específico, utilizando o método da diferença central. Oferece também a opção de exibir o gráfico da função e sua derivada localmente.

---

## Passo 1 - Importação das bibliotecas

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

text
As bibliotecas importadas são:
- `streamlit` para criar a interface web interativa.
- `numpy` para operações matemáticas, como funções e manipulação de arrays.
- `matplotlib.pyplot` para criar os gráficos exibidos na aplicação.

---

## Passo 2 - Configuração da página do Streamlit

st.set_page_config(page_title="Derivada Numérica", layout="centered")

text
Configura o título da aba do navegador e centraliza o layout da aplicação na tela.

---

## Passo 3 - Criação do título e descrição da aplicação

st.title("🔢 Calculadora de Derivada Numérica")
st.markdown("Escolha a função, método, ponto de cálculo e veja gráficos!")

text
Exibe o título principal e uma breve descrição para instruir o usuário sobre o propósito da aplicação.

---

## Passo 4 - Definição da função para cálculo da derivada numérica

def derivada_central(func, x, h=1e-7):
"""
Calcula a derivada numérica de uma função usando o método da diferença central.

text
Parâmetros:
func : função matemática a ser diferenciada
x : ponto onde a derivada será calculada (float)
h : passo pequeno para a aproximação da derivada (float, padrão 10^-7)

Retorna:
float : valor aproximado da derivada de func em x
"""
return (func(x + h) - func(x - h)) / (2 * h)
text
Esta função recebe uma outra função `func`, um ponto `x` e um passo pequeno `h`. Ela calcula a derivada aproximada no ponto `x` pela fórmula da diferença central:
\[
f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}
\]

---

## Passo 5 - Criando o formulário de entrada no Streamlit

with st.form("formulario_calculo"):
st.markdown("Exemplo: np.sin(x)*x**2 ou np.exp(x) / (x**2+2)")
str_funcao = st.text_input("Digite a função f(x):", value="np.sin(x)*x**2")
ponto_x = st.number_input("Calcular a derivada no ponto x =", value=1.0, step=0.1, format="%.2f")
mostra_grafico = st.checkbox("Mostrar gráfico local da função e derivada")
submitted = st.form_submit_button("Calcular Derivada")

text

Dentro deste formulário, o usuário:
- Digita a função matemática em notação Python com `numpy`.
- Define o ponto onde quer calcular a derivada.
- Escolhe se deseja mostrar o gráfico.
- Envia o formulário para processar o cálculo.

---

## Passo 6 - Processamento após submissão do formulário

if submitted:
try:
funcao_criada = lambda x: eval(str_funcao, {"np": np, "builtins": {}}, {"x": x})
funcao_criada(ponto_x) # Testa a função no ponto x
resultado = derivada_central(funcao_criada, ponto_x, h=1e-7)
st.success("Cálculo realizado!")
st.metric(label=f"Derivada f'({ponto_x})", value=f"{resultado:.6f}")

text
    if mostra_grafico:
        xs = np.linspace(ponto_x - 2, ponto_x + 2, 200)
        ys = [funcao_criada(x) for x in xs]
        dys = [derivada_central(funcao_criada, x, h=1e-7) for x in xs]
        fig, ax = plt.subplots()
        ax.plot(xs, ys, label="f(x)")
        ax.plot(xs, dys, label="f'(x)")
        ax.axvline(ponto_x, color='gray', linestyle='--')
        ax.legend()
        st.pyplot(fig)

except Exception as e:
    st.error(f"Erro ao processar a função: {e}")
    st.error("Exemplo válido: `np.sin(x)*x**2`.")
text

- A string da função é convertida para uma função Python usando `eval` com segurança básica.
- A função é testada no ponto escolhido.
- A derivada numérica é calculada usando o método da diferença central.
- O resultado é exibido com até 6 casas decimais.
- Se o usuário optou pelo gráfico, ele é gerado ao redor do ponto escolhido, mostrando a função original e a derivada.
- Caso haja erro na função ou no cálculo, mensagens de erro são exibidas.

---

## Considerações finais

Este projeto utiliza uma interface simples mas funcional para cálculos matemáticos em tempo real. A abordagem com `eval` permite flexibilidade para o usuário digitar diversas funções usando `numpy`. A visualização gráfica auxilia na compreensão da derivada localmente.

---

Este detalhamento cobre cada etapa do código do projeto "teste_derivada1.py", explicando a estrutura e funcionamento da aplicação de cálculo de derivada numérica. Caso queira, posso ajudar com melhorias neste código ou outras funcionalidades relacionadas.

