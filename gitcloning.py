import os 

url = 'https://github.com/hothaifa96/playbooks'

try:
    os.system('rm -rf playbooks')
except:
    print('haha ')

os.system(f'git clone {url}')

print('done')