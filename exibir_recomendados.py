def main():

    import os
    if not os.path.exists('livros_recomendados.txt'):
        print("Execute primeiro: python livros_recomendados.py")
        return

    with open('livros_recomendados.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    livros = []

    for linha in linhas:
        dados = linha.strip.split(',')
        if len(dados) >= 3:

            nota = float(dados[-2])

            info_livro =','.join(dados[:-2])
            status = dados[-1]

            livros.append((nota, info_livro, status))

    livros.sort(reverse=True)

    print("\n" + "="*60)
    print("LIVROS RECOMENDADOS (melhores avaliados)")
    print("="*60)

    for i, (nota, info_livro, status) in enumerate(livros, 1):
        print(f"\n{i}° - Nota: {nota:.1f}/10 | status: {status}")
        print(f"{info_livro}")

if __name__ == "__main__":
    main()