from zoom.classes.impl.pparser import PParser
from zoom.classes.impl.worker import Worker

class Delegate:

    def __init__(self,parser:PParser) -> None:
        self.parser=parser


    def delegate(self):
        data=self.parser.read_parse()
        worker=Worker(data)
        worker.do()
        
                
        
