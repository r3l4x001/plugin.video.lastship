# -*- coding: UTF-8 -*-

"""
    Lastship Add-on (C) 2017
    Credits to Placenta and Covenant; our thanks go to their creators

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Addon Name: Lastship
# Addon id: plugin.video.lastship
# Addon Provider: LastShip


import urlparse,sys,urllib
from resources.lib.modules import control
from resources.lib.modules import cache
from resources.lib.modules import views
from resources.lib.modules import playcount
from resources.lib.modules import trailer
from resources.lib.modules import trakt
from resources.lib.modules import sources
from resources.lib.modules import downloader
from resources.lib.modules import libtools
from resources.lib.indexers import navigator
from resources.lib.indexers import movies
from resources.lib.indexers import channels
from resources.lib.indexers import tvshows
from resources.lib.indexers import episodes
import xbmcgui

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0


if action == None:
    cache.cache_version_check()
    navigator.navigator().root()

elif action == 'newsNavigator':
    navigator.navigator().news()

elif action == 'movieNavigator':
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    navigator.navigator().mytvshows(lite=True)

elif action == 'downloadNavigator':
    navigator.navigator().downloads()

elif action == 'libraryNavigator':
    navigator.navigator().library()

elif action == 'toolNavigator':
    navigator.navigator().tools()

elif action == 'searchNavigator':
    navigator.navigator().search()

elif action == 'viewsNavigator':
    navigator.navigator().views()

elif action == 'clearCache':
    navigator.navigator().clearCache()

elif action == 'clearCacheSearch':
    navigator.navigator().clearCacheSearch()

elif action == 'clearCacheAll':
    navigator.navigator().clearCacheAll()

elif action == 'clearCacheMeta':
    navigator.navigator().clearCacheMeta()

elif action == 'infoCheck':
    navigator.navigator().infoCheck('')

elif action == 'movies':
    movies.movies().get(url)

elif action == 'moviePage':
    movies.movies().get(url)

elif action == 'movieWidget':
    movies.movies().widget()

elif action == 'movieSearch':
    movies.movies().search()

elif action == 'movieSearchnew':
    movies.movies().search_new()

elif action == 'movieSearchterm':
    movies.movies().search_term(name)

elif action == 'moviePerson':
    movies.movies().person()

elif action == 'movieGenres':
    movies.movies().genres()

elif action == 'movieLanguages':
    movies.movies().languages()

elif action == 'movieCertificates':
    movies.movies().certifications()

elif action == 'movieYears':
    movies.movies().years()

elif action == 'moviePersons':
    movies.movies().persons(url)

elif action == 'movieUserlists':
    movies.movies().userlists()

elif action == 'channels':
    channels.channels().get()

elif action == 'tvshows':
    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    tvshows.tvshows().search()

elif action == 'tvSearchnew':
    tvshows.tvshows().search_new()

elif action == 'tvSearchterm':
    tvshows.tvshows().search_term(name)

elif action == 'tvPerson':
    tvshows.tvshows().person()

elif action == 'tvGenres':
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    tvshows.tvshows().networks()

elif action == 'tvLanguages':
    tvshows.tvshows().languages()

elif action == 'tvCertificates':
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    tvshows.tvshows().userlists()

elif action == 'seasons':
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    episodes.episodes().widget()

elif action == 'calendars':
    episodes.episodes().calendars()

elif action == 'episodeUserlists': 
    episodes.episodes().userlists()

elif action == 'refresh':
    control.refresh()

elif action == 'queueItem':
    control.queueItem()

elif action == 'openSettings':
    control.openSettings(query)

elif action == 'artwork':
    control.artwork()

elif action == 'addView':
    views.addView(content)

elif action == 'moviePlaycount':
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'traktManager':
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    trakt.authTrakt()

elif action == 'urlResolver':
    try: import urlresolver
    except: pass
    urlresolver.display_settings()

elif action == 'download':
    import json
    try: downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except: pass

elif action == 'play':
    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    sources.sources().addItem(title)

elif action == 'playItem':
    sources.sources().playItem(title, source)

elif action == 'alterSources':
    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    sources.sources().clearSources()

elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':

        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':

        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':

        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':

        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"

    from random import randint
    import json
    try:
        rand = randint(1,len(rlist))-1
        for p in ['title','year','imdb','tvdb','season','episode','tvshowtitle','premiered','select']:
            if rtype == "show" and p == "tvshowtitle":
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand]['title'])
                except: pass
            else:
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand][p])
                except: pass
        try: r += '&meta='+urllib.quote_plus(json.dumps(rlist[rand]))
        except: r += '&meta='+urllib.quote_plus("{}")
        if rtype == "movie":
            try: control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        elif rtype == "episode":
            try: control.infoDialog(rlist[rand]['tvshowtitle']+" - Season "+rlist[rand]['season']+" - "+rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)

elif action == 'movieToLibrary':
    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    libtools.libmovies().range(url)

elif action == 'moviesToLibrarySilent':
    libtools.libmovies().silent(url)

elif action == 'tvshowToLibrary':
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    libtools.libtvshows().range(url)

elif action == 'tvshowsToLibrarySilent':
    libtools.libtvshows().silent(url)

elif action == 'updateLibrary':
    libtools.libepisodes().update(query)

elif action == 'service':
    libtools.libepisodes().service()
