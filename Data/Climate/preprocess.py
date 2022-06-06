import sys
import subprocess
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])

wget.download('https://esdac.jrc.ec.europa.eu/projects/RenewableEnergy/Data/Climate_Zone.zip')


zipfile.ZipFile('Climate_Zone.zip').extractall()

zipfile.ZipFile('Climate_Zone.zip').close()

a_file = open("preprocess.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[25] = date_string
a_file = open("preprocess.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2022-06-06 08-47-39.499369#gdalwarp -s_srs EPSG:4326 -t_srs EPSG:4326 -dstnodata 255.0 -tr 0.05 0.05 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff "CLIMATE_ZONE.rst" "IPCC_ClimateZoneMap.tif"
