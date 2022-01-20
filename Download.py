import requests
import json
import os

# Criar diretório para as imagens
os.mkdir(os.getcwd() + '/downloaded-images')

# Array com as imagens à serem baixadas
images = open("images.json")
imagesJson = json.load(images)

# Função para baixar imagem
def baixar_imagem(endereco, url):
   resposta = requests.get(url)
   novo_endereco = "downloaded-images/" + endereco.replace(" ", "-")

   if(resposta.status_code == requests.codes.OK):
      with open(novo_endereco, 'wb') as nova_imagem:
         nova_imagem.write(resposta.content)
      print("Download finalizado, {}".format(endereco.replace(" ", "-")))
   else:
      resposta.raise_for_status()
      print("Ocorreu um erro no download da imagem: {}".format(endereco))

# Iterar na array de imagens para fazer download
for idx, image in enumerate(imagesJson):
   baixar_imagem(image["name"] + ".jpg", image["image"])