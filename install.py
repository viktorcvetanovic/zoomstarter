import os
import shutil
cwd = os.getcwd()
os.system('cd '+cwd)
os.system('python setup.py install')
os.system('echo END INSTALLATION')
os.system("pyinstaller --onefile --icon=ico.ico runner.py")
desktop =  desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
shutil.move("dist\\runner.exe", desktop+"\\zoomstarter.exe")
os.system('echo kraj')