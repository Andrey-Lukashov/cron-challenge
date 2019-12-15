import unittest
import functions
import os


class FunctionsTest(unittest.TestCase):
    def test_log_can_write(self):
        functions.log('test.log', 'message')
        self.assertEqual(os.path.isfile('test.log'), True)

    def test_valid_time_format(self):
        time = "21:15"
        self.assertEqual(functions.validate_time_format(time), True)

        time = "18:15"
        self.assertEqual(functions.validate_time_format(time), True)

        time = "07:45"
        self.assertEqual(functions.validate_time_format(time), True)

    def test_invalid_time_format(self):
        time = "oogabooga"
        self.assertEqual(functions.validate_time_format(time), False)

        time = "222:333"
        self.assertEqual(functions.validate_time_format(time), False)

    def test_correct_config_format(self):
        line = "45 8 /bin/run_me_daily"
        self.assertEqual(functions.check_config_format(line), True)

        line = "11 * /bin/run_me_hourly"
        self.assertEqual(functions.check_config_format(line), True)

        line = "* * /bin/run_me_every_minute"
        self.assertEqual(functions.check_config_format(line), True)

        line = "* 23 /bin/run_me_sixty_time"
        self.assertEqual(functions.check_config_format(line), True)

    def test_incorrect_config_format(self):
        line = ""
        self.assertEqual(functions.check_config_format(line), False)

        line = "45 whatever /bin/whatever_running"
        self.assertEqual(functions.check_config_format(line), False)

        line = "* what"
        self.assertEqual(functions.check_config_format(line), False)

        line = "*"
        self.assertEqual(functions.check_config_format(line), False)

        line = "what * /bin/yoyoyo"
        self.assertEqual(functions.check_config_format(line), False)

    def test_correct_transform_config_time(self):
        current_time = "20:15"

        hours = "20"
        minutes = "*"
        command = "/bin/run_me_daily"
        self.assertEqual(functions.transform_config_time(current_time, hours, minutes, command), "20:15 today - /bin/run_me_daily")

        hours = "19"
        minutes = "*"
        command = "/bin/run_me_daily"
        self.assertEqual(functions.transform_config_time(current_time, hours, minutes, command), "19:00 tomorrow - /bin/run_me_daily")

        hours = "21"
        minutes = "15"
        command = "/bin/run_me_daily"
        self.assertEqual(functions.transform_config_time(current_time, hours, minutes, command), "21:15 today - /bin/run_me_daily")


class ApplicationTest(unittest.TestCase):
    def test_missing_time(self):
        self.assertEqual(True, False)

    def test_invalid_time(self):
        self.assertEqual(True, False)

    def test_missing_config(self):
        self.assertEqual(True, False)

    def test_invalid_config(self):
        self.assertEqual(True, False)

    def test_correct_call(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
