import os
import pyautogui as pg
import time
nomedapasta=r"C:\Users\Aluno\Desktop\projeto formulario\imagens"



def google_open ():
    os.system("start chrome")
    time.sleep(3)


def  forms_open():
    pg.typewrite ("https://forms.gle/SBiMqdeLnc4bCQPr8")
    time.sleep(3)
    pg.press("enter")

def preencher():
    pg.sleep(3)
    pg.press("tab")
    pg.press("tab")
    pg.write("Kelvin")
    pg.press("tab")
    pg.write("Programacao em Python")
    pg.press("enter")
    pg.press("tab")
    pg.press("enter")
    time.sleep(3)
    pg.press("Tab",presses=5)
    pg.press("enter")
    time.sleep(3)

def abrir_imagem(arquivos):
    total_imagens = ( len(arquivos)) 
#com ajuda dos universitarios vencemos uma batalha
    for i in range(total_imagens):
        arquivo = arquivos[i]    
        time.sleep(3)
        pg.typewrite(f'{nomedapasta}\{arquivos[i]}')
        time.sleep(1)
        pg.press("Enter")
        time.sleep(10)  # Reduzido para 2 segundo para maior eficiência
        pg.press('tab',presses=2)
        pg.press("enter")
        time.sleep(10)  #Evitando o que dê ruim 
        pg.press("tab")
        pg.press("enter")
        preencher() 

   

def lerArquivos():
    global arquivos
    arquivos= os.listdir(nomedapasta) #Apanhando feio do código

google_open()
forms_open()
lerArquivos()
preencher()
abrir_imagem(arquivos)