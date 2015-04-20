DEFAULT_ERROR_MESSAGE = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code:</p>
        <p>Message:</p>
        <p>Error code explanation:</p>
    </body>
</html>
"""

print('Content-Type: text/plain')
print('')
print(DEFAULT_ERROR_MESSAGE)