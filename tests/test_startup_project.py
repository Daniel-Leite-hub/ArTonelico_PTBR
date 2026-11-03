import unittest
from pathlib import Path
from unittest.mock import patch
from main import startup_project

class StartupTests(unittest.TestCase):
    def test_explicit_project_wins(self):
        self.assertEqual(startup_project(['chosen.atproj']),Path('chosen.atproj'))

    def test_adjacent_adapted_project_is_selected(self):
        with patch('main.sys.frozen',True,create=True),patch('main.sys.executable','C:/delivery/Studio.exe'),patch.object(Path,'is_file',return_value=True):
            self.assertEqual(startup_project([]),Path('C:/delivery/ArTonelico_PTBR_adaptado_108_20260926.atproj'))

    def test_missing_project_keeps_empty_startup(self):
        with patch.object(Path,'is_file',return_value=False):
            self.assertIsNone(startup_project([]))
