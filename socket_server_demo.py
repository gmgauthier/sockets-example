from multiprocessing.context import Process
from multiprocessing.spawn import freeze_support
from time import sleep

from echo_client import EchoClient
from echo_server import EchoServer

if __name__ == '__main__':
    # freeze_support()
    s = Process(target=EchoServer)
    s.start()
    sleep(1)  # need to figure out a way to make this intelligent.
    c = EchoClient()
    c.echo("Now is the time for all good men.")
    c.echo("You load 14 tons, and what do you get?")
    c.echo("!quit")





