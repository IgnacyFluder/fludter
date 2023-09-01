#!/bin/bash
git clone --depth 1 https://github.com/deepfakes/faceswap.git
cd faceswap
# Change the following line to your python3 path if it is not /usr/bin/python3
python3 setup.py