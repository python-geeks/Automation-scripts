# Bulk Renamer 

Basic script for renaming files in bulk.

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## No prerequisite

## How to use

`py bulk_renamer.py C:\\path\\to\\your\\folder new_name`

or

`py bulk_renamer.py C:/path/to/your/folder new_name`

### Example

`py bulk_renamer.py C:/my/path Baguette`

Old name    |   New Name
---         |   ---
Lorem.txt   |   Baguette - (0).txt
Ipsum.jpg   |   Baguette - (1).jpg
Dolores.png |   Baguette - (2).png
Lers.txt    |   Baguette - (3).txt