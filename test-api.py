import requests
import pandas as pd
import urllib3

urllib3.disable_warnings()

url = "https://pfsitdodgecityservices.meat.cargill.com:50209/api/itProduction/sap-plants/1CCO/from-business-dates/01-01-2023/to-business-dates/01-10-2023/product-production-shift"

def main():
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Authorization": "Basic VEVTVF9VU1I6VEVTVF9QU1dE" 
    }

    payload = ""

    resp = requests.request("GET", url, verify=False, data=payload,  headers=headersList)
    resp_json = resp.json()
    data = resp_json['results']
    df = pd.json_normalize(data)
    df.to_csv('ipfs_data.csv', encoding='utf-8', index=False)
    print('IPFS API data successfully export!')

main()