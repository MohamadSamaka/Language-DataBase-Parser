import sqlite3
import random
from tabulate import tabulate
class Program:
    def __init__(self, con_string, Args):
        try:
            self.con_string = con_string
            self.conn = sqlite3.connect(con_string)
            self.C = self.conn.cursor()
            self.Args = Args
            # print("[+] Connected To Database")
            # print("-"*50)
            self.CheckAction()
        except sqlite3.Error as e:
            print("[-] Error in Connection: ", e)


    def __del__(self):
            self.conn.close()
            # print("File Closed Successfuly!")


    def CheckAction(self):
        A = self.Args.Action
        L = self.Args.Language
        StringCommand = None
        if A == "add":
            values = self.AddCommandMaker()
            StringCommand = "INSERT INTO {} ({}) VALUES({});".format(L, values[0], values[1])
        elif A == "edit":
            StringCommand = "UPDATE {} SET {} WHERE Id = {};".format(L, self.EditCommandMaker(), self.Args.ID)
            pass
        elif A == "delete":
            values = self.DeleteCommandMaker()
            StringCommand = "DELETE FROM {} WHERE {} = {};".format(L, values[0], values[1])
            pass
        elif A == "select":
            values = self.SelectCommandMaker()
            StringCommand = "SELECT * FROM {} {} '{}';".format(L, values[0], values[1])
        self.Excecuter(StringCommand)

    
    def AddCommandMaker(self):
        p = self.Args
        args = [["'Word'"] ,["'{}'".format(p.word)]]
        str1 = ","
        str2 = ","
        if p.desc:
            args[0].append("'Description'")
            args[1].append("'{}'".format(p.desc))
        if p.meaning:
            args[0].append("'Meaning'")
            args[1].append("'{}'".format(p.meaning))
        if p.voiceId:
            args[0].append("'Voice ID'")
            args[1].append(str(random.randint(0,2*10**3)))
        str1 = str1.join(args[0])
        str2 = str2.join(args[1])
        args[0].clear()
        args[1].clear()
        args[0] = str1
        args[1] = str2
        return args


    def EditCommandMaker(self):
        p = self.Args
        args = []
        string = ","
        if p.word:
            args.append("Word = '{}'".format(p.word))
        if p.desc:
            args.append("Description = '{}'".format(p.desc))
        if p.meaning:
            args.append("Meaning = '{}'".format(p.meaning))
        if p.voiceId:
            args.append("'Voice ID' = {}".format(p.voiceId))
        string = string.join(args)
        return string



    def DeleteCommandMaker(self):
        p = self.Args
        T = self.Args.Language
        args = []
        if p.id:
            args.append("id")
            args.append("'{}'".format(p.id))
            if self.C.execute("SELECT EXISTS(SELECT 1 FROM {} WHERE Id='{}' LIMIT 1);".format(T,p.id)).fetchone()[0] == 1:
                self.AutoIncrementChanger()
            else:
                print("[-] This ID Dosen't Exist!")
                self.__del__()
                exit()
        elif p.word:
            args.append("word")
            args.append("'{}'".format(p.word))
            if self.C.execute("SELECT EXISTS(SELECT 1 FROM {} WHERE Word='{}' LIMIT 1);".format(T,p.word)).fetchone()[0] == 1:
                self.AutoIncrementChanger()
            else:
                print("[-] This Word Dosen't Exist!")
                self.__del__()
                exit()
        return args

    
    def SelectCommandMaker(self):
        if(self.Args.all):
            return ["",""]
        elif(self.Args.id):
            return ["WHERE Id = ", self.Args.id]
        elif(self.Args.word):
            return ["WHERE Word = ", self.Args.word]
        elif(self.Args.voiceId):
            return ["WHERE \"Voice ID\" = ", self.Args.voiceId]


    def AutoIncrementChanger(self):
        CurrentAutoIncrementVal = self.C.execute("SELECT seq FROM sqlite_sequence;").fetchone()[0]
        if CurrentAutoIncrementVal > 0:
            self.C.execute("UPDATE sqlite_sequence SET seq = {}".format(CurrentAutoIncrementVal - 1))


    def Excecuter(self, str):
        self.C.execute(str)
        if self.Args.Action == "select":
            print(tabulate(self.C.fetchall(), headers=["ID" ,"Word","Meaning", "Description", "Voice ID"]))
        self.conn.commit()
        # SuccessMssg()
        # print("[+] Command has been executed successfully!")

    # def SuccessMssg(self):
    #     A = self.Args.Action
    #     if(A == d)

