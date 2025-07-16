# test_ledgerforge.py
"""
Tests for LedgerForge module.
"""

import unittest
from ledgerforge import LedgerForge

class TestLedgerForge(unittest.TestCase):
    """Test cases for LedgerForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerForge()
        self.assertIsInstance(instance, LedgerForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
