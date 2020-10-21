# Contributing to Automation Scripts

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features


## Steps to contribute

* Comment on the issue you want to work on. Make sure it's not assigned to someone else.

## What to contribute

* Any Pytorch real life implementation
* Should add README.txt to execute, required environment and dataset link
* Compatible old implementations with new fixes
* Add REQUIREMENTS.txt with the your Jupyter notebook

### Making a PR

> - Make sure you have been assigned the issue to which you are making a PR.
> - If you make PR before being assigned, It will be labeled `invalid` and closed without merging.

* Fork the repo and clone it on your machine.
* Add a upstream link to main branch in your cloned repo
    ```
    git remote add upstream https://github.com/python-geeks/Automation-scripts.git
    ```
* Keep your cloned repo up to date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
    ```
    git pull upstream main
    ```
* Create your feature branch
    ```
    git checkout -b <feature-name>
    ```
* Commit all the changes
    ```
    git commit -am "Meaningful commit message"
    ```
* Push the changes for review
    ```
    git push origin <branch-name>
    ```
* Create a PR from our repo on Github.

### Additional Notes

* Code should be properly commented to ensure it's readability.
* If you've added code that should be tested, add tests as comments.
* Make sure your code properly formatted.
* Issue that pull request!
* use Flake8 for python code

## Issue suggestions/Bug reporting

When you are creating an issue, make sure it's not already present. Furthermore, provide a proper description of the changes. If you are suggesting any code improvements, provide through details about the improvements.

**Great Issue suggestions** tend to have:

- A quick summary of the changes.
- In case of any bug provide steps to reproduce
  - Be specific!
  - Give sample code if you can.
  - What you expected would happen
  - What actually happens
  - Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)


## License

By contributing, you agree that your contributions will be licensed under its  [MIT License](http://choosealicense.com/licenses/mit/).
