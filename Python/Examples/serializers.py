import json
from pathlib import Path
import sys
import time


# Doesn't work...
class ExtendedDecoder(json.JSONDecoder):
    def default(self, obj):
        if '__class__' in obj:
            if obj['__class__'] == 'bytes':
                return bytes(obj['__value__'])

            if obj['__class__'] == 'complex':
                return complex(obj['__value__'][0], obj['__value__'][1])

            if obj['__class__'] == 'time.asctime':
                return time.strptime(obj['__value__'])

        return json.JSONDecoder.default(self, obj)



class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return dict(__class__='bytes', __value__=list(obj))

        if isinstance(obj, complex):
            return dict(__class__='complex', __value__=(obj.real, obj.imag))

        if isinstance(obj, time.struct_time):
            return dict(__class__='time.asctime', __value__=time.asctime(obj))

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


def from_json(obj):
    '''Add JSON support for deserializing additional object types'''
    if '__class__' in obj:
        if obj['__class__'] == 'time.asctime':
            return time.strptime(obj['__value__'])

        if obj['__class__'] == 'bytes':
            return bytes(obj['__value__'])

    return obj


def to_json(obj):
    '''Add JSON support for serializing additional object types'''
    if isinstance(obj, bytes):
        return dict(__class__='bytes', __value__=list(obj))

    # Doesn't work - this is converted to a list of 9 numbers
    # Way to override???
    if isinstance(obj, time.struct_time):
        return dict(__class__='time.asctime', __value__=time.asctime(obj))

    raise TypeError(repr(obj) + ' is not JSON serializable')


def tests():
    # Test entry:
    entry = dict(title='Dive into history, 2009 edition', article_link=
                'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
                comments_link=None, internal_id=b'\xDE\xD5\xB4\xF8',
                tags=('diveintopython', 'docbook', 'html'), published=True,
                published_date=time.strptime('Fri Mar 27 22:20:42 2009'))

    # Serialize:
    entry_jstr1 = json.dumps(entry, default=to_json)
    entry_jstr2 = json.dumps(entry, cls=ExtendedEncoder)

    # Deserialize:
    entry_jds1 = json.loads(entry_jstr1, object_hook=from_json)
    entry_jds2 = json.loads(entry_jstr2, cls=ExtendedDecoder)

    print(f'Original entry:\n{entry}\n')
    print(f'JSON Serialized 1:\n{entry_jstr1}\n')
    print(f'JSON Deserialized 1:\n{entry_jds1}\n')
    print(f'JSON Serialized 2:\n{entry_jstr2}\n')
    print(f'JSON Deserialized 2:\n{entry_jds2}\n')


if __name__ == '__main__':
    # print(f'Usage:  {Path(sys.argv[0]).name} <Python-Object-To-Serialize>')
    # print('Usage:  to_json(<Python-Object-To-Serialize>)')
    tests()

    '''
    Usage:

    Deserialize:
    with open('entry.json', encoding='utf-8') as f:
        entry = json.load(f, object_hook=serializers.from_json)

    Serialize:
    with open('entry.json', 'w', encoding='utf-8') as f:
        json.dump(entry, f, default=serializers.to_json)
    '''
