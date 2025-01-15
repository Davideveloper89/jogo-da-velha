import tkinter as tk
from tkinter import messagebox
import random

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")

        self.modo_jogo = None  # Define o modo de jogo: 'IA' ou 'Humano'
        self.tabuleiro = ["" for _ in range(9)]
        self.jogador_atual = "X"

        self.frame_modo = tk.Frame(self.master)
        self.frame_modo.pack()

        tk.Label(self.frame_modo, text="Escolha o modo de jogo:").pack()
        tk.Button(self.frame_modo, text="Contra IA", command=self.iniciar_contra_ia).pack()
        tk.Button(self.frame_modo, text="Contra Humano", command=self.iniciar_contra_humano).pack()

    def iniciar_contra_ia(self):
        self.modo_jogo = "IA"
        self.frame_modo.destroy()
        self.iniciar_jogo()

    def iniciar_contra_humano(self):
        self.modo_jogo = "Humano"
        self.frame_modo.destroy()
        self.iniciar_jogo()

    def iniciar_jogo(self):
        self.frame_tabuleiro = tk.Frame(self.master)
        self.frame_tabuleiro.pack()

        self.botoes = []
        for i in range(9):
            botao = tk.Button(self.frame_tabuleiro, text="", font=("Arial", 24), height=2, width=5,
                              command=lambda i=i: self.fazer_jogada(i))
            botao.grid(row=i // 3, column=i % 3)
            self.botoes.append(botao)

        self.label_status = tk.Label(self.master, text=f"Vez de {self.jogador_atual}", font=("Arial", 14))
        self.label_status.pack()

    def fazer_jogada(self, pos):
        if self.tabuleiro[pos] == "":
            self.tabuleiro[pos] = self.jogador_atual
            self.botoes[pos].config(text=self.jogador_atual, state="disabled")

            if self.verificar_vencedor():
                messagebox.showinfo("Fim de Jogo", f"{self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif "" not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.trocar_jogador()

                if self.modo_jogo == "IA" and self.jogador_atual == "O":
                    self.master.after(500, self.jogada_ia)

    def jogada_ia(self):
        posicoes_disponiveis = [i for i, v in enumerate(self.tabuleiro) if v == ""]
        pos = random.choice(posicoes_disponiveis)
        self.fazer_jogada(pos)

    def trocar_jogador(self):
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
        self.label_status.config(text=f"Vez de {self.jogador_atual}")

    def verificar_vencedor(self):
        combinacoes = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
            (0, 4, 8), (2, 4, 6)             # Diagonais
        ]

        for a, b, c in combinacoes:
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != "":
                return True

        return False

    def reiniciar_jogo(self):
        self.tabuleiro = ["" for _ in range(9)]
        self.jogador_atual = "X"
        self.frame_tabuleiro.destroy()
        self.label_status.destroy()
        self.frame_modo = tk.Frame(self.master)
        self.frame_modo.pack()

        tk.Label(self.frame_modo, text="Escolha o modo de jogo:").pack()
        tk.Button(self.frame_modo, text="Contra IA", command=self.iniciar_contra_ia).pack()
        tk.Button(self.frame_modo, text="Contra Humano", command=self.iniciar_contra_humano).pack()

if __name__ == "__main__":
    root = tk.Tk()
    JogoDaVelha(root)
    root.mainloop()
