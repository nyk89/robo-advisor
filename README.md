# robo-advisor
This program will give advice to hold, sell, or buy stocks.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork this [remote repository](https://github.com/nyk89/robo-advisor) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd app/robo-advisor
```

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

From within the virtual environment, install the required packages specified in the "requirements.txt":

```sh
pip install -r requirements.txt
```

From within the virtual environment, install the plotly package specified below:

```sh
pip install plotly
```

## Use
Run the program by typing the following into your terminal:
```sh
python app/robo_advisor.py
```
Type in a stock ticker for updated individual stock information and a graph plotting the daily highs over the last 100 days.

