# app/main.py

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from mapa_de_sala.mapa import MapaDeSala  # Importa a classe MapaDeSala

class MapaDeSalaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mapa de Sala Escolar")
        
        # Dados iniciais do mapa
        self.mapa_sala = MapaDeSala("Sala 101")
        
        # Configuração da interface
        self.configurar_interface()

    def configurar_interface(self):
        self.nome_sala_label = tk.Label(self.root, text="Nome da Sala:")
        self.nome_sala_label.grid(row=0, column=0)
        
        self.nome_sala_entry = tk.Entry(self.root, width=20)
        self.nome_sala_entry.insert(0, self.mapa_sala.nome_sala)
        self.nome_sala_entry.grid(row=0, column=1)

        self.renomear_button = tk.Button(self.root, text="Renomear Sala", command=self.renomear_sala)
        self.renomear_button.grid(row=0, column=2)
        
        self.adicionar_fileira_button = tk.Button(self.root, text="Adicionar Fileira", command=self.adicionar_fileira)
        self.adicionar_fileira_button.grid(row=1, column=0, columnspan=2)
        
        self.definir_mesa_prof_button = tk.Button(self.root, text="Definir Mesa do Professor", command=self.definir_mesa_professor)
        self.definir_mesa_prof_button.grid(row=2, column=0, columnspan=2)
        
        self.exportar_button = tk.Button(self.root, text="Exportar Mapa", command=self.exportar_mapa)
        self.exportar_button.grid(row=3, column=0, columnspan=2)
        
        self.exibir_mapa_button = tk.Button(self.root, text="Exibir Mapa", command=self.exibir_mapa)
        self.exibir_mapa_button.grid(row=4, column=0, columnspan=2)

    def renomear_sala(self):
        novo_nome = self.nome_sala_entry.get()
        self.mapa_sala.nomear_sala(novo_nome)
        messagebox.showinfo("Renomear Sala", f"A sala foi renomeada para {novo_nome}.")

    def adicionar_fileira(self):
        num_mesas = simpledialog.askinteger("Adicionar Fileira", "Quantas mesas nesta fileira?")
        if num_mesas:
            self.mapa_sala.adicionar_fileira(num_mesas)
            messagebox.showinfo("Adicionar Fileira", f"Fileira com {num_mesas} mesas adicionada.")

    def definir_mesa_professor(self):
        pos_fileira = simpledialog.askinteger("Definir Mesa do Professor", "Número da fileira:")
        pos_mesa = simpledialog.askinteger("Definir Mesa do Professor", "Número da mesa na fileira:")
        if pos_fileira and pos_mesa:
            self.mapa_sala.definir_mesa_professor(pos_fileira - 1, pos_mesa - 1)
            messagebox.showinfo("Definir Mesa do Professor", f"Mesa do professor definida: Fileira {pos_fileira}, Mesa {pos_mesa}.")

    def exportar_mapa(self):
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if caminho_arquivo:
            self.mapa_sala.exportar_mapa(caminho_arquivo)
            messagebox.showinfo("Exportar Mapa", f"Mapa exportado para {caminho_arquivo}")

    def exibir_mapa(self):
        self.mapa_sala.exibir_mapa()

# Inicializar a aplicação Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = MapaDeSalaApp(root)
    root.mainloop()
