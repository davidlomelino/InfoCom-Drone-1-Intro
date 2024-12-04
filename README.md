# LP2 Drone Project - Lab 1
Intall the required Python packages if not done already (some packages might already be installed):
```
sudo apt update
sudo apt install python3-socketio
sudo apt install python3-engineio
sudo apt install python3-flask-socketio
sudo apt install python3-flask-cors

```
Go to `/webserver` in a terminal window, run the flask server:
```
export FLASK_APP=build.py
export FLASK_DEBUG=1
flask run
```
Go to `/pi` in another terminal window, run the Pi controller:
```
python3 pi_controller.py
```
In the terminal running `pi_controller.py`, use the keys 'wasd' to move the 'drone' on the website. 

Note: Don't use `python3 build.py` to run the webserver, since this does not porvide all the functionalities required by the application.

