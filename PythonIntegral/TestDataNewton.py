#!/usr/bin/env python3
import unittest
import h5py
from TestDataSearch import *

testnewton=TestDataSearch('DataNewtonCotes.h5')
testnewton.test_search_x()
testnewton.test_search_w()
