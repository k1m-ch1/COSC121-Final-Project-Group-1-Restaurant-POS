from pypager.source import GeneratorSource
from pypager.pager import Pager


def generate_a_lot_of_content():
    """
    This is a function that generates content on the fly.
    It's called when the pager needs to display more content.

    This should yield prompt_toolkit `(style_string, text)` tuples.
    """
    counter = 0
    while True:
        yield [("", 'line: %i\n' % counter)]
        counter += 1

if __name__ == '__main__':
    p = Pager()
    p.add_source(GeneratorSource(generate_a_lot_of_content()))
    p.run()
