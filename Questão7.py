respostas = 0

if input("Telefonou para a vítima? (s/n): ").lower() == "s":
    respostas += 1

if input("Esteve no local do crime? (s/n): ").lower() == "s":
    respostas += 1

if input("Mora perto da vítima? (s/n): ").lower() == "s":
    respostas += 1

if input("Devia para a vítima? (s/n): ").lower() == "s":
    respostas += 1

if input("Já trabalhou com a vítima? (s/n): ").lower() == "s":
    respostas += 1

if respostas == 2:
    print("Suspeita")
elif respostas in [3, 4]:
    print("Cúmplice")
elif respostas == 5:
    print("Assassino")
else:
    print("Inocente")
