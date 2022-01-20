<h1 align="center">Download from JSON</h1>

<p align="center">Aplicação para fazer o download de imagens a partir de um JSON.<p>

<p align="center">
    <a href="#pre-requisitos">Pré-Requisitos</a> •
    <a href="#rodando-a-aplicacao">Rodando a Aplicação</a>
<p>

---

<a href="https://www.dududornelees.com.br">
    <img alt="Download from JSON GIF" title="Download from JSON GIF" src="./github/DownloadFromJSON.gif" width="100%" />
</a>

<p align="center">Apenas alguns downloads da aplicação.<p>


<h3 id="pre-requisitos">Pré-Requisitos</h3>
Antes de começar, você vai precisar ter instalado em sua máquina as seguinte ferramentas: <a href="https://git-scm.com" target="_blank">Git</a> e <a href="https://www.python.org/downloads/" target="_blank">Python</a>.



<h3 id="rodando-a-aplicacao">Rodando a Aplicação</h3>

```bash
# Clone o repositório
$ git clone https://github.com/dududornelees/download-from-json.git
# Acesse a pasta do projeto no terminal
$ cd download-from-json
# Crie um arquivo chamado "images.json", e tenha uma array de objetos como este:
$ {"name": nome-imagem, "image": url-da-imagem}
# Instale as dependencias
$ pip install requests
# Inicie a aplicação
$ py Download.py
# A aplicação comecará a rodar!
```