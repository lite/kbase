# -*- coding: utf-8 -*- 
#print u"你好"

import re
import urllib2

def spider_root(host):
    url = "%s/lofi/" %(HOST)    
    print(url)
    f = urllib2.urlopen(url)
    txt = f.read().decode('utf-8')
    handle_root(txt)

"""
def handle_root(root):
    #r = re.compile(r'<li><strong>(.+?)</strong></li>.+?</ul>', re.MULTILINE|re.DOTALL)
    r = re.compile(r'<li><strong>(.+?)</strong></li>.+?<ul>\s+(.+?)\s+</ul>', re.MULTILINE|re.DOTALL)
    #r = re.compile(r"<li><strong>(?P<title>.+?)</strong></li>.+<ul>", re.MULTILINE|re.DOTALL)
    if 0:
        matches = r.findall(root)
        print(matches)
    else:
        matches = r.finditer(root)
        for match in matches:
            print "%s: %s %s" % (match.start(), match.group(1), match.group(2))
    return
"""
    
def handle_root(root):
    # <li><strong>Category</strong></li> 
    # <ul><li><a href="/forum/1/lofi">Forum</a> <span class="desc">(3 posts)</span></li> 
    # </ul>
    #r = re.compile(r'<li>.+</li>')
    r = re.compile(r'<li><strong>(?P<title>.+?)</strong></li>.+?<ul>\s+(?P<topics>.+?)\s+</ul>', re.MULTILINE|re.DOTALL)
    #r = re.compile(r'<ul>.+</ul>', re.MULTILINE|re.DOTALL)
    #r = re.compile(r'<ul>(?P<topics>.+?)</ul>', re.MULTILINE|re.DOTALL)
    #r = re.compile(r'<li><strong>(?P<category>.+)</strong></li>\s+<ul>(?P<topics>.+)</ul>')
    matches = r.finditer(root)
    for m in matches:
        title = m.group('title')
        #print("==", title)
        topics = m.group('topics')
        #print("----", topics)
        handle_categories(topics)
    
def handle_categories(categories):
    # <li><a href="/forum/1/lofi">Forum</a> <span class="desc">(3 posts)</span></li> 
    r = re.compile(r'<li><a href=".*?/(?P<categroy>\d+)/lofi">(?P<title>.+?)</a>.+?</li>', re.MULTILINE|re.DOTALL)
    matches = r.finditer(categories)
    for m in matches:
        categroy = m.group('categroy')
        title = m.group('title')
        #print('++++++', categroy, title)
        spider_topics_pages(categroy)
        
def spider_topics_pages(categroy):
    # http://support.djangobb.org/3/lofi/
    url = "%s/%s/lofi/" %(HOST, categroy)
    print(url)
    f = urllib2.urlopen(url)
    txt = f.read().decode('utf-8')
    handle_topics_pages(categroy, txt)
    
def handle_topics_pages(categroy, topics):
    # <div class="djangobbpagespan"> 
    #   <a href="?page=1">1</a> 
    #   <a href="?page=2">2</a> 
    # </div> 
    #print(topics)
    #r = re.compile(r'<div class="djangobbpagespan">(?P<pages>.+?)</div>', re.MULTILINE|re.DOTALL)
    r = re.compile(r'<div class="djangobbpagespan">\s+(?P<pages>.+?)\s+</div>', re.MULTILINE|re.DOTALL)
    match = r.search(topics)
    if match:
        txt = match.group('pages')
        #print(txt)
        r = re.compile(r'<a href="\?page=(?P<page>\d+)">(.+?)</a>', re.MULTILINE|re.DOTALL)
        matches = r.finditer(txt)
        for m in matches:
            page = m.group('page')
            #print('++++++', categroy, page)
            spider_topics(categroy, page)

def spider_topics(categroy, page):
    # http://192.168.1.113:8000/forum/1/lofi/?page=1
    url = "%s/%s/lofi/?page=%s" %(HOST, categroy, page)
    #print(url)
    f = urllib2.urlopen(url)
    txt = f.read().decode('utf-8')
    handle_topics(txt)
            
def handle_topics(topics):
    # <li><a href="/forum/topic/1/lofi">Subject</a> <span class="desc">(2 replies)</span></li> 
    r = re.compile(r'<li><a href=".*?/topic/(?P<topic>\d+)/lofi">(?P<title>.+?)</a>.+?</li>', re.MULTILINE|re.DOTALL)
    matches = r.finditer(topics)
    for m in matches:
        topic = m.group('topic')
        title = m.group('title')
        #print('********', topic, title)
        spider_posts_pages(topic)

def spider_posts_pages(topic):
    # http://support.djangobb.org/topic/24/lofi/
    url = "%s/topic/%s/lofi/" %(HOST, topic)
    print(url)
    f = urllib2.urlopen(url)
    txt = f.read().decode('utf-8')
    handle_posts_pages(topic, txt)

def handle_posts_pages(topic, posts):
    # <div class="djangobbpagespan"> 
    #   <a href="?page=1">1</a> 
    #   <a href="?page=2">2</a> 
    # </div>
    r = re.compile(r'<div class="djangobbpagespan">\s+(?P<pages>.+?)\s+</div>', re.MULTILINE|re.DOTALL)
    match = r.search(posts)
    if match:
        txt = match.group('pages')
        r = re.compile(r'<a href="\?page=(?P<page>\d+)">(.+?)</a>', re.MULTILINE|re.DOTALL)
        matches = r.finditer(txt)
        for m in matches:
            page = m.group('page')
            print('++++++', topic, page)
        spider_posts(topic, page)
        
def spider_posts(topic, page):
    # http://support.djangobb.org/topic/24/lofi/?page=2
    url = "%s/topic/%s/lofi/?page=%s" %(HOST, topic, page)
    print(url)
    f = urllib2.urlopen(url)
    txt = f.read().decode('utf-8')
    handle_posts(txt)

def handle_posts(posts):
    # <div class='postwrapper'> 
    #   <div class='posttopbar'> 
    #     <div class='postname'>lorien</div> 
    #     <div class='postdate'>Jan. 5, 2010 16:02:36</div> 
    #   </div> 
    #   <div class='postcontent'> 
    #       User could change its own reputation<br/>
    #       Prooflink: <a href="http://support.djangobb.org/reputation/lorien/"rel="nofollow">http://support.djangobb.org/reputation/lorien/</a> 
    #   </div> 
    # </div>
    # r = re.compile(r"<div class='postwrapper'>\s+<div class='posttopbar'>\s+<div class='postname'>(?P<postname>.+?)</div>\s+<div class='postdate'>(?P<postdate>.+?)</div>\s+</div>\s+<div class='postcontent'>(?P<postconent>.+?)</div>\s+</div>", re.MULTILINE|re.DOTALL)
    #print(posts)
    r = re.compile(r"<div class='postwrapper'>\s+<div class='posttopbar'>\s+<div class='postname'>(?P<postname>.+?)</div>\s+<div class='postdate'>(?P<postdate>.+?)</div>\s+</div>\s+<div class='postcontent'>(?P<postconent>.+?)</div>\s+</div>", re.MULTILINE|re.DOTALL)
    matches = r.finditer(posts)
    for m in matches:
        postname = m.group('postname')
        postdate = m.group('postdate')
        postconent = m.group('postconent')
        print('########', postname, postdate)
        print('########:', postconent)

#HOST = "http://192.168.1.113:8000/forum"
HOST = "http://support.djangobb.org"

if __name__ == '__main__':
    #spider_root(HOST)
    #spider_topics_pages(3)
    #spider_topics(3, 2)
    #spider_posts_pages(24)
    spider_posts(24, 2)
    