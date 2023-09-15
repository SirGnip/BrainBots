import brainbot.common.util


def run() -> None:
    print(f'running app. __name__:{__name__} __file__:{__file__}')
    print(brainbot.common.util.double(42))
