import apikey
from rich.console import Console

console = Console()

def set_data_directory_path(path: str) -> None:
    """
    Sets data directory path.

    :param path: Path to data directory
    """
    apikey.save("JSTOR_JOURNAL_SELECTOR_DIRECTORY_PATH", path)
    console.print(f'JSTOR journal selector data directory path set to {path}', style='bold blue')

def get_data_directory_path() -> str:
    """
    Gets data directory path.

    :return: Data directory path
    """
    return apikey.load("JSTOR_JOURNAL_SELECTOR_DIRECTORY_PATH")