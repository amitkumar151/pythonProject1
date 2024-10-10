from abc import ABC, abstractmethod
class Excelreader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass


class Browser(Excelreader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass


class TC1(Browser):
    def star_Browser(self):
        print(" Starting")

    def stopBrowser(self):
        print("Stop Browser")

    def readFromExcel(self):
        print("read from excel is ready ")

    def run_tc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()


bs =TC1()
bs.run_tc()
