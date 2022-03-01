import os
import shutil
cwd = os.getcwd()
os.system('cd '+cwd)
os.system('python setup.py install')
os.system('echo END INSTALLATION')
os.system("pyinstaller --onefile runner.py")
desktop =  os.environ['USERPROFILE']+"\\OneDrive\\Desktop"
print(desktop)
shutil.move("dist\\runner.exe", desktop+"\\runner.exe")
os.system('echo kraj')