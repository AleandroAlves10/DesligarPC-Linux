from tkinter import *
import os



def desligar():
    return os.system('shutdown')
def reiniciar():
    return os.system('shutdown -f')
def sair():
    return os.system('shutdown -f')
def sleep():
    return os.system('shutdown 90')
def cancelar():
    return os.system('shutdown –c')

master = Tk()
master.geometry('320x200')

master.configure(bg='light grey')

Button(master, text=' Desligar  ', command=desligar).place(x=22, y=20)
Button(master, text=' Reiniciar ', command=reiniciar).place(x=22, y=50)
Button(master, text='   Sair    ', command=sair).place(x=22, y=80)
Button(master, text='Sleep 90min', command=sleep).place(x=22, y=110)
Button(master, text='  Cancelar ', command=sleep).place(x=22, y=140)


mainloop()



#  -h Finalizar e desligar o sistema
#  -r Reiniciar o sistema
#  -f Inicialização rápida – não faz verificação do sistema de arquivos (fsck) no próximo boot
#  -k Enviar mensagens de aviso, mas sem finalizar o sistema
#  -F Forçar a verificação do sistema de arquivos na próxima inicialização
#  -c Cancelar a finalização ou reinicialização do sistema
#  -P Desliga o computador
#  -h 20:50  desligar no horario especifico