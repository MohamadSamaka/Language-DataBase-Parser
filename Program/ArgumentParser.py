# from app import Program
import argparse
import os
# import sys

class Parser:
    def __init__(self, Str_Input):
        self.Str_Input = Str_Input
        self.EditInput()
        self.MainParser = argparse.ArgumentParser(description='Language DataBase', usage=UsageMassage())
        self.ActionsSuperParser = None
        self.ActionsSubParser = None
        self.MainParserArgMaker()
        self.AddParserArgs()
        self.EditPraserArgs()
        self.DeleteParserArgs()
        self.SelectParserArgs()
        self.Args = self.MainParser.parse_args(Str_Input)


    def EditInput(self):
        if(len(self.Str_Input) > 1 and "--help" not in self.Str_Input and "-h" not in self.Str_Input):
            self.Str_Input.append(self.Str_Input[0])
            self.Str_Input.pop(0)


    def MainParserArgMaker(self):
        self.ActionsSuperParser = self.MainParser.add_subparsers(dest = "Action", help="Possible Actions")
        self.ActionsSubParser = [self.ActionsSuperParser.add_parser("add", help="Adding Data.", ),
                                self.ActionsSuperParser.add_parser("edit", help="Edditing Data."),
                                self.ActionsSuperParser.add_parser("delete", help="Delete Colunm."),
                                self.ActionsSuperParser.add_parser("select", help="Showing Data.")]
        self.MainParser.add_argument("Language", choices=("hebrew" ,"english"), help="Language Dictionary")


    def AddParserArgs(self):
        self.ActionsSubParser[0].add_argument("Word", help="Provide The Key Word")
        self.ActionsSubParser[0].add_argument("-m", "--meaning", help="Provides a Meaning")
        self.ActionsSubParser[0].add_argument("-d", "--desc", help="Provides Description")
        self.ActionsSubParser[0].add_argument("-v", "--voiceId", help="Provides Voice Id", action="store_true")

    
    def EditPraserArgs(self):
        self.ActionsSubParser[1].add_argument("ID", type=int, help="Provide The *Id* Of The Required Column That Needs To Be Edited")
        self.ActionsSubParser[1].add_argument("-w", "--word", help="Edit Word")
        self.ActionsSubParser[1].add_argument("-m", "--meaning", help="Edit Meaning")
        self.ActionsSubParser[1].add_argument("-d", "--desc", help="Edit Description")
        self.ActionsSubParser[1].add_argument("-v", "--voiceId", type=int, help="Edit Voice Id")
    

    def DeleteParserArgs(self):
        self.ActionsSubParser[2].add_argument("-i", "--id", type=int, help="Provide The *Id* Of The Required Column That Needs To Be Deleted")
        self.ActionsSubParser[2].add_argument("-w", "--word", help="Provide The *Word* Of The Required Column That Needs To Be Deleted")


    def SelectParserArgs(self):
        self.ActionsSubParser[3].add_argument("-i", "--id", type=int, help="Provide The *Id* Of The Required Column That Needs To Be Selected")
        self.ActionsSubParser[3].add_argument("-w", "--word", help="Provide The *Word* Of The Required Column That Needs To Be Selected")
        self.ActionsSubParser[3].add_argument("-v", "--voiceId", type=int, help="Provide The *Voice Id* Of The Required Column That Needs To Be Selected")


    def Check(self, flag = None):
        if(flag == 1):
            if len([x for x in (self.Args.id,self.Args.word,self.Args.VoiceId) if x is not None]) == 3 or len([x for x in (self.Args.id,self.Args.word,self.Args.VoiceId) if x is not None]) == 2:
                print('[-] Only ONE of These Should Be Gived: --id / --word / --VoiceId')
                exit()
            elif len([x for x in (self.Args.id,self.Args.word,self.Args.VoiceId) if x is not None]) == 0:
                print('[-] ONE of These Must Be Gived:: --id / --word / --VoiceId')
                exit()
        elif(flag == 2):
            if len([x for x in (self.Args.id,self.Args.word) if x is not None]) == 2:
                print('[-] Either --id OR --word must be given not both!')
                exit()
            elif len([x for x in (self.Args.id,self.Args.word) if x is not None]) == 0:
                print('[-] --id OR --word must be given')
                exit()
        elif(flag == 3):
            if len([x for x in (self.Args.word,self.Args.desc,self.Args.meaning,self.Args.voiceId) if x is not None]) == 0:
                print('[-] At Least One of These Should Be Used: --word/ --desc/ --meaning/ --voiceId')
                exit()


    def AfterParseArgs(self):
        if self.Args and self.Args.Action == "delete":
            self.Check(2)
        elif self.Args and self.Args.Action == "edit":
            self.Check(3)
        elif self.Args and self.Args.Action == "select":
            self.Check(1)
        print(self.Args)


def UsageMassage():
    return "{} [-h] {{hebrew,english}} ... {{add,edit,delete,select}}".format(os.path.basename(__file__))
