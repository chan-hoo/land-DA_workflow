# UFS offline Land Data Assimilation System

The Unified Forecast System (UFS) is a community-based, coupled, comprehensive Earth modeling system. It is designed to be the source system for NOAA's operational numerical weather prediction applications while enabling research, development, and contribution opportunities for the broader Weather Enterprise. For more information about the UFS, visit the UFS Portal at https://ufscommunity.org/.

The UFS includes [multiple applications](https://ufscommunity.org/science/aboutapps/) that support different forecast durations and spatial domains. This repository hosts the source code for the UFS Land Data Assimilation (DA) System. Land DA is an offline version of the Noah Multi-Physics (Noah-MP) land surface model (LSM) used in the UFS Weather Model (WM). Its data assimilation framework uses the Joint Effort for Data assimilation Integration (JEDI) software stack, which includes the Object-Oriented Prediction System (OOPS) for the data assimilation algorithm, the Interface for Observation Data Access (IODA) for observation formatting and processing, and the Unified Forward Operator (UFO) for comparing model forecasts and observations. 

The offline Noah-MP LSM is a standalone, uncoupled model used to execute land surface simulations. In this traditional uncoupled mode, near-surface atmospheric forcing data is required as input forcing. This LSM simulates soil moisture (both liquid and frozen), soil temperature, skin temperature, snow depth, snow water equivalent (SWE), snow density, canopy water content, and the energy flux and water flux terms of the surface energy balance and surface water balance. Its data assimilation framework applies the Local Ensemble Transform Kalman Filter-Optimal Interpolation (LETKF-OI) algorithm to combine the state-dependent background error derived from an ensemble forecast with the observations and their corresponding uncertainties to produce an analysis ensemble (Hunt et al., 2007).

The Noah-MP LSM has evolved through community efforts to pursue and refine a modern-era LSM suitable for use in the National Centers for Environmental Prediction (NCEP) operational weather and climate prediction models. This collaborative effort continues with participation from entities such as NCAR, NCEP, NASA, and university groups. The development branch of the Land DA System is continually evolving as the system undergoes open development. The latest Land DA release (v1.0.0) represents a snapshot of this continuously evolving system. 

The Land DA System User's Guide associated with the development branch is at: https://land-da.readthedocs.io/en/develop/, while the guide specific to the Land DA v1.0.0 release can be found at: https://land-da.readthedocs.io/en/release-public-v1.0.0/. Users may download data for use with the most recent release from the [Land DA data bucket](https://noaa-ufs-land-da-pds.s3.amazonaws.com/index.html#current_land_da_release_data/). The [Land DA Docker Hub](https://hub.docker.com/r/noaaepic/ubuntu20.04-intel-landda) hosts Land DA containers. These containers package the Land DA System together with all its software dependencies for an easier experience building and running Land DA.

For any publications based on work with the UFS Offline Land Data Assimilation System, please include a citation to the DOI below:

UFS Development Team. (2023, March 6). Unified Forecast System (UFS) Land Data Assimilation (DA) System (Version v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.7675721

