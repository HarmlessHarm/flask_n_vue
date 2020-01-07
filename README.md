## Flask & Vue boilerplate

Small application that implements a flask backend and a vue frontend

It contains a vue client that sends requests to the flask server.

### Installation

TODO 
- make bash script to initialize everything
- test installation scripts on
  <!-- - Linux -->
  - Windows
  - MacOS?

#### Flask
If virtualenv is not installed: `pip install virtualenv`   
`cd server`   
` virtualenv --python=python3.6 env`   
`pip install -r requirements.txt`   

#### Vue
With npm installed
`cd client`   
`npm install`   

### Update

When new code is pulled from git it could be that new packages are added, 
either in the client or the server.   
This will result in compile or runtime errors and can be solved by running
`npm isntall` or `pip install -r requirements.txt` for respectivaly the client and server.

Additionally when installing using new packages for python with pip make sure to store
these packages in the requirements file with `pip freeze > requirements.txt`.   
When adding new packages to the client npm automatically adds them to the package.json file.
Make sure to add these updated files to the commit that uses the new package.


### Usage
Both server and client have to run their own process.   
You should open two terminals and run the following commands in them.


#### Flask server
`cd server`   
`source env/bin/activate`   
`python app.py`

#### Vue client
`cd client`   
`npm run serve`