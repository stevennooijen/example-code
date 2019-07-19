# Example Code repo

This repo is meant for code demonstrations of various tools and methods.

## What's included?

Demonstrations can be found in the `notebooks/` folder. Examples
included currently concern from topics like:
* Statistics
* Programming
* Time series modelling
* Tools such as MLflow and `python-dotenv`

## Virtualenv

The dependencies needed are listen in `requirements.txt`. Some of the
packages like `arviz` don't work well with Conda, so it's advised to use
`virtualenv`:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Credentials

For some demonstrations credentials to external services are required.
This will be discussed in the specific demo, but in general these are
handled through the `python-dotenv` package. Copy the `.env-example`
file and save it as `.env`. Then add your own usernames and passwords to
it for the credentials that you need.

## Data

The data required for each demonstration is indicated in the specific
notebook. Often data will be saved locally to the `data/` folder.
