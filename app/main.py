import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from mapa.mapa_de_sala import MapaDeSala  # Importa a classe MapaDeSala

class MapaDeSalaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mapa de Sala Escolar")
        
        # Dados iniciais do mapa
        self.mapa_sala = MapaDeSala("Sala 101")
        
        # Configuração da interface
        self.configurar_interface()

    def configurar_interface(self):
        # Área de desenho para o mapa
        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)

        # Label e botão para renomear a sala
        self.nome_sala_label = tk.Label(self.root, text="Nome da Sala:")
        self.nome_sala_label.grid(row=1, column=0)
        
        self.nome_sala_entry = tk.Entry(self.root, width=20)
        self.nome_sala_entry.insert(0, self.mapa_sala.nome_sala)
        self.nome_sala_entry.grid(row=1, column=1)

        self.renomear_button = tk.Button(self.root, text="Renomear Sala", command=self.renomear_sala)
        self.renomear_button.grid(row=1, column=2)

        self.adicionar_fileira_button = tk.Button(self.root, text="Adicionar Fileira", command=self.adicionar_fileira)
        self.adicionar_fileira_button.grid(row=2, column=0, columnspan=3)
        
        self.exportar_button = tk.Button(self.root, text="Exportar Mapa", command=self.exportar_mapa)
        self.exportar_button.grid(row=3, column=0, columnspan=3)
        
        self.exibir_mapa_button = tk.Button(self.root, text="Exibir Mapa", command=self.exibir_mapa)
        self.exibir_mapa_button.grid(row=4, column=0, columnspan=3)

    def renomear_sala(self):
        novo_nome = self.nome_sala_entry.get()
        self.mapa_sala.nomear_sala(novo_nome)
        messagebox.showinfo("Renomear Sala", f"A sala foi renomeada para {novo_nome}.")

    def adicionar_fileira(self):
        num_mesas = simpledialog.askinteger("Adicionar Fileira", "Quantas mesas nesta fileira?")
        if num_mesas:
            self.mapa_sala.adicionar_fileira(num_mesas)
            messagebox.showinfo("Adicionar Fileira", f"Fileira com {num_mesas} mesas adicionada.")
            self.desenhar_mapa()  # Desenha o mapa atualizado

    def exportar_mapa(self):
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if caminho_arquivo:
            self.mapa_sala.exportar_mapa(caminho_arquivo)
            messagebox.showinfo("Exportar Mapa", f"Mapa exportado para {caminho_arquivo}")

    def exibir_mapa(self):
        self.mapa_sala.exibir_mapa()

    def desenhar_mapa(self):
        self.canvas.delete("all")  # Limpa o canvas

        # Desenha as fileiras
        for i, fileira in enumerate(self.mapa_sala.mapa):
            y = 50 + i * 50  # Distância entre fileiras
            for j, mesa in enumerate(fileira):
                x = 50 + j * 70  # Distância entre mesas
                self.canvas.create_rectangle(x, y, x + 60, y + 40, fill="lightblue", outline="black")
                self.canvas.create_text(x + 30, y + 20, text=mesa)  # Adiciona o número da mesa

        # Se houver fileiras, define a mesa do professor no centro
        if self.mapa_sala.mapa:
            num_fileiras = len(self.mapa_sala.mapa)
            num_mesas = len(self.mapa_sala.mapa[num_fileiras // 2]) if num_fileiras > 0 else 0
            pos_fileira_prof = num_fileiras // 2  # Fileira central
            pos_mesa_prof = num_mesas // 2 if num_mesas > 0 else 0  # Mesa central

            x = 50 + pos_mesa_prof * 70  # Posição da mesa do professor
            y = 50 + pos_fileira_prof * 50  # Posição da fileira do professor

            # Destaque para a mesa do professor
            self.canvas.create_rectangle(x, y, x + 60, y + 40, fill="yellow", outline="black")
            self.canvas.create_text(x + 30, y + 20, text="Professor", fill="black")

# Inicializar a aplicação Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = MapaDeSalaApp(root)
    root.mainloop()
