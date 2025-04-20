from dataclasses import dataclass
from typing import List

class HtmlParser:
    def getUrls(self, url: str) -> List[str]:
        """
        Mock implementation of the HtmlParser interface
        Returns a list of URLs found on the given webpage
        """
        return []

@dataclass
class Url:
    fullUrl: str
    hostname: str


PREFIX = "http://"
def get_hostname(url: str) -> str:
    tmp = url.replace(PREFIX, "")
    parts = tmp.split("/")
    return parts[0]

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        traverse = [
            Url(
                fullUrl=startUrl, 
                hostname=get_hostname(startUrl)
            )
        ]
        seenUrls = set()
        
        while traverse:
            curr = traverse.pop()

            if curr.fullUrl in seenUrls:
                continue

            # Get all urls on the webpage, then filter all urls
            # which do match the webpage hostname.
            allUrlsRaw = htmlParser.getUrls(curr.fullUrl)
            allUrls = list(
                map(
                    lambda x: Url(fullUrl=x, hostname=get_hostname(x)), 
                    allUrlsRaw
                )
            )
            filteredHostnames = list(
                filter(
                    lambda x: x.hostname == curr.hostname, 
                    allUrls
                )
            )

            # add all unseen urls to the crawl
            for url in filteredHostnames:
                if url.fullUrl not in seenUrls:
                    traverse.append(url)
            
            # add the current url to the seen set to ensure we
            # do not traverl again.
            seenUrls.add(curr.fullUrl)

        return list(seenUrls)