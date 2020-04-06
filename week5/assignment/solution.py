import socket
import time
import ast

class ClientError(RuntimeError):
    def __init__(self, *args, **kwargs):
        self.args = args

class Client:
    def __init__(self, address, port, timeout=None):
        self.address = address
        self.port = port
        self.timeout = timeout

    def put(self, key, value, timestamp=None):
        try:
            val = float(value)
            ts = int(timestamp) if timestamp != None else 0

            if key.find('.') == -1 and key != '*':
                raise ValueError('wrong key without dot')

        except:
            raise ClientError('Wrong request')

        timestamp = int(time.time()) if timestamp == None else ts

        message = "put {} {} {}\n".format(key, value, timestamp)

        with socket.create_connection((self.address, self.port)) as sock:
            sock.settimeout(self.timeout)
            try:
                sock.sendall(message.encode("utf-8"))
                data = sock.recv(1024)

                resp = data.decode('utf-8').split('\n')
            except:
                raise ClientError('Wrong request')

            if resp[0] != 'ok':
                raise ClientError('response status error')


    @staticmethod
    def _parse_response( response ):
        out = dict()

        for it in response:
            if it == '':
                return out

            r = it.split(' ')
            if r[0] == '':
                return out

            if len(r) != 3:
                return None

            key = r[0];  
            #if key.find('.') == -1:
            #    return None

            try:
                value = float(r[1]); 
                ts = int(r[2])

            except:
                raise ClientError('bad values in the answer')

            if key in out.keys():
                out[key].append((ts, value))
            else:
                out[key] = [(ts, value),]

        return out
 
    def get(self, key):
        message = "get {}\n".format(key)
        #print(message)

        out = dict()

        with socket.create_connection((self.address, self.port)) as sock:
            sock.settimeout(self.timeout)
            try:
                sock.sendall(message.encode("utf-8"))
                data = sock.recv(1024).decode('utf-8')

                resp = data.split('\n')
                if resp[0].lower() != 'ok':
                    raise ValueError('response status error')

                resp.remove(resp[0])
                out = self._parse_response(resp)
            except:
                raise ClientError('wrong answer')
            
        if out == None:
            raise ClientError('Something is wrong in the answer {}'.format(data))

        # sort values
        for key in out:
            out[key].sort()

        return out

   
