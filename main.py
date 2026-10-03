import qrcode

texto = input("Digite o link: ")

imagem = qrcode.make(texto)

imagem.save("qrcode.png")

print("QR Code gerado com sucesso!")
