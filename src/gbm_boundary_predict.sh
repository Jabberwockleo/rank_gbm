#!/bin/bash
./lightgbm config=predict_boundary.conf
python evaluate_result.py "boundary.gbm_data"
