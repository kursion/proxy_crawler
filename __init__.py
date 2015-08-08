__all__ = ["crawler"]

if __name__ == '__main__':
    import crawler
    import py_console.colors as consoleColors
    console = consoleColors

    proxies = []
    for page in range(1, 5):
        console.success("Getting page %i on nntime.com" % (page))
        proxies = proxies+proxy_crawler.getProxies(page)
    print(proxies)
    console.header("Retrieved %i proxies" % (len(proxies)))
else:
    import crawler
    getProxies = crawler.getProxies
