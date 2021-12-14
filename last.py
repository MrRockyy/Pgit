import os
#fdsf
f=open('./config.pgit','r')
contenido=f.readline()
repository=contenido.split('/')[-1].split('.')[0]
link=contenido.split('=')[1]
#sdf
os.chdir('..')
os.system(f'sudo rm -r {repository}')
os.system(f'git clone {link}')
