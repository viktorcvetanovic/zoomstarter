
class Argument:

    def __init__(self,key,value,flag=False) -> None:
        self.key=key
        self.value=value
        self.flag=flag
        


    def __str__(self):
        return str(self.key) + " " + str(self.value)    