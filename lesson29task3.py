import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode()
        print(f"Received message: {message}")
        writer.write(data)
        await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 65432)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())