from datetime import datetime
from app.models.usuario import Usuario
from app.models.contacto import Contacto
from app.models.mensaje import Mensaje

# ✅ Caso de éxito: crear un usuario
def test_crear_usuario_exito():
    usuario = Usuario(alias="mati123", nombre="Matías")
    assert usuario.alias == "mati123"
    assert usuario.nombre == "Matías"

# ❌ Error: crear usuario sin alias
def test_crear_usuario_sin_alias():
    try:
        Usuario(nombre="Matías")
        assert False  # Esto no debería ejecutarse
    except:
        assert True

# ❌ Error: crear contacto sin alias
def test_crear_contacto_sin_alias():
    try:
        Contacto(fechaRegistro=datetime.now())
        assert False
    except:
        assert True

# ❌ Error: crear mensaje sin remitente
def test_crear_mensaje_sin_remitente():
    try:
        Mensaje(destinatario="lucas", contenido="Hola", fechaEnvio=datetime.now())
        assert False
    except:
        assert True


#pip install pytest coverage

# 5. Ejecuta pruebas con coverage
# python -m coverage run -m pytest
# python -m coverage report