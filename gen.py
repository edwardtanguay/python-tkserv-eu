import site_parts
import tools

with open("/var/www/python/index.html","w") as file:
    file.write(site_parts.header() + """
<h1>Python Site</h1>
<p>This page is being generated by a Python script.</p>
<p>The purpose of this page is to learn Python</p>

<h2>How to build this site and learn Python</h2>
<ul>
    <li>cd ~/projects/python</li>
    <li>vim gen.py</li>
    <li>sudo python gen.py</li>
    <li>repo is here: 
<ul>
    <li><a href="https://github.com/edwardtanguay/python-tkserv-eu/blob/dev/gen.py" target="_blank">gen.py</a></li>
    <li><a href="https://github.com/edwardtanguay/python-tkserv-eu/blob/dev/site_parts.py" target="_blank">site_parts.py</a></li>
</ul>
    </li>
</ul>
<h2>Vim tips</h2>
<ul>
    <li>SAVE AND PUBLISH: :!bash | sudo python gen.py | CTRL-D</li>
    <li>CREATE NEW TAB: :tabe {filename}</li>
    <li>CLOSE TAB: :tabclose</li>
</ul>
<h2>Todo</h2>
<ul>
    <li>put each section in a function</li>
</ul>
<h2>Learning Resources</h2>
<ul>
    <li><a href="https://www.w3schools.com/python/default.asp" target="_blank">W3Schools Python</a></li>
</ul>
<h3>W3Schools</h3>
               
<h4><a href="https://www.w3schools.com/python/python_comments.asp" target="_blank">Comments</a></h4>
<p>both work</p>

<h4>Function test</h4>
""" + site_parts.test() + """

<h4>Slice</h4>
""" + site_parts.slice() + """

<h4>function test</h4>
""" + tools.uppercase_first_letter("this is a test") + """

</body>
</html>

""")

print("file created")

"""
this is a comment
and so is this
"""

# this is the last line
print("finished")
