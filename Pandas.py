import pandas as pd , os 
import openpyxl 
caminho_csv= r"C:\Users\Aluno\Desktop\projeto formulario\analise de imoveis\CSV - Houses.csv"
caminho_exel= r"C:\Users\Aluno\Desktop\projeto formulario\analise de imoveis\CSV - new-houses.xlsx"
conteudo_arquivo = ""
def lerCSV():
    global conteudo_arquivo
    conteudo_arquivo = pd.read_csv(caminho_csv)
    print(conteudo_arquivo)


def converterCSVemExcel():
    conteudo_arquivo.to_excel(caminho_exel, index=False)
    print(f"Arquivo exel criado: {caminho_exel}")
 
def abrirExcel():
    os.startfile(caminho_exel)

def selececinar_Bairro():
    global conteudo_arquivo
    bairros = ["Mooca", "Tatuapé", "Bela Vista"]
    conteudo_arquivo =  conteudo_arquivo[conteudo_arquivo["district"].isin(bairros)]
    print(conteudo_arquivo)

def selecionarTamanho():
    global conteudo_arquivo
    conteudo_arquivo = conteudo_arquivo[conteudo_arquivo["area"] > 50 ]
    print(conteudo_arquivo)

def excluir_casa():
    global conteudo_arquivo
    conteudo_arquivo = conteudo_arquivo[conteudo_arquivo["type"] != 'Casa']   
    print(conteudo_arquivo) 

lerCSV()
selececinar_Bairro()
selecionarTamanho()
converterCSVemExcel()
abrirExcel()
