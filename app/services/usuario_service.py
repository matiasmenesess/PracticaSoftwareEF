from app.models.usuario import Usuario
from app.models.contacto import Contacto
from datetime import datetime   
from app.repositories.usuario_repository import guardar_usuario, obtener_usuario_por_alias

def crear_usuario_service(usuario: Usuario):
    guardar_usuario(usuario)
    return {"mensaje": f"Usuario {usuario.alias} creado"}


def crear_contacto(alias: str, contacto: str, nombre: str):
    usuario = obtener_usuario_por_alias(alias)
    if not usuario:
        return {"error": f"Usuario '{alias}' no existe"}

    usuario_existente = obtener_usuario_por_alias(contacto)
    if not usuario_existente:
        nuevo_contacto = Usuario(alias=contacto, nombre=nombre)
        guardar_usuario(nuevo_contacto)
    else:
        nuevo_contacto = usuario_existente

    ya_existe = any(c.alias == contacto for c in usuario.listaContactos)
    if not ya_existe:
        nuevo_contacto = Contacto(alias=contacto, fechaRegistro=datetime.now())
        usuario.listaContactos.append(nuevo_contacto)
        guardar_usuario(usuario)

    return {"mensaje": f"Contacto '{contacto}' agregado al usuario '{alias}'"}

def enviar_mensaje(usuario: str, contacto: str, mensaje: str):
    mensaje_obj = {
        "remitente": usuario,
        "destinatario": contacto,
        "contenido": mensaje,
        "fechaEnvio": datetime.now()
        }
    user_obj = obtener_usuario_por_alias(usuario)
    if not user_obj:
        return {"error": f"Usuario '{usuario}' no existe"}
    contacto_obj = obtener_usuario_por_alias(contacto)
    user_obj.mensajesEnviados.append(mensaje_obj)
    contacto_obj.mensajesRecibidos.append(mensaje_obj)
    guardar_usuario(user_obj)
    guardar_usuario(contacto_obj)
    return {"mensaje": f"Mensaje enviado de {usuario} a {contacto}"}