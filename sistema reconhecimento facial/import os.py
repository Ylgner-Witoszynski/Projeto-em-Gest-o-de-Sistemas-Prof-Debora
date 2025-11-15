import os

predictor_model = "shape_predictor_68_face_landmarks.dat"
face_rec_model = "dlib_face_recognition_resnet_model_v1.dat"

# Verifica se os arquivos existem
if not os.path.exists(predictor_model):
    print(f"Arquivo {predictor_model} não encontrado.")
else:
    print(f"Arquivo {predictor_model} encontrado.")

if not os.path.exists(face_rec_model):
    print(f"Arquivo {face_rec_model} não encontrado.")
else:
    print(f"Arquivo {face_rec_model} encontrado.")
