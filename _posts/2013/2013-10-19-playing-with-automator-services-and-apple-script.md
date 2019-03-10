---
title: Playing with Automator Services and Apple Script
date: 2013-10-19 01:15
permalink: /blog/2013/10/playing-with-automator-services-and-apple-script
tags:
  - Personal
  - Automator
  - AppleScript
  - Blog Images
  - Mac Power Users
  - Podcasts
  - Wikipedia
  - TextExpander
  - L-- Tri-Cities Washington
categories:
  - Personal Blog
locations: 
  - Tri-Cities Washington
---

![ A Header Image I created for my blog article about my playing with automator & AppleScript ][1] A Header Image I created for my blog article about my playing with automator & AppleScript 

   [1]: /assets/media/Automator-and-AppleScript-Header-Image.jpg

I've never really been a programmer, but I always have been a geek. One thing that I think is kind of cool about my transition from Windows to a Mac has been a lot of the utilities. One utility that I have tried a couple of times to play with, but I haven't found an interesting enough use (or been able to figure out how to do uses that I did want to do). [Automator][2]) on the Mac is a pretty powerful application. Doing some research, there could be some applications that could be downloaded used in Windows, but nothing built in like automator and [services][3].

   [2]: http://en.wikipedia.org/wiki/Automator_(software
   [3]: http://en.wikipedia.org/wiki/Services_menu

There have been several times that [Mac Power Users][4] has talked about automator, but specifically [MPU 070: Working with Automator][5]. Its good, and a great Podcast if your interested.

   [4]: http://www.macpowerusers.com/
   [5]: http://www.macpowerusers.com/2012/01/22/mpu-070-working-with-automator/

Another application that I have been loving has been [TextExpander][6]. For some reason, with all of my popup select features (I think it's because I'm syncing it with [Phrase Express][7] on Windows). I created a service which uses an [AppleScript][8] which searches copied text for the "`|`" and replaces it with ":" a pretty simple apple script is below (Its probably not very efficient, but it's my first one.
    
   [6]: http://smilesoftware.com/TextExpander/index.html
   [7]: http://www.phraseexpress.com/
   [8]: http://en.wikipedia.org/wiki/AppleScript


	on replace_chars(this_text, search_string, replacement_string)
	        set AppleScript's text item delimiters to the search_string
	        set the item_list to every text item of this_text
	        set AppleScript's text item delimiters to the replacement_string
	        set this_text to the item_list as string
	        set AppleScript's text item delimiters to ""
	        return this_text
	    end replace_chars
	    
	    
	    set the message_text to get the clipboard
	    set the message_text to replace_chars(message_text, "|", ":")
	    
	    return message_text
    

