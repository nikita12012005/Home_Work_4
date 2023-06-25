import re
#1_exercise
string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"

string= string.strip()
params =string.split('&')
pairs= {}

for param in params:
    if param:
        key, value = param.split('=', maxsplit=1)
        pairs[key]= value

print(pairs)
#2_exercise
camel_case_names= ["FirstItem", "FriendsList", "MyTuple"]
snake_case_names= []

for name in camel_case_names:
    some= re.sub(r"([A-Z][a-z]+)([A-Z][a-z]+)", r"\1_\2", name).lower()
    print(some)

#3_exercise
text = """The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that was" \
      " launched into low Earth orbit in 1990 and remains in operation.... It was not the first space telescope," \
      " but it is one of the largest and most versatile, renowned both as a vital research tool and as a public " \
      "relations boon for astronomy. The Hubble telescope is named after astronomer Edwin Hubble and is one of " \
      "NASA's Great Observatories.... The Space Telescope Science Institute (STScI) selects Hubble's " \
      "targets and processes the resulting data, while the Goddard Space Flight Center (GSFC) controls the spacecraft.A" \
      " commission headed by Lew Allen, director of the Jet Propulsion Laboratory, was established to determine how " \
      "the error could have arisen. The Allen Commission found that a reflective null corrector," \
      " a testing device used to achieve a properly shaped non-spherical mirror, had been incorrectly" \
      " assembled—one lens was out of position by 1.3 mm (0.051 in)."""

replaced_text = re.findall(r"^[A-Z].+\.$", text)

print(replaced_text)



#4_exercise
index = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="https://www.google.com.ua/?hl=ru">
                Google
            </a>
        <div/>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="https://www.amazon.com/">
                    Amazon
                </a>
            </div>
        </div>
    </div>
</body>
</html>
'''

pattern = r'<div id="([^"]+)">\s*<a href="([^"]+)">\s*([^<]+)\s*</a>\s'

result = re.findall(pattern, index)

cleaned_result = [(group1.strip(), group2.strip(), group3.strip()) for group1, group2, group3 in result]

print(cleaned_result)

