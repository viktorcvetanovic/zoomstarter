import argparse
from zoom.classes import Argument

class PParser:
    parser = argparse.ArgumentParser()
    defined_groups=[
        {
            "start":{
                "flag":"-s",
                "action":"store",
                "type":str,
                "nargs":1,
                "help":"flag for starting zoom meetings"
            },
            "add":{
                "flag":"-a",
                "action":"store",
                "type":str,
                "nargs":2,
                "help":"flag for adding zoom meetings links"
            },
            "delete":{
                "flag":"-d",
                "action":"store",
                "type":str,
                "nargs":1,
                "help":"flag for deleting zoom meetings links"
            },
            "read":{
                "flag":"-r",
                "action":"store",
                "type":str,
                "nargs":'*',
                "help":"flag for reading zoom meetings links, you can read specific link by entering his name"
            },
            "start_write":{
                "flag":"-sw",
                "action":"store",
                "type":str,
                "nargs":2,
                "help":"flag for starting and writing some text in meetings"
            }

        },
        {
                "cron":{
                "flag":"-c",
                "action":"store",
                "type":int,
                "nargs":1,
                "help":"flag for adding cron to start your meetings"
                }
        }
    ]
        

    def __init__(self) -> None:
        self.parsed_data=None
        for i,group in enumerate(self.defined_groups):
            gr=self.parser.add_mutually_exclusive_group()
            for arg in group:
                obj=self.defined_groups[i][arg]
                gr.add_argument(obj["flag"],action=obj["action"],type=obj["type"],help=obj["help"],nargs=obj["nargs"])

    def __parse__(self)-> object:
        self.parsed_data=self.parser.parse_args()   
        return self.parsed_data


    def __check_prio__(self,val:str):
        data=self.defined_groups[1]
        for obj in data:
            if data[obj]["flag"] == "-"+val:
                return True
        return False


    def read_parse(self)-> object:
        parsed_list=[]
        arguments=vars(self.__parse__())
        for value in arguments:
            if arguments[value] is not None:
                if self.__check_prio__(value):
                    parsed_list.append(Argument(value,arguments[value],True))
                else:
                    parsed_list.append(Argument(value,arguments[value]))
        return parsed_list

  