# Gerador de QR Code em Python

Projeto simples criado para gerar um QR Code a partir de um texto ou link.

## Instalação
# Para ultilziar a biblioteca, instale no terminal ultizando esse comando?
pip install "qrcode[pil]"

# O que cada linha faz:

import qrcode - > Importa a biblioteca usada para gerar o QR Code.

input() - > Recebe o texto ou link digitado pelo usuário.

qrcode.make() - > Cria o QR Code a partir do conteúdo informado.

.save() - > Salva o QR Code como uma imagem PNG.

print() - > Mostra uma mensagem no terminal confirmando que terminou.
