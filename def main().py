def main():
    with open('livros.txt', 'r', encoding= 'latin-1') as arquivo:
        linhas = arquivo.read().splitlines()

    print(f"Encontrados {len(linhas)} livros")

    avaliacoes = []

    for linha  in linhas: 
        linha = linha.strip()
        if linha:
            print(f"\nlivro: {linha}")

            while True:
                try:
                    nota = float(input("nota (0-10):"))
                    if 0 <= nota <= 10:
                        break
                    else:
                        print("nota deve estar entre 0 a 10!")
                except:
                    print("Digite um número válido!")
    
            while True:
                status = input("Status (lido/lendo/ na fila):").lower()
                if status in ["lido", "lendo", "na fila"]:
                    break
                else:
                    print("Status inválidos!")

            avaliacoes.append(f"{linha}, {nota}, {status}\n")

    with open(' livros_avaliacao.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(avaliacoes)

    print(f"\n Salvo! {len(avaliacoes)} livros avaliados.")
if __name__ == "__main__":
    main()