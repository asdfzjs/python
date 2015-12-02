#coding:utf-8
import urllib
path = '<a target="_blank" href="http://www.iteblog.com/archives/1534" title="Hive中order by,Sort by,Distribute by和Cluster By介绍">Hive中order by,Sort by,Distribute by和Cluster By介绍  </a>'
href=path.find('href')
title=path.find('title')
url=path[href+6:title-2]
content=urllib.urlopen(url).read()
filename=url[-4:]+'.html'
file = open(filename, 'w')
file.write(content)
