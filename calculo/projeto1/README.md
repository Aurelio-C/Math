# Projeto: Calculadora de Derivada Numérica em Streamlit

Este projeto é uma aplicação web simples desenvolvida com Streamlit que permite calcular a derivada numérica de uma função matemática fornecida pelo usuário em um ponto específico, utilizando o método da diferença central. Além disso, oferece a opção de mostrar o gráfico da função original junto com sua derivada, facilitando a visualização do comportamento local da função.

## Importação das bibliotecas

O projeto utiliza três bibliotecas principais:

- **Streamlit** para criar a interface web interativa, permitindo receber entradas do usuário e mostrar resultados dinâmicos.
- **NumPy** para trabalhar com funções matemáticas e manipular arrays numéricos.
- **Matplotlib** para criar os gráficos que serão exibidos na aplicação, mostrando a função e sua derivada.

## Configuração da página no Streamlit

A aplicação configura a página do Streamlit definindo o título que aparece na aba do navegador e centraliza o layout da aplicação na tela para uma melhor apresentação visual ao usuário.

## Título e descrição da aplicação

A tela inicial apresenta um título claro com um ícone, indicando que se trata de uma Calculadora de Derivada Numérica. Também é exibida uma breve descrição orientando o usuário sobre o que pode fazer na aplicação.

## Definição do cálculo da derivada numérica

A derivada numérica é calculada usando o método da diferença central, que aproxima a derivada em um ponto \(x\) utilizando a fórmula:

$$
f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}
$$


Aqui, \(h\) é um pequeno valor positivo que determina a proximidade para calcular a diferença. Esse método calcula a variação média no entorno de \(x\), oferecendo uma aproximação precisa da derivada.

## Entrada de dados pelo usuário

O usuário interage com a aplicação por meio de um formulário onde:

- Digita a função matemática \(f(x)\) em notação Python utilizando as funções do NumPy, como seno, exponencial, potências etc.
- Escolhe o ponto específico \(x\) no qual deseja calcular a derivada.
- Opta por visualizar ou não o gráfico da função e sua derivada no entorno do ponto escolhido.
- Envia o formulário para o cálculo.

## Processamento do cálculo

Quando o formulário é enviado:

- A string da função matemática digitada pelo usuário é convertida em uma função Python para avaliação.
- A função é testada no ponto informado para verificar se está válida.
- A derivada é calculada no ponto usando o método da diferença central.
- O resultado da derivada é exibido com até seis casas decimais para clareza.

## Visualização gráfica (opcional)

Se o usuário pedir, a aplicação gera e exibe um gráfico que mostra:

- A função original \(f(x)\) no intervalo ao redor do ponto escolhido.
- A curva da derivada \(f'(x)\) calculada nesse intervalo.
- Uma linha vertical destacando o ponto onde a derivada foi calculada.

Isso ajuda a entender visualmente como a função está se comportando localmente e como sua taxa de variação (derivada) muda.

## Tratamento de erros

Se o usuário inserir uma função inválida ou ocorrer algum erro durante a execução da avaliação ou cálculo, a aplicação mostra mensagens de erro claras, indicando que o formato da função deve seguir exemplos válidos em notação NumPy.

## Considerações finais

Este projeto apresenta uma interface simples, prática e funcional para o cálculo de derivadas numéricas online em tempo real. A utilização do `eval` com restrições permite flexibilidade para o usuário inserir diversas funções matemáticas. A possibilidade de visualizar o gráfico ajuda muito na compreensão do conceito de derivada e do comportamento local da função.
