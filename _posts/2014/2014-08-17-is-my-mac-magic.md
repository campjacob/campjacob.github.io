---
title: Is My Mac Magic?
date: 2014-08-17 16:10
permalink: /blog/2014/8/is-my-mac-magic
tags:
    - Technology
    - Personal
    - Work
    - TCCH BHS
    - Pasco School District
    - Heritage University
    - Keyboard Maestro
    - L-- Tri-Cities Washington
categories:
  - Personal Blog
locations: 
  - Tri-Cities Washington
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: "assets/media/is-my-mac-magic-photo.jpg"
  caption: "Photo credit: A photo of my MacBook Pro taken as I was writing this post at Starbucks off of 390 in Kennewick"
excerpt: "Using Keyboard Maestro to get stuff done on my computer."
---

![Photo of MacBook Pro](/assets/media/is-my-mac-magic-photo.jpg "A Photo of My MacBook Pro")
<p class="caption">A photo of my MacBook Pro taken as I was writing this post at Starbucks off of 390 in Kennewick...</p>




This last week, I had my last day at [Tri-Cities Community Health Behavioral Health Services][0], and my have started some of my training for my work at the [Pasco School District][1]. I've also still been spending quite a bit of time preparing my class lectures for the [Heritage Courses][2] I will be teaching. All that being said, its still a really busy time right now. I figured I'd share some of my geekary from last night that I put together. One of the benefits of being a geek is that can make my computer do magic tricks sometimes, and save myself a lot of hassle and time (although it also means that sometimes I spend a significant amount of time doing things that don't deserve that much time, but that's neither here or there).

The reason I am so in love with my mac, is some of the amazing software and things that I can do with it, that just weren't possible on a Windows PC. I just downloaded [Keyboard Maestro - KM][3], a really powerful and amazing piece of software. I'm very excited to see what I can all automate with it on my mac. I've put together a couple of what KM calls macros. The first one I did was in apple mail to make keyboard like shortcuts. I'm not going to write about about it, but I did the same as described [Stack Exchange][4].

I love my Apple TV, and even like the little four button remote that comes with it. I like to use it even when I'm given presentations as my clicker. The only problem is that it always tries to control my mac. We will be sitting on the couch and watching [Chuck][5], our current show of choice on Netflix, and you click a button and it turns on iTunes or click another button and the volume on my mac goes up and down. It's a bit of a pain to toggle the IR remote on and off. It's kind of hidden in the system preferences. If you are turning it on and off, it might look something like this [short screencast][6]. While it doesn't take way to long, it is kind of an annoying process, and KM can come to the rescue. It wasn't too hard to set it up and automate the process. I created a keyboard short cut that goes though the whole process with minimal needs for me to do anything when turning on and off the remote.

Basically here is what it does:

![A screenshot of my Keyboard Maestro's macro for toggling the IR remote.](/assets/media/keyboard-maestro-macro-ir-remote.png)

A screenshot of my Keyboard Maestro's macro for toggling the IR remote.

1. Click ⇧⌘→
2. Open "Security &amp; Privacy Preferences Pane"
3. Pause for 1.5 seconds (so that it has time to open)
4. Click the gatekeeper lock to unlock the advanced settings
5. Pause until "Advanced button is available" (waiting for me to put in my password)
6. Press "Advanced..." button.
7. Wait for user to (I have to click the check box and pair the IR remote).
8. Click the "Ok" button
9. Re-lock the gatekeeper.
10. Quite the system's preferences pane.

It makes me feel a little bit like my mac does magic for me, so beautiful. You can see the [short screencast][7].

Now, I can just click a couple of keys, and turn on and off my Apple TV Remote when I'm teaching... easy as that.


[0]: http://www.mytcch.org/
[1]: http://www.psd1.org/site/default.aspx?PageID=1
[2]: http://www.heritage.edu/CampusLocations/TriCities.aspx
[3]: http://www.keyboardmaestro.com/main/
[4]: http://apple.stackexchange.com/questions/53254/gmail-like-keyboard-shortcuts-in-mail-app-keys-without-modifiers
[5]: http://www.imdb.com/title/tt0934814/
[6]: https://v.usetapes.com/AxaSINsYsY
[7]: https://v.usetapes.com/KVk70MAAFE