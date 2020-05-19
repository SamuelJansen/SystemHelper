class SystemHelper:

    UNEXPECTED_KEYWORD_ARGUMMENT = '__init__() got an unexpected keyword argument'

    def __init__(self,globals,**kwargs):
        self.globals = globals
        self.kwargs = kwargs

        self.apiSet = {}
        self.addGitCommitter()
        self.addOfficeTrackIntegrationTests()
        self.addVoiceAssistant()
        self.addWebScrapHelper()

    def handleSystemArgumentValue(self,systemArgumentValueList,externalFunction):
        try :
            globals = self.globals
            apiKey = systemArgumentValueList[1]
            commandList = systemArgumentValueList[1:]
            apiClass = self.apiSet[apiKey]
            if globals.systemHelperRunning :
                globals.apiName = apiClass.__name__
                globals.apiPath = globals.apiPath.replace(self.__class__.__name__,globals.apiName)
                settingFilePath = f'{globals.apiPath}{globals.baseApiPath}{globals.RESOURCE_BACK_SLASH}{apiClass.__name__}.{globals.extension}'
                globals.addTree(settingFilePath)
            if apiKey in self.apiSet.keys() :
                if globals.apiName == apiClass.__name__ and not globals.systemHelperRunning :
                    api = apiClass(globals,**self.kwargs)
                else :
                    api = apiClass(globals)
                print(f'{self.__class__.__name__} running {apiClass.__name__}')
                return api.handleCommandList(commandList)
            else :
                print(f'{apiClass.__name__} running all alone')
                return externalFunction(commandList,globals,**self.kwargs)
        except Exception as exception :
            print(f'''{self.globals.ERROR}{SystemHelper.__name__} error processing "{systemArgumentValueList[1]}" call. Cause: {str(exception)}''')

    def addGitCommitter(self):
        apiKey = self.globals.GIT_COMMITTER
        try :
            import GitCommitter
            apiClass = GitCommitter.GitCommitter
            self.addApi(apiKey,apiClass)
        except Exception as exception :
            self.apiNotFound(apiKey,str(exception))

    def addOfficeTrackIntegrationTests(self):
        apiKey = self.globals.OFFICE_TRACK_INTEGRATION_TESTS
        try :
            import OfficeTrackIntegrationTests
            apiClass = OfficeTrackIntegrationTests.OfficeTrackIntegrationTests
            self.addApi(apiKey,apiClass)
        except Exception as exception :
            self.apiNotFound(apiKey,str(exception))

    def addVoiceAssistant(self):
        apiKey = self.globals.VOICE_ASSISTANT
        try :
            import VoiceAssistant
            apiClass = VoiceAssistant.VoiceAssistant
            self.addApi(apiKey,apiClass)
        except Exception as exception :
            self.apiNotFound(apiKey,str(exception))

    def addWebScrapHelper(self):
        apiKey = self.globals.CIFRAS_CLUB_WEB_SCRAPER
        try :
            import CifrasClubWebScraper
            apiClass = CifrasClubWebScraper.CifrasClubWebScraper
            self.addApi(apiKey,apiClass)
        except Exception as exception :
            self.apiNotFound(apiKey,str(exception))

    def addApi(self,apiKey,apiClass):
        self.apiSet[apiKey] = apiClass

    def apiNotFound(self,apiKey,cause):
        self.globals.debug(f'Not possible to reach {apiKey} due command line. Cause: {cause}')


def run(externalFunction,globals,**kwargs):
    import sys
    systemArgumentValueList = sys.argv.copy()
    systemHelper = SystemHelper(globals,**kwargs)
    systemHelper.handleSystemArgumentValue(systemArgumentValueList,externalFunction)
