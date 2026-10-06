from fastapi import FastAPI, File, UploadFile
from supabase import create_client, Client
import shutil
import os

app = FastAPI(title="API Flora y Fauna Puebla")

# Configuración de Supabase
url: str = os.environ.get("SUPABASE_URL", "https://pmfkrsbpdaljzbwuviiv.supabase.co/rest/v1/")
key: str = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBtZmtyc2JwZGFsanpid3V2aWl2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTEyOTIyMDQsImV4cCI6MjEwNjg2ODIwNH0.2pYPCp1mLwv9duXnbuCd4uhlGnQCclafGl5uXrkElyg")
supabase: Client = create_client(url, key)

@app.get("/")
def read_root():
    return {"mensaje": "API de Reconocimiento de Flora y Fauna activa"}

@app.post("/identificar")
async def identificar_especie(imagen: UploadFile = File(...)):
    # 1. Crear una carpeta llamada 'uploads' si no existe
    os.makedirs("uploads", exist_ok=True)
    
    # 2. Definir la ruta donde se guardará la imagen
    ruta_archivo = f"uploads/{imagen.filename}"
    
    # 3. Guardar el archivo físicamente en tu computadora
    with open(ruta_archivo, "wb") as buffer:
        shutil.copyfileobj(imagen.file, buffer)
        
    return {
        "filename": imagen.filename, 
        "status": "recibida y guardada", 
        "ruta": ruta_archivo
    }