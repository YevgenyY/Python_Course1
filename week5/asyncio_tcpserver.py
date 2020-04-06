import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print("received %r from %r" % (message, addr))
    #writer.write('ok\n\n'.encode('utf-8'))
    writer.write("ok\npalm.cpu 2.0 1150864248\npalm.cpu 0.5 1150864247\neardrum.cpu 3.0 1150864250\n\n".encode('utf-8'))
    #writer.write("\n\n".encode('utf-8'))
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
server = loop.run_until_complete(coro)

try: 
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
