#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2017 Wan Li. All Rights Reserved
#
########################################################################

"""
File: convert_svm_to_gbm.py
Author: Wan Li
Date: 2017/12/11 14:42:13
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    svm_fn = sys.argv[1]
    gbm_feature_fn = svm_fn + ".gbm_data"
    gbm_qd_count_fn = gbm_feature_fn + ".query"

    svm_fi = open(svm_fn, "r")
    gbm_feature_fo = open(gbm_feature_fn, "w")
    gbm_qd_count_fo = open(gbm_qd_count_fn, "w")

    last_qid = ""
    accumulate_query_count = 0
    for line in svm_fi:
        line = line.rstrip()
        elems = line.split(" ")
        label = elems[0]
        qid = elems[1]
        feature_vec = elems[2:]
        gbm_feature_fo.write("%s" % (label))
        for fea in feature_vec:
            gbm_feature_fo.write(" %s" % (fea))
        gbm_feature_fo.write("\n")
        if qid == last_qid:
            accumulate_query_count += 1
        else:
            if last_qid != "":
                gbm_qd_count_fo.write("%d\n" % (accumulate_query_count))
            last_qid = qid
            accumulate_query_count = 1
    gbm_qd_count_fo.write("%d\n" % (accumulate_query_count))
