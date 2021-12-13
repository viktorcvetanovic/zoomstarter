from classes.pparser import PParser

class Delegate:

    def __init__(self,parser:PParser) -> None:
        self.parser=parser


    def delegate(self):
        data=self.parser.read_parse()
        for val in data:
            print(val)
        
                
        
