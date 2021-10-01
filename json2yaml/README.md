JSON 2 YAML Converter
========================

json2yaml is a python script to convert valid json file to a valid yaml file.

Description
-----------
While working with config files or if we need to expose YAML via an API, we find ourselves needing to convert a file from JSON to YAML. This script will do the same. The output can either be sent to stdout or to a specified file.

Running the Script
--------------------
Download the project source code directly or clone the repository on GitHub.  Navigate to the folder with the source code on your machine in a terminal window.
>  'Usage: json2yaml.py <source_file.json> [target_file.yaml]'
or
>  'Usage: json2yaml.py <source_file.json> ' for stdout

Demo
------
Let the json be:
```json
	{
		"foo": "bar",
		"baz": [ "qux","quxx"],
		"corge": null,
		"grault": 1,
		"garply": true,
		"waldo": "false",
		"fred": "undefined",
		"emptyArray": [],
		"emptyObject": {},
		"emptyString": ""
	}
```
Then, for result > stdout:
```sh
python json2yaml.py test-input.json
baz:
- qux
- quxx
corge: null
emptyArray: []
emptyObject: {}
emptyString: ''
foo: bar
fred: undefined
garply: true
grault: 1
waldo: 'false'
```
for result > file:
```sh
python json2yaml.py test-input.json test-output.yaml
```
