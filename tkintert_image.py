#importo as bibliotecas
from tkinter import *
from PIL import ImageTk, Image

#abro uma janela
root = Tk()

#abro a imagem e a salvo em uma variável
imagem = Image.open("capivara.png")

#defino a imagem com foto/imagem
imagem_tk = ImageTk.PhotoImage(imagem)

#defino os parâmetros da imagem
imagem_Label = Label(root, image=imagem_tk)

#abro a imagem na janela
imagem_Label.pack()

#rodo a janela
root.mainloop()