import os
version = input('please put the version for this release: ')
os.system(f'git tag {version}')
os.system(f'git push master {version}')
