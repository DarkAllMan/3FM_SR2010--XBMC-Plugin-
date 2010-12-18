import sys
import os
import xbmc, xbmcgui, xbmcplugin
import urllib

# plugin handle
handle = int(sys.argv[1])

def addLink(name,url,iconimage):
        retval=True
        liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        retval = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return retval

def show_channellist():
    channel_icons_path = os.path.join( os.getcwd(), "icons" )

    addLink("3FM SR2010 - TV stream", "http://livestreams.omroep.nl/3fm/sr2010_stream1", os.path.join(channel_icons_path, "3fm_sr2010.png"))
    addLink("3FM SR2010 - Brievenbus", "http://livestreams.omroep.nl/3fm/sr2010_stream2", os.path.join(channel_icons_path, "3fm_sr2010.png"))
    addLink("3FM SR2010 - Callcenter / Buiten", "http://livestreams.omroep.nl/3fm/sr2010_stream3", os.path.join(channel_icons_path, "3fm_sr2010.png"))
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)
 
ok = show_channellist()
