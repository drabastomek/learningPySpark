#!/bin/bash
unset PYSPARK_DRIVER_PYTHON
spark-submit $*
export PYSPARK_DRIVER_PYTHON=jupyter