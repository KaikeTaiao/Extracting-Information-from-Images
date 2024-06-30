# links uteis:
# corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# pegar linguas: print(pytesseract.get_languages())


import pytesseract
import cv2

# passo 1: ler a imagem
imagem = cv2.imread("imagens\email.JPG")
caminho = r"C:\Program Files\Tesseract-OCR"

# passo 2: pedir para o tesseract extrair o texto da image
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem)

print(texto)