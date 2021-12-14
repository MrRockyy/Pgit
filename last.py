import os
#fdsf
f=open('./config.pgit','r')
contenido=f.readline()
repository=contenido.split('/')[-1].split('.')[0]
link=contenido.split('=')[1]
#sdf
os.system('source ~/.config/pgit/cd.sh ..')
os.system(f'sudo rm -r {repository}')
os.system(f'git clone {link}')
os.system(f'source ~/.config/pgit/cd.sh {repository}')
