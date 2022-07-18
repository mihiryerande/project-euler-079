# Scratch file to clean up passcode attempts given in `keylog.txt`

if __name__ == '__main__':
    input_filename = 'keylog.txt'
    with open(input_filename, 'r') as f:
        lines = set()
        for line in f:
            lines.add(line.strip())

    # Sort and uniquify passcode attempts
    lines = list(sorted(lines))

    output_filename = 'keylog_clean.txt'
    with open(output_filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
