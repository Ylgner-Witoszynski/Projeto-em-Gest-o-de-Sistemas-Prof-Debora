
# Sistema de Reconhecimento Facial com Cadastro e Login

Este projeto apresenta um sistema de autenticação biométrica baseado em reconhecimento facial, permitindo o cadastro e login de usuários por meio da câmera do dispositivo. A aplicação possui uma interface gráfica simples e intuitiva, facilitando a interação do usuário durante o processo de registro e autenticação. Utilizando bibliotecas modernas de visão computacional, o sistema garante uma identificação precisa e eficiente.

## Funcionalidades

- **Cadastro de Usuário**: Captura o rosto do usuário por meio da câmera e armazena seus dados faciais, verificando automaticamente se já existe um rosto semelhante cadastrado, evitando duplicidade.
- **Login com Reconhecimento Facial**: Realiza a autenticação ao comparar a imagem capturada em tempo real com os dados previamente cadastrados.
- **Interface Gráfica**: Interface intuitiva com botões de fácil acesso para cadastro e login.

## Tecnologias Utilizadas

- **Python 3.11** (recomendado)
- **face_recognition**: Utilizada para detecção e comparação facial.
- **dlib**: Responsável pela extração dos pontos faciais e geração dos descritores.
- **OpenCV (cv2)**: Utilizada para captura e processamento de imagens em tempo real.
- **Tkinter**: Biblioteca padrão do Python para criação da interface gráfica.
- **NumPy**: Suporte ao processamento de dados numéricos, essencial no cálculo de similaridade entre faces.

## Pré-requisitos

- **Python 3.11** (recomendado)
- Pip atualizado:
  
```bash
python -m pip install --upgrade pip
```

## Instruções de Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

> Substitua pelo seu nome de usuário e repositório reais no GitHub.

### 2. Crie e ative um ambiente virtual com Python 3.11

```bash
# Crie o ambiente (certifique-se de que python aponta para a versão 3.11)
python -m venv venv

# Ative o ambiente
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install face_recognition dlib opencv-python Pillow numpy
```

> ✅ O módulo `cv2` é incluído automaticamente com o pacote `opencv-python`.

### 4. Baixe os arquivos `.dat` do dlib

Você precisa dos seguintes arquivos:

- [`shape_predictor_68_face_landmarks.dat`](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
- [`dlib_face_recognition_resnet_model_v1.dat`](http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2)

Descompacte os arquivos `.bz2` e coloque os arquivos `.dat` na pasta raiz do projeto.

### 5. Ajuste de Caminhos dos Arquivos `.dat`

Certifique-se de que o código aponte corretamente para os arquivos `.dat` usando um caminho dinâmico, como no exemplo abaixo:

```python
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
predictor_model = os.path.join(base_dir, "shape_predictor_68_face_landmarks.dat")
face_rec_model = os.path.join(base_dir, "dlib_face_recognition_resnet_model_v1.dat")
```

### 6. Execute a aplicação

```bash
python main.py
```

> Substitua `main.py` pelo nome real do seu script principal.

## Finalidade

Este projeto é ideal para fins educacionais e experimentações práticas nas áreas de reconhecimento facial, visão computacional e autenticação biométrica utilizando Python.
