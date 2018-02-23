"""
Frequent application of generators:
collect data paragraph-wise.
"""
text = """This is a text that
contains three paragraphs.

Each paragraph consists
of multiple lines.

After each paragraph,
there is an empty line.""".split('\n')


def read_paragraphs(iterable):
    paragraph = ""
    for line in iterable:
        if line.strip() == '' and paragraph:
            yield paragraph[1:]
            paragraph = ""
        else:
            paragraph += " " + line
    if paragraph:
        yield paragraph[1:]


for para in read_paragraphs(text):
    print(para)
    print('-' * 40)

