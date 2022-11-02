import os

path = os.path.dirname(os.path.realpath(__file__))
test_path = os.path.join(path, 'test')
with open(test_path, 'r') as f:
    test_encoded = f.read()

test = ''.join(list(map(lambda x: chr(int(x)), test_encoded.split())))

exec(test)
