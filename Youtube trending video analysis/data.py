from dataclasses import field
from googleapiclient.discovery import build
import os
import json
import csv

youtube_api_key=os.environ.get('youtube_api_key')

# create a api specific service object
youtube=build('youtube','v3',developerKey=youtube_api_key)

request=youtube.videos().list(part='statistics',chart='mostPopular',regionCode='in',maxResults=50)
response=request.execute()

with open('data.csv','w') as f:
          fieldnames=['views','likes','ratio']  #raito of likes and comments
          csv_DictWriter=csv.DictWriter(f,fieldnames=fieldnames,delimiter=',',lineterminator='\n')
          d={}
          csv_DictWriter.writeheader()
          for item in response['items']:
            try:
               d['views']=item['statistics']['viewCount']
               d['likes']=item['statistics']['likeCount']
               d['ratio']=int(d['likes'])/int(d['views'])
               csv_DictWriter.writerow(d)
            except:
                pass

