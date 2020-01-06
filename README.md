## Flask & Vue boilerplate

Small application that implements a flask backend and a vue frontend

It contains a vue client that sends requests to the flask server.

### Installation

TODO 
- make bash script to initialize everything
- test installation scripts on
  - Linux
  - Windows
  - MacOS?

#### Flask
`cd server`   
`virtualenv env`   
`pip install -r requirements.txt`   

#### Vue
`cd client`   
`npm install`   


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