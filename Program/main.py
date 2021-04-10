from ArgumentParser import Parser
from Sql import Program
import sys

if __name__ == "__main__":
    con_string = r"C:\Users\TheXJ\Desktop\MyCodes\python\Languages\Files\TLanguages.db"
    P = Parser(sys.argv[1:])
    P.AfterParseArgs()
    prog = Program(con_string, P.Args)
    del prog