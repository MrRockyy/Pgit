import os
import shutil
f=open('./config.pgit','r')
contenido=f.readline()
repository=contenido.split('/')[-1].split('.')[0]
link=contenido.split('=')[1]
#sdf
files=os.listdir('.')
for file in files:
    try:
        os.remove(file)
    except:
        try:
            os.rmdir(file)
        except:
             shutil.rmtree(file)


os.system(f'git clone {link}')
os.chdir(repository)

file2 =os.listdir('.')
for file in file2:
    shutil.move(file, '../')
os.chdir('../')
shutil.rmtree(repository)

