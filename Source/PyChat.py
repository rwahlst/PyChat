# PyChat.py
# Python Internet Chat Program
# Author: Axel Wahlstrom
# Date: October 26th 2025

import sys
import os

class Server():

    def __init__(self):
        print("Server")

class Client():

    def __init__(self):
        print("Client")

class Controller():

    running: bool = False
    isClient: bool = False
    isServer: bool = False
    client: Client = None
    server: Server = None
    cursor: str = "> "

    def __init__(self, argv):
        self.ClearConsole()
        if len(argv) == 1:
            self.Shell()
        else:
            self.ParseArgs(argv)
        
        if self.isClient:
            self.client = Client()
        elif self.isServer:
            self.server = Server()
        else:
            print("Failed to initialize server or client subroutines: Please try again")
            exit(-1)


    def Shell(self):
        self.running = True

        print("Select a mode:\n1) Client\n2) Server\n3) Exit")
        while self.running:
            cmd = input(self.cursor)
            if cmd.upper() == "CLIENT":
                print("Initializing PyChat client...")
                self.running = False
                self.isClient = True
                self.isServer = False
            elif cmd.upper() == "SERVER":
                print("Initializing PyChat server...")
                self.running = False
                self.isServer = True
                self.isClient = False
            elif cmd.upper() == "EXIT":
                self.running = False
                print("Goodbye...")
                exit(0)
            else:
                print("Command '" + cmd + "' not recognized...")

    
    def ClearConsole(self):
    # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
    # For macOS and Linux
        else:
            _ = os.system('clear')


    def ParseArgs(self, argv):
        if (len(argv) > 2):
            print("usage: python PyChat.py <-c OR -s>")
            print("example client: python PyChat.py -c")
            exit(-1)
        else:
            for i in range(1, len(argv)):
                if (argv[i].upper() == "-C"):
                    print("Initializing PyChat client...")
                    self.isClient = True
                    self.isServer = False
                elif (argv[i].upper() == "-S"):
                    print("Initializing PyChat server...")
                    self.isServer = True
                    self.isClient = False
                else:
                    print("Defaulting to host as server...")
                    self.isServer = True
                    self.isClient = False


# Entry point
args = sys.argv
_controller = Controller(args)