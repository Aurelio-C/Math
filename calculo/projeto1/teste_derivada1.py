import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Derivada Numérica", layout="centered")
# Define o título da aplicação na aba do navegador e centraliza o layout da página

st.title("🔢 Calculadora de Derivada Numérica")
# Exibe o título principal na página Streamlit

st.markdown("Escolha a função, método, ponto de cálculo e veja gráficos!")
# Texto explicativo para o usuário sobre o que a aplicação faz

# Função para calcular a derivada numérica pela diferença central
def derivada_central(func, x, h=1e-7):
    """
    Calcula a derivada numérica de uma função usando o método da diferença central.

    Parâmetros:
    func : a função matemática a ser diferenciada
    x : float, o ponto onde a derivada será calculada
    h : float, passo pequeno para aproximação (padrão = 10^-7)

    Retorna:
    float : valor aproximado da derivada de func em x
    """
    return (func(x + h) - func(x - h)) / (2 * h)

# Bloco de formulário para entrada de dados pelo usuário
with st.form("formulario_calculo"):
    st.markdown("Exemplo: `np.sin(x)*x**2` ou `np.exp(x) / (x**2+2)`")
    # Mostra exemplos de funções que podem ser digitadas pelo usuário

    str_funcao = st.text_input("Digite a função f(x):", value="np.sin(x)*x**2")
    # Campo para o usuário digitar a função em notação Python, usando biblioteca numpy

    ponto_x = st.number_input("Calcular a derivada no ponto x =", value=1.0, step=0.1, format="%.2f")
    # Campo para o usuário digitar o ponto x onde quer calcular a derivada, com valor padrão 1.0

    mostra_grafico = st.checkbox("Mostrar gráfico local da função e derivada")
    # Checkbox para o usuário optar por visualizar o gráfico da função e sua derivada

    submitted = st.form_submit_button("Calcular Derivada")
    # Botão para submeter o formulário e iniciar o cálculo

# Após submissão do formulário
if submitted:
    try:
        # Cria a função matemática a partir da string digitada pelo usuário
        funcao_criada = lambda x: eval(str_funcao, {"np": np, "__builtins__": {}}, {"x": x})
        funcao_criada(ponto_x)  # Testa se a função pode ser avaliada no ponto x

        # Calcula a derivada numérica usando a função derivada_central
        resultado = derivada_central(funcao_criada, ponto_x, h=1e-7)
        st.success("Cálculo realizado!")
        # Mostra o resultado da derivada no ponto x com 6 casas decimais
        st.metric(label=f"Derivada f'({ponto_x})", value=f"{resultado:.6f}")

        # Se o usuário quer ver o gráfico, gera e exibe o gráfico da função e derivada localmente
        if mostra_grafico:
            xs = np.linspace(ponto_x - 2, ponto_x + 2, 200)  # valores x ao redor do ponto
            ys = [funcao_criada(x) for x in xs]  # valores da função f(x)
            dys = [derivada_central(funcao_criada, x, h=1e-7) for x in xs]  # valores da derivada f'(x)
            fig, ax = plt.subplots()
            ax.plot(xs, ys, label="f(x)")
            ax.plot(xs, dys, label="f'(x)")
            ax.axvline(ponto_x, color='gray', linestyle='--')  # linha vertical no ponto de cálculo
            ax.legend()
            st.pyplot(fig)

    except Exception as e:
        # Tratamento de erro para entrada inválida ou cálculo inválido
        st.error(f"Erro ao processar a função: {e}")
        st.error("Exemplo válido: `np.sin(x)*x**2`.")
