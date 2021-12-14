import os 
f=open('./config.pgit','rb')
contenido=f.readline()
print contenido 
os.chdir('..')
os.system(f'rm -r {repository}')
os.system('git clone {link}')
