# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import threading
import queue

PREFIX="http://"
STOP_SIGNAL="STOP"
N_WORKERS=4

def parse_domain(url: str) -> str:
    url = url.replace(PREFIX, "")
    parts = url.split("/")
    return parts[0]

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        base_domain = parse_domain(startUrl)
        seen_urls = set()
        seen_urls_lock = threading.Lock()
        to_process = queue.Queue()

        def worker():
            while True:
                url = to_process.get()
                if url == STOP_SIGNAL:
                    to_process.task_done()
                    break

                scrapedUrls = htmlParser.getUrls(url)

                seen_urls_lock.acquire()
                for url in scrapedUrls:
                    domain = parse_domain(url)

                    if domain == base_domain and url not in seen_urls:
                        to_process.put(url)
                        seen_urls.add(url)

                seen_urls_lock.release()
                to_process.task_done()

        # start all our consumers
        threads = []
        for _ in range(N_WORKERS):
            t = threading.Thread(target=worker, daemon=True)
            t.start()
            threads.append(t)

        # seed the queue
        seen_urls.add(startUrl)
        to_process.put(startUrl)

        # block main thread until queue is fully processed
        to_process.join()

        # stop all the workers
        for _ in range(N_WORKERS):
            to_process.put(STOP_SIGNAL)

        # clean up all workers
        for t in threads:
            t.join()

        return list(seen_urls)