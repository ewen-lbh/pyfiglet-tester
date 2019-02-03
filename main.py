def main():
    import random
    import re
    import shutil
    import sys
    import webbrowser
    import pyfiglet
    FONTS_LIST = [
        '3-d',
        '3x5',
        '5lineoblique',
        'acrobatic',
        'alligator2',
        'alligator',
        'alphabet',
        'avatar',
        'banner3-D',
        'banner3',
        'banner4',
        'banner',
        'barbwire',
        'basic',
        'bell',
        'bigchief',
        'big',
        'binary',
        'block',
        'broadway',
        'bubble',
        'bulbhead',
        'calgphy2',
        'caligraphy',
        'catwalk',
        'chunky',
        'coinstak',
        'colossal',
        'computer',
        'contessa',
        'contrast',
        'cosmic',
        'cosmike',
        'crawford',
        'cricket',
        'cyberlarge',
        'cybermedium',
        'cybersmall',
        'decimal',
        'diamond',
        'digital',
        'doh',
        'doom',
        'dotmatrix',
        'double',
        'drpepper',
        'eftichess',
        'eftifont',
        'eftipiti',
        'eftirobot',
        'eftitalic',
        'eftiwall',
        'eftiwater',
        'epic',
        'fender',
        'fourtops',
        'fuzzy',
        'goofy',
        'gothic',
        'graffiti',
        'hex',
        'hollywood',
        'invita',
        'isometric1',
        'isometric2',
        'isometric3',
        'isometric4',
        'italic',
        'ivrit',
        'jazmine',
        'katakana',
        'kban',
        'larry3d',
        'lcd',
        'lean',
        'letters',
        'linux',
        'lockergnome',
        'madrid',
        'marquee',
        'maxfour',
        'mike',
        'mini',
        'mirror',
        'mnemonic',
        'nancyj-fancy',
        'nancyj',
        'nancyj-underlined',
        'nipples',
        'o8',
        'octal',
        'ogre',
        'os2',
        'pawp',
        'peaks',
        'pebbles',
        'pepper',
        'poison',
        'puffy',
        'pyramid',
        'rectangles',
        'relief2',
        'relief',
        'rev',
        'roman',
        'rot13',
        'rounded',
        'rowancap',
        'rozzo',
        'sblood',
        'script',
        'serifcap',
        'shadow',
        'short',
        'slant',
        'slide',
        'slscript',
        'small',
        'smisome1',
        'smkeyboard',
        'smscript',
        'smshadow',
        'smslant',
        'speed',
        'stacey',
        'stampatello',
        'standard',
        'starwars',
        'stellar',
        'stop',
        'straight',
        'tanja',
        'term',
        'thick',
        'thin',
        'threepoint',
        'ticks',
        'ticksslant',
        'tinker-toy',
        'tombstone',
        'trek',
        'twopoint',
        'univers',
        'usaflag',
        'weird',
        'whimsy',
    ]
    LOGOS_FONT_LIST = [
        'avatar',
        'banner',
        'bell',
        'big',
        'chunky',
        'cybermedium',
        'digital',
        'doom',
        'double',
        'graffiti',
        'madrid',
        'ogre',
        'pepper',
        'puffy',
        'rectangles',
        'rounded',
        'script',
        'shadow',
        'short',
        'slant',
        'small',
        'smkeyboard',
        'standard',
        'stop',
        'straight',
        'threepoint',
        'tombstone',
        'twopoint',
        'weird'
    ]

    # Function by critiqjo:
    # https://gist.github.com/critiqjo/2ca84db26daaeb1715e1
    def col_print(lines, term_width=None, indent=0, pad=2):
        if not term_width:
            size = shutil.get_terminal_size((80, 20))
            term_width = size.columns
        n_lines = len(lines)
        if n_lines == 0:
            return

        col_width = max(len(line) for line in lines)
        n_cols = int((term_width + pad - indent) / (col_width + pad))
        n_cols = min(n_lines, max(1, n_cols))

        col_len = int(n_lines / n_cols) + (0 if n_lines % n_cols == 0 else 1)
        if (n_cols - 1) * col_len >= n_lines:
            n_cols -= 1

        cols = [lines[i * col_len: i * col_len + col_len] for i in range(n_cols)]

        rows = list(zip(*cols))
        rows_missed = zip(*[col[len(rows):] for col in cols[:-1]])
        rows.extend(rows_missed)

        for row in rows:
            print(" " * indent + (" " * pad).join(line.ljust(col_width) for line in row))

    website_url = 'mx3creations.com'
    repo_url = 'github.com/ewen-lbh/pyfiglet-tester'
    font = 'big'
    logo_font = random.choice(LOGOS_FONT_LIST)
    text = base_text = 'The quick brown fox JUMPS over the lazy dog !'
    startup_logo = pyfiglet.figlet_format('Pyfiglet\nTester', font=logo_font) + '\n\n\n'
    tutorial = f"""
    ===COMMANDS
    set <text|-r>   Set the text displayed
                    -r or -reset to reset it to "{base_text}"

    ?               Shows this

    /repo           Go to the github repo of this script

    ls              List some fonts (not sure if its all of them)

    random          Select a font randomly from the ones shown with ls

    <anything else> Displays the text using the font specified


    ===INFO
    Script by Mx3 - {website_url}
    Column print function by critiqjo (github)
    Repo - {repo_url}
    """
    print(startup_logo + tutorial)

    while font not in ('exit', 'close'):
        font = str(input('Choose a font...\n>>'))
        if font[:3] == 'set':
            req_text = font[4:]
            if req_text in ('-reset', '-r'):
                text = base_text
            else:
                text = str(req_text)
            print('Displayed text set to "' + text + '"')
        elif font[:2] in ('/h', '/?', '?'):
            print(tutorial)
        elif font[:2] == '/r':
            webbrowser.open(repo_url)
        elif font[:2] == '/w':
            webbrowser.open(website_url)
        elif font[:2] in ('/l', 'ls'):
            print('Fonts list:\n')
            col_print(FONTS_LIST)
            print('\n')
        elif font.strip() == 'exit':
            sys.exit('Script closed.')
        else:
            if font.strip() == 'random':
                font = random.choice(FONTS_LIST)
                print(f'\n\nFont:{font}\n\n')
            try:
                pyfiglet.print_figlet(text, font=font)
            except pyfiglet.FontNotFound:
                print(f'No font named "{font}" !')


if __name__ == '__main__':
    main()