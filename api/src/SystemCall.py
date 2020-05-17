def systemHelper(commandList,globals,**kwargs):
    pass

if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)
    import SystemHelper
    import sys
    SystemHelper.run(systemHelper,globals)
