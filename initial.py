from zipfile import ZipFile

with ZipFile('tibero/Tibero_6_FS06_linux_64_20170303.zip.001') as myzip:
    myzip.extractall()