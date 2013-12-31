from urllib import urlencode
from json import loads
from cgi import escape

categories = ['videos']
localization = 'en'

# see http://www.dailymotion.com/doc/api/obj-video.html
search_url = 'https://api.dailymotion.com/videos?fields=title,description,duration,url,thumbnail_360_url&sort=relevance&limit=25&page=1&{query}'

def request(query, params):
    global search_url
    params['url'] = search_url.format(query=urlencode({'search': query, 'localization': localization }))
    return params


def response(resp):
    results = []
    search_res = loads(resp.text)
    if not 'list' in search_res:
        return results
    for res in search_res['list']:
        title = res['title']
        url = res['url']
        if res['thumbnail_360_url']:
            content = '<a href="{0}" title="{0}" ><img src="{1}" /></a><br />'.format(url, res['thumbnail_360_url'])
        else:
            content = ''
        if res['description']:
            content += escape(res['description'][:500])
        results.append({'url': url, 'title': title, 'content': content})
    return results