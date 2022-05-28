import sys
import subprocess
import wget
import zipfile
import gdal

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'<gdal-utils>'])

wget.download(https://esdac.jrc.ec.europa.eu/projects/RenewableEnergy/Data/Climate_Zone.zip)


zipfile.Zipfile(Climate_Zone.zip).extractall()

zipfile.Zipfile(Climate_Zone.zip).close()

gdalwarp -s_srs EPSG:4326 -t_srs EPSG:4326 -dstnodata 255.0 -tr 0.05 0.05 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff "CLIMATE_ZONE.rst" "IPCC_ClimateZoneMap.tif"
