# Pylinter

Pylint is a static code analysis tool for the Python programming language

## Prerequisites

- Make sure Python 3 is installed in your system

## Setup instructions

- Kindly install the system dependencies using the below command,

```shell
pip install -r requirements.txt
```

## Running pylinter

```shell
# before
$ python -m mccabe foo/bar.py -m 10
4:0: 'complex_fun' 12

# after
$ ./ci/init.sh
$ bad.py:4:0 complex_fun 12
```

For simplified execution, kindly update the init.sh file with the python script name and start the ./init.sh

```shell
#!/bin/bash -xe

pycodestyle .
python ./run-pyflakes.py
python ./run-mccabe.py 10
pylint ./test.py
```

### To run,

```shell
sh ./init.sh
```

## Output

![image](https://user-images.githubusercontent.com/15235122/194733562-68167398-238d-49eb-a310-29812427c01d.png)


## Author(s)

Divakar R
