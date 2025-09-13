import sys
from modules.banner import (
    BRACKETS_COLOR,       # Color for brackets in messages
    FOREGROUND_RESET,     # Resets text color to terminal default
    CUSTOM_COLOR,         # Custom accent color for info messages
    NUMBERS_COLOR,        # Color for numeric indicators / warnings
    CUSTOM_TEXT_COLOR,    # Color for success messages
    TEXTS_COLOR,          # Color for error messages
    DEFAULT_SUB_BANNER_COLOR,  # Color for standard message text
    INPUTS_COLOR          # Color for input prompts
)


def SUCCESS(message: str):
    """
    Prints a success message to the terminal with colorized prefix.
    
    Format: [ + ] message
    Colors:
        + sign: CUSTOM_TEXT_COLOR
        brackets: BRACKETS_COLOR
        message: CUSTOM_TEXT_COLOR
    """
    sys.stdout.write(
        f'  {BRACKETS_COLOR}[ {CUSTOM_TEXT_COLOR}+ {BRACKETS_COLOR}]{CUSTOM_TEXT_COLOR} ' +
        message + f'\n{FOREGROUND_RESET}'  # Reset colors after message
    )
    sys.stdout.flush()  # Ensure message is immediately displayed


def ERROR(message: str):
    """
    Prints an error message to the terminal with colorized prefix.
    
    Format: [ - ] message
    Colors:
        - sign: TEXTS_COLOR (red)
        brackets: BRACKETS_COLOR
        message: TEXTS_COLOR
    """
    sys.stdout.write(
        f'  {BRACKETS_COLOR}[ {TEXTS_COLOR}- {BRACKETS_COLOR}]{TEXTS_COLOR} ' +
        message + f'\n{FOREGROUND_RESET}'
    )
    sys.stdout.flush()


def INFO(message: str):
    """
    Prints an informational message to the terminal with colorized prefix.
    
    Format: [ # ] message
    Colors:
        # sign: CUSTOM_COLOR (cyan)
        brackets: BRACKETS_COLOR
        message: DEFAULT_SUB_BANNER_COLOR (white)
    """
    sys.stdout.write(
        f'  {BRACKETS_COLOR}[ {CUSTOM_COLOR}# {BRACKETS_COLOR}]{DEFAULT_SUB_BANNER_COLOR} ' +
        message + f'\n{FOREGROUND_RESET}'
    )
    sys.stdout.flush()


def WARNING(message: str):
    """
    Prints a warning message to the terminal with colorized prefix.
    
    Format: [ ! ] message
    Colors:
        ! sign: NUMBERS_COLOR (yellow)
        brackets: BRACKETS_COLOR
        message: NUMBERS_COLOR
    """
    sys.stdout.write(
        f'  {BRACKETS_COLOR}[ {NUMBERS_COLOR}! {BRACKETS_COLOR}]{NUMBERS_COLOR} ' +
        message + f'\n{FOREGROUND_RESET}'
    )
    sys.stdout.flush()


def INPUT(message: str):
    """
    Generates a colorized input prompt for user interaction.
    
    Format: [ > ] message
    Colors:
        > sign: INPUTS_COLOR (magenta)
        brackets: BRACKETS_COLOR
        message: DEFAULT_SUB_BANNER_COLOR (white)
    
    Returns:
        str: Formatted prompt ready to pass to input() function
    """
    return (
        f'  {BRACKETS_COLOR}[ {INPUTS_COLOR}> {BRACKETS_COLOR}]{DEFAULT_SUB_BANNER_COLOR} ' +
        message + FOREGROUND_RESET
    )
