import os
import time
#sdfsdfsdfdsf this is a comment
path="."
def archivos(path):
  coc=[]
  with os.scandir(path) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
  for file in ficheros:
        file_c=open(f'{path}/{file}','rb')
        contenido=file_c.read()
        file_c.close()
        coc.append(contenido)
  return coc


def subdirectorios(path):
    coc=[]
    with os.scandir(path) as ficheros:
     subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
     try:
         subdirectorios.remove('.git')
     except ValueError:
          pass
    for carpeta in subdirectorios:
              
       x=f'./{carpeta}'
       conten=archivos(x)
       coc.append(conten)
    
    for carpet in subdirectorios:
     with os.scandir(carpet) as ficheros23:
       subdirectorios_2 = [fichero23.name for fichero23 in ficheros23 if fichero23.is_dir()]
     try:
         subdirectorios_2.remove('.git')
     except ValueError:
          pass

     for v in subdirectorios_2:
       x=f'./{carpet}/{v}'
       conten=archivos(x)
       coc.append(conten)


    return coc 


while True:


   contenido_1 =[]
   contenido_1.append(archivos(path))
   contenido_1.append(subdirectorios(path))
   time.sleep(30)

   contenido_2 = []
   contenido_2.append(archivos(path))
   contenido_2.append(subdirectorios(path))






   if contenido_1 == contenido_2:
     print('no hubo cambios ')
   else:
     print('hubo camios ')
     os.system("git add .; git commit -m 'comit';git push -u origin master") 

 
