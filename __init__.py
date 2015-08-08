__all__ = ["crawler"]

if __name__ == '__main__':
    import crawler

    proxies = []
    for page in range(1, 5):
        print("Getting page %i on nntime.com" % (page))
        proxies = proxies+crawler.getProxies(page)
    print(proxies)
    print("Retrieved %i proxies" % (len(proxies)))
else:
    import crawler
    getProxies = crawler.getProxies
