import os
#sfd
archi1=open(f"./config.pgit","w")
repositorio=input("please wtrite the repository .git: ")
archi1.write(f"repository={repositorio}\n")
time=input("please put the updates period")
archi1.write(f"time={int(time)}\n")

os.system(f"echo '# real time' >> README.md ; git init ; git add README.md ;git commit -m 'first commit' ; git branch -M master;git remote remove origin;git remote add origin {repositorio};git push -u origin master")
