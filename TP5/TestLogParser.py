import unittest
from io import StringIO

from mockito import mock, when, verify
from LogParser import *

class TestLogParserAvecStringIO(unittest.TestCase):

    def test_parse_file_ok(self):
        parser = LogParser()

        logFactory = mock()
        log = mock()
        when(log).get_date().thenReturn("2010-02-25")
        when(log).get_priority().thenReturn(5)
        when(log).get_message().thenReturn("error in database")
        when(logFactory).create_log("2010-02-25", 5, "error in database").thenReturn(log)

        parser.set_log_factory(logFactory)
        parser.set_text_io(StringIO("2010-02-25, 5, error in database\n"))

        logs = parser.get_logs()

        self.assertEqual(1, len(logs))
        self.assertTrue(log in logs)

    def test_open_test_file_ok_multline(self):
        parser = LogParser()

        logFactory = mock()
        log = mock()
        log42 = mock()
        when(log).get_date().thenReturn("2010-02-25")
        when(log).get_priority().thenReturn(5)
        when(log).get_message().thenReturn("error in database")
        when(log42).get_date().thenReturn("2010-02-42")
        when(log42).get_priority().thenReturn(42)
        when(log42).get_message().thenReturn("error in HAL9000")
        when(logFactory).create_log("2010-02-25", 5, "error in database").thenReturn(log)
        when(logFactory).create_log("2010-02-42", 42, "error in HAL9000").thenReturn(log42)

        parser.set_log_factory(logFactory)
        parser.set_text_io(StringIO("2010-02-25, 5, error in database\n2010-02-42, 42, error in HAL9000\n"))

        logs = parser.get_logs()

        self.assertEqual(2, len(logs))
        self.assertTrue(log in logs)
        self.assertTrue(log42 in logs)

    def test_text_io_est_null_renvoie_erreur(self):
        parser = LogParser()
        parser.set_log_factory(mock())
        with self.assertRaises(FileNotOpenException):
            logs = parser.get_logs()


    def test_log_factory_est_null_renvoie_erreur(self):
        parser = LogParser()
        parser.set_text_io(mock())
        with self.assertRaises(NoLogFactoryException):
            logs = parser.get_logs()
