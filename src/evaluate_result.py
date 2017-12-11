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
import operator
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    feature_fn = sys.argv[1]
    count_fn = feature_fn + ".query"
    predict_fn = feature_fn + ".predict"
    eval_fn = feature_fn + ".eval"

    feature_fi = open(feature_fn, "r")
    count_fi = open(count_fn, "r")
    predict_fi = open(predict_fn, "r")
    eval_fo = open(eval_fn, "w")

    feature_lines = feature_fi.readlines()
    for i in xrange(len(feature_lines)):
        feature_lines[i] = feature_lines[i].rstrip()
    count_lines = count_fi.readlines()
    for i in xrange(len(count_lines)):
        count_lines[i] = count_lines[i].rstrip()
    predict_lines = predict_fi.readlines()
    for i in xrange(len(predict_lines)):
        predict_lines[i] = predict_lines[i].rstrip()

    fp_count = 0
    query_count = len(count_lines)
    query_doc_idx = 0
    for cnt_idx in xrange(len(count_lines)):
        qid = "qid:" + str(cnt_idx)
        cnt = int(count_lines[cnt_idx])
        features = feature_lines[query_doc_idx: query_doc_idx + cnt]
        predicts = predict_lines[query_doc_idx: query_doc_idx + cnt]
        result = "falsepositive"
        feature_sort = []
        predict_sort = []
        for i in xrange(cnt):
            label = float(features[i].split(" ")[0])
            predict = float(predicts[i])
            feature_sort.append({"idx": i, "val": label})
            predict_sort.append({"idx": i, "val": predict})

        feature_sort = sorted(feature_sort, key=operator.itemgetter("val"), reverse=True)
        predict_sort = sorted(predict_sort, key=operator.itemgetter("val"), reverse=True)
        if feature_sort[0]["idx"] == predict_sort[0]["idx"]:
            result = "true_positive"
        else:
            fp_count += 1
        for i in xrange(cnt):
            eval_fo.write("%s\t%s\t%s\t%s\n" % (result, predicts[i], features[i], qid))
        query_doc_idx += cnt
    print "=== RESULT ==="
    print "precision: %d/%d = %f" % (query_count - fp_count, query_count,
        1.0 * (query_count - fp_count) / query_count)

