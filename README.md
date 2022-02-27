# rate-limit

# hacker.py
in this file simply 4 request will be send to server trying to login
the first attempt is correct
but the other attempts will make the hacker blocked

# server.py
we build an HTTP server using 'bottle' API the function 'myIP' just finds the IP of the one who has send a request to server
and in function 'login' we check the the username and password if its correct just login if its not correct
we store the last time this IP tried to login and then with a new request we check if the time gap is less than 3 second 
then its probably a hacker so we store its IP in blocked_ip and if he tries to login again we will we won't let it happen
