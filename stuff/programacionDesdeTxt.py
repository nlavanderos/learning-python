with open('stuff\programacionDesdeTxt.txt') as f:
    [exec(compile(line,'testeo','eval')) for line in f ]