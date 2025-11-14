import os
import re

# Directorio de las clases
clases_dir = r"c:\Users\erick.merino\OneDrive - Ministerio de Educación\Documentos\MisApps\probest\clases\probabilidad y estadistica"

# Lista de archivos a procesar
archivos = [
    "0-introduccion.yml",
    "1-tablas_graficos.yml",
    "2-medidas_posicion.yml",
    "3-reglas_probabilidades.yml"
]

def remove_emojis(text):
    """Elimina emojis y algunos caracteres especiales problemáticos"""
    # Patrón para emojis y caracteres especiales
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)

for archivo in archivos:
    filepath = os.path.join(clases_dir, archivo)
    
    if os.path.exists(filepath):
        print(f"Procesando {archivo}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Eliminar emojis
        contenido_limpio = remove_emojis(contenido)
        
        # Reemplazar ✓ con •
        contenido_limpio = contenido_limpio.replace('✓', '•')
        contenido_limpio = contenido_limpio.replace('✅', '•')
        
        # Escribir el archivo limpio
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(contenido_limpio)
        
        print(f"  ✓ {archivo} actualizado")
    else:
        print(f"  ✗ {archivo} no encontrado")

print("\n¡Proceso completado!")
