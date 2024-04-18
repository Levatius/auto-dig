import os
import socket
import time

HOST = "irc.twitch.tv"
PORT = 6667
USERNAME = "levatius"
OAUTH = os.getenv("OAUTH")
CHANNEL = "teaguvnor"
VALUE = 5
LIVE = True


def main():
    while True:
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send(f"PASS {OAUTH}\nNICK {USERNAME}\nJOIN #{CHANNEL}\n".encode())

        for _ in range(VALUE):
            for i in range(0, VALUE + 1):
                progress_bar = i * ["teaguvMANGO"] + (VALUE - i) * ["Digging"]
                message = "!dig " + " ".join(progress_bar) + f" {i * 100 // VALUE}%"
                if LIVE:
                    s.send(f"PRIVMSG #{CHANNEL} :{message}\n".encode())
                print(f"Sent: {message}")
                time.sleep(10.1)

        s.close()
        print("Restarting...")


if __name__ == '__main__':
    main()
