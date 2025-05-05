# Package/Script Name

Add configurable frame/borders to all pages in your PDF

## Setup instructions

1. Install PyMuPDF pypi package:
```bash
pip install PyMuPDF
```

2. Run with default frame config:
```bash
python pdf_border_frame.py <path_to_pdf>
```

<br>
3. Run with custom config: <br>

| Flag      | Description         | Default |
|-----------|---------------------|---------|
| `--l`     | Left margin (pt)    | 20      |
| `--r`     | Right margin (pt)   | 20      |
| `--t`     | Top margin (pt)     | 20      |
| `--b`     | Bottom margin (pt)  | 20      |
| `--th`    | Frame thickness (pt)| 2       |


```bash
python pdf_border_frame.py --t 20 --b 20 --l 20 --r 20 --th 2 <path_to_pdf>
```


## Author
[sk5268](github.com/sk5268)