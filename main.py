nome = input("Bem vindo herói, qual seu nome? ")
print("Que bom ter você conosco, ",nome,". Poderia me informar quantas partidas foram vencidas, por favor?", sep="", end=" ")
vitorias = int(input())
derrotas = int(input("Obrigada, poderia me informar a quantidade de derrotas também, por favor? "))
pontos = vitorias - derrotas
    
if pontos<11:
    nivel = "Ferro"
elif pontos<21:
    nivel = "Bronze"
elif pontos<51:
    nivel = "Prata"
elif pontos<81:
    nivel = "Ouro"
elif pontos<91:
    nivel = "Diamante"
elif pontos<101:
    nivel = "Lendário"
else:
    nivel = "Imortal"
print("Seu saldo de vitórias é de ", pontos, ". Você está no nível ", nivel, ". Parabéns!", sep="")
