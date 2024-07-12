# Ler o arquivo CSV usando Pandas.
# Processar os dados usando NumPy.
# Gerar gráficos usando Matplotlib.
# Exibir a interface gráfica com Tkinter.
# Crie 5 botões 
# Em cada botão precisa mostrar um tipo de grafico
# Mostre a estatistica também

# total de vendas por vendedor


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def apagar(): 
    btn.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy() 

def pizza():
    dados = pd.read_csv('dados.csv')
    vendas = dados['vendas'].to_list()
    vendedor = dados['vendedor'].to_list()
    vendas = np.array(vendas)
    vendedor = np.array(vendedor)
    fig, grafico = plt.subplots()
    grafico.pie(vendas, labels=vendedor,  wedgeprops={"linewidth": 1, "edgecolor": "white"}, autopct='%1.1f%%')
    grafico.legend(vendedor,title='Vendedor',bbox_to_anchor=(1,0,0.5,1))
    grafico.set_title('Total de Vendas por Vendedor')
    # plt.show()  
    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

    # fora do tkinter
    # canvas = FigureCanvasAgg(fig, master = janela)
    # canvas.draw()
    # canvas.get_width_height().pack().side(side = tk.RIGHT, fill=tk.BOTH, expand= True)

def barras():
    dados = pd.read_csv('dados.csv')
    vendas = dados['vendas'].to_list()
    vendedor = dados['vendedor'].to_list()
    vendas = np.array(vendas)
    vendedor = np.array(vendedor)
    fig, grafico = plt.subplots()
    grafico.bar(vendedor, vendas, color='green')
    grafico.set_title('Total de Vendas por Vendedor')
    grafico.set_xlabel('Vendedores')
    grafico.set_ylabel('Total de Vendas')
    grafico.grid(True)
    # plt.show()
    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

def linhas():
    dados = pd.read_csv('dados.csv')
    vendas = dados['vendas'].to_list()
    vendedor = dados['vendedor'].to_list()
    vendas = np.array(vendas)
    vendedor = np.array(vendedor)
    fig, grafico = plt.subplots()
    grafico.plot(vendedor, vendas, marker='o', color='red')
    grafico.set_title('Total de Vendas por Vendedor')
    grafico.set_xlabel('Vendedores')
    grafico.set_ylabel('Total de Vendas')
    grafico.grid(True)
    # plt.show()
    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

def desvio():
    dados = pd.read_csv('dados.csv')
    vendas = dados['vendas'].to_list()
    vendedor = dados['vendedor'].to_list()
    vendas = np.array(vendas)
    vendedor = np.array(vendedor)
    fig, grafico = plt.subplots()
    grafico.scatter(vendedor, vendas, c='black')
    grafico.set_title('Total de Vendas por Vendedor')
    grafico.set_xlabel('Vendedores')
    grafico.set_ylabel('Total de Vendas')
    grafico.grid(True)
    # plt.show()
    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

def haste():
    dados = pd.read_csv('dados.csv')
    vendas = dados['vendas'].to_list()
    vendedor = dados['vendedor'].to_list()
    vendas = np.array(vendas)
    vendedor = np.array(vendedor)
    fig, grafico = plt.subplots()
    grafico.stem(vendedor, vendas)
    grafico.set_title('Total de Vendas por Vendedor')
    grafico.set_xlabel('Vendedores')
    grafico.set_ylabel('Total de Vendas')
    grafico.grid(True)
    # plt.show()
    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)



janela =  tk.Tk()

btn = tk.Button(janela, text='Gráfico de Pizza',command=pizza)
btn.pack(pady=5)

btn2 = tk.Button(janela, text='Gráfico de Barras', command=barras)
btn2.pack(pady=5)

btn3 = tk.Button(janela, text='Gráfico de Linhas', command=linhas)
btn3.pack(pady=5)

btn4 = tk.Button(janela, text='Gráfico de Dispersão', command=desvio)
btn4.pack(pady=5)

btn5 = tk.Button(janela, text='Gráfico de Haste', command=haste)
btn5.pack(pady=5)

b = tk.Button(janela, text='KKKKK', fg='red', command=apagar) 
b.pack() 

janela.mainloop()