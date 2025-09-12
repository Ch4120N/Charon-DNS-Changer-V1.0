import sys
from modules.banner import BRACKETS_COLOR, FOREGROUND_RESET, CUSTOM_COLOR, CUSTOM_TEXT_COLOR, TEXTS_COLOR, DEFAULT_SUB_BANNER_COLOR


def SUCCESS(message: str):
    sys.stdout.write(
        f'{BRACKETS_COLOR}[ {CUSTOM_TEXT_COLOR}+ {BRACKETS_COLOR}]{CUSTOM_TEXT_COLOR} ' +
        message + f'\n{FOREGROUND_RESET}'
    )
    sys.stdout.flush()


def ERROR(message: str):
    sys.stdout.write(
        f'{BRACKETS_COLOR}[ {TEXTS_COLOR}- {BRACKETS_COLOR}]{TEXTS_COLOR} ' +
        message + f'\n{FOREGROUND_RESET}'
    )
    sys.stdout.flush()


def INFO(message: str):
    sys.stdout.write(
        f'{BRACKETS_COLOR}[ {CUSTOM_COLOR}# {BRACKETS_COLOR}]{DEFAULT_SUB_BANNER_COLOR} ' +
        message + f'\n{FOREGROUND_RESET}'
    )
    sys.stdout.flush()
