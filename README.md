# Wildlife Response Post-Fire

[![DOI](https://zenodo.org/badge/965872045.svg)](https://doi.org/10.5281/zenodo.15208532)

# Data Sources - 
MTBS (Monitoring Trends in Burn Severity) is an interagency program whose goal is to consistently map the burn severity and extent of large fires across all lands of the United States from 1984 to present. This includes all fires 1,000 acres or greater in the western United States and 500 acres or greater in the eastern Unites States. The extent of coverage includes the continental U.S., Alaska, Hawaii and Puerto Rico.

I will be using this to map the Mullen Fire, which took place in 2020 between September 17 to October 20.

To determine the boundary of the Mullen Fire, MTBS delineates on-screen interpretation of the reflectance imagery and the NBR (Normalized Burn Ratio), dNBR (Differenced Normalized Burn Ratio) and RdNBR (Relativized difference Normalized Burn Ratio) images. The mapping analyst digitizes a perimeter to include any detectable fire area derived from these images. Clouds, cloud shadows, snow or other anomalies intersecting the fire area are also delineated and used to generate a mask later in the workflow. To ensure consistency and high spatial precision, digitization is performed at on-screen display scales between 1:24000 and 1:50000.
https://www.mtbs.gov/mapping-methods

Source #2 CSV data file provided by our partner. 
This file contains location data for all three fires but I will filter it down to the Mullen Fire and then break it out by data collection point (there are 50 points in the Mullen fire area) area and number of total bats per area over time ( I will first have to figure out how to determine the total number of bats given that there is a high frequency pass and a low frequency pass that counts the number of bats). Time frame is from 5/27/2024 to 08/19/2024.
Burn severity is also recorded on a scale of 1-4. 

