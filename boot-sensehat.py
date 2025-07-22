from sense_hat import SenseHat
import socket
import time

sense = SenseHat()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't have to be reachable
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "No IP"
    finally:
        s.close()
    return ip

time.sleep(15)
ip_address = get_ip()
sense.show_message(ip_address, scroll_speed=0.05, text_colour=[0, 255, 0])
