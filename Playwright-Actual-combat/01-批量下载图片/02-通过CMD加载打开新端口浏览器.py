import subprocess


def start_playwright(port):
    edge_command = f'start msedge --remote-debugging-port={port}'
    subprocess.Popen(edge_command, shell=True)

if __name__ == '__main__':
    start_playwright(port=6666)
