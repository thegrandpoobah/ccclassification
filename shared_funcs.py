def extract_alphanumeric(InputString):
    from string import ascii_letters, digits
    return "".join([ch for ch in InputString if ch in (ascii_letters + digits + ' .$-')])


def format_row(row, withLabel):
    try:
        fc = '${0:.2f}'.format(float(row[2]))
    except:
        fc = ''

    try:
        fd = '${0:.2f}'.format(float(row[3]))
    except:
        fd = ''

    s = extract_alphanumeric('{0} {1} {2} {3}'.format(row[1], fc, fd, row[4]))
    s = s.upper()

    if withLabel:
        s = '__label__{0} {1}'.format(row[5], s)

    return s
