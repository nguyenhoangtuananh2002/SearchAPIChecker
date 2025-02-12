import requests
import csv
from datetime import datetime
import concurrent.futures
import sys

class URLSearch1Fetcher():
     URL = 'https://www.boschrexroth.com/api/content-search/dc-de-dwn-p/search.json?lang=de&num=10&q=test&getfields=Search%252Edc_fileextension.Search%252Edc_filename.Search_dc_asset_identifier.Search%252Edc_prd_grp.Search%252Edc_mediatype.Search%252Edc_filetype.Search%252Edc_title_en.Search%252Edc_subtitle_en.Search_dc_description_en.Search_dc_document_status.Search%252Edc_asset_version_identifier.Search%252Edc_subtitle_de.Search%252Edc_title_de.Search_dc_description_de'
     def __init__(self): 
          self.times = 10
          self.max_workers = 5 
          self.response = []
          self.status_total = None
          
     def _fetch_single_request(self):
        try:
            response = requests.get(url=self.URL)
            return response
        except Exception as e:
            print(f'There was an error: {e}')
            return None

     def _makerequest(self):
        try:
            with open('api_calling.csv', mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Datetime', 'URL', 'Status Code'])
                with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                    futures = [executor.submit(self._fetch_single_request) for _ in range(self.times)]
                    for i,future in enumerate(concurrent.futures.as_completed(futures)):
                        response = future.result()
                        if response.status_code == 200:
                            self.response.append(response.status_code)
                            current_time = datetime.now().strftime('%H:%M:%S')
                            writer.writerow([current_time, self.URL, response.status_code])
                            # print(f"Time: {current_time}, Status Code: {response.status_code}, URL: {self.URL}")
                        else: 
                            self.response.append(response.status_code)
                            current_time = datetime.now().strftime('%H:%M:%S')
                            writer.writerow([current_time, self.URL, response.status_code])
                            # print(f'There was a error with the status {response.status_code} when sending the request to search API at {current_time}')
                return self.response
        except Exception as e:
            print(e)
class URLSearch2Fetcher():
     URL = 'https://www.boschrexroth.com/api/content-search/dc-de-p/search.json?lang=vi&num=10&q=Test&getfields=searchdcprd_thumbnail.page_category.Search_dc_subtitle_1.Search_contenttype.Search_dc_thumbnail.description.Search_dc_subtitle_2_prd_grp.Search%252Edc_prd_grp.Search%252Edc_prd_subgrp_lv2.Search_dc_presslocation.Search_dc_pressdisplaydate.Search_dc_presslabelcontent.Search_dc_presslabeltopic.DCSext%252Ewtg_blogpicture.DCSext%252Ewtg_blogcategory.DCSext%252Ewtg_blogauthor.DCSext%252Ewtg_blogdate.Search%252Edc_fileextension.Search%252Edc_title_en.Search%252Edc_subtitle_en.Search%252Edc_subtitle_de.Search%252Edc_title_de'
     def __init__(self): 
          self.times = 10
          self.max_workers = 5 
          self.response = []
          self.status_total = None
          
     def _fetch_single_request(self):
        try:
            response = requests.get(url=self.URL)
            return response
        except Exception as e:
            print(f'There was an error: {e}')
            return None

     def _makerequest(self):
        try:
            with open('api_calling_2.csv', mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Datetime', 'URL', 'Status Code'])
                with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                    futures = [executor.submit(self._fetch_single_request) for _ in range(self.times)]
                    for i,future in enumerate(concurrent.futures.as_completed(futures)):
                        response = future.result()
                        if response.status_code == 200:
                            self.response.append(response.status_code)
                            current_time = datetime.now().strftime('%H:%M:%S')
                            writer.writerow([current_time, self.URL, response.status_code])
                            # print(f"Time: {current_time}, Status Code: {response.status_code}, URL: {self.URL}")
                        else: 
                            self.response.append(response.status_code)
                            current_time = datetime.now().strftime('%H:%M:%S')
                            writer.writerow([current_time, self.URL, response.status_code])
                            # print(f'There was a error with the status {response.status_code} when sending the request to search API at {current_time}')
                return self.response
        except Exception as e:
            print(e)


apiStatus = URLSearch1Fetcher()
status_search = apiStatus._makerequest()
print(status_search)


api1Status = URLSearch2Fetcher()
status_1_search = api1Status._makerequest()
print(status_1_search)

exit_code = 0

for status in status_search:
    if status != 200:
        exit_code = 1

for status in status_1_search:
    if status != 200:
        exit_code = 1
print(exit_code)

sys.exit(exit_code)






