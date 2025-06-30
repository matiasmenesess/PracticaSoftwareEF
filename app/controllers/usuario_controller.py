from fastapi import APIRouter
from app.models.usuario import Usuario
from app.services.usuario_service import crear_usuario_service

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/crear")
def crear_usuario(usuario: Usuario):
    try:
        print(f"Creando usuario: {usuario.alias}")
        print(f"NOMBRE: {usuario.nombre}")    
        return crear_usuario_service(usuario)
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return {"error": str(e)}


@router.post("/health")
def health():
    """
    Endpoint de salud para verificar que el servicio está funcionando.
    """
    print("Verificando estado del servicio de usuarios...")

    return {"status": "ok", "message": "El servicio de usuarios está funcionando correctamente."}