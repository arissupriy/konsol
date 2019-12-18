class Color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def colorize(self, text):
        return text + self.ENDC

    def blue(self, text):
        return self.colorize(self.OKBLUE + text)

    def warning(self, text):
        return self.colorize(self.WARNING + text)

    def error(self, text):
        return self.colorize(self.FAIL + text)

    def success(self, text):
        return self.colorize(self.OKGREEN + text)

    def header(self, text):
        return self.colorize(self.HEADER + text)


import sys

try:
    import readline
except:
    from pyreadline import Readline
    readline = Readline()



class KonsolException(Exception):
    pass


class CommandExit(EOFError):
    pass


class CommandNotFound(Exception):
    pass


import inspect
from tabulate import tabulate


class Command:
    def add_command(self, name, func):
        setattr(self, "do_" + name, func)

    def do_help(self):
        'List available commands with "help" or detailed help with "help konsol".'

        menu_list = ["Options", "Description"]
        methods = [
            [str(func).replace("do_", ""), getattr(self, func).__doc__]
            for func in dir(self)
            if callable(getattr(self, func))
            and not func.startswith("__")
            and func.startswith("do_")
        ]

        sys.stdout.writelines(tabulate(methods, headers=menu_list))

    def call_function(self, name):
        execute = getattr(self, "do_" + str(name).lower(), lambda: self.error(name))
        return execute()

    def error(self, text):
        raise CommandNotFound(text)

    def do_clear(self):
        "Clear console history"
        import os

        os.system("cls" if os.name == "nt" else "printf '\033c'")


class Konsol:
    """
    asdasd
    """

    __NAME__ = Color().blue("Konsol")
    __CONSOLE_NAME__ = None
    linestrip = ">"
    write = sys.stdout.writelines
    read = sys.stdout.readline
    COMMAND = None
    DESC = None

    def __init__(self, command, desc="", console_name="konsol", linestrip="~"):
        self.__NAME__ = Color().blue("({}) {} ".format(console_name, self.linestrip))
        self.__CONSOLE_NAME__ = console_name
        self.COMMAND = command
        self.DESC = desc

    def pre_command(self):
        self.COMMAND.call_function("clear")
        return "\n-- {} --\n{}\n".format(
            Color().header(self.__CONSOLE_NAME__.upper()), self.DESC,
        )

    def start(self):
        stop = None
        self.write(self.pre_command())
        readline.get_line_buffer()
        while not stop:
            try:
                sys.stdout.write(self.__NAME__)
                sys.stdout.flush()

                line = sys.stdin.readline()

                if line.strip() == "quit()" or not line:
                    raise CommandExit

                self.COMMAND.call_function(line.strip())

            except CommandExit:
                stop = 1
                self.write("\nExit Successfully\n".format(self.__NAME__))
            except KeyboardInterrupt as e:
                pass
                sys.stdout.writelines('\ntype "quit() or ctrl + D for quit" \n')
            except CommandNotFound as e:
                self.write(
                    Color().error(
                        "'{}' Command Not Found, type 'help' for show menu available\n".format(
                            e
                        )
                    )
                )
            except Exception as e:
                self.write(str(e) + "\n")

        self.COMMAND.call_function("clear")
