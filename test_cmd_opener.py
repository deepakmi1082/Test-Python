import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from cmd_opener import open_cmd

class TestCmdOpener(unittest.TestCase):

    @patch('subprocess.Popen')
    @patch('os.getcwd')
    def test_open_cmd_success(self, mock_getcwd, mock_popen):
        mock_getcwd.return_value = '/fake/path'
        mock_popen.return_value = MagicMock()
        
        # Should not raise exception
        try:
            open_cmd()
        except SystemExit:
            self.fail("open_cmd raised SystemExit unexpectedly")
        
        # Check that Popen was called twice (as per the code)
        self.assertEqual(mock_popen.call_count, 2)
        mock_popen.assert_any_call('cmd.exe', cwd='/fake/path', shell=True)
        mock_popen.assert_any_call('cmd.exe', cwd='/fake/path')

    @patch('subprocess.Popen')
    @patch('os.getcwd')
    def test_open_cmd_failure(self, mock_getcwd, mock_popen):
        mock_getcwd.return_value = '/fake/path'
        mock_popen.side_effect = Exception("Mock error")
        
        with self.assertRaises(SystemExit):
            open_cmd()

if __name__ == '__main__':
    unittest.main()