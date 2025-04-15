# SmartAudioRestore

## Descripción
SmartAudioRestore es un proyecto diseñado para procesar y restaurar archivos de audio utilizando técnicas avanzadas de procesamiento de señales. Este proyecto incluye herramientas para la evaluación de calidad, diagnóstico y restauración de audio.

## Estructura del Proyecto
```
SmartAudioRestore/
├── __init__.py
├── main.py
├── README.md
├── requirements.txt
├── __pycache__/
├── Tests/
│   └── TestFiles/
```

- **main.py**: Contiene la clase `AudioProcessor` para procesar archivos de audio.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.
- **Tests/TestFiles/**: Carpeta con archivos de audio de prueba.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Ejemplo de uso de la clase `AudioProcessor`:
```python
from SmartAudioRestore.main import AudioProcessor

processor = AudioProcessor("Tests/TestFiles/Carlos_Gardel_-_Congojas_(1924).flac")
print(processor.AudioIn)
```

## Dependencias
- numpy==1.24.3
- librosa==0.10.0
- soundfile

## Contribuciones
No abierto a contribuciones.

## Licencia
Este proyecto está bajo la Licencia MIT.

