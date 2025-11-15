import cv2
import face_recognition
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Verifica se a pasta 'usuarios' existe; se não, cria
if not os.path.exists('usuarios'):
    os.makedirs('usuarios')

def verificar_usuario_existente(nova_imagem_encoding):
    # Percorre as imagens na pasta 'usuarios' para ver se já existe um rosto semelhante
    for filename in os.listdir('usuarios'):
        caminho_imagem = os.path.join('usuarios', filename)
        imagem_existente = face_recognition.load_image_file(caminho_imagem)
        encoding_existente = face_recognition.face_encodings(imagem_existente)
        
        if encoding_existente:
            resultados = face_recognition.compare_faces([encoding_existente[0]], nova_imagem_encoding)
            if resultados[0]:
                return True  # Retorna verdadeiro se o usuário já existe
    return False  # Retorna falso se o usuário não existe

def iniciar_cadastro(nome):
    if not nome:
        messagebox.showwarning("Aviso", "Por favor, insira seu nome.")
        return

    # Inicia a captura de vídeo
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        messagebox.showerror("Erro", "Falha ao acessar a câmera.")
        return

    # Reduz a resolução da câmera para melhorar o desempenho
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    rosto_detectado_consecutivo = 0
    FRAMES_NECESSARIOS = 5  # Número de frames consecutivos necessários

    frame = None  # Declara 'frame' no escopo da função

    def atualizar_frame():
        nonlocal rosto_detectado_consecutivo, frame

        ret, frame = cam.read()
        if not ret:
            messagebox.showerror("Erro", "Falha ao acessar a câmera.")
            cam.release()
            root.destroy()
            return

        # Redimensiona o frame para acelerar o processamento
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Converte para RGB (necessário para face_recognition)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Detecta os rostos
        loc_rostos = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=1)
        num_rostos = len(loc_rostos)

        # Verifica se há exatamente um rosto detectado
        if num_rostos == 1:
            rosto_detectado_consecutivo += 1
            cor_retangulo = (0, 255, 0)  # Verde
        else:
            rosto_detectado_consecutivo = 0
            cor_retangulo = (0, 0, 255)  # Vermelho

        # Escala as coordenadas de volta para o tamanho original
        for (top, right, bottom, left) in loc_rostos:
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            cv2.rectangle(frame, (left, top), (right, bottom), cor_retangulo, 2)

        # Exibe uma mensagem na tela
        if rosto_detectado_consecutivo >= FRAMES_NECESSARIOS:
            cv2.putText(frame, "Rosto estável detectado", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Detectando rosto...", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Converte o frame para imagem compatível com Tkinter
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label_video.imgtk = imgtk
        label_video.configure(image=imgtk)

        # Continua atualizando o frame
        label_video.after(10, atualizar_frame)

    def capturar_imagem(event):
        nonlocal rosto_detectado_consecutivo, frame
        if event.keysym == 'Escape':
            messagebox.showinfo("Encerrando", "Cadastro cancelado.")
            cam.release()
            root.destroy()
        elif event.keysym == 'space':
            if rosto_detectado_consecutivo >= FRAMES_NECESSARIOS:
                # Realiza a verificação com a imagem capturada
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                nova_imagem_encoding = face_recognition.face_encodings(rgb_frame)[0]

                if verificar_usuario_existente(nova_imagem_encoding):
                    messagebox.showinfo("Cadastro", "Usuário já cadastrado!")
                else:
                    # Salva a imagem se o usuário não existe
                    try:
                        cv2.imwrite(f'usuarios/{nome}.jpg', frame)
                        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
                    except Exception as e:
                        messagebox.showerror("Erro", f"Erro ao salvar a imagem: {e}")
                
                cam.release()
                root.destroy()
            else:
                messagebox.showwarning("Aviso", "Rosto não estável detectado. Mantenha-se imóvel por alguns instantes.")

    # Cria a janela principal
    root = tk.Tk()
    root.title("Cadastro de Usuário")

    # Exibe a mensagem de instrução na tela
    label_instrucao = tk.Label(root, text="Pressione 'Espaço' para capturar a imagem ou 'Esc' para sair.")
    label_instrucao.pack(pady=5)

    # Label para exibir o vídeo
    label_video = tk.Label(root)
    label_video.pack()

    # Inicia a captura de frames
    atualizar_frame()

    # Vincula as teclas 'space' e 'Escape' aos eventos correspondentes
    root.bind('<KeyPress-space>', capturar_imagem)
    root.bind('<KeyPress-Escape>', capturar_imagem)

    root.mainloop()

# Cria a interface para inserir o nome
janela_nome = tk.Tk()
janela_nome.title("Entrada de Nome")

label_nome = tk.Label(janela_nome, text="Digite seu nome:")
label_nome.pack(pady=5)

entry_nome = tk.Entry(janela_nome)
entry_nome.pack(pady=5)

def on_iniciar_cadastro():
    nome = entry_nome.get().strip().replace(" ", "_")
    if not nome:
        messagebox.showwarning("Aviso", "Por favor, insira seu nome.")
        return
    janela_nome.destroy()
    iniciar_cadastro(nome)

button_iniciar = tk.Button(janela_nome, text="Iniciar Cadastro", command=on_iniciar_cadastro)
button_iniciar.pack(pady=10)

janela_nome.mainloop()
