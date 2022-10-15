
from time import sleep
from progress.spinner import MoonSpinner


def progress_bar():
    with MoonSpinner('Processing…') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()


if __name__ == '__main__':
    progress_bar()