#!/usr/bin/env python3
import unittest
import h5py
from TestDataSearch import *

testgauss=TestDataSearch('DataLegendre.h5')
testgauss.test_search_x()
testgauss.test_search_w()
