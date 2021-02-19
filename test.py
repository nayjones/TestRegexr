#!/bin/python

def search_github(github_token, search):
    results = []
    h = {"Authorization":"token "+ github_token}
    url = "https://api.github.com/search/code?per_page=100&q=" + search  # actual limit of 100
    r = requests.get( url, headers=h, timeout=30)
    result = r.json()
    if 'total_count' in result:
        log.info("total results: {}".format(result['total_count']))
        log.warning("total results: {}".format(result['total_count']))
        #log.error("total results: {}".format(result['total_count']))

    else:
        log.error("no results found for the search: {}".format(search))
        
