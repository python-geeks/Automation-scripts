import json


def json_to_xml(json_obj, line_padding=""):
    """
    Convert a JSON object to an XML string.
    """
    result_list = []

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            result_list.append(f"{line_padding}<{key}>")
            result_list.append(json_to_xml(value, line_padding + "  "))
            result_list.append(f"{line_padding}</{key}>")
    elif isinstance(json_obj, list):
        for element in json_obj:
            result_list.append(json_to_xml(element, line_padding))
    else:
        result_list.append(f"{line_padding}{json_obj}")

    return "\n".join(result_list)


def save_xml_file(xml_str, output_file):
    """
    Save the XML string to a file.
    """
    with open(output_file, "w") as file:
        file.write(xml_str)


def main():
    """
    Main function to convert a JSON file to an XML file.
    """
    # Input JSON file
    input_json_file = "test-input.json"
    # Output XML file
    output_xml_file = "test-output.xml"

    try:
        # Load JSON data from a file
        with open(input_json_file, "r") as json_file:
            json_data = json.load(json_file)

        # Convert JSON to XML
        xml_data = json_to_xml(json_data)

        # Add XML header
        xml_data_with_header = (
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + xml_data
        )

        # Save to XML file
        save_xml_file(xml_data_with_header, output_xml_file)
        print(f"XML file saved successfully to {output_xml_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
