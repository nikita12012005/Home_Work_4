import re
#1_exercise
line = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"

for sssss in line.split('=sssss'):
    for equals in sssss.replace('=', ':'):
        for ampersand in equals.replace('&', ','):
            print(ampersand)

#2_exercise
def camel_to_snake(variable_name):
    result = ''
    for i, char in enumerate(variable_name):
        if char.isupper() and i > 0:
            result += '_'
        result += char.lower()
    return result

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = [camel_to_snake(variable_name) for variable_name in camel_case_list]

print(snake_case_list)

#3_exercise
text = "'''The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that was" \
      " launched into low Earth orbit in 1990 and remains in operation.... It was not the first space telescope," \
      " but it is one of the largest and most versatile, renowned both as a vital research tool and as a public " \
      "relations boon for astronomy. The Hubble telescope is named after astronomer Edwin Hubble and is one of " \
      "NASA's Great Observatories.... The Space Telescope Science Institute (STScI) selects Hubble's " \
      "targets and processes the resulting data, while the Goddard Space Flight Center (GSFC) controls the spacecraft.A" \
      " commission headed by Lew Allen, director of the Jet Propulsion Laboratory, was established to determine how " \
      "the error could have arisen. The Allen Commission found that a reflective null corrector," \
      " a testing device used to achieve a properly shaped non-spherical mirror, had been incorrectly" \
      " assembled—one lens was out of position by 1.3 mm (0.051 in).'''"

replaced_text = text.replace("....", ".") \
                   .replace(".A", ". A") \
                   .replace("Hubble.Space.Telescope", "Hubble Space Telescope")

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

pattern = r'<div id="([^"]+)">\s*<a href="([^"]+)">\s*([^<]+)\s*</a>\s*</div>'

result = re.findall(pattern, index)

print(result)
