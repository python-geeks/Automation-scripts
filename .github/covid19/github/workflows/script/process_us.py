import pandas as pd
import numpy as np

# from tqdm import tqdm

base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
confirmed_url = "time_series_covid19_confirmed_US.csv"
dead_url = "time_series_covid19_deaths_US.csv"

# ===============
# Confirmed Cases
print("===============\nWorking on Confirmed Cases\n\n")
confirmed = pd.read_csv(base_url + confirmed_url)
combined_keys = confirmed["Combined_Key"].unique()
# print(confirmed.columns[:15])
# print(combined_keys)


def adjust_date(s):
    l = s.split("/")
    return f"20{l[2]}-{int(l[0]):02d}-{int(l[1]):02d}"


frame_dict = {
    "Combined_Key": [],
    "UID": [],
    "iso2": [],
    "iso3": [],
    "code3": [],
    "FIPS": [],
    "Admin2": [],
    "Province/State": [],
    "Country/Region": [],
    "Lat": [],
    "Long": [],
    "Case": [],
    "Date": [],
}

# for key in tqdm(combined_keys):
for key in combined_keys:
    # print(key)
    df_c = confirmed[confirmed["Combined_Key"] == key]

    # Save static info for location
    UID = df_c["UID"].values[0]
    iso2 = df_c["iso2"].values[0]
    iso3 = df_c["iso3"].values[0]
    code3 = df_c["code3"].values[0]
    FIPS = df_c["FIPS"].values[0]
    Admin2 = df_c["Admin2"].values[0]
    Province_State = df_c["Province_State"].values[0]
    Country_Region = df_c["Country_Region"].values[0]
    Lat = df_c["Lat"].values[0]
    Long = df_c["Long_"].values[0]

    # transpose
    df_c = df_c.drop(
        [
            "UID",
            "iso2",
            "iso3",
            "code3",
            "FIPS",
            "Admin2",
            "Province_State",
            "Country_Region",
            "Lat",
            "Long_",
            "Combined_Key",
        ],
        axis=1,
    ).transpose()
    df_c.columns = ["Case"]

    for row in df_c.iterrows():
        # print(row[0], row[1][0])
        frame_dict["Date"].append(row[0])
        frame_dict["Case"].append(row[1][0])

        # static info
        frame_dict["Combined_Key"].append(key)
        frame_dict["UID"].append(UID)
        frame_dict["iso2"].append(iso2)
        frame_dict["iso3"].append(iso3)
        frame_dict["code3"].append(code3)
        frame_dict["FIPS"].append(FIPS)
        frame_dict["Admin2"].append(Admin2)
        frame_dict["Province/State"].append(Province_State)
        frame_dict["Country/Region"].append(Country_Region)
        frame_dict["Lat"].append(Lat)
        frame_dict["Long"].append(Long)

    # print(frame_dict)
    # quit()

    """
    # old way with static values
    UID = df_c['UID'].values[0]
    iso2 = df_c['iso2'].values[0]
    iso3 = df_c['iso3'].values[0]
    code3 = df_c['code3'].values[0]
    FIPS = df_c['FIPS'].values[0]
    Admin2 = df_c['Admin2'].values[0]
    Province_State = df_c['Province_State'].values[0]
    Country_Region = df_c['Country_Region'].values[0]
    Lat = df_c['Lat'].values[0]
    Long = df_c['Long_'].values[0]
    row_dict['Case'] = df_c['Case']
    # Repopulate static info
    df_c['UID'] = UID
    df_c['iso2'] = iso2 
    df_c['iso3'] = iso3
    df_c['code3'] = code3 
    df_c['FIPS'] = FIPS
    df_c['Admin2'] = Admin2 
    df_c['Province/State'] = Province_State 
    df_c['Country/Region'] = Country_Region 
    df_c['Lat'] = Lat 
    df_c['Long'] =  Long 
    df_c['Combined_Key'] = key 
    # Add date as column and rearrange to YYYY-DD-MM
    df_c['Date'] = df_c.index
    df_c['Date'] = df_c['Date'].map(adjust_date)
    #print(UID, iso2, iso3, code3, FIPS, Admin2, Province_State, Country_Region, Lat, Long)
    df = df.append(df_c[['UID', 'iso2','iso3','code3','FIPS','Admin2','Lat','Combined_Key','Date','Case','Long','Country/Region','Province/State']])
    
    
    """
    # break


df_confirmed = pd.DataFrame(data=frame_dict)
df_confirmed["Date"] = df_confirmed["Date"].map(adjust_date)
df_confirmed = df_confirmed[
    [
        "UID",
        "iso2",
        "iso3",
        "code3",
        "FIPS",
        "Admin2",
        "Lat",
        "Combined_Key",
        "Date",
        "Case",
        "Long",
        "Country/Region",
        "Province/State",
    ]
]
df_confirmed = df_confirmed.reset_index(drop=True)
print(df_confirmed)
df_confirmed.to_csv("data/us_confirmed.csv", index=False)


# ===============
# Deaths
print("\n\n===============\nWorking on Deaths\n\n")

confirmed = pd.read_csv(base_url + dead_url)
combined_keys = confirmed["Combined_Key"].unique()
# print(confirmed.columns[:15])
# print(combined_keys)

frame_dict = {
    "Combined_Key": [],
    "UID": [],
    "iso2": [],
    "iso3": [],
    "code3": [],
    "FIPS": [],
    "Admin2": [],
    "Province/State": [],
    "Population": [],
    "Country/Region": [],
    "Lat": [],
    "Long": [],
    "Case": [],
    "Date": [],
}
# for key in tqdm(combined_keys):
for key in combined_keys:
    # print(key)
    df_c = confirmed[confirmed["Combined_Key"] == key]

    # Save static info for location
    UID = df_c["UID"].values[0]
    iso2 = df_c["iso2"].values[0]
    iso3 = df_c["iso3"].values[0]
    code3 = df_c["code3"].values[0]
    FIPS = df_c["FIPS"].values[0]
    Admin2 = df_c["Admin2"].values[0]
    Province_State = df_c["Province_State"].values[0]
    Country_Region = df_c["Country_Region"].values[0]
    Lat = df_c["Lat"].values[0]
    Long = df_c["Long_"].values[0]
    Population = df_c["Population"].values[0]

    # transpose
    df_c = df_c.drop(
        [
            "UID",
            "iso2",
            "iso3",
            "code3",
            "FIPS",
            "Admin2",
            "Province_State",
            "Country_Region",
            "Lat",
            "Long_",
            "Combined_Key",
            "Population",
        ],
        axis=1,
    ).transpose()
    df_c.columns = ["Case"]

    for row in df_c.iterrows():
        # print(row[0], row[1][0])
        frame_dict["Date"].append(row[0])
        frame_dict["Case"].append(row[1][0])

        # static info
        frame_dict["Combined_Key"].append(key)
        frame_dict["UID"].append(UID)
        frame_dict["iso2"].append(iso2)
        frame_dict["iso3"].append(iso3)
        frame_dict["code3"].append(code3)
        frame_dict["FIPS"].append(FIPS)
        frame_dict["Admin2"].append(Admin2)
        frame_dict["Province/State"].append(Province_State)
        frame_dict["Country/Region"].append(Country_Region)
        frame_dict["Lat"].append(Lat)
        frame_dict["Long"].append(Long)
        frame_dict["Population"].append(Population)

    """# Old way
    # Repopulate static info
    df_c['UID'] = UID
    df_c['iso2'] = iso2 
    df_c['iso3'] = iso3
    df_c['code3'] = code3 
    df_c['FIPS'] = FIPS
    df_c['Admin2'] = Admin2 
    df_c['Province/State'] = Province_State 
    df_c['Country/Region'] = Country_Region 
    df_c['Lat'] = Lat 
    df_c['Long'] =  Long 
    df_c['Combined_Key'] = key 
    df_c['Population'] = Population 
    # Add date as column and rearrange to YYYY-DD-MM
    df_c['Date'] = df_c.index
    df_c['Date'] = df_c['Date'].map(adjust_date)
    #print(UID, iso2, iso3, code3, FIPS, Admin2, Province_State, Country_Region, Lat, Long)
    df = df.append(df_c[['UID', 'iso2','iso3','code3','FIPS','Admin2','Lat','Combined_Key','Population','Date','Case','Long','Country/Region','Province/State']])
    """  # break

df_dead = pd.DataFrame(data=frame_dict)
df_dead["Date"] = df_dead["Date"].map(adjust_date)
df_dead = df_dead[
    [
        "UID",
        "iso2",
        "iso3",
        "code3",
        "FIPS",
        "Admin2",
        "Lat",
        "Combined_Key",
        "Population",
        "Date",
        "Case",
        "Long",
        "Country/Region",
        "Province/State",
    ]
]
df_dead = df_dead.reset_index(drop=True)
print(df_dead)
df_dead.to_csv("data/us_deaths.csv", index=False)


# Simplified data
df_simple = df_confirmed[
    ["Date", "FIPS", "Admin2", "Province/State", "Country/Region"]
]
df_simple.insert(4, "Confirmed", df_confirmed["Case"])
df_simple.insert(5, "Deaths", df_dead["Case"])
df_simple.insert(6, "Population", df_dead["Population"])
print(df_simple)
df_simple.to_csv("data/us_simplified.csv", index=False)


# Create reference.csv
import urllib.request as req

req.urlretrieve(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv",
    "data/reference.csv",
)
