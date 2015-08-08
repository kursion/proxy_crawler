# proxy_crawler
Get a list of proxies.

**requirements**: python 2

# Usage
Just like that:
```python
import proxy_crawler
proxies = crawler.getProxies()
```
*This retrieves 35 proxies.*


# Complete example
If you need more proxies simply call the function with a new page number.
And concatenate the list of proxies. Example:

```python
import crawler

proxies = []
for page in range(1, 5):
    proxies = proxies+crawler.getProxies(page)
print(proxies)
print("Retrieved %i proxies" % (len(proxies)))
```


# Author
Yves Lange
