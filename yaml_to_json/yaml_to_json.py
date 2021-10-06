from ruyaml import YAML
import json


def get_yaml_data():
    yaml_name = input("Enter the yaml file name: ")

    try:
        with open(yaml_name, "r+") as f:
            yaml_data = YAML().load(f)
            return yaml_data
    except:  # noqa
        print("Invalid input enter a valid yaml file name e.g. example.yaml")
        yaml_data = get_yaml_data()


def convert_to_json(yaml_data):
    json_name = input("Enter the name of output json file: ")

    try:
        with open(json_name, "w+") as o:
            o.write(json.dumps(yaml_data))
    except:  # noqa
        print("Invalid input enter a valid json file name e.g. example.json")
        convert_to_json(yaml_data)


yaml_data = get_yaml_data()
convert_to_json(yaml_data)

print("Your yaml file has been converted and saved as json")
