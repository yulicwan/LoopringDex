# test_loopringdex.py
"""
Tests for LoopringDex module.
"""

import unittest
from loopringdex import LoopringDex

class TestLoopringDex(unittest.TestCase):
    """Test cases for LoopringDex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LoopringDex()
        self.assertIsInstance(instance, LoopringDex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LoopringDex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
