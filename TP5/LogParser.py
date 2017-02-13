class LogParser():

    def __init__(self):
        self.text_io = None
        self.logFactory = None

    def set_log_factory(self, logFactory):
        self.logFactory = logFactory

    def set_text_io(self, text_io):
        self.text_io = text_io

    def get_logs(self):
        if self.text_io == None:
            raise FileNotOpenException
        if self.logFactory == None:
            raise NoLogFactoryException

        logs = []
        logLines = self.text_io.readlines()

        for logLineString in logLines:
            logLine = logLineString.split(",")
            logs.append(self.logFactory.create_log(logLine[0].strip(), int(logLine[1].strip()), logLine[2].strip()))

        return logs


class FileNotOpenException(Exception):
    pass

class NoLogFactoryException(Exception):
    pass
