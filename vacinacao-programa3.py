print("Digite sua idade e aperte 'Enter': ")
idade = int(input())
if idade < 75:
    print("\nAguarde as novas fases da Campanha de Vacinação.")
if 75 <= idade <= 95:
    print("Agora escreva seu nome e aperte 'Enter': ")
    nome = input()
    print("\nBem-vindo(a),", nome, "! Você tem ", idade, "anos, certo?")
    print("=== Escolha um Local de Vacinação ===")
    print("1 - Digite '1', depois 'Enter', para vacinação em casa;")
    print("2 - Digite '2', depois 'Enter', para vacinação no shopping.")
    local_vacinacao = int(input())
    if local_vacinacao == 1:
        print("\nLocal de Vacinação: \nEm casa.")
    else:
        print("\nLocal de Vacinação: \nNo shopping.")
if 95 < idade <= 120:
    print("\nLocal de Vacinação: \nEm casa.")
if idade > 120:
    print("\nParabéns pela idade, você é incrível!")
    print("\nLocal de Vacinação: \nEm casa.")
print("\nAgradecemos sua participação!")
