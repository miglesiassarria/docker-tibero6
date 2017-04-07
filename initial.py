from subprocess import call

url = "https://github.com/miglesiassarria/tibero/tree/master/tibero"
for i in range(5):
    call("curl -s --retry 3 -m 60 -o /$part -L $ur{}".format(i+1))