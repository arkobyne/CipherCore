# test_ciphercore.py
"""
Tests for CipherCore module.
"""

import unittest
from ciphercore import CipherCore

class TestCipherCore(unittest.TestCase):
    """Test cases for CipherCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CipherCore()
        self.assertIsInstance(instance, CipherCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CipherCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
