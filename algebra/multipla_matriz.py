def ler_matriz_arquivo(filepath):
    """
    Lê matrizes de um arquivo texto onde cada matriz começa com duas linhas:
    número de linhas e número de colunas, seguidas pelos elementos separados por espaço.
    Retorna uma lista com todas as matrizes encontradas no arquivo.
    """
    matrizes = []
    try:
        with open(filepath, "r") as f:
            linhas = [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{filepath}' não encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao ler arquivo: {e}")

    idx = 0
    while idx < len(linhas):
        try:
            n_lin = int(linhas[idx])
            n_col = int(linhas[idx + 1])
            idx += 2
        except (IndexError, ValueError):
            raise ValueError("Formato inválido nas linhas de dimensões da matriz.")

        if idx + n_lin > len(linhas):
            raise ValueError("Arquivo não contém linhas suficientes para a matriz declarada.")

        matriz = []
        for i in range(n_lin):
            elementos_str = linhas[idx + i].split()
            if len(elementos_str) != n_col:
                raise ValueError(f"Quantidade de elementos incorreta na linha {idx + i + 1} da matriz.")
            try:
                elementos = [float(x) for x in elementos_str]
            except ValueError:
                raise ValueError(f"Elemento não numérico encontrado na linha {idx + i + 1} da matriz.")
            matriz.append(elementos)
        idx += n_lin
        matrizes.append(matriz)

    if len(matrizes) < 2:
        raise ValueError("O arquivo deve conter pelo menos duas matrizes para multiplicação.")

    return matrizes

# Exemplo de uso aprimorado

def main():
    try:
        caminho = input("Digite o nome do arquivo com as matrizes: ")
        matrizes = ler_matriz_arquivo(caminho)
        A, B = matrizes[0], matrizes[1]
        exibir_matriz(A, "A (arquivo)")
        exibir_matriz(B, "B (arquivo)")
        C = multiplicar_matrizes(A, B)
        exibir_matriz(C, "Resultado A x B")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
