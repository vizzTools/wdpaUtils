from datetime import datetime, date
import os
import zipfile as zf
import requests
import geopandas as gpd
class ProtectedAreas:
    def __init__(self, download_path='./data', version='WDPA_Feb2021_Public_shp'):
        
        self.created_at = self.getDate()
        self.version = version
        self.download_path = download_path
        self.url = f'https://d1gam3xoknrgr2.cloudfront.net/current/{version}.zip'
    
    def getDate(self, date_format= '%Y-%m-%d %H:%M:%S'): 
        pa_date = datetime.now()
        return date.strftime(pa_date, '%Y-%m-%d %H:%M:%S')

    def fetchTable(self, download_path=None, filename=None):
        """ Fetches a table from https://d1gam3xoknrgr2.cloudfront.net/current/ """

        if download_path: self.download_path = download_path
        if not filename:
            filename = f"wdpa_download_{self.created_at.split(' ')[0]}"

        ## remove zip if its there for now
        filename = filename.replace('.zip','')

        ## check if downloads exist
        files = [file for file in os.listdir(download_path) if filename in file]

        if len(files) > 0: save_to += f'_{len(files)}'

        filename += '.zip' 
        save_to = download_path + f'/{filename}'
        self.zipfile = save_to 

        try:
            print('Starting download...')
            
            ## Make request and save zip file in save_to
            ## fetch function here self.downloadUrl()

            print(f"Download complete! Saving to: {save_to}")
            
            ## Save zipfile location to self
        except:
            print("Failed to download")
            self.zipfile = None

    def selectTable(self, zipfile=None)
        """Selects table from downloaded contents"""
        
        # https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract
        if not zipfile: zipfile = self.zipfile

        archive = zipfile.ZipFile(zipfile, 'r')
        print({i+1: file for i,file in enumerate(archive.namelist())})

        ## prompt to select index i
        ## return input i

    def downloadUrl(self, save_path=None, chunk_size=128):
        ## this should live in utils

        ## make request by streaming data to local path 
        destination = save_path or self.zipfile

        r = requests.get(self.url, stream=True)
        with open(destination, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def populateTable(self, inplace=False):
        """ Fetches WDPA shapefile from Protected Planet. """
        
        ## if it doesnt exist, fetched and saves zipfile locally unzip file
        
        ## prompt which version of the table to unpck 
        ## delete the others (otional)

        ## load data from path and convert to gdf

        ## clean and unpack metadata

        ## update self 

        # self.table = gdf
        # self.metadata ## metadata class?
        
        # return self if inplace else None
