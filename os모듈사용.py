import os
import shutil

print(os.getcwd()) # 현재 작업 경로 확인하기
print(os.listdir()) # 현재 작업 경로 내에 들어있는 파일 리스트 확인하기
os.chdir('c:/Users')
print(os.getcwd())
os.path.isdir('D:/python/이것은직접만든거시아니여~') # 경로가 존재하는지 확인하기
if(os.path.isdir('D:/python/이것은직접만든거시아니여~') == False): os.mkdir('D:/python/이것은직접만든거시아니여~') # 입력한 경로에 폴더 만들기
os.rename('D:/python/이것은직접만든거시아니여~', 'D:/python/2') # 파일이나 경로 이름 바꾸기
os.rmdir('D:/python/2') # 폴더 삭제하기
os.remove('D:/python/number.txt') # 파일 삭제하기

shutil.copy('D:/python/test.txt', 'D:/python/test2.txt') # 파일 복사하기
shutil.rmtree('D:/python') # 경로(폴더)와 파일을 한꺼번에 모두 삭제하기