"""
regexp
Regular Expression
Syntax
regexp identifiers
\d
    numbers; equivalent to class [0-9].
\D
    anything but numbers; equivalent to class [^0-9].
\s
    whitespace; equivalent to class [ \t\n\r\f\v].
\S
    anything but whitespace; equivalent to class [^ \t\n\r\f\v].
\w
    character; equivalent to class [a-zA-Z0-9_].
\W
    anything but character; equivalent to class [^a-zA-Z0-9_].
.
    any character, except for new lines
\.
    period, dot, scape for dot
\b whitespace around the character


regexp modifiers
{1,3}
    expecting 1-3
        \d{1,3}
+
    match 1 or more
?
    match 0 or 1
*
    match 0 or more
$
    match the end of a string
^
    match the beginning of a string
|
    either or
        \d{1,3} | \w{5,6}
[]
    range or variance [A-Za-z]
{X}
    expecting X amount

whitespace characters
\n
    new line
\s
    space
\t
    tab
\e
    escape
\f
    form feed
\r
    return
"""

import re

foo = """
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar is 102.
"""
ages = re.findall(r'\d{1,3}', foo)
names = re.findall(r'[A-Z][a-z]*', foo)

print(ages)
# ['15', '27', '97', '102']

print(names)
# ['Jessica', 'Daniel', 'Edward', 'Oscar']

ageDict = {}

x = 0

for name in names:
    ageDict[name] = ages[x]
    x += 1

print(ageDict)
# {'Jessica': '15', 'Daniel': '27', 'Edward': '97', 'Oscar': '102'}
