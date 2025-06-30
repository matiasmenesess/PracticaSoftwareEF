from fastapi import APIRouter
from app.models.mensaje import Mensaje
from app.repositories import usuario_repository
from app.services import usuario_service


router = APIRouter(prefix="/mensajeria", tags=["mensajeria"])


#En FastAPI, si declaras un parámetro que no está en la ruta, automáticamente se interpreta como query parameter.

@router.get("/contactos")
def obtener_contactos(mialias: str):
    return usuario_repository.obtener_usuario_por_alias(mialias).listaContactos

@router.post("/contactos/{alias}")
def crear_contacto(alias: str, contacto: str, nombre: str):
    return usuario_service.crear_contacto(alias, contacto, nombre)

@router.post("/enviar")
def enviar_mensaje(usuario: str, contacto: str , mensaje: str):
    remitente = usuario_repository.obtener_usuario_por_alias(usuario)
    destinatario = usuario_repository.obtener_usuario_por_alias(contacto)

    if not remitente or not destinatario:
        return {"error": "Remitente o destinatario no encontrado"}
    
    #si el remitente no tiene al destinatario en su lista de contactos, falla
    if not any(c.alias == destinatario.alias for c in remitente.listaContactos):
        return {"error": f"El usuario {remitente.alias} no tiene a {destinatario.alias} en su lista de contactos"}
    
    usuario_service.enviar_mensaje(usuario,contacto,mensaje)

    print(f"Mensaje enviado de {remitente.alias} a {destinatario.alias}: {mensaje}")

    return {"mensaje": "Mensaje enviado correctamente"}
