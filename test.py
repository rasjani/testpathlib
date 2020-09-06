from unittest import TestCase
from unittest import main as run_tests
from pathlib import Path
import os
import subprocess


class TestLibTest(TestCase):
    def test_pathlib_in_subprocess_with_shell(self):
        path_like_object = Path("C:/Temp")
        res = subprocess.run(["echo", path_like_object], shell=True)

    def test_pathlib_in_subprocess_without_shell(self):
        path_like_object = Path("C:/Temp")
        res = subprocess.run(["echo", path_like_object], shell=False)

if __name__ == '__main__':
    run_tests(failfast=False, buffer=False, catchbreak=False)
