from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import pygame 
from pygame import mixer

import os


##cores
background = '#1a1b1c'
cor1 = '#333e50'
cor2 = '#5c6e6e'
cor3 = '#f1debd'
cor5 = '#320139'


white = "#ffffff"



janela = Tk()
janela.title("Player Music Gabriel")
janela.geometry('800x620')
janela.resizable(False, False)
janela.config(bg=background)


frame_esquerda = Frame(janela, width=400, height=492, bg=cor3)
frame_esquerda.place(x=6, y=6)

frame_direita = Frame(janela, width=370, height=492, bg=cor1)
frame_direita.place(x=421, y=6)

frame_inferior = Frame(janela, width=784, height=96, bg=cor1)
frame_inferior.place(x=7, y=510)



imgMan = Image.open('manrock.jpg')
imgMan = imgMan.resize((480, 480))
imgMan = ImageTk.PhotoImage(imgMan)


label_man = Label(frame_esquerda, height=480, image=imgMan, compound=LEFT,  anchor='n', bg=cor1)
label_man.place(x=0, y=0)



##funções

def play_musica():
    rodando = lista_musicas.get(ACTIVE)
    musica_atual['text'] = rodando

    mixer.music.load(rodando)
    mixer.music.play()



lista_musicas = Listbox(frame_direita, width= 36, height=25,  selectmode=SINGLE, font=('ivy 11 bold'), fg=cor3, bg=cor1)
lista_musicas.grid(row=0, column=0)



sc_bar = Scrollbar(frame_direita, )
sc_bar.grid(row=0, column=1, sticky=NSEW)


lista_musicas.config(yscrollcommand=sc_bar.set)
sc_bar.config(command=lista_musicas.yview)


musica_atual = Label(frame_inferior, text='escolha uma musica na lista ', width=984, justify=LEFT ,  anchor='nw',font=('ivy 10 bold'), bg=cor2, fg=white)
musica_atual.place(x=0, y=1)


btn_anterior = Button(frame_inferior, text='', width=11, height=2, justify=LEFT , relief=RAISED, overrelief=RIDGE,  anchor='nw',font=('ivy 10 bold'), bg=cor2, fg=white)
btn_anterior.place(x=22, y=32)



btn_play = Button(frame_inferior,command=play_musica, text='  ', width=11, height=2, justify=CENTER , relief=RAISED, overrelief=RIDGE,  anchor='nw',font=('ivy 10 bold'), bg=cor2, fg=white)
btn_play.place(x=162, y=32)



btn_step = Button(frame_inferior, text='  ', width=11, height=2, justify=LEFT , relief=RAISED, overrelief=RIDGE,  anchor='nw',font=('ivy 10 bold'), bg=cor2, fg=white)
btn_step.place(x=302, y=32)


btn_pause = Button(frame_inferior, text='   ', width=6, height=2, justify=LEFT , relief=RAISED, overrelief=RIDGE,  anchor='nw',font=('ivy 10 bold'), bg=cor2, fg=white)
btn_pause.place(x=438, y=32)


btn_stop = Button(frame_inferior, text='   ', width=6, height=2, justify=LEFT , relief=RAISED, overrelief=RIDGE,  anchor='nw',font=('ivy 10 bold'), bg=cor2, fg=white)
btn_stop.place(x=534, y=32)


os.chdir(r'/home/gabriel/Músicas') ## <-- coloque o caminho onde suas musicas estão --fis no linux não sei se vai funcionar no windows kk
musicas = os.listdir()



def mostrar_msc():
    for i in musicas:
        lista_musicas.insert(END, i)

mostrar_msc()


mixer.init()

janela.mainloop()