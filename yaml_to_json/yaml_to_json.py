from ruyaml import YAML
import argparse
import json


def get_yaml_data(yaml_name=None):
    if not yaml_name:
        yaml_name = input("Enter the yaml file name: ")

    try:
        with open(yaml_name, "r+") as f:
            yaml_data = YAML().load(f)
            return yaml_data
    except:  # noqa
        print("Invalid input enter a valid yaml file name e.g. example.yaml")
        yaml_data = get_yaml_data()


def convert_to_json(yaml_data, json_name=None, intent=None):
    if not json_name:
        json_name = input("Enter the name of output json file: ")

    try:
        with open(json_name, "w+") as o:
            o.write(json.dumps(yaml_data, indent=intent))
    except:  # noqa
        print("Invalid input enter a valid json file name e.g. example.json")
        convert_to_json(yaml_data)


def main():
    parser = argparse.ArgumentParser(description='Convert YAML file to JSON')
    parser.add_argument('--yaml', type=str, help='YAML filename')
    parser.add_argument('--json', type=str, help='JSON filename')
    parser.add_argument('--intent', type=int, help="intent value for JSON")
    args = parser.parse_args()

    yaml_name = args.yaml
    json_name = args.json
    intent = args.intent

    yaml_data = get_yaml_data(yaml_name)
    convert_to_json(yaml_data, json_name, intent=intent)

    print("Your yaml file has been converted and saved as json")


if __name__ == "__main__":
    main()
