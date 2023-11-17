#importo as bibliotecas
from tkinter import *
from PIL import ImageTk, Image
import os

#abro uma janela
root = Tk()

#pega um arquivo e faz uma lista com o que tem tudo no arquivo
arquivos = os.listdir("imagens")

#armazena as imagens
imagens = []

#percorre cada arquivo dentro de arquivos
for arquivo in arquivos:
    #abre imagem
    img = Image.open("imagens/" + arquivo)
    #adiciona a imagem na lista
    imagens.append(ImageTk.PhotoImage(img))

#exibe arquivos em um label
#arquivos_label = Label(root, text=arquivos)
#arquivos_label.pack()

#defino os parâmetros da imagem
imagem_Label = Label(root, image=imagens[0])

#abro a imagem na janela
imagem_Label.pack()

#rodo a janela
root.mainloop()