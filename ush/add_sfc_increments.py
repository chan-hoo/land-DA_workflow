#!/usr/bin/env python3

###################################################################### CHJ #####
## Name		: add_sfc_increments.py
## Usage	: add increments of snow depth to sfc_data files
## Input files  : sfc_data.tile#.nc and xainc.sfc_data.tile#.nc
## NOAA/EPIC
## History ===============================
## V000: 2024/06/15: Chan-Hoo Jeon : Preliminary version
###################################################################### CHJ #####

import os
import sys
import argparse
import numpy as np
import xarray as xr

# Main part (will be called at the end) ============================= CHJ =====
def add_sfc_increments(path_data,fn_sfc_base,fn_inc_base):
# =================================================================== CHJ =====

    # Number of tiles
    num_tiles=6
    # Number of decimal places to round to
    num_decimals=12
    # variable name to be extraced
    sfc_var_nm='snwdph'

    for it in range(num_tiles):
        itp=it+1

        # open sfc_data file
        fn_sfc=fn_sfc_base+str(itp)+'.nc'
        print(' ===== sfc_data files: '+fn_sfc+' ========================')
        fp_sfc=os.path.join(path_data,fn_sfc)
        try: sfc=xr.open_dataset(fp_sfc)
        except: raise Exception('Could NOT find the file',fp_sfc)
        #print(sfc)
        # Extract snow depth
        sfc_var_orig=np.ma.masked_invalid(sfc[sfc_var_nm].data)
        sfc_var_orig=np.round(sfc_var_orig,decimals=num_decimals)
        sfc_var=np.squeeze(sfc_var_orig,axis=0)
        (nx_sfc,ny_sfc)=sfc_var.shape

        # open increment file
        fn_inc=fn_inc_base+str(itp)+'.nc'
        print(' ===== increment files: '+fn_inc+' ========================')
        fp_inc=os.path.join(path_data,fn_inc)
        try: inc=xr.open_dataset(fp_inc)
        except: raise Exception('Could NOT find the file',fp_inc)
        #print(inc)
        # Extract snow depth
        sfc_inc_orig=np.ma.masked_invalid(inc[sfc_var_nm].data)
        sfc_inc_orig=np.round(sfc_inc_orig,decimals=num_decimals)
        sfc_inc=np.squeeze(sfc_inc_orig,axis=(0,1))
        (nx_inc,ny_inc)=sfc_inc.shape
        
        # Check array sizes
        if nx_sfc != nx_inc or ny_sfc != ny_inc:
            sys.exit('FATAL ERROR: array sizes are NOT the same !!!')

        # new values
        sfc_var_new=sfc_var+sfc_inc
        sfc_var_new=np.round(sfc_var_new,decimals=num_decimals)

        # check new values
        sfc_var_chk=sfc_var_new-sfc_inc
        sfc_var_chk=np.round(sfc_var_chk,decimals=num_decimals)
        sfc_diff=np.absolute(sfc_var_chk-sfc_var)
        sfc_diff_max=np.max(sfc_diff)
        print("sfc_data diff check: max=",sfc_diff_max)
        err_tol=1e-12
        if sfc_diff_max > err_tol:
            sys.exit('FATAL ERROR: new values are NOT correct !!!')

        sfc_var_orig_new=sfc_var_orig
        print("original sfc max=",np.max(sfc_var_orig_new))
        sfc_var_orig_new[0,:,:]=sfc_var_new
        print("new sfc max=",np.max(sfc_var_orig_new))

        # Replace sfc values with new ones
        sfc.variables[sfc_var_nm].values=sfc_var_orig_new
        sfc.to_netcdf(fn_sfc_base+str(itp)+'_new.nc')

    return True


def parse_args(argv):
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Add increments to sfc_data files."
    )

    parser.add_argument("-p",
        "--path_data", 
        dest="path_data", 
        required=True, 
        help="Path to input data files.")

    parser.add_argument("-s",
        "--fn_sfc_base",
        dest="fn_sfc_base",
        required=True,
        help="Base name of sfc_data files.")

    parser.add_argument("-i",
        "--fn_inc_base",
        dest="fn_inc_base",
        required=True,
        help="Base name of increment files.")

    return parser.parse_args(argv)



# Main call ========================================================= CHJ =====
if __name__=='__main__':
    args = parse_args(sys.argv[1:])
    add_sfc_increments(
        path_data=args.path_data,
        fn_sfc_base=args.fn_sfc_base,
        fn_inc_base=args.fn_inc_base       
    )   
