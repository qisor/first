import httpx
import time
import threading
import httpx


def sync_main(url, sign):#同步
    response = httpx.get(url).status_code
    print(f"sync_main: {threading.current_thread()}: {sign}: {response}")


sync_start = time.time()
[sync_main(url='http://www.baidu.com', sign=i) for i in range(200)]
sync_end = time.time()
print(sync_end - sync_start)
