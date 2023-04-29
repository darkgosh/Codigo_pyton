import os
import shutil
import pandas
from docxtpl import DocxTemplate, Inlineimage
from docx.shared import Mm


############# Configuracion de Usuario ##############

# Ruta de Salida
OUTPUT_PATH = '.\Outputs'

#Ruta fichero Excel
EXCEL_PATH = '.\Inputs\People_Data.xlsx'

#Ruta ficheros plantillas de Word
ES_WORD_TPL_PATH = '.\Inputs\Templates\WordTeplate_ES.docx'
EN_WORD_TPL_PATH = '.\Inputs\Templates\WordTeplate_EN.docx'

#Ruta de Imagenes
IMAGE_PATH = '.\Inputs\Images'

############# Configuracion de Usuario ##############

# Rutina para eliminar y crear carpetas
def EliminarCrearCarpetas(path)
    #Verificar si la carpeta existe y eliminarla
    if(os.path.exists(path)):
        shutil.rmtree(path)
    #Crear carpeta de salida
    os.mkdir(OUTPUT_PATH)    
    