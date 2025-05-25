import unittest
from gp_logging import gp_logging

class gp_logger_test(unittest.TestCase):

    def setUp(self):
        self.logger = gp_logging.gp_logger()


    def test_01_basic_functions(self) -> None:
        print("\nBasic functions test!")
        self.logger.log(gp_logging.gp_log_level.INFO, "Basic Test, Log_level = INFO, Color = standard")
        self.logger.log(gp_logging.gp_log_level.DEBUG, "Basic Test, Log_level = DEBUG, Color = blue")
        self.logger.log(gp_logging.gp_log_level.WARNING, "Basic Test, Log_level = WARNING, Color = yellow")
        self.logger.log(gp_logging.gp_log_level.ERROR, "Basic Test, Log_level = ERROR, Color = red")

        return

    
    def test_singleline_debug_message(self) -> None:
        print("\nAdvanced functions test!")
        self.logger.log(gp_logging.gp_log_level.DEBUG, "Test Single Line message")
        self.logger.log(gp_logging.gp_log_level.INFO, "Test\nMulti\nLine\nmessage")

        print("Test")

        return