"""Tests for Lab 1 Question 3"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q3 import (
    income_tax_fed,
    income_tax_ca,
    income_tax_ma,
    income_tax_ny,
    calculate_income_tax
)

class TestIncomeTaxFed(unittest.TestCase):
    """
    Unit tests for income_tax_fed function at zero
    """
    def test_fed_first_threshold(self)-> None:
        """Test income_tax_fed with $10,000 an income within first threshold"""
        self.assertAlmostEqual(income_tax_fed(10000),1000.0, places = 2)
        
    def test_fed_exactly_at_threshold(self)-> None:
        """ Tests income_tax_fed with $11,600 an income at exact threshold"""
        self.assertAlmostEqual(income_tax_fed(11600),1160.0, places = 2)
        
    def test_fed_multiple_thresholds(self)-> None:
        """Tests income_tax_fed with $50,000 an income at after multiple threshold"""
        self.assertAlmostEqual(income_tax_fed(50000),6053.0, places = 3)
        
    def test_fed_high_income(self)-> None:
        """Tests income_tax_fed with $500,000 a high income"""
        self.assertAlmostEqual(income_tax_fed(500000),145374.75, places = 2)
    
    def test_fed_zero_income(self) -> None:
        """Tests income_tax_fed with $0 income"""
        self.assertAlmostEqual(income_tax_fed(0), 0.0, places=2)

class TestIncomeTaxCA(unittest.TestCase):
    def test_ca_first_threshold(self)-> None:
        """Test income_tax_ca with $9,000 an income within first threshold"""
        self.assertAlmostEqual(income_tax_ca(9000),90.0, places = 2)
 
    def test_ca_exactly_at_threshold(self)-> None:
         """ Tests income_tax_ca with $10,756 an income at exact threshold"""
         self.assertAlmostEqual(income_tax_ca(10756),107.56, places = 2)
     
    def test_ca_multiple_brackets(self)-> None:
        """Tests income_tax_ca with $60,000 an income at after multiple threshold"""
        self.assertAlmostEqual(income_tax_ca(60000),2260.24, places = 2)
 
    def test_ca_high_income(self)-> None:
        """Tests income_tax_ca with $400,000 a high income"""
        self.assertAlmostEqual(income_tax_ca(400000), 34135.77, places=2)

    def test_ca_zero_income(self) -> None:
        """Tests income_tax_ca with $0 income"""
        self.assertAlmostEqual(income_tax_ca(0), 0.0, places=2)

class TestIncomeTaxMA(unittest.TestCase):
    def test_ma_low_income(self)-> None:
        """testing income_tax_ma with low income"""
        self.assertAlmostEqual(income_tax_ma(20000),1000.0, places = 2)
        
    def test_ma_medium_income(self)-> None:
         """testing income_tax_ma with medium income"""
         self.assertAlmostEqual(income_tax_ma(50000),2500.0, places = 2)

    def test_ma_high_income(self)-> None:
         """testing income_tax_ma with high income"""
         self.assertAlmostEqual(income_tax_ma(100000),5000.0, places = 2)
    
    def test_ma_zero_income(self) -> None:
        """Testing income_tax_ma with zero income"""
        self.assertAlmostEqual(income_tax_ma(0), 0.0, places=2)

class TestIncomeTaxNY(unittest.TestCase):
    def test_ny_first_threshold(self)-> None:
         """Test income_tax_ny with $7,000 an income within first threshold"""
         self.assertAlmostEqual(income_tax_ny(7000),280.0, places = 2)
        
    def test_ny_exactly_at_threshold(self)-> None:
         """ Tests income_tax_ny with $8500 an income at exact threshold"""
         self.assertAlmostEqual(income_tax_ny(8500),340.0, places = 2)

    def test_ny_multiple_throsholds(self)-> None:
         """Tests income_tax_ny with 100,000 an income at after multiple threshold"""
         self.assertAlmostEqual(income_tax_ny(100000), 5432.0, places=1)
        
    def test_ny_high_income(self)-> None:
        """Tests income_tax_ny with $6,000,000 a high income"""
        self.assertAlmostEqual(income_tax_ny(60000), 600 + (60000 - 13900) * 0.055)
    
    def test_ny_zero_income(self) -> None:
        """Tests income_tax_ny with $0 income"""
        self.assertAlmostEqual(income_tax_ny(0), 0.0, places=2)

class TestCalculateIncomeTax(unittest.TestCase):
    """ Unit tests for calculate_income_tax function"""

    @patch('builtins.input', side_effect=['NY', '50000'])
    @patch('builtins.print')
    def test_calculate_ny_tax(self, mock_print: Mock, mock_input: Mock)-> None:
        """Test calculate_income_tax with NY state and $50,000 income"""
        calculate_income_tax()
        tax = income_tax_ny(50000)
        after_tax = 50000 - tax
        self.assertTrue(mock_print.called)
        output = str(mock_print.call_args[0][0])
        self.assertTrue('50000' in output or '50,000' in output)
        self.assertIn('income', output.lower())
        self.assertIn('tax', output.lower())

    @patch('builtins.input', side_effect=['CA', '60000'])
    @patch('builtins.print')
    def test_calculate_ca_tax(self, mock_print: Mock, mock_input: Mock)-> None:
        """Test calculate_income_tax with CA state and $60,000 income"""
        calculate_income_tax()
        tax = income_tax_ca(60000)
        after_tax = 60000 - tax
        self.assertTrue(mock_print.called)
        output = str(mock_print.call_args[0][0])
        self.assertTrue('60000' in output or '60,000' in output)
        self.assertIn('income', output.lower())
        self.assertIn('tax', output.lower()) 
        
    @patch('builtins.input', side_effect=['MA', '40000'])
    @patch('builtins.print')
    def test_calculate_ma_tax(self, mock_print: Mock, mock_input: Mock)-> None:
        """Test calculate_income_tax with MA state and $40,000 income"""
        calculate_income_tax()
        tax = income_tax_ma(40000)
        after_tax = 40000 - tax
        self.assertTrue(mock_print.called)
        output = str(mock_print.call_args[0][0])
        self.assertTrue('40000' in output or '40,000' in output)
        self.assertIn('income', output.lower())
        self.assertIn('tax', output.lower())
    
    @patch('builtins.input', side_effect=['NJ', 'CA', '30000'])
    @patch('builtins.print')
    def test_invalid_state_then_valid(self, mock_print: Mock, mock_input: Mock)-> None:
        """Test calculate_income_tax with invalid state first, then valid"""
        calculate_income_tax()
        self.assertGreaterEqual(mock_print.call_count, 2)
        total_calls = [str(call[0][0]) for call in mock_print.call_args_list]
        error_raised = any('not a valid input' in call or 'NJ' in call 
                         for call in total_calls[:-1])  
        self.assertTrue(error_raised, "error message for invalid state input")
        output = total_calls[-1]
        self.assertIn('30000', output)
    
    @patch('builtins.input', side_effect=['NY', 'not_a_number', '25000'])
    @patch('builtins.print')
    def test_invalid_income_then_valid(self, mock_print: Mock, mock_input: Mock)-> None:
        """Test calculate_income_tax with invalid income first, then valid"""
        calculate_income_tax()
        self.assertGreaterEqual(mock_print.call_count, 2)
        total_calls = [str(call[0][0]) for call in mock_print.call_args_list]
        error_raised = any('not a number' in call or 'not a valid input' in call 
                        for call in total_calls[:-1])
        self.assertTrue(error_raised, "error message for invalid income input")
        output = total_calls[-1]
        self.assertIn('25000', output)

if __name__ == '__main__':
    unittest.main()