import os
import tarfile
import urllib3

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = "housing/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    # Create http connection pool
    http = urllib3.PoolManager()
    # GET response as bits
    response = http.request('GET',housing_url)
    # Write response as bits
    with open(tgz_path,'wb') as f:
        f.write(response.data)
    # Extract tgz
    with tarfile.open(tgz_path) as housing_tgz:
        housing_tgz.extractall(path=housing_path)
    response.release_conn()
    print("Extraction finished.")
    return

    
if __name__=='__main__':
    fetch_housing_data()