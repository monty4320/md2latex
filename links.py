def links(line: str):
    """
    Function takes line input from Markdown and looks for
    Markdown's in-text citation format of "...text...[text to be linked]{url}",
    and replaces it with that of LaTeX's.
    :param line: line to be edited
    :return: LaTeX equivalent of markdown linked string
    """

    # Ensuring line of interest has key operators
    # Repeatedly checks line for repeated instances
    # of hyperlinks.

    fi = ''

    while ('[' and ']' and '(' and ')') in line:
        url = line[line.find('(') + 1: line.find(')')]
        # LaTeX in-text hyperlinks are not compatible
        # with the title feature of Markdown links.
        if ' ' in url:
            url = url[0: url.find(' ')]
        sent = line[0: line.find('[')]
        h_sent = line[line.find('[') + 1: line.find(']')]
        fi += sent + '\href{' + url + '}{' + h_sent + '}'
        if (len(line) == line.find(')') + 1):
            line = line[line.find(')') + 1]

        return fi
