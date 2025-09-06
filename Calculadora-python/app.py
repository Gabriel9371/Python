from tkinter import*
from tkinter import ttk


janela = Tk()


#cores 
cor1 = '#363533' #preto
cor2 = "#ece7df" #branco 
cor3 = '#bdb8af' #brancoEscuro
cor4 = '#919599' #corBotão numeros
cor5 = "#d1b732" #cor operaçoes





janela.title("Calculadora Teste")
janela.geometry("400x346")
janela.config(bg=cor1)



all_valores = ''
valor_texto = StringVar()

#funçoes

def entrada_de_valores(x):
    global all_valores
    all_valores += str(x)
    
    valor_texto.set(all_valores)  



def calcular():
    global all_valores
    resultado = eval(all_valores)
    valor_texto.set(str(resultado))



def clear_tela():
    global all_valores
    all_valores = ""
    valor_texto.set("")



#criando frames




frame_visor = Frame(janela, width=435, height=94, bg=cor2)
frame_visor.grid(row=0, column=0)

frame_corpo = Frame(janela, width=435, height=633)
frame_corpo.grid(row=1, column=0)



##criando label

app_label = Label(frame_visor, textvariable=valor_texto, width=28, height=4, padx=5, relief=FLAT, anchor='e', justify=RIGHT, font=('ivy 16'), bg=cor1, fg=cor2)
app_label.place(x=0, y=0)



#botões
##fonte que talvez use mais tarde '  "JetBrainsMono Nerd Font"  '

bt1 = Button(frame_corpo, command=clear_tela,text='C', width=19, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
bt1.place(x=0, y=0)



bt2 = Button(frame_corpo, command=lambda: entrada_de_valores('%'), text='%', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
bt2.place(x=201, y=0)


bt3 = Button(frame_corpo, command=lambda: entrada_de_valores(' / '), text='/', width=8, height=2, bg=cor5, fg=cor2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
bt3.place(x=301, y=0)


n7 = Button(frame_corpo, command=lambda: entrada_de_valores('7'), text='7', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n7.place(x=1, y=49)

n8 = Button(frame_corpo,command=lambda: entrada_de_valores('8'),  text='8', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n8.place(x=101, y=49)

n9 = Button(frame_corpo,command=lambda: entrada_de_valores('9'),  text='9', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n9.place(x=201, y=49)

bt4 = Button(frame_corpo, command=lambda: entrada_de_valores(' * '), text='*', width=8, height=2, bg=cor5, fg=cor2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=301, y=49)


n4 = Button(frame_corpo,command=lambda: entrada_de_valores('4'),  text='4', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n4.place(x=1, y=98)

n5 = Button(frame_corpo, command=lambda: entrada_de_valores('5'), text='5', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n5.place(x=101, y=98)

n6 = Button(frame_corpo, command=lambda: entrada_de_valores('6'), text='6', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n6.place(x=201, y=98)

bt5 = Button(frame_corpo, command=lambda: entrada_de_valores(' - '), text='-', width=8, height=2, bg=cor5, fg=cor2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=301, y=98)


n1 = Button(frame_corpo, command=lambda: entrada_de_valores('1'), text='1', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n1.place(x=1, y=147)

n2 = Button(frame_corpo, command=lambda: entrada_de_valores('2'), text='2', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n2.place(x=101, y=147)

n3 = Button(frame_corpo,command=lambda: entrada_de_valores('3'),  text='3', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
n3.place(x=201, y=147)

bt5 = Button(frame_corpo,command=lambda: entrada_de_valores(' + '),  text='+', width=8, height=2, bg=cor5, fg=cor2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=301, y=147)

bt0 = Button(frame_corpo,command=lambda: entrada_de_valores('0'),  text='0', width=19, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
bt0.place(x=1, y=196)


btdot = Button(frame_corpo,command=lambda: entrada_de_valores('.'),  text='.', width=8, height=2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
btdot.place(x=201, y=196)


bt_equals = Button(frame_corpo, command=calcular,  text='=', width=8, height=2, bg=cor5, fg=cor2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
bt_equals.place(x=301, y=196)




janela.mainloop()