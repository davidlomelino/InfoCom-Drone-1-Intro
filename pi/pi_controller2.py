import requests
import time
import random
import click
from sense_hat import SenseHat
sense = SenseHat()


d_long = 0
d_la = 0
send_vel = False

def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    
    def left():
        click.echo('Left')
        send_vel = True
        d_long = -1
        d_la = 0
        return d_long, d_la, send_vel
        
        
    def right():
        click.echo('Right')
        send_vel = True
        d_long = 1
        d_la = 0
        return d_long, d_la, send_vel

    def up():
        click.echo('Up')
        send_vel = True
        d_long = 0
        d_la = 1
        return d_long, d_la, send_vel

    def down():
        click.echo('Down')
        send_vel = True
        d_long = 0
        d_la = -1
        return d_long, d_la, send_vel

sense.stick.direction_up = up
sense.stick.direction_down = down
sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_middle = sense.clear


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)

