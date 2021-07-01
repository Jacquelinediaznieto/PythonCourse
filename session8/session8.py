import pip
import requests
# get pip
# http://environment.data.gov.uk/flood-monitoring
# /id/stations?parameter=rainfall

response = requests.get("http://environment.data.gov.uk/flood-monitoring/id/stations?parameter=rainfall")
print(response.text)
with open("testdata.text","w") as file:
    file.write(response.text)