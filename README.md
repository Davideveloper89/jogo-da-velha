# Jogo da Velha com IA e Multijogador

Este é um jogo da velha com interface gráfica, desenvolvido em Python usando a biblioteca Tkinter. 
O jogo permite que você jogue contra outro humano ou desafie a IA, com funcionalidades simples e intuitivas!

---

## 🎮 Funcionalidades

- Modo **Multijogador**: Dois jogadores humanos.
- Modo **Contra IA**: Desafie o computador!
- Interface gráfica amigável.
- Regras clássicas do Jogo da Velha.

---

## 🛠️ Pré-requisitos

Para executar o jogo, você precisará de:

- **Python 3.7 ou superior**
- **Tkinter** (normalmente já incluído com o Python)

### Como instalar dependências

#### Linux

##### Ubuntu/Debian

1. Atualize os pacotes:
   ```bash
   sudo apt update
   ```

2. Instale Python e Tkinter:
   ```bash
   sudo apt install python3 python3-tk
   ```

##### Fedora

1. Atualize os pacotes:
   ```bash
   sudo dnf update
   ```

2. Instale Python e Tkinter:
   ```bash
   sudo dnf install python3 python3-tkinter
   ```

##### openSUSE

1. Atualize os pacotes:
   ```bash
   sudo zypper refresh
   ```

2. Instale Python e Tkinter:
   ```bash
   sudo zypper install python3 python3-tk
   ```

##### Alpine Linux

1. Atualize os pacotes:
   ```bash
   doas apk update
   ```

2. Instale Python e Tkinter:
   ```bash
   doas apk add python3 tk tk-dev python3-dev
   ```

3. Compile Python com suporte a Tkinter (se necessário):
   ```bash
   wget https://www.python.org/ftp/python/3.12.8/Python-3.12.8.tgz
   tar -xzf Python-3.12.8.tgz
   cd Python-3.12.8
   ./configure --enable-optimizations
   make
   doas make altinstall
   ```

#### Windows

1. Baixe e instale o [Python](https://www.python.org/downloads/).
2. Durante a instalação, marque a opção **Add Python to PATH**.
3. Tkinter já vem incluído no instalador padrão do Python.

---

## 🚀 Como executar o jogo

1. Clone este repositório:
   ```bash
   git clone https://github.com/Davideveloper89/Jogo-da-Velha.git
   cd jogo-da-velha
   ```

2. Execute o jogo:
   ```bash
   python3 jogo-da-velha.py
   ```

---

## 📖 Regras do Jogo

- Dois jogadores se revezam para marcar "X" ou "O" em um tabuleiro 3x3.
- O primeiro a alinhar três símbolos na horizontal, vertical ou diagonal vence.
- Se o tabuleiro for preenchido sem vencedor, o jogo termina em empate.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## ❤️ Agradecimentos

Feito com dedicação por [Davideveloper89].

