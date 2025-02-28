
quantidade = int(input("quantos livros vai comprar"))

livro = 24.95
desconto = 40/100
livro_desconto = livro - (desconto * livro)
preco_total = quantidade * livro_desconto

transporte = (quantidade-1) *0.75 + 3 

total = transporte + preco_total

print(f"o valor total do seus livros é {total}")