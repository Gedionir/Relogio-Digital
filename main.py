from tkinter import *
import tkinter
from datetime import datetime
import locale
import pyglet


pyglet.font.add_file("font/digital-7.ttf")


############ CORES #############
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul
cor7 = "#FF6347"  # tomato

fundo = cor1
cor = cor6

janela = Tk()
janela.title("Relogio Digital")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)   # Não pode alterar o tamanho da janela.
janela.configure(bg=cor1)


def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    # dia_semana = locale.setlocale(locale.LC_TIME, 'pt_BR')
    dia = tempo.day   # dia da semana
    mes = tempo.strftime("%B")  # %b -> mes abreviado       %B -> mes por extenso
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)  # A cada 200 milisegundos ira executar  função relogio.
    l2.config(text=dia_semana + "   " + str(dia) + "   " + str(mes) + "  " + str(ano))


l1 = Label(janela, text="", font="digital-7 100", bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font="digital-7 32", bg=fundo, fg=cor7)
l2.grid(row=1, column=0, sticky=NW, padx=5)
l2.place(x=5, y=130)

relogio()
janela.mainloop()
