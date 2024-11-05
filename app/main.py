# app/main.py

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
from mapa.mapa_de_sala import MapaDeSala  # Importa a classe MapaDeSala

class MapaDeSalaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mapa de Sala Escolar")
        
        # Configuração de tela cheia
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.fechar_fullscreen)
        
        # Mapa de sala
        self.mapa_sala = MapaDeSala("Sala 101")
        
        # Configuração da interface
        self.configurar_interface()

    def configurar_interface(self):
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o frame

        # Área de desenho para o mapa
        self.canvas = tk.Canvas(self.frame, width=800, height=600, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=4)

        # Entrada para nomear a sala
        self.nome_sala_label = tk.Label(self.frame, text="Nome da Sala:")
        self.nome_sala_label.grid(row=1, column=0)
        
        self.nome_sala_entry = tk.Entry(self.frame, width=20)
        self.nome_sala_entry.insert(0, self.mapa_sala.nome_sala)
        self.nome_sala_entry.grid(row=1, column=1)

        self.renomear_button = tk.Button(self.frame, text="Renomear Sala", command=self.renomear_sala)
        self.renomear_button.grid(row=1, column=2)

        # Botões para adicionar e remover fileiras
        self.adicionar_fileira_button = tk.Button(self.frame, text="Adicionar Fileira", command=self.adicionar_fileira)
        self.adicionar_fileira_button.grid(row=2, column=0)

        self.remover_fileira_button = tk.Button(self.frame, text="Remover Fileira", command=self.remover_fileira)
        self.remover_fileira_button.grid(row=2, column=1)

        # Botão para renomear mesa
        self.renomear_mesa_button = tk.Button(self.frame, text="Renomear Mesa", command=self.renomear_mesa)
        self.renomear_mesa_button.grid(row=2, column=2)

        # Botões para importar e exportar mapa
        self.importar_button = tk.Button(self.frame, text="Importar Mapa", command=self.importar_mapa)
        self.importar_button.grid(row=3, column=0)

        self.exportar_button = tk.Button(self.frame, text="Exportar Mapa", command=self.exportar_mapa)
        self.exportar_button.grid(row=3, column=1)

        self.exibir_mapa_button = tk.Button(self.frame, text="Exibir Mapa", command=self.exibir_mapa)
        self.exibir_mapa_button.grid(row=3, column=2)
        
        # Desenha a primeira fileira inicial
        self.mapa_sala.adicionar_fileira(3)  # Exemplo com 3 mesas
        self.desenhar_mapa()

    def fechar_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)

    def renomear_sala(self):
        novo_nome = self.nome_sala_entry.get()
        self.mapa_sala.nomear_sala(novo_nome)
        messagebox.showinfo("Renomear Sala", f"A sala foi renomeada para {novo_nome}.")

    def adicionar_fileira(self):
        if len(self.mapa_sala.mapa) < 10:
            num_mesas = simpledialog.askinteger("Adicionar Fileira", "Quantas mesas nesta fileira?")
            if num_mesas:
                self.mapa_sala.adicionar_fileira(num_mesas)
                messagebox.showinfo("Adicionar Fileira", f"Fileira com {num_mesas} mesas adicionada.")
                self.desenhar_mapa()
        else:
            messagebox.showwarning("Limite de Fileiras", "O máximo de 10 fileiras já foi atingido.")

    def remover_fileira(self):
        if self.mapa_sala.mapa:
            self.mapa_sala.mapa.pop()
            messagebox.showinfo("Remover Fileira", "A última fileira foi removida.")
            self.desenhar_mapa()
        else:
            messagebox.showwarning("Remover Fileira", "Não há fileiras para remover.")

    def renomear_mesa(self):
        fileira = simpledialog.askinteger("Renomear Mesa", "Informe o número da fileira:")
        mesa = simpledialog.askinteger("Renomear Mesa", "Informe o número da mesa na fileira:")
        
        if fileira and mesa:
            try:
                # Solicita o novo nome da mesa
                novo_nome = simpledialog.askstring("Renomear Mesa", "Digite o nome para a mesa:")
                if novo_nome:
                    # Atualiza o nome da mesa especificada
                    self.mapa_sala.mapa[fileira - 1][mesa - 1] = novo_nome
                    messagebox.showinfo("Renomear Mesa", f"A mesa foi renomeada para {novo_nome}.")
                    self.desenhar_mapa()
            except IndexError:
                messagebox.showerror("Erro", "Posição de mesa inválida.")

    def importar_mapa(self):
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if caminho_arquivo:
            with open(caminho_arquivo, 'r') as f:
                mapa_dict = json.load(f)
                self.mapa_sala.nomear_sala(mapa_dict["nome_sala"])
                self.mapa_sala.mapa = mapa_dict["mapa"]
                self.desenhar_mapa()

    def exportar_mapa(self):
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if caminho_arquivo:
            self.mapa_sala.exportar_mapa(caminho_arquivo)

    def exibir_mapa(self):
        self.mapa_sala.exibir_mapa()

    def desenhar_mapa(self):
        self.canvas.delete("all")
        for i, fileira in enumerate(self.mapa_sala.mapa):
            y = 50 + i * 50
            num_mesas = len(fileira)
            largura_canvas = 800
            espaco_total = num_mesas * 70
            margem = (largura_canvas - espaco_total) // 2
            
            for j, mesa in enumerate(fileira):
                x = margem + j * 70
                self.canvas.create_rectangle(x, y, x + 60, y + 40, fill="lightblue", outline="black")
                self.canvas.create_text(x + 30, y + 20, text=mesa)
        
        if self.mapa_sala.mapa:
            mesa_prof_x = (800 - 60) // 2
            mesa_prof_y = 50 + len(self.mapa_sala.mapa) * 50
            self.canvas.create_rectangle(mesa_prof_x, mesa_prof_y, mesa_prof_x + 60, mesa_prof_y + 40, fill="yellow", outline="black")
            self.canvas.create_text(mesa_prof_x + 30, mesa_prof_y + 20, text="Professor", fill="black")

# Inicializar a aplicação Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = MapaDeSalaApp(root)
    root.mainloop()
