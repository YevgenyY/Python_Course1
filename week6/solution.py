import asyncio

class MetricSingleton:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if MetricSingleton.__instance == None:
            MetricSingleton()
        return MetricSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MetricSingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MetricSingleton.__instance = self

        self.map = dict()

    def addKeyValue(self, key, value, ts):
        if key in self.map.keys():
            # check if the same ts exists
            for it in self.map[key]:
                if it[0] == ts:
                    self.map[key].remove(it)
                    break
                    
            self.map[key].append((ts, value))
            self.map[key].sort()
        else:
            self.map[key] = [(ts, value),]

    def getKeyValue(self, key):
        out = 'ok\n'
        try:
            if key == '*':
                for kit in self.map.keys():
                    for it in self.map[kit]:
                        ts, value = it
                        out += "{} {} {}\n".format(kit, value, ts)
                        print("* {} {} ts {}".format(kit, value, ts))


            else:
                for it in self.map[key]:
                    ts, value = it
                    out += "{} {} {}\n".format(key, value, ts)
                    print("{} {} ts {}".format(key, value, ts))
        except:
            pass

        out += '\n'
        return out

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.db = MetricSingleton.getInstance()

    def connection_made(self, transport):
        self.transport = transport

    def process_data(self, data):
        resp = "error\nwrong command\n\n"

        r = data.split(' ')
        if r[0] == 'put' and len(r) == 4:
            print("{}".format(data))
            try:
                key = r[1]
                value = float(r[2])
                ts = int(r[3].rstrip())

                print("{} {} {}".format(key, value, ts))

                self.db.addKeyValue(key, value, ts)

                resp = 'ok\n\n'
            except:
                pass

        elif r[0] == 'get' and len(r) == 2:
            key = r[1].rstrip()
            resp = self.db.getKeyValue(key)

        return resp

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())


def run_server(host, port):
    
    loop = asyncio.get_event_loop()
    srv = loop.create_server(
        ClientServerProtocol,
       host, port 
    )

    server = loop.run_until_complete(srv)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == "__main__":
    run_server("127.0.0.1", 8888)
