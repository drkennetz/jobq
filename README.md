# jobq - a local job scheduler

## TODO QUEUE PRIORITIES:
- add priorities to queues - run jobs based on priority

## TODO HASHPASSWORD:
- add a utilities script and add hashpassword to it

## TODO CONFIG DETAILS:
- add the option to start a server based on config instead of command line [this way could configure everything without going through all the commands bs]

## TODO STARTSERVER:
- Add password protection to server start server - can be null. If so, skip check for shutdown
- named server instead of port(?)
- password should be stored as crypto hash


## TODO STOPSERVER:
- add a command to kill the server - should honor password validation and verification

## TODO JOBCLASS:
- need to add a job class that holds simple details about a job such as start time, end time, queue, submitter, status (anything else?)
- this should just be a warehouse about the job

## TODO CLIENT COMMANDS
- jobq client init_queue -p PORT -q QUEUE -t TOTAL_CONCURRENT_JOBS 
- jobq client check_for_queue -p PORT -q QUEUENAME
- jobq client send_job -p PORT -j azcopy copy /path/to/dir 'https://' 
- jobq client list_all_queues -p PORT
- jobq client stop_server -p PORT --password