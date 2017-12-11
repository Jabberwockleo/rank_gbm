#!/bin/bash
./lightgbm config=predict.conf
python evaluate_result.py "toy.test.gbm_data"
