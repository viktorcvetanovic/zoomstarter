from classes.impl.delegate import Delegate
from classes.pparser import PParser

def main():
   parser=PParser()
   delegate=Delegate(parser=parser)
   delegate.delegate()   
   
   

if __name__ == "__main__":
    main()