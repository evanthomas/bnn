#!/bin/bash


/home/evan/.virtualenvs/tf37/bin/python ./train.py \
    --run r12 \
    --steps 300 \
    --train-steps 50 \
    --train-image-dir ../beedata/train/ \
    --test-image-dir ../beedata/test/ \
    --label-dir ../beedata/labels/ \
    --height 768 --width 1024


