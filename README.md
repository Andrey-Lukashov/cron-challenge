# cron-challenge
## todo
- is a CLI command that can run
- is a CLI command that accepts  time as argument and config via pipe

We want to run your code on the command line using an input like: 

./<your app> HH:MM < config

For example: ./application.py 16:10 < config

- test that there are only 3 arguments
- test that config is a file and can be opened
- test that the time supported is in a correct format (regex?)
- throw exceptions whenever any tests above fail


# Running the app
- Open the terminal
- Go to the root directory of this project
- Make sure the file is executable by running the following command:

chmod +x application.py

- Run the command by typing in ./application.py 2:30 < config