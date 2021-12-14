import os 
f=open('./config.pgit','rb')
contenido=f.readline()
repository=contenido.split('/')[-1].split('.')[0]
link=contenido.split('=')[1]
#sdf
os.chdir('..')
os.system(f'rm -r {repository}')
os.system('git clone {link}')
