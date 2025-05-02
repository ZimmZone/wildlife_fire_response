# Wildlife Response Post-Fire

[![DOI](https://zenodo.org/badge/965872045.svg)](https://doi.org/10.5281/zenodo.15208532)

# Special Data
 - Bat and site data located in the 00_Data file in the repository
 - MTBS Data that can be found at: https://www.mtbs.gov/
 - STRM Data that can be found at: https://www.earthdata.nasa.gov/data/instruments/srtm

This code is designed to combine several data sets in order to understand the return rate of bats post-fire and what factors impact this rate of return. This analysis looks specifically at the Mullen Fire burn area in Colorado and Wyoming. This fire occured in 2020, approximately 28 miles West of Laramie, WY. It began on September 17th, 2020, destroyed 66 structures and burned 176,878 acres.


![Mullen Fire Burn Area Map](image.png)

The goal of the project is to create a variety of visuals that demonstrate the:
- boundary of the Mullen Fire
- location of acoustic monitors
- bat occupancy
- elevation
- burn severity

** Notebooks

The project is broken into one folder and several notebooks:

    Folder 00 - Data (contains all the data about and from the observation sites)
    
    Notebook 01 - Introduction to the project, data types, and additional information 
    
    Notebook 02 - Code determining the boundary of the Mullen fire (I did my best to make this code reproducable)
    
    Notebook 03 - Import - Notebook contains data wrangling and has information on how the data was processes to have the same format across columns and then combined to create a .gdf. 
    
    Notebook 04 - (future) Will have visuals showing the elevation within the boundaries of the Mullen Fire
    
    Notebook 05 - (future) Will show total bat occupancy at a single point in time, then bat occupancy divided into hi and lo frequency calls, then bat occupancy by species. 
    
    Notebook 06 - (future) Will contain an interactive map showing the changes of bat occupany over time and by species should be have sufficient data.
    
    Notebook 07 - Analysis discussing what has been learned from this data and potential further reserach steps. 

