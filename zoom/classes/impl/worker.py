

import time
import webbrowser
from zoom.util.sysconfig import *
from zoom.classes import Argument


class Worker:

    def __init__(self,arguments: list) -> None:
        self.config=get_config(0)
        self.arguments=arguments


    def do(self): 
        for item in self.arguments:
            key=item.key
            if key=="a":
                self.add_link(item)
            elif key=="r":
                self.read_link(item)
            elif key=="s":
                self.start_link(item)
            elif key=="sw":
                self.start_write_link(item)
            elif key=="d":
                self.remove_link(item)
            elif key=="c":
                if os.name == "nt":
                        self.create_task(item)
                else:
                    raise SystemError("Not implemented on linux")
                


    def add_link(self,argument:Argument):
        self.read_data()
        self.data[argument.value[0]]=argument.value[1]
        with open(self.config, 'w') as f:
            json.dump(self.data, f)

    def read_link(self,argument:Argument):
        self.read_data()
        if len(argument.value) >= 1:
            try:
                return print(self.data[argument.value[0]])
            except Exception:
                raise ValueError("Config file does not contains that key")
        return print(self.data)

    def remove_link(self,argument:Argument):
        self.read_data()
        if argument.value[0] is None:
            raise ValueError("You need to define key and value to add a link")
        del self.data[argument.value[0]]
        with open(self.config, 'w') as f:
            json.dump(self.data, f)


    def start_link(self,argument:Argument):
        self.read_data()
        try:
            webbrowser.open(self.data[argument.value[0]], new=0, autoraise=True)
        except Exception:
            raise ValueError("You have not definied that link !!! " +
                            "\n Link name: " + argument.value[0] +
                            "\n Check your config.json or use -a function")

    def start_write_link(self,argument:Argument):
        self.read_data()
        self.start_link(argument)
        if argument.value[1] is None:
            raise ValueError("Please enter your name")
        import pygetwindow as gw
        import pyautogui
        zooms=gw.getWindowsWithTitle('Zoom Meeting')
        while len(zooms)<1:
            zooms=gw.getWindowsWithTitle('Zoom Meeting')
        time.sleep(2)    
        handle = zooms[0]
        handle.activate() 
        handle.maximize()
        pyautogui.hotkey('alt', 'h')
        for char in argument.value[1]:
            pyautogui.press(char)
        pyautogui.press("enter")


    #TODO: to be refactored and fixed
    def create_task(argument:Argument):
        import datetime
        import win32com.client
        global args
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        root_folder = scheduler.GetFolder('\\')
        task_def = scheduler.NewTask(0)

        # Create trigger

        start_time = datetime.datetime.now() + datetime.timedelta(minutes=float(args[-1]))
        args=args[:-1]
        TASK_TRIGGER_TIME = 1
        trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
        trigger.StartBoundary = start_time.isoformat()

        # Create action
        TASK_ACTION_EXEC = 0
        action = task_def.Actions.Create(TASK_ACTION_EXEC)
        action.ID = 'zoom'
        action.Path = args[0]
        action.Arguments = " ".join(args)

        # Set parameters
        task_def.RegistrationInfo.Description = 'Task for starting zoom meetings'
        task_def.Settings.Enabled = True
        task_def.Settings.StopIfGoingOnBatteries = False

        # Register task
        # If task already exists, it will be updated
        TASK_CREATE_OR_UPDATE = 6
        TASK_LOGON_NONE = 0
        root_folder.RegisterTaskDefinition(
            'zoom starter',  # Task name
            task_def,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE)





    def read_data(self):
        try:
            with open(self.config, 'r') as f:
                self.data=json.load(f)
        except EnvironmentError:
            raise FileNotFoundError("Please add config.json in this path: " + self.config)

                    
        