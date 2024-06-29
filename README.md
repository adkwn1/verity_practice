# Verity Practice

## Introduction
A simple Streamlit app to allow Guardians practice the Verity encounter from Destiny 2's Salvation's Edge Raid. Randomly generates the initial starting condition and indicates when the main room puzzle has been solved with the number of moves used. Provides feedback for illegal moves.

## Usage - Local Browser

To run the project in a local web browser, clone the repository ensuring the files are in the correct directory structure:
- Directory: project_folder/.streamlit/config.toml
- Directory: project_folder/images/[.png files]
- Python file: project_folder/verity.py (top level)

The config.toml specifies the server address and port number to run the web app locally via streamlit. In command prompt or terminal, navigate to the cloned directory and run the following command:

<code>streamlit run verity.py</code>

Open a web browser and navigate to http://localhost:10000 (or other port if changed in .toml file) to interact with the project application.

## Usage - Render
- Hosted on Render: https://verity-practice.onrender.com/
- Free service... be patient :)
  
## Required Packages
- random
- streamlit

## Screenshots
![image](https://github.com/adkwn1/verity_practice/assets/119823114/040854bb-98fd-44f6-bffd-0d0bc601c71f)
