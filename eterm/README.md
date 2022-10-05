# Eterm

Send or view emails through the terminal with style.

## Installation

Use git to install it

```bash
git clone https://github.com/Brist0l/Eterm.git
```

![eterm](https://github.com/mrHola21/Eterm/blob/main/imgs/eterm.png?raw=true)
## Usage

```bash
cd eterm/src
```

This example over here sends an email with a body , subject and a file:

```bash
python3 main.py {from_email} --to {to_email} --body --subject --file {files}
```

Note : You can send multiple files too just by specifying the files after the file.

For help:

```bash
python3 main.py -h
```

## Autocompletion

To add autocompletion add the phrases and Locations in Autocompletions/files.txt and greeting. eg. in the files.txt you
can add a folder name in which you have kept all the documents you want to email someone, you can specify the folder .

```text
/home/foo/Documents/stuff
```

## Using Autocompletion

To use autocompletion just press the `tab` key

## 10 reasons to use it

1) Easy To Use
2) Fast
3) Secure
4) Supports Autocompletion
5) Stores Autocompletion History For Speed
6) Lightweight
7) Recursive email searching
8) Compact Email viewing options
9) Be a terminal geek
10) Configurable SMTP

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/)
