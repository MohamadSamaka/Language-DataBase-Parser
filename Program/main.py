from app import Program
import argparse

class Parser:
    def __init__(self, parser):
        self.parser = parser
        self.values = [{"1":"Hebrew", "2":"English"}, {"1":"Add", "2":"Edit"}]
        self.index = -1
        self.SuperSubParser = None
        self.ListSubParser = None
        self.AppSubParser = None
        self.SuperActionsSubParser = None
        self.ActionsSubParser = None

    def SubParserMaker(self):
        self.SuperSubParser = self.parser.add_subparsers(dest = "command")
        self.ListSubParser = self.SuperSubParser.add_parser("list", help="Lists The Options Of Argument/s")
        self.AppSubParser = self.SuperSubParser.add_parser("app", help="The Actual Program")
        self.SuperActionsSubParser = self.AppSubParser.add_subparsers(dest = "command")
        self.ActionsSubParser = [self.SuperActionsSubParser.add_parser("add", help="Adding Data."),
                                self.SuperActionsSubParser.add_parser("edit", help="Edditing Data."),
                                self.SuperActionsSubParser.add_parser("delete", help="Delete Colunm."),
                                self.SuperActionsSubParser.add_parser("select", help="Showing Data.")]

    def AddPositionalArgs(self):
        self.ListSubParserArgs()
        self.AppSubParserArgs()

    def ListSubParserArgs(self):
        self.ListSubParser.add_argument("Argument", choices=("language", "action"), help="Name Of The Argument")
    

    def AppSubParserArgs(self):
        self.AppSubParser.add_argument("Language", type=self.convertvalues, help="Language Dictionary")

    # def SuperActionsSubParser(self):


    def convertvalues(self, value):
        self.index+=1
        if(self.values[self.index].get(value)):
            return self.values[self.index].get(value)
        else:
            print("[-] Wrong Value Please Do --help/-h and take a look on usage!")
            exit()

    



# def convertvalues(value):
#     global index
#     index+=1
#     if(values[index].get(value)):
#         return values[index].get(value)
#     else:
#         print("[-] Wrong Value Please Do --help/-h and take a look on usage!")
#         exit()


# from app import Program
# import argparse

# values = [{"1":"Hebrew", "2":"English"}, {"1":"Add", "2":"Edit"}]
# index = -1

# def Usage():
#     return '''
#     i will make it soon
#     '''

# def convertvalues(value):
#     global index
#     index+=1
#     if(values[index].get(value)):
#         return values[index].get(value)
#     else:
#         print("[-] Wrong Value Please Do --help/-h and take a look on usage!")
#         exit()

# parser = argparse.ArgumentParser(description='Language DataBase', usage= Usage())
# subparsers = parser.add_subparsers(dest = "command")

# list_parser = subparsers.add_parser("list", help="Lists The Options Of Argument/s")
# list_parser.add_argument("Argument", choices=("language", "action"), help="Name Of The Argument")

# app_parser = subparsers.add_parser("app", help="The Actual Program")

# subparsers_app = app_parser.add_subparsers(dest = "command")
# add_subparsers = subparsers_app.add_parser("add", help="Adding Data.")
# edit_subparsers = subparsers_app.add_parser("edit", help="Edditing Data.")
# delete_subparsers = subparsers_app.add_parser("delete", help="Delete Colunm.")
# select_subparsers = subparsers_app.add_parser("select", help="Showing Data.")

# # app_parser.add_argument("Language", type=convertvalues, help="Language Dictionary")
# # app_parser.add_argument("Action", type=convertvalues, help="The Action Needed")
# # app_parser.add_argument("-w", "--word" ,help="The Word You Wanna Enter To DataBas")
# args = parser.parse_args()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Language DataBase')
    P = Parser(parser)
    P.SubParserMaker()
    P.AddPositionalArgs()
    args = parser.parse_args()
    # con_string = r"C:\Users\TheXJ\Desktop\MyCodes\python\Languages\Files\Languages.db"
    # prog = Program(con_string)
    # del prog
