from zoom.classes.impl import Delegate
from zoom.classes.impl import PParser

def main():
   parser=PParser()
   delegate=Delegate(parser=parser)
   delegate.delegate()   
   
   
   

if __name__ == "__main__":
    main()