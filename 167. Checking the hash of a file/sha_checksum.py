import hashlib

published_hash = '854bf444933e37f5824ae7bfc1e98d5bce2ebe4160d46b5edf346a89358e99da'

filename = 'colorama-0.4.5-py2.py3-none-any.whl'

with open(filename, 'rb') as downloaded_file:
    contents = downloaded_file.read()

file_hash = hashlib.sha256(contents).hexdigest()
print(file_hash)

if file_hash != published_hash:
    print(f'The file {filename} has been modified')
else:
    print(f'file {filename} hash is correct')
