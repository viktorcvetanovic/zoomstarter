import os
import shutil
cwd = os.getcwd()
os.system('cd '+cwd)
os.system('python setup.py install')
os.system('echo END INSTALLATION')
os.system("pyinstaller --onefile --icon=ico.ico runner.py")
desktop =  os.environ['USERPROFILE']+"\\OneDrive\\Desktop"
shutil.move("dist\\runner.exe", desktop+"\\zoomstarter.exe")
os.system('echo kraj')