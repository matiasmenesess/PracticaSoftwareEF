from app.models.usuario import Usuario

# Simulación de base de datos en memoria
usuarios_db = []

def guardar_usuario(usuario: Usuario):
    usuarios_db.append(usuario)
    print(f"Usuario {usuario.alias} guardado en la base de datos.")

def obtener_usuario_por_alias(alias: str) -> Usuario:
    for usuario in usuarios_db:
        if usuario.alias == alias:
            print(f"Usuario encontrado: {usuario.alias}")
            return usuario
    print(f"Usuario con alias {alias} no encontrado.")
    return None