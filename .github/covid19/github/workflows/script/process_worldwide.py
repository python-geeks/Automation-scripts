import pandas as pd
import numpy as np


def calculate_increase_rate(csv_file: str = "data/worldwide-aggregate.csv"):
    with open(csv_file) as read_file:
        rows = read_file.read().splitlines()
    with open(csv_file, "w") as write_file:
        header_row = rows[0] + ",Increase rate"
        write_file.write(f"{header_row}\n")
        previous_row = None
        for row in rows[1:]:  # exclude header row
            if previous_row:
                prev_confirmed = int(previous_row.split(",")[1])
                confirmed = int(row.split(",")[1])
                rate = (confirmed - prev_confirmed) / prev_confirmed * 100
                write_file.write(f"{row},{rate}\n")
            else:
                write_file.write(f"{row},\n")
            previous_row = row


def adjust_date(s):
    l = s.split("/")
    return f"20{l[2]}-{int(l[0]):02d}-{int(l[1]):02d}"


base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
confirmed_url = "time_series_covid19_confirmed_global.csv"
dead_url = "time_series_covid19_deaths_global.csv"
recovered_url = "time_series_covid19_recovered_global.csv"


print("===============\nWorking on basic time series\n")

df = pd.read_csv(base_url + confirmed_url)
confirmed_copy = df.copy()  # for time series file with provinces
df = df.drop(["Lat", "Long"], axis=1)

to_concat = df[df["Province/State"].notna()]["Country/Region"].unique()
# We have to combine the numbers from the countries that are split up into provinces
for country in to_concat:
    new_row = df[df["Country/Region"] == country].sum()
    new_row["Country/Region"] = country
    new_row["Province/State"] = np.NaN
    df = df.drop(df[df["Country/Region"] == country].index)
    df = df.append(new_row, ignore_index=True)

confirmed = df[df["Province/State"].isna()].drop(
    "Province/State", axis=1
)  # take only countries (no territories)
# print(to_concat)

df = pd.read_csv(base_url + dead_url)
dead_copy = df.copy()  # for time series file with provinces
df = df.drop(["Lat", "Long"], axis=1)
to_concat = df[df["Province/State"].notna()]["Country/Region"].unique()
for country in to_concat:
    new_row = df[df["Country/Region"] == country].sum()
    new_row["Country/Region"] = country
    new_row["Province/State"] = np.NaN
    df = df.drop(df[df["Country/Region"] == country].index)
    df = df.append(new_row, ignore_index=True)

dead = df[df["Province/State"].isna()].drop(
    "Province/State", axis=1
)  # take only countries (no territories)
# print(to_concat)

df = pd.read_csv(base_url + recovered_url)
recovered_copy = df.copy()  # for time series
df = df.drop(["Lat", "Long"], axis=1)
to_concat = df[df["Province/State"].notna()]["Country/Region"].unique()
for country in to_concat:
    # print(df[df['Country/Region']==country])
    new_row = df[df["Country/Region"] == country].sum()
    new_row["Country/Region"] = country
    new_row["Province/State"] = np.NaN
    df = df.drop(df[df["Country/Region"] == country].index)
    df = df.append(new_row, ignore_index=True)

recovered = df[df["Province/State"].isna()].drop(
    "Province/State", axis=1
)  # take only countries (no territories)
# print(to_concat)

dates = np.intersect1d(
    np.intersect1d(
        confirmed.drop("Country/Region", axis=1).columns, dead.columns
    ),
    recovered.columns,
)
df = df[df["Province/State"].isna()].drop(
    "Province/State", axis=1
)  # take only countries (no territories)
countries = np.intersect1d(
    np.intersect1d(
        confirmed["Country/Region"].unique(), dead["Country/Region"].unique()
    ),
    confirmed["Country/Region"].unique(),
)
# print(countries)


data = pd.DataFrame()
for country in countries:
    # confirmed cases
    cntry_c = (
        confirmed[confirmed["Country/Region"] == country]
        .transpose()
        .drop("Country/Region")
    )
    cntry_c.columns = ["Confirmed"]
    cntry_c["Date"] = cntry_c.index

    # total deaths
    cntry_d = (
        dead[dead["Country/Region"] == country]
        .transpose()
        .drop("Country/Region")
    )
    cntry_d.columns = ["Deaths"]
    cntry_d["Date"] = cntry_d.index

    # recovered
    cntry_r = (
        recovered[recovered["Country/Region"] == country]
        .transpose()
        .drop("Country/Region")
    )
    cntry_r.columns = ["Recovered"]
    cntry_r["Date"] = cntry_r.index

    # concatenate (not the best way)
    cntry = cntry_c
    cntry["Deaths"] = cntry_d["Deaths"]
    cntry["Recovered"] = cntry_r["Recovered"]

    cntry = cntry.reset_index(drop=True)
    cntry["Country"] = country
    # print(cntry)
    data = data.append(
        cntry[["Date", "Country", "Confirmed", "Recovered", "Deaths"]]
    )


# data=data.sort_values(by=['Date', 'Country'])
data["Date"] = data["Date"].map(adjust_date)
data = data.reset_index(drop=True)
data.to_csv("data/countries-aggregated.csv", index=False)


# ==============================================================================================
# Now create the more detailed time series
print("\n===============\nWorking on more detailed time series\n")

confirmed = confirmed_copy.copy()
confirmed["Province/State"] = confirmed["Province/State"].fillna("")
dead = dead_copy.copy()
dead["Province/State"] = dead["Province/State"].fillna("")
recovered = recovered_copy.copy()
recovered["Province/State"] = recovered["Province/State"].fillna("")

# these are the country-province combinations, we go through them to reformat the columns
combos = np.array(
    confirmed[["Country/Region", "Province/State"]].to_records(index=False)
)
# print(combos)

# countries = confirmed['Country/Region'].unique()
# states = confirmed['Province/State'].unique()

data = pd.DataFrame()
for country, state in combos:

    # Here we just need to check if we are dealing with a country-province or just a country
    is_na = False
    if state == "":
        is_na = True

    df_c = confirmed[
        (confirmed["Country/Region"] == country)
        & ((confirmed["Province/State"] == state))
    ]

    try:
        Lat, Long = df_c["Lat"].values[0], df_c["Long"].values[0]
    except IndexError:
        print("  Skipping, Index Error")
        continue
    except Exception as e:
        raise (e)
    # print(Lat, Long)

    df_r = recovered.loc[
        (recovered["Country/Region"] == country)
        & ((recovered["Province/State"] == state))
    ].transpose()
    df_r = df_r.drop(["Province/State", "Country/Region", "Lat", "Long"])

    # Canada is annoying and doesn't report recovered at a province level
    try:
        df_r.columns = ["Recovered"]
    except:
        df_r["Recovered"] = np.NaN  # May change this to the empty string

    df_c = df_c.transpose().drop(
        ["Province/State", "Country/Region", "Lat", "Long"]
    )
    df_c.columns = ["Confirmed"]

    df_d = dead[
        (dead["Country/Region"] == country)
        & ((dead["Province/State"] == state))
    ].transpose()
    df_d = df_d.drop(["Province/State", "Country/Region", "Lat", "Long"])
    df_d.columns = ["Deaths"]

    df = df_c
    df["Recovered"] = df_r["Recovered"]
    df["Deaths"] = df_d["Deaths"]
    df["Country/Region"] = country
    df["Province/State"] = state
    df["Lat"] = Lat
    df["Long"] = Long
    df["Date"] = df.index
    # print(df)

    data = data.append(
        df[
            [
                "Date",
                "Country/Region",
                "Province/State",
                "Lat",
                "Long",
                "Confirmed",
                "Recovered",
                "Deaths",
            ]
        ]
    )

data["Date"] = data.index
data["Date"] = data["Date"].map(adjust_date)
data = data.reset_index(drop=True)
data.to_csv("data/time-series-19-covid-combined.csv", index=False)


# ==============================================================================================
# Now create the key countries pivoted
print("\n===============\nWorking on Key Countries\n")
confirmed = confirmed_copy.copy()
confirmed["Province/State"] = confirmed["Province/State"]

to_concat = confirmed[confirmed["Province/State"].notna()][
    "Country/Region"
].unique()
# We have to combine the numbers from the countries that are split up into provinces
for country in to_concat:
    new_row = confirmed[confirmed["Country/Region"] == country].sum()
    new_row["Country/Region"] = country
    new_row["Province/State"] = np.NaN
    confirmed = confirmed.drop(
        confirmed[confirmed["Country/Region"] == country].index
    )
    confirmed = confirmed.append(new_row, ignore_index=True)

confirmed = confirmed[confirmed["Province/State"].isna()].drop(
    ["Province/State", "Lat", "Long"], axis=1
)  # take only countries (no territories)
key_countries = confirmed[
    (confirmed["Country/Region"] == "US")
    | (confirmed["Country/Region"] == "China")
    | (confirmed["Country/Region"] == "United Kingdom")
    | (confirmed["Country/Region"] == "Italy")
    | (confirmed["Country/Region"] == "France")
    | (confirmed["Country/Region"] == "Germany")
    | (confirmed["Country/Region"] == "Spain")
    | (confirmed["Country/Region"] == "Iran")
]
key_countries = key_countries.transpose()
key_countries.columns = key_countries.iloc[0]
key_countries = key_countries.drop("Country/Region")
key_countries["Date"] = key_countries.index
key_countries["Date"] = key_countries["Date"].map(adjust_date)
key_countries = key_countries.rename(
    {"United Kingdom": "United_Kingdom"}, axis="columns"
)
key_countries = key_countries[
    [
        "Date",
        "China",
        "US",
        "United_Kingdom",
        "Italy",
        "France",
        "Germany",
        "Spain",
        "Iran",
    ]
]
key_countries.to_csv("data/key-countries-pivoted.csv", index=False)


# ==============================================================================================
# Now create the world aggregate
print("\n===============\nWorking on world aggregate\n")
confirmed = confirmed_copy.copy().drop(
    ["Lat", "Long", "Province/State", "Country/Region"], axis=1
)
dead = dead_copy.copy().drop(
    ["Lat", "Long", "Province/State", "Country/Region"], axis=1
)
recovered = recovered_copy.copy().drop(
    ["Lat", "Long", "Province/State", "Country/Region"], axis=1
)

df = pd.DataFrame()
df["Confirmed"] = confirmed.sum()
df["Recovered"] = recovered.sum()
df["Deaths"] = dead.sum()
df["Date"] = df.index
df["Date"] = df["Date"].map(adjust_date)
df = df[["Date", "Confirmed", "Recovered", "Deaths"]]
df.to_csv("data/worldwide-aggregate.csv", index=False)

calculate_increase_rate()