import os
cwd = os.getcwd()
print(cwd)
list = os.listdir()
print(list)
for name in list:
    if os.path.isfile(name):
        if name.endswith('.py'):
            print(name)
'''
ucwd = 'test'
os.chdir(ucwd) # 타겟 디렉토리를 ucwd로 바꿈
'''
print(os.getcwd())