import streamlit as st
import sympy
import numpy as np
import matplotlib.pyplot as plt


# Função principal do passo a passo visual da derivada
def gerar_passos_derivada_visual(expr, var):
    """
    Renderiza passo a passo detalhado da derivada simbólica da expressão em relação à variável var.
    """
    st.subheader("Passo a Passo Detalhado da Derivada")
    st.markdown(f"Vamos derivar a função em relação a \\( {var} \\):")
    st.latex(f"f({var}) = {sympy.latex(expr)}")
    st.markdown("---")

    derivada_final = _derivar_com_explicacao(expr, var)

    st.markdown("---")
    st.success("**Resultado Final da Derivada:**")
    st.latex(f"\\frac{{d}}{{d{var}}} \\left( {sympy.latex(expr)} \\right) = {sympy.latex(derivada_final)}")


def _derivar_com_explicacao(expr, var):
    """
    Função recursiva que calcula a derivada de expr em relação a var
    e exibe passo a passo utilizando st.markdown e st.latex.
    """

    # Casos base
    if expr.is_number or (expr.is_constant() and not expr.has(var)):
        st.markdown(f"* A derivada da constante \\( {sympy.latex(expr)} \\) é 0.")
        return sympy.Integer(0)
    if expr == var:
        st.markdown(f"* A derivada de \\( {var} \\) em relação a si mesmo é 1.")
        return sympy.Integer(1)
    if expr.is_symbol and expr != var:
        st.markdown(f"* A derivada de \\( {sympy.latex(expr)} \\) (constante em relação a \\({var}\\)) é 0.")
        return sympy.Integer(0)

    # Regra da soma
    if isinstance(expr, sympy.Add):
        st.info("**Regra da Soma**")
        st.markdown("Derivamos cada termo separadamente:")
        st.latex(sympy.latex(expr))
        termos_derivados = []
        for i, termo in enumerate(expr.args, 1):
            st.markdown(f"**Termo {i}:** Derivando \\( {sympy.latex(termo)} \\)")
            with st.expander("Mostrar derivação do termo"):
                termos_derivados.append(_derivar_com_explicacao(termo, var))
        resultado = sympy.Add(*termos_derivados)
        st.success("**Resultado da Soma:**")
        st.latex(sympy.latex(resultado))
        return resultado

    # Regra do produto e multiplicação por constante
    if isinstance(expr, sympy.Mul):
        constante, funcao = expr.as_coeff_Mul()
        if constante != 1:
            st.info("**Regra da Constante Múltipla**")
            st.markdown("Mantemos a constante e derivamos a função:")
            st.latex(sympy.latex(expr))
            derivada_funcao = _derivar_com_explicacao(funcao, var)
            resultado = constante * derivada_funcao
            st.success("**Resultado:**")
            st.latex(f"{sympy.latex(constante)} \\cdot \\left({sympy.latex(derivada_funcao)}\\right) = {sympy.latex(resultado)}")
            return resultado
        else:
            # Regra do produto para u*v
            u, v = expr.args[0], sympy.Mul(*expr.args[1:])
            st.info("**Regra do Produto**")
            st.markdown("Dada a expressão:")
            st.latex(sympy.latex(expr))
            st.latex("(u \\cdot v)' = u' \\cdot v + u \\cdot v'")
            st.latex(f"u = {sympy.latex(u)}")
            st.latex(f"v = {sympy.latex(v)}")

            st.markdown("Derivando \\( u \\):")
            du = _derivar_com_explicacao(u, var)
            st.markdown("Derivando \\( v \\):")
            dv = _derivar_com_explicacao(v, var)

            resultado = du * v + u * dv
            st.success("**Resultado da Regra do Produto:**")
            st.latex(f"({sympy.latex(du)}) \\cdot ({sympy.latex(v)}) + ({sympy.latex(u)}) \\cdot ({sympy.latex(dv)}) = {sympy.latex(resultado)}")
            return resultado

    # Regra da potência com cadeia
    if isinstance(expr, sympy.Pow):
        base, expoente = expr.args
        if not expoente.has(var):
            st.info("**Regra da Potência com Regra da Cadeia**")
            st.markdown("Para expressão:")
            st.latex(sympy.latex(expr))
            st.latex("\\frac{d}{dx}[u(x)]^n = n \\cdot [u(x)]^{n-1} \\cdot u'(x)")
            st.latex(f"u = {sympy.latex(base)}, \\quad n = {sympy.latex(expoente)}")

            st.markdown("Derivando a base \\( u \\):")
            du = _derivar_com_explicacao(base, var)

            resultado = expoente * base**(expoente - 1) * du
            st.success("**Resultado da Regra da Potência:**")
            st.latex(f"{sympy.latex(expoente)} \\cdot ({sympy.latex(base)})^{{{sympy.latex(expoente - 1)}}} \\cdot ({sympy.latex(du)}) = {sympy.latex(resultado)}")
            return resultado

    # Funções especiais com Regra da Cadeia
    func_map = {
        sympy.sin: sympy.cos,
        sympy.cos: lambda x: -sympy.sin(x),
        sympy.tan: lambda x: sympy.sec(x)**2,
        sympy.exp: sympy.exp,
        sympy.log: lambda x: 1/x
    }
    if expr.func in func_map:
        u = expr.args[0]
        f_name = expr.func.__name__
        df_str = sympy.latex(func_map[expr.func](var)).replace(str(var), 'u')
        st.info(f"**Regra da Cadeia para função {f_name}**")
        st.markdown("Expressão:")
        st.latex(sympy.latex(expr))
        st.latex(f"\\frac{{d}}{{dx}} {f_name}(u) = {df_str} \\cdot \\frac{{du}}{{dx}}")
        st.latex(f"u = {sympy.latex(u)}")

        st.markdown("Derivando a função interna \\( u \\):")
        du = _derivar_com_explicacao(u, var)

        df = func_map[expr.func](u)
        resultado = df * du
        st.success("**Resultado da Regra da Cadeia:**")
        st.latex(f"({sympy.latex(df)}) \\cdot ({sympy.latex(du)}) = {sympy.latex(resultado)}")
        return resultado

    # Caso geral: derivada direta pelo sympy se nenhum caso anterior aplicado
    st.warning(f"Derivando diretamente com SymPy para expressão \\({sympy.latex(expr)}\\).")
    return sympy.diff(expr, var)


def main():
    # Configuração da aplicação
    st.set_page_config(page_title="Calculadora de Derivadas com Passo a Passo", layout="wide")
    st.title("🧮 Calculadora de Derivadas com Passo a Passo Dinâmico")
    st.write("Calcula derivadas com visualização, simplificação, avaliação e passo a passo com LaTeX.")

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.subheader("Entradas")
        str_expr = st.text_input("Digite a função f(x, y, z...):", value="tan(5*x)/sqrt(x**3 + 2)",
                                 help="Use sintaxe Python: sin, cos, tan, exp, log, sqrt.")
        str_var = st.text_input("Variável para derivação:", value="x", max_chars=1)
        ordem = st.number_input("Ordem da derivada:", min_value=1, value=1, step=1)
        pontos_txt = st.text_input("Avaliar em (pontos separados por vírgula):", value="1",
                                  help="Valores numéricos para avaliação da função e derivada.")
        simplificacao = st.selectbox("Manipulação simbólica:",
                                     ["Nenhuma", "Simplificar", "Expandir", "Fatorar"])
        mostrar_passo = st.checkbox("Mostrar passo a passo", value=True)
        mostrar_grafico = st.checkbox("Mostrar gráfico", value=True)

    with col2:
        st.subheader("Resultados")

        # Define símbolos para variáveis na expressão
        variavel = sympy.symbols(str_var)
        local_dict = {str_var: variavel}
        for c in str_expr:
            if c.isalpha() and c not in local_dict:
                local_dict[c] = sympy.symbols(c)
        local_dict.update({'sin': sympy.sin, 'cos': sympy.cos, 'tan': sympy.tan, 'sec': sympy.sec,
                           'log': sympy.log, 'exp': sympy.exp, 'sqrt': sympy.sqrt,
                           'Abs': sympy.Abs, 'pi': sympy.pi, 'E': sympy.E})

        # Tentativa de transformar a expressão em símbolo SymPy
        try:
            expr_original = sympy.sympify(str_expr, locals=local_dict)
            numerador, denominador = expr_original.as_numer_denom()
            expr = sympy.powdenest(numerador * sympy.Pow(denominador, -1))

            derivada = expr
            for _ in range(ordem):
                derivada = sympy.diff(derivada, variavel)

            # Aplicação de manipulação simbólica opcional
            if simplificacao == "Simplificar":
                derivada = sympy.simplify(derivada)
            elif simplificacao == "Expandir":
                derivada = sympy.expand(derivada)
            elif simplificacao == "Fatorar":
                derivada = sympy.factor(derivada)

            st.markdown("##### Função Original:")
            st.latex(f"f({str_var}) = {sympy.latex(expr_original)}")
            st.markdown(f"##### Derivada (Ordem {ordem} em relação a {str_var}):")
            st.latex(f"\\frac{{d^{ordem}}}{{d{str_var}^{ordem}}} f = {sympy.latex(derivada)}")

            # Avaliação numérica nos pontos especificados
            pontos = []
            if pontos_txt:
                try:
                    pontos = [float(p.strip()) for p in pontos_txt.split(",") if p.strip()]
                except:
                    st.warning("Erro ao interpretar pontos de avaliação.")

            if pontos:
                st.markdown("##### Avaliações numéricas:")
                for pt in pontos:
                    try:
                        val_f = expr_original.subs(variavel, pt).evalf()
                        val_d = derivada.subs(variavel, pt).evalf()
                        st.write(f"Para \\({str_var}={pt}\\):  \\(f({pt}) \\approx {val_f:.4f}\\) e \\(f'({pt}) \\approx {val_d:.4f}\\)")
                    except Exception as e:
                        st.write(f"Não foi possível avaliar em {pt}: {e}")

            # Mostrar passo a passo para derivada de primeira ordem
            if mostrar_passo:
                if ordem == 1:
                    gerar_passos_derivada_visual(expr, variavel)
                else:
                    st.info("Passo a passo visual disponível somente para derivada de primeira ordem.")

            # Mostrar gráfico da função e derivada
            if mostrar_grafico:
                st.markdown("---")
                st.markdown("##### Gráfico da Função e Derivada")
                x_min, x_max = (min(pontos) - 2, max(pontos) + 2) if pontos else (-5, 5)
                x_vals = np.linspace(x_min, x_max, 400)
                f_np = sympy.lambdify(variavel, expr_original, modules=["numpy"])
                d_np = sympy.lambdify(variavel, derivada, modules=["numpy"])
                with np.errstate(divide='ignore', invalid='ignore'):
                    y_vals, dy_vals = f_np(x_vals), d_np(x_vals)
                y_vals[np.abs(y_vals) > 50] = np.nan
                dy_vals[np.abs(dy_vals) > 50] = np.nan
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label=f"f({str_var})")
                ax.plot(x_vals, dy_vals, label=f"Derivada (ordem {ordem})", linestyle='--')
                ax.legend()
                ax.set_title("Gráficos da Função e Derivada")
                ax.set_ylim(-20, 20)
                ax.grid(True)
                st.pyplot(fig)

        except (sympy.SympifyError, SyntaxError) as e:
            st.error(f"Erro na expressão: {e}. Verifique a sintaxe.")
        except Exception as e:
            st.error(f"Erro inesperado: {e}. Verifique a entrada.")


if __name__ == "__main__":
    main()
