nome = input("Digite seu nome:")
idade= int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))

resultado = (idade > 18) and (altura > 1.75)

msg = f"Pode participar do evento: {resultado}"

print(msg)