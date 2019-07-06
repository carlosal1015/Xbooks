#!/usr/bin/env python

from Xbooks_converter.repoClonnerAndFetcher import ClonnerAndFetcher
from Xbooks_converter.repoCommiterAndPusher import CommiterAndPusher

url = "https://github.com/XinYaanZyoy/test_gitpy1.git"

# candf = ClonnerAndFetcher(url)
# print(candf.clone().fetch())

candp = CommiterAndPusher(url)
print(candp.commit().push())