import requests
import pandas as pd
import os

SAVE_FOLDER = "data/raw"

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    history = pd.DataFrame(data["data"])

    output_file = os.path.join(SAVE_FOLDER, f"{scheme_name}.csv")

    history.to_csv(output_file, index=False)

    print(f"Saved: {scheme_name}.csv")