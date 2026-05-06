
# import xarray as xr

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

# # The official new home for CORe data
# # Note: You'll construct this URL dynamically based on the user's date selection
# BASE_URL = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/core/para/core.20260401/00/post/flx/"
#
# @app.get("/get-anomaly")
# def get_wind_anomaly(date: str, level: int):
#     # This 'engine=netcdf4' or 'pydap' allows streaming via OPeNDAP
#     # No local storage required!
#     ds = xr.open_dataset(f"{BASE_URL}core.t00z.flx.ensmean.grib2", engine="cfgrib")
#
#     # Perform your LLJ math here
#     # Select level, calculate wind speed, subtract pre-calculated climatology
#     return {"data": "json_array_of_values"}


