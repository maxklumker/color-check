#!/usr/bin/env python3
from color_list import colors
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
user_input = form.getvalue("fcolor")

print("""
<h1></h1>
""")
if user_input in colors:
    print("<h1>{} is a color!</h1>".format(user_input))
else:
    print("<h1>{} is NOT a color!</h1>".format(user_input))
