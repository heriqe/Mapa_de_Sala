import json
import os
class MapaDeSala:
    def __init__(self, nome_sala):
        self.nome_sala = nome_sala
        self.mapa = []
        self.mesa_professor = None

    def adicionar_fileira(self, num_mesas):
        # Adiciona uma nova fileira com a quantidade de mesas especificada
        fileira = [f"Mesa {i+1}" for i in range(num_mesas)]
        self.mapa.append(fileira)

    def definir_mesa_professor(self, posicao_fileira, posicao_mesa):
        # Define a mesa do professor como ponto norteador
        if 0 <= posicao_fileira < len(self.mapa) and 0 <= posicao_mesa < len(self.mapa[posicao_fileira]):
            self.mesa_professor = (posicao_fileira, posicao_mesa)
        else:
            print("Posição inválida para a mesa do professor.")

    def nomear_sala(self, novo_nome):
        # Permite renomear a sala
        self.nome_sala = novo_nome

    def exportar_mapa(self, caminho_arquivo):
        # Exporta o mapa de sala para um arquivo JSON
        mapa_dict = {
            "nome_sala": self.nome_sala,
            "mapa": self.mapa,
            "mesa_professor": {
                "fileira": self.mesa_professor[0],
                "mesa": self.mesa_professor[1]
            } if self.mesa_professor else None
        }
        with open(caminho_arquivo, 'w') as f:
            json.dump(mapa_dict, f, indent=4)
        print(f"Mapa de sala exportado para {caminho_arquivo}")

    def exibir_mapa(self):
        # Exibe o mapa de sala de forma organizada
        print(f"Nome da sala: {self.nome_sala}")
        for i, fileira in enumerate(self.mapa):
            print(f"Fileira {i + 1}: {fileira}")
        if self.mesa_professor:
            print(f"Mesa do professor: Fileira {self.mesa_professor[0] + 1}, Mesa {self.mesa_professor[1] + 1}")

    def imprimir_mapa(self, caminho_arquivo):
        try:
            #Enviar o arquivo para a impressora
            os.system(f"Mapa de sala enviando para impressora:{caminho_arquivo}")
        except Exception as e :
            print(f"Ocorreu um erro ao tentar imprimir o mapa:{e}")

# Exemplo de uso do sistema

# Inicializar a sala
sala = MapaDeSala("Sala 101")

# Adicionar fileiras com um número específico de mesas
sala.adicionar_fileira(5)  # Adiciona uma fileira com 5 mesas
sala.adicionar_fileira(4)  # Adiciona uma fileira com 4 mesas

# Definir a mesa do professor
sala.definir_mesa_professor(0, 0)  # Define a primeira mesa da primeira fileira como a mesa do professor

# Renomear a sala
sala.nomear_sala("Laboratório de Informática")


# Exportar o mapa para um arquivo JSON
sala.exportar_mapa("mapa_de_sala.json")

# Exibir o mapa na tela
sala.exibir_mapa()

# Imprimir o mapa
sala.imprimir_mapa("mapa_de_sala.json")
