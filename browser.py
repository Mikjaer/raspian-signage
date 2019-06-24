#!/usr/bin/env python

# apt-get install python-webkit python-webkit-dev

import gtk, webkit
 
window = gtk.Window()
window.set_position(gtk.WIN_POS_CENTER)
window.set_size_request(1920,1080)
 
browser = webkit.WebView()
browser.open("http://dashboard.company.com");
window.add(browser);
 
window.show_all()
 
gtk.main()

