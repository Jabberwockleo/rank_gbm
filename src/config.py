#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2017 Wan Li. All Rights Reserved
#
########################################################################

"""
File: config.py
Author: Wan Li
Date: 2017/11/27 10:41:01
"""

USE_TOY_DATA = True
IS_NONLINEAR_MODEL = True
FEATURE_NUM = 2
if USE_TOY_DATA == True:
    TRAIN_DATA = "./toy.train"
    TEST_DATA = "./toy.test"
MOCK_QUERY_DOC_COUNT = 4
