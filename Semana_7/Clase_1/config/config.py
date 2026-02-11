def obtener_db_config():
    try:
        return {
        "host":"localhost",
        "user":"root",
        "password":"root",
        "database":"clientes_python"
        }
    except Exception as e:
        raise RuntimeError(f"Error creado la configuracio de la Base de Datos: {e}")