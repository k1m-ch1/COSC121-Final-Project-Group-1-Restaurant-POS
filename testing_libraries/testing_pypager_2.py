from pypager.source import GeneratorSource
from pypager.pager import Pager
from prompt_toolkit.formatted_text import ANSI, to_formatted_text
from colorama import init, Fore, Style

init()

def generate_a_lot_of_content():
    for i in range(50):
        ansi_line = f"{Fore.CYAN}line: {i}{Style.RESET_ALL}\n"

        fragments = list(to_formatted_text(ANSI(ansi_line)))
        # yield a list of (style_str, text) fragments
        yield fragments

if __name__ == "__main__":
    p = Pager()
    p.add_source(GeneratorSource(generate_a_lot_of_content()))
    p.run()

