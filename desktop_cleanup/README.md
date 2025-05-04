

Script expect the user to pass limit in days beyond which the file if not modified would be listed/ deleted 
depending on the arguments provided to the scipts

## install requirements/dependencies:

No external requirements/dependencies to be installed

## how to use:

call the program using:
`python main.py --limit <limit in days> --delete <1 or 0>`
--limit -> argument to specify the limit in days beyond which if modifications were not done, the file would be listed
--delete -> optional argument to specify whether to delete the files or not, takes values of 0 or 1, 0 to not delete, 1 
to delete