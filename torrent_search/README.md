# torrent_search.py
A torrent-meta-searcher

This script searches (scrapes) on multiple Torrent sites for supplied keywords and returns the results grouped by categories as `JSON`.

Currently, the following sites are queried:
- thepiratebay10.org
- 1337x.to
- torlock.com

## Requirements and Dependencies
Recommendet Python-Version
- `3.5+`

The only external dependency are
- `BeautifulSoap`
- `aiohttp`

## Installation
Install the required external dependencies with

```shell
$ pip3 install -r requirements.txt
```

Also, a `chmod +x torrent_search.py` *can* be needed to make the script executable, otherwise You have to call it with `python3` (see [Usage Examples](#usage-examples))

## Usage examples
Getting help:
```shell
$ (python3) torrent_search.py -h
```

Perform a simple search:
```shell
$ (python3) torrent_search.py doom
```

Filter results with at least 20 seeders for `big bang theory`:
```shell
$ (python3) torrent_search.py "big bang theory" -s 20
```

Filter by categories:
```shell
$ (python3) torrent_search.py doom -c Movies Games
```
