from random import randint
class Codec:
    stringToURL = {}
    urlToString = {}
    TINYURL = "https://tinyurl.com/"
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        generatedURL = self.stringToURL.get(longUrl, "".join([chr(randint(ord('A'), ord('z'))) for _ in range(10)]))
        self.urlToString[generatedURL] = longUrl
        return self.TINYURL + generatedURL
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        prefixLength = len(self.TINYURL)
        return self.urlToString[shortUrl[prefixLength::]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))