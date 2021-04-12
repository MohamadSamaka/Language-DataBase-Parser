from ArgumentParser import Parser
from Sql import Program
import sys
import os

if __name__ == "__main__":
    con_string = "{}\\Files\\TLanguages.db".format(os.getcwd())
    P = Parser(sys.argv[1:])
    P.AfterParseArgs()
    prog = Program(con_string, P.Args)
    del prog