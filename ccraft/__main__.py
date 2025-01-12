__all__ = ['launch']

from .config.config import Config

def launch():
    Config.initialize()

if __name__ == '__main__':
    launch()
