#!/usr/bin/env python3
import unittest
import h5py

class TestDataSearch(unittest.TestCase):
    def __init__(self,file_name):
        self.hf=h5py.File(file_name,'r')

    def test_search_x(self):
        target_name='abscissa_x'
        for key in self.hf.keys():
            names=list(self.hf[key].keys())
            search_result=target_name in names
            if search_result==True:
                print("abscissa_x exists")
                break
        self.assertTrue(search_result,"abscissa_x can't be found")


    def test_search_w(self):
        target_name='weight_w'
        for key in self.hf.keys():
            names=list(self.hf[key].keys())
            search_result=target_name in names
            if search_result==True:
                print("weight_w exists")
                break
        self.assertTrue(search_result,"weight_w can't be found")
