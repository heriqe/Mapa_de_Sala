from PIL import Image, ImageDraw, ImageFont
from mapa.mapa_de_sala import MapaDeSala

class ImprimirMapa:
    def __init__(self, mapa_sala):
        self.mapa_sala = mapa_sala

    def gerar_imagem_mapa(self, caminho_arquivo):
        # Configurações de imagem
        largura_canvas = 800
        altura_canvas = 100 + len(self.mapa_sala.mapa) * 60
        imagem = Image.new("RGB", (largura_canvas, altura_canvas), "white")
        draw = ImageDraw.Draw(imagem)
        
        # Carrega a fonte (use o caminho correto para sua fonte)
        try:
            fonte = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            fonte = ImageFont.load_default()
        
        # Desenha o nome da sala no topo
        draw.text((largura_canvas // 2 - 50, 20), self.mapa_sala.nome_sala, fill="black", font=fonte)

        # Desenha cada fileira de mesas
        for i, fileira in enumerate(self.mapa_sala.mapa):
            y = 60 + i * 60
            num_mesas = len(fileira)
            espaco_total = num_mesas * 80
            margem = (largura_canvas - espaco_total) // 2
            
            for j, mesa in enumerate(fileira):
                x = margem + j * 80
                draw.rectangle([x, y, x + 60, y + 40], fill="lightblue", outline="black")
                draw.text((x + 10, y + 10), mesa, fill="black", font=fonte)

        # Desenha a mesa do professor
        mesa_prof_x = (largura_canvas - 60) // 2
        mesa_prof_y = 60 + len(self.mapa_sala.mapa) * 60
        draw.rectangle([mesa_prof_x, mesa_prof_y, mesa_prof_x + 60, mesa_prof_y + 40], fill="yellow", outline="black")
        draw.text((mesa_prof_x + 5, mesa_prof_y + 10), "Professor", fill="black", font=fonte)
        
        # Salva a imagem
        imagem.save(caminho_arquivo)
        print(f"Imagem do mapa de sala salva em {caminho_arquivo}")

# Exemplo de uso
if __name__ == "__main__":
    # Inicializa o mapa de sala e adiciona fileiras e mesas
    sala = MapaDeSala("Laboratório de Informática")
    sala.adicionar_fileira(4)
    sala.adicionar_fileira(3)
    sala.adicionar_fileira(5)
    
    # Instancia a classe de impressão e gera a imagem
    impressao = ImprimirMapa(sala)
    impressao.gerar_imagem_mapa("mapa_sala_impressao.png")
