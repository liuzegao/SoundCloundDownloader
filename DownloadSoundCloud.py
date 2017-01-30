# -*- coding: utf-8 -*-

import urllib2
import json

with open('/home/zegaoliu/Dropbox/PythonScripts/PythonLearning/RemixMusic/MusicUrl.json') as inFile:
    print "downloading with urllib2"
    text = inFile.read()
    url_dict = json.loads(text)
    i = 0
    for url in url_dict:
        print url
    #url = 'https://cf-media.sndcdn.com/gUErfdPEPfeK.128.mp3?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLW1lZGlhLnNuZGNkbi5jb20vZ1VFcmZkUEVQZmVLLjEyOC5tcDMiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE0ODU3NDc3OTN9fX1dfQ__&Signature=OtXufAcJso-3X8ySqOdT1xN-qK9JDnRHHMgc68UmlSfwKnv7xAMTguoPkwAmvQ3Ft3dJpYmetPOgTJeB6zmKyvsj-l3cn0bXnVaonzTbBpheMpbxF7GV~Uowz0cDbKSXTAYxTqjZaCSaKfBhl3DfD1UEkbcQiWsyiXExR20XtlqYYBOvK0-ahtSlXKEmF5hp4vabiTbw2y8H5zFpZBbNc1tY3qcIfOhJ3CLdHZQ0jqb~Xo4qdZ7V5PHE98gGpuWXmWBfsWtXGGqd-4fBIR8T--XYeICdnRTv~erezd0Y~NOYTryWSjH4WzBhXCbqLO9SYEgtLiHrt3cHEk3xPIf5Tw__&Key-Pair-Id=APKAJAGZ7VMH2PFPW6UQ'
        f = urllib2.urlopen(url)
        data = f.read()
        with open("Testmusic"+str(i)+".mp3", "wb") as code:
            code.write(data)
        i=i+1
asdfasdfasdfasdfasdfxzcvz
