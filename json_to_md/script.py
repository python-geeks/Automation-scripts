import sys
import json
import argparse

markdown = ""
tab = "  "
list_tag = '* '
inline_code = '`'
code_block = '```'
subtitle = '## '
htag = '#'


if sys.version_info < (3, 0):
    raise Exception("[ERROR] This program requires Python 3.0 or greater")


def load_json(file):
    try:
        with open(file, 'r') as f:
            data = f.read()
        return json.loads(data)
    except:  # noqa
        print("[ERROR] File must be a valid json file")


def parse_json(json_block, depth, options):
    if isinstance(json_block, dict):
        parse_dict(json_block, depth, options)
    if isinstance(json_block, list):
        parse_list(json_block, depth, options)


def parse_dict(d, depth, options):
    for k in d:
        if k in options['ignore']:
            continue
        if options['keep'] != '':
            if k not in options['keep']:
                continue
        if isinstance(d[k], (dict, list)):
            add_header(k, depth)
            parse_json(d[k], depth + 1, options)
        else:
            add_value(k, d[k], depth)


def parse_list(l, depth, options):  # noqa
    for value in l:
        if not isinstance(value, (dict, list)):
            index = l.index(value)
            add_value(index, value, depth)
        else:
            parse_dict(value, depth, options)


def build_header_chain(depth):
    chain = list_tag * (bool(depth)) + htag * (depth + 1) + \
        ' value ' + (htag * (depth + 1) + '\n')
    return chain


def build_value_chain(key, value, depth):
    chain = tab * (bool(depth - 1)) + list_tag + \
        str(key) + ": " + inline_code + str(value) + inline_code + "\n"
    return chain


def add_header(value, depth):
    chain = build_header_chain(depth)
    global markdown
    markdown += chain.replace('value', value.title())


def add_value(key, value, depth):
    chain = build_value_chain(key, value, depth)
    global markdown
    markdown += chain


def write_out(markdown, output_file):
    with open(output_file, 'w+') as f:
        f.write(markdown)


def convert(input_file, output_file, options):
    json_data = load_json(input_file)
    depth = 0
    parse_json(json_data, depth, options)
    global markdown
    markdown = markdown.replace('#######', '######')
    write_out(markdown, output_file)


def main():
    parser = argparse.ArgumentParser(description="Json to Markdown converter",
                                    usage='%(prog)s -i $INPUTFILENAME [options]',  # noqa
                                    epilog="Ca va bien aller!")  # noqa
    parser.add_argument('-i', '--input', help='Input filename', required=True)
    parser.add_argument('-o', '--output', help='Output filename')
    parser.add_argument('-x', '--ignore', help='A list of keys to ignore in a json file')
    parser.add_argument('-k', '--keep', help='A list of keys to convert exclusively in a json file')
    parser.add_argument('-r', '--replace', help='A list of dict to replace keys values. Not implemented')
    args = parser.parse_args()

    if args.input is None:
        print('[Error] User must specify input')
        exit
    else:
        input_file = args.input

    if args.output is None:
        output_file = f'{args.input[:-4]}md'
    else:
        output_file = args.output
    print(f'[INFO] output: {output_file}')

    if args.ignore is not None:
        keys_to_ignore = load_json(args.ignore)
        print(keys_to_ignore)
    else:
        keys_to_ignore = ''

    if args.keep is not None:
        keys_to_keep = load_json(args.keep)
        print(keys_to_keep)
    else:
        keys_to_keep = ''

    options = dict()
    options['ignore'] = keys_to_ignore
    options['keep'] = keys_to_keep
    print(options)

    convert(input_file, output_file, options)
    """
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = input_file[:-4] + 'md'
        if input_file[-4:] == 'json':
            convert(input_file, output_file)
        else:
            print('Input must be a .json file')
    else:
        print("[ERROR] You must specify an input file.")
        print("Usage: \n       python json_to_md.py $JSONFILE" + '\n')
    """


if __name__ == "__main__":
    main()
