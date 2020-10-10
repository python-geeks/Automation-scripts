import json
import os

with open("data/datapackage.json") as f:
    content = f.read()
    json_data = json.loads(content)

print("Updating metadata...")

# Set correct metadata
json_data["name"] = "covid-19"
json_data["title"] = "Novel Coronavirus 2019"
json_data["views"] = [
    {
        "title": "Total world to date",
        "resources": ["worldwide-aggregate"],
        "specType": "simple",
        "spec": {
            "group": "Date",
            "series": ["Confirmed", "Deaths"],
            "type": "line",
        },
    },
    {
        "title": "Number of confirmed cases in key countries",
        "resources": ["key-countries-pivoted"],
        "specType": "simple",
        "spec": {
            "group": "Date",
            "series": [
                "China",
                "US",
                "United_Kingdom",
                "Italy",
                "France",
                "Germany",
                "Spain",
                "Iran",
            ],
            "type": "line",
        },
    },
    {
        "title": "Mortality rate in percentage",
        "resources": [
            {
                "name": "worldwide-aggregate",
                "transform": [
                    {
                        "type": "formula",
                        "expressions": [
                            "data['Deaths'] / data['Confirmed'] * 100 + '%'"
                        ],
                        "asFields": ["Mortality rate"],
                    }
                ],
            }
        ],
        "specType": "simple",
        "spec": {
            "group": "Date",
            "series": ["Mortality rate"],
            "type": "bar",
        },
    },
    {
        "title": "Increase rate from previous day in confirmed cases worldwide",
        "resources": ["worldwide-aggregate"],
        "specType": "simple",
        "spec": {"group": "Date", "series": ["Increase rate"], "type": "bar",},
    },
]

# Set the correct format for dates
for resource in json_data["resources"]:
    for field in resource["schema"]["fields"]:
        if field.get("name") == "Date":
            field["format"] = "%Y-%m-%d"

with open("datapackage.json", "w") as f:
    json.dump(json_data, f, sort_keys=True, indent=2)

os.unlink("data/datapackage.json")