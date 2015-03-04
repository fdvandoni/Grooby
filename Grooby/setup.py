# =============================================================================
#     Author: K Perkins
#     Date:   Jul 25, 2013
#     Taken From: http://programmingnotes.freeweq.com/
#     File:  setup.py
#     Description: This is the cx_Freeze setup file for creating an exe program
# =============================================================================
from cx_Freeze import setup, Executable
# NOTE: you can include any other necessary external imports here aswell

includefiles = []
excludes = []
packages = []

exe = Executable(
 # what to build
   script = "main.py", # the name of your main python script goes here
   initScript = None,
   base = None, # if creating a GUI instead of a console app, type "Win32GUI"
   targetName = "Grooby.exe", # this is the name of the executable file
   copyDependentFiles = True,
   compress = True,
   appendScriptToExe = True,
   appendScriptToLibrary = True,
   icon = None # if you want to use an icon file, specify the file name here
)

setup(
 # the actual setup & the definition of other misc. info
    name = "Grooby", # program name
    version = "1.0",
    description = 'Game',
    author = "estudiantes UNLA",
    author_email = " ",
    options = {"build_exe": {"excludes":excludes,"packages":packages,
      "include_files":includefiles}},
    executables = [exe]
)
# http://programmingnotes.freeweq.com/
#"acercade.png", "bola1.png", "bola2.png", "bola3.png", "controles.png", "estrella.png", "estrella1.png",
#    "finpantalla.png", "Gretoon.ttf", "historia.png", "kirby.png", "kirbydanio.png", "mapa2.png", "pajaro.png", "pajaro2.png",
#    "presentacion.png", "VCR_OSD_MONO.ttf", "dies.wav", "Green Greens.mp3", "groovy.mp3", "historia.mp3", "intro.mp3", "Vegetable Valley.exe"] # include any files here that you wish
#includes = ["creacion_sprites.py", "enemigo1.py", "enemigo2.py", "enemigo3.py", "enemigo4.py", "enemigo5.py", "estrella.py", "jugador.py",
#     "jugador2.py", "menu.py"



