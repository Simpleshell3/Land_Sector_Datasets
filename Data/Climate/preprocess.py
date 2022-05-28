pip install gdal-utils
wget https://esdac.jrc.ec.europa.eu/projects/RenewableEnergy/Data/Climate_Zone.zip
unzip Climate_Zone.zip
gdalwarp -s_srs EPSG:4326 -t_srs EPSG:4326 -dstnodata 255.0 -tr 0.05 0.05 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff "CLIMATE_ZONE.rst" "IPCC_ClimateZoneMap.tif"
