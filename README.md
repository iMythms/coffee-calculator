# Coffee Calculator

A simple and clean Streamlit app to help you calculate the perfect coffee-to-water ratio for your brews.

## Features

- Quickly calculate pour-over stages based on coffee grams
- One-click presets for one cup (16g) or two cups (32g)
- Responsive and user-friendly interface

## How It Works

Given a coffee input in grams, the app:

- Multiplies it by 15 to get total water needed
- Allocates water into 4 stages:
  - First pour: 2x grams
  - Remaining water split equally into 3 stages

## Installation

```bash
git clone https://github.com/iMythms/coffee-calculator
cd coffee-calculator
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install streamlit
```

## Run the App

```bash
streamlit run app.py
```

## Screenshot

![Coffee Calculator Screenshot](screenshot.png)

## Author & Contributors

- Author: [@iMythms](https://github.com/iMythms)
- Contributor: [@hyusuf95](https://github.com/hyusuf95)
