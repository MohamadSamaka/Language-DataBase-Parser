from app import Program
import argparse

values = [{"1":"Hebrew", "2":"English"}, {"1":"Add", "2":"Edit"}]
index = -1

def Usage():
    return '''
    i will make it soon
    '''

def convertvalues(value):
    global index
    index+=1
    if(values[index].get(value)):
        return values[index].get(value)
    else:
        print("[-] Wrong Value Please Do --help/-h and take a look on usage!")
        exit()

parser = argparse.ArgumentParser(description='Language DataBase', usage= Usage())
subparsers = parser.add_subparsers(dest = "command")

list_parser = subparsers.add_parser("list", help="Lists The Options Of Argument/s")
list_parser.add_argument("Argument", choices=("language", "action"), help="Name Of The Argument")

app_parser = subparsers.add_parser("app", help="The Actual Program")

subparsers_app = app_parser.add_subparsers(dest = "command")
add_subparsers = subparsers_app.add_parser("add", help="Adding Data.")
edit_subparsers = subparsers_app.add_parser("edit", help="Edditing Data.")
delete_subparsers = subparsers_app.add_parser("delete", help="Delete Colunm.")
select_subparsers = subparsers_app.add_parser("select", help="Showing Data.")

# app_parser.add_argument("Language", type=convertvalues, help="Language Dictionary")
# app_parser.add_argument("Action", type=convertvalues, help="The Action Needed")
# app_parser.add_argument("-w", "--word" ,help="The Word You Wanna Enter To DataBas")
args = parser.parse_args()
