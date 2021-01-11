import random
import string
from urllib.parse import urlparse


ALPHABET = string.ascii_letters + string.digits


class Codec:
    def __init__(self):
        self.url_map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = ''.join(random.sample(ALPHABET, 6))
        self.url_map[key] = longUrl
        return f'http://tinyurl.com/{key}'   

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = urlparse(shortUrl).path[1:]
        return self.url_map.get(key)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))