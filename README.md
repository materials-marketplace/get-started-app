# MarketPlace App Creation

This package uses [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) to facilitate the creation of MarketPlace applications.
For more information on what applications are and other related concepts, refer to the [MarketPlace documentation](https://materials-marketplace.readthedocs.io/en/latest/)

Carry out the following steps to create your own application with MarketPlace:

## Create the application from the template

First, install cookiecutter if it is not already in your system.
We recommend using a [virtual environment](https://docs.python.org/3/tutorial/venv.html) or a environment manager like [conda](https://docs.conda.io/en/latest/).

```sh
pip install cookiecutter
```

Now you can create the application **without** having to clone the repository
```sh
cookiecutter https://github.com/materials-marketplace/get-started-app.git
```

You will be prompted to answer the questions needed to create the app.

## Customise your app

The first step to create your own version of the app is to modify the `app.py` file to support the paths your app requires.
These capabilities should be matched in the `openAPI.yml` file, and mapped to a MarketPlace capability.

The application can now be deployed and registered.
Refer to the application's README for a detailed explanation.

## Misc.
### Pre-commit configuration check

A basic `pre-commit-config.yaml` file for [pre-commit](https://pre-commit.com/) has been created for the application.
You can use it to run sanity checks before each commit.

Set it up via:
```sh
pip install pre-commit
pre-commit install
```
The pre-commit hooks will now be automatically run before every commit.
To run them explicitly, use the command:
```sh
pre-commit run --all-files
```
### Continuous Integration
Depending on the chosen platform to host your code (e.g. GitHub or GitLab), your CI scripts will follow a different format.

However, we recommend to at least run the pre-commit hooks there, to ensure a minimum of consistence.

For GitHub, the job would look something like:
```yml
jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Run pre-commit
      run: |
          pip install pre-commit
          pre-commit install
          pre-commit run --all-files
```

For GitLab:
```yml
stages:
  - code_analysis

pre-commit:
  stage: code_analysis
  script:
    - pip install pre-commit
    - pre-commit install
    - pre-commit run --all-files
```
Note that these steps could be optimised if ran on a platform with pre-commit installed.
