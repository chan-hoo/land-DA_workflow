#!/bin/bash
#SBATCH -o out.ctest

set -eux

source ../../versions/build.ver_hera
module use ../../modulefiles
module load build_hera_intel

ctest

wait

echo "ctest is done"
