#!/usr/bin/python
from os import execvp
import ConfigParser
from re import match
from sys import argv

CONFIGFILE = './smart-browser.cfg'

class smartBrowser():

    def __init__(self):
        # Parse arguments
        self.url = argv[1]

        # Parse config
        self.config = ConfigParser.RawConfigParser()
        self.config.read(CONFIGFILE)

        self.browsers = self.config.items('browsers')
        if self.config.has_section('custom urls'):
            self.urls = self.config.items('custom urls')

        self.browser_open(self.url)

    def browser_open(self, url):

        # Retrieve first candidate for this url
        open_with = None
        for candidate in self.urls:
            if candidate[0].strip('"') in self.url:
                open_with = candidate[1]
                break

        if open_with:
            if ':' in open_with:
                (browser, profile) = open_with.split(':')
            else:
                browser = open_with
                profile = None

            command = [c[1] for c in self.browsers if c[0] == browser][0]
        else:
            #If no preset is found, open with the first configured browser
            browser = self.browsers[0][0]
            command = self.browsers[0][1]
            profile = None

        #Build full command
        browser_args = [command]
        if profile:
            browser_args.append('-P')
            browser_args.append(profile)

        #Launch browser
        browser_args.append(url)
        print "Opening with: ", browser, "Profile: ", profile
        execvp(command, browser_args)

if __name__ == '__main__':
    smartBrowser()
