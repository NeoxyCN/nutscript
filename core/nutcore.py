from core import version, io
shouldExit = False


def run(arg):
    if(len(arg) == 1):
        print("nutscript {} copyright Neoxy 2021\nType \"help\" for help information".format(
            version.VERSION))
        while shouldExit:
            getInput = io.inp("nutscript>")
