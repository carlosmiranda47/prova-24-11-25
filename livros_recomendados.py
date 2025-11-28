def main():
    try:
        with open('livros_avaliacao.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except:
        print("Execute primeiro: python livros_avaliacao.py")
        return
    
    livros = []

    for linha in linhas:
        dados = linha.strip().split(',')
        if len(dados) >= 3 and dados[-1] in ["lido","lendo"]:
            nota = float(dados[-2])
            livros.append((nota, linha.strip()))

    livros.sort(reverse=True)
    top_5 = livros[:5]

    with open('livros_recomendados.txt' 'w', encoding='utf-8') as arquivo:
        for nota, linha_completa in top_5:
            arquivo.write(linha_completa + '\n')
    print(f"{len(top_5)} recomendações salvas!")

if __name__ == "__main__":
    main()