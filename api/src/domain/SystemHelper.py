class SystemHelper(self,sys.argv,globals):

    def __init__(self,globals):
        self.globals = globals

        self.apiSet = {}
        try :
            import GitCommitter
            gitCommitter = GitCommitter.GitCommitter(globals)
            self.apiSet[globals.GITC_GIT_COMMITTER] : gitCommitter.handleCommandList
        except :
            self.apiNotFoundDebug(GitCommitter.GitCommitter)

        try :
            import OfficeTrackIntegrationTests
            officeTrackIntegrationTests = OfficeTrackIntegrationTests.OfficeTrackIntegrationTests(globals)
            self.apiSet[self.globals.GITC_GIT_COMMITTER] : officeTrackIntegrationTests.handleCommandList
        except :
            self.apiNotFoundDebug(OfficeTrackIntegrationTests.OfficeTrackIntegrationTests)

    def handleSystemArgumentValue(self,systemArgumentValueList,run):
        argumentValueList = systemArgumentValueList.copy()
        try :
            self.apiSet[argumentValueList[1]](argumentValueList[1:])
        except Exception as exception :
            print(f'''{self.globals.ERROR}{SystemHelper.__class__.__name__} error processing "{argumentValueList[1]}" call: {str(exception)}''')
            run(self.globals,argumentValueList)

    def apiNotFoundDebug(self,apiClass):
        self.globals.debug(f'{apiClass.__class__.__name__} not found')
