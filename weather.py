import requests 
import arrow
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd

DATETIME_DEFAULT_FORMAT = 'YYYY-MM-DDTHH:mm:ssZZ'

#starttime = arrow.now().format('YYYY-MM-DDTHH:mm:ssZZ')
#endtime = arrow.now().shift(hours=+70).format('YYYY-MM-DDTHH:mm:ssZZ')
starttime = "2023-03-24T15:00:00+02:00"
endtime = "2023-03-26T20:00:00+03:00"


response = response = requests.get(
            'http://opendata.fmi.fi/wfs',
            params={
                'service': 'WFS',
                'version': '2.0.0',
                'request': 'getFeature',
                'storedquery_id': 'fmi::forecast::harmonie::surface::point::timevaluepair',
                'latlon': f'{"65.73556"},{"24.56574"}',
                'parameters': 'Pressure,Temperature,DewPoint,Humidity,WindDirection,WindSpeedMS,WindGust,PrecipitationAmount',
                'starttime': starttime,
                'endtime': endtime,
            },
        )
        
def Convert_to_dataframe(content):
        parsed = Parse_data(content)
        df_fmi = pd.DataFrame(parsed)
        df_fmi.columns = ['datetime', 'Pressure', 'Temperature', 'Dewpoint', 'Humidity',
                          'Wind_direction', 'Wind_speed', 'Wind_gust', 'Precipitation_amount']
        df_fmi.dropna(inplace=True)

        return df_fmi
        
def Parse_data(data):
        rootElement = ET.fromstring(data)
        fmiData = {'datetime': []}
        for member in rootElement.findall('{http://www.opengis.net/wfs/2.0}member'):
            pointTimeSeriesObservation = member.find(
                '{http://inspire.ec.europa.eu/schemas/omso/3.0}PointTimeSeriesObservation')
            result = pointTimeSeriesObservation.find(
                '{http://www.opengis.net/om/2.0}result')
            measurementTimeSeries = result.find(
                '{http://www.opengis.net/waterml/2.0}MeasurementTimeseries')
            type = measurementTimeSeries.attrib['{http://www.opengis.net/gml/3.2}id']
            type2 = type.replace('mts-1-1-', '')
            for point in measurementTimeSeries.findall('{http://www.opengis.net/waterml/2.0}point'):
                datetime = point.find(
                    '{http://www.opengis.net/waterml/2.0}MeasurementTVP/{http://www.opengis.net/waterml/2.0}time').text
                value = point.find(
                    '{http://www.opengis.net/waterml/2.0}MeasurementTVP/{http://www.opengis.net/waterml/2.0}value').text
                datetime_local = arrow.get(datetime).to(
                    'Europe/Helsinki').format(DATETIME_DEFAULT_FORMAT)
                if datetime_local not in fmiData['datetime']:
                    fmiData['datetime'].append(datetime_local)
                if type2 not in fmiData.keys():
                    fmiData[type2] = []
                if value == 'NaN':
                    # value = np.nan
                    value = "1"
                fmiData[type2].append(value)
                #print(datetime_local)

        return fmiData

df = Convert_to_dataframe(response.text)

# virhe tapahtuu!
#df['hour'] = pd.DatetimeIndex(
            #pd.to_datetime(df['datetime'])).hour
            
# korjaus:   
df['hour'] = pd.DatetimeIndex(
            pd.to_datetime(df['datetime'], utc= True)).hour
df['month'] = pd.DatetimeIndex(
            pd.to_datetime(df['datetime'], utc= True)).month
df['weekday'] = pd.DatetimeIndex(
            pd.to_datetime(df['datetime'], utc= True)).weekday            
		
print(df)
