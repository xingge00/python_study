import time
import socket
import asyncio

ip = "94.143.158.45"  #扫描的ip地址

socket_timeout = 3 #请求超时时间
sem = asyncio.Semaphore(300) #异步并发数


def port_gen():
    for i in range(1, 10000):
        yield i


async def tcp_scan(ip, port):
    fut = asyncio.open_connection(ip, port)
    async with sem: #在设定异步并发数的上下文中执行
        try:
            await asyncio.wait_for(fut, timeout=socket_timeout)
            print(f"{ip}:{port} is open")
        except Exception:
            pass


if __name__ == '__main__':
    time1 = time.time()

    loop = asyncio.get_event_loop()
    tasks = [tcp_scan(ip, port) for port in port_gen()]
    loop.run_until_complete(asyncio.wait(tasks))

    time2 = time.time()
    print(time2-time1)
