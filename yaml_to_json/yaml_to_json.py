from ruyaml import YAML
import json
print("Welcome to Yaml to Json converter !")

yaml_name = input("Enter the yaml file name: ")
json_name = input("Enter the name of output json file: ")

def get_yaml_data(yaml_name):
    with open(yaml_name,"r+") as f:
        yaml_data = YAML().load(f)
    return yaml_data

def convert_to_json(yaml_data,json_data):
    with open(json_name,"w+") as o:
        o.write(json.dumps(yaml_data))
try:
    yaml_data = get_yaml_data(yaml_name)
except:
    print("Invalid input enter a valid yaml file name e.g. example.yaml")
    yaml_data = get_yaml_data(yaml_name)

try:
    convert_to_json(yaml_data, json_name)
except:
    print("Invalid input enter a valid json file name e.g. example.json")
    convert_to_json(yaml_data, json_name)


print(f"Your yaml file has been converted and saved as {json_name}")