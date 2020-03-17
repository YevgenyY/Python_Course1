import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', action='store', help='key_name')
parser.add_argument('-v', '--val', help='value')
key_args = parser.parse_args()

def save_value(key_name, value):
    #print('Saving value')
    mymap = dict() 
    raw = myjson = ''
    try:
        with open(storage_path, 'r') as f:
            raw = f.read()
            myjson = json.loads(json.dumps(raw))
            if (myjson == ''): 
                mymap = dict()
            else:
                mymap = json.loads( myjson )

            #print(type(mymap))
            #print(mymap)

    except IOError:
        pass
        #print("File not accessible")

    if key_name in mymap.keys():
        #for val in mymap[key_name]:
            #print('Values: {} {} {}'.format(mymap[key_name], val, value))

            # if(val == value):  return
        mymap[key_name].append(value)
    else:
        mymap[key_name] = [value]

    myjson = json.dumps(mymap) 

    with open(storage_path, 'w') as f:
        f.write(myjson)
        #print(storage_path)
 
def print_value(key_name): 
    mymap = dict() 
    raw = myjson = ''
    try:
        with open(storage_path, 'r') as f:
            raw = f.read()
            myjson = json.loads(json.dumps(raw))
            if (myjson == ''):
                print('')
                return
            mymap = json.loads( myjson )
            #print(type(mymap))
            #print(mymap)

    except IOError:
        #print("File not accessible")
        print('')
        return

    if key_name in mymap.keys():
        #print(mymap[key_name])
        out = ''
        for val in mymap[key_name]:
            if (out == ''):
                out = val 
            else:
                out = out + ', ' + val
    else:
        return

    print(out)

if (key_args.val and key_args.key):
    save_value(key_args.key, key_args.val)
    exit()

if (key_args.key):
    print_value(key_args.key)
    exit()

print('Usage: task1.py --key key_name --val value')

