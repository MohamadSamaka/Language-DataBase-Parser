from ArgumentParser import Parser
from Sql import Program
import sys

if __name__ == "__main__":
    # P = Parser(sys.argv[1:])
    # P.AfterParseArgs()
    con_string = r"C:\Users\TheXJ\Desktop\MyCodes\python\Languages\Files\TLanguages.db"
    prog = Program(con_string)
    del prog
    pass