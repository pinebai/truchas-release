#!/usr/bin/env python

import sys
import os

import numpy

import Truchas
import TruchasTest

class DS6(TruchasTest.GoldenTestCase):

  test_name = 'ds6'
  num_procs = 4 # with a parallel executable
  
  def test_early_cycle_number(self):
    '''DS6: checking the final cycle number'''
    test_series = self.test_output.get_simulation().find_series(id=2)
    gold_series = self.gold_output.get_simulation().find_series(id=2)
    self.assertTrue(test_series.cycle == gold_series.cycle)
  
  def test_final_cycle_number(self):
    '''DS6: checking the final cycle number'''
    test_series = self.test_output.get_simulation().find_series(id=3)
    gold_series = self.gold_output.get_simulation().find_series(id=3)
    self.assertTrue(test_series.cycle == gold_series.cycle)

  def test_early_temperature(self):
    '''DS6: verifying the temperature field at early time'''
    tol = 1.0e-10
    test = self.test_output.get_simulation().find_series(id=2).get_data('Z_TEMP')
    gold = self.gold_output.get_simulation().find_series(id=2).get_data('Z_TEMP')
    error = max(abs(test-gold)/gold)
    print 'early temp max rel error=', error, '(tol=', tol, ')'
    self.assertTrue(error <= tol)

  def test_final_temperature(self):
    '''DS6: verifying the temperature field at final time'''
    tol = 1.0e-10
    test = self.test_output.get_simulation().find_series(id=3).get_data('Z_TEMP')
    gold = self.gold_output.get_simulation().find_series(id=3).get_data('Z_TEMP')
    error = max(abs(test-gold)/gold)
    print 'final temp max rel error=', error, '(tol=', tol, ')'
    self.assertTrue(error <= tol)

  def test_early_phi1(self):
    '''DS6: verifying the phi1 field at early time'''

    tol = 1.0e-10
    C    = self.test_output.get_simulation().find_series(id=2).get_data('phi1')
    Cref = self.gold_output.get_simulation().find_series(id=2).get_data('phi1')
    error = max(abs(C-Cref)/Cref)
    print 'early phi1 max rel error=', error, '(tol=', tol, ')'
    self.assertTrue(error <= tol)

  def test_final_phi1(self):
    '''DS6: verifying the phi1 field at final time'''
    tol = 1.0e-10
    C    = self.test_output.get_simulation().find_series(id=3).get_data('phi1')
    Cref = self.gold_output.get_simulation().find_series(id=3).get_data('phi1')
    error = max(abs(C-Cref)/Cref)
    print 'final phi1 max rel error=', error, '(tol=', tol, ')'
    self.assertTrue(error <= tol)

  def test_early_phi2(self):
    '''DS6: verifying the phi2 field at early time'''

    tol = 1.0e-10
    C    = self.test_output.get_simulation().find_series(id=2).get_data('phi2')
    Cref = self.gold_output.get_simulation().find_series(id=2).get_data('phi2')
    error = max(abs(C-Cref)/Cref)
    print 'early phi2 max rel error=', error, '(tol=', tol, ')'
    self.assertTrue(error <= tol)

  def test_final_phi2(self):
    '''DS6: verifying the phi2 field at final time'''
    tol = 1.0e-10
    C    = self.test_output.get_simulation().find_series(id=3).get_data('phi2')
    Cref = self.gold_output.get_simulation().find_series(id=3).get_data('phi2')
    error = max(abs(C-Cref)/Cref)
    print 'final phi2 max rel error=', error, '(tol=', tol, ')'
    self.assertTrue(error <= tol)

if __name__ == '__main__':
  import unittest
  unittest.main()

