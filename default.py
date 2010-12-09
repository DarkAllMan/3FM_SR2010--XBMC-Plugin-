import sys
import os
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
import urllib,urllib2,re

# plugin handle
handle = int(sys.argv[1])

#add a channel to the list
# name		= default name
# url 		= stream url
# channelId	= channelId for epg information
# iconimage	= icon file name
def addChannel(name,url, channelId, iconimage):
        retval=True

	if channelId!="0":
		HTML=urllib2.urlopen("http://player.omroep.nl/?zenid=" + channelId).read()
		nowTitle=((re.search(r'<span id="nowTitle">([^*]*?)</span>',HTML)).group(1)).strip()
		nowPlot=(re.search(r'<p id="nowText">([^*]*?)</p>',HTML)).group(1)
		channelTitle =  "%s - %s" % (name, nowTitle)
	else:
		channelTitle = name
		nowTitle = name
		nowPlot = "test\r\ntest"

        liz = xbmcgui.ListItem(channelTitle, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": nowTitle, "Plot" : nowPlot } )
        retval = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return retval

#construct the list of channels
def show_channellist():
    Addon = xbmcaddon.Addon( id="plugin.video.nederland24")
    channel_icons_path = os.path.join(Addon.getAddonInfo("path"),"icons")

    addChannel("101TV", "http://livestreams.omroep.nl/npo/101tv-bb", "246", os.path.join(channel_icons_path, "101tv.png"))
    addChannel("Consumenten 24", "http://livestreams.omroep.nl/npo/consumenten24-bb", "238", os.path.join(channel_icons_path, "consumenten24.png"))
    addChannel("Cultura 24", "http://livestreams.omroep.nl/npo/cultura24-bb", "239", os.path.join(channel_icons_path, "cultura24.png"))
    addChannel("Geschiedenis 24", "http://livestreams.omroep.nl/npo/geschiedenis24-bb", "0", os.path.join(channel_icons_path, "geschiedenis24.png"))
    addChannel("Best 24", "http://livestreams.omroep.nl/npo/best24-bb", "252", os.path.join(channel_icons_path, "best24.png"))
    addChannel("Holland Doc 24", "http://livestreams.omroep.nl/npo/hollanddoc24-bb", "227", os.path.join(channel_icons_path, "hollanddoc24.png"))
    addChannel("Humor TV 24", "http://livestreams.omroep.nl/npo/humortv24-bb", "241", os.path.join(channel_icons_path, "humortv24.png"))
    addChannel("Journaal 24", "http://livestreams.omroep.nl/nos/journaal24-bb", "230", os.path.join(channel_icons_path, "journaal24.png"))
    addChannel("Politiek 24", "http://livestreams.omroep.nl/nos/politiek24-bb", "247", os.path.join(channel_icons_path, "politiek24.png"))
    addChannel("Spirit 24", "http://livestreams.omroep.nl/npo/spirit24-bb", "255", os.path.join(channel_icons_path, "spirit24.png"))
    addChannel("Sterren 24", "http://livestreams.omroep.nl/npo/sterren24-bb", "249", os.path.join(channel_icons_path, "sterren24.png"))
    addChannel("Z@ppelin/Familie 24", "http://livestreams.omroep.nl/npo/familie24-bb", "261", os.path.join(channel_icons_path, "familie24.png"))
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)

#init 
ok = show_channellist()

