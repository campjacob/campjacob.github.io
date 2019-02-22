---
layout: single
title: Mileage Tracking Form and Launch Center Pro
date: 2014-08-30 20:55
permlink: /blog/2014/8/mileage-tracking-form-and-launch-center-pro
category: Blog
locations: 
  - Tri-Cities Washington
---

feature_row:
  - image_path: /assets/media/iphone-launch-center-pro-action-screen.png
    alt: "A screenshot of the new action screen blank and ready to be set up"
    title: "New Action Screen"
    excerpt: "A screenshot of the new action screen blank and ready to be set up. iPhone mock-up thanks to [Pixel Den](href="http://www.pixeden.com/psd-mock-up-templates/iphone-5s-psd-vector-mockup)"
  - image_path: /assets/media/iphone-launch-center-pro-action-screen-mileage-tracker.png
    alt: "A screenshot of my completed action"
    title: "Completed Action"
    excerpt: "A screenshot of my completed action. You can have it go through and make a list, or add text or a number. iPhone mock-up thanks to [Pixel Den](http://www.pixeden.com/psd-mock-up-templates/iphone-5s-psd-vector-mockup)"
  - image_path: /assets/media/iphone-launch-center-pro-action-screen-list.png
  	alt: "A screenshot of my list in action"
    title: "List in Action"
    excerpt: "A screenshot of my list in action. Two clicks and I'm done... iPhone mock-up thanks to [Pixel Den](href="http://www.pixeden.com/psd-mock-up-templates/iphone-5s-psd-vector-mockup)"
 
tags: 
	- "Technology"
	- "Personal"
	- "Professional"
	- "Launch Center Pro"
	- "Google"
	- "Google Drive"
	- "Mac Power Users" 
location: "Tri-Cities Washington"


![Mileage Tracking with Launch Center Pro, IFTTT and Google Sheets](/assets/media/mileage-tracking-lauch-center-pro-ifttt-google-sheets.jpg "Mileage Tracking with Launch Center Pro, IFTTT and Google Sheets")

On [my favorite podcast][0], [Mac Power Users][1] I feel like I've heard about [Launch Center Pro][2] a number of times. I've thought about purchasing it a number of times, because I really like the concept automation. I've kept putting off purchasing it because I didn't know exactly what I would do with it. I use [Drafts][3] all of the time on my iPhone and my iPad, and it's always seemed like enough.

I was reading Dr. Drang's article [Late to Launch][4] earlier today, and decided that I did need to buy Launch Center Pro (LCP). I figured that it was ok, because he is late coming to LCP too.

Basically LCP is an iPhone / iPad app that launches other applications or does tasks within those application. It also gives interaction for IFTTT (which I talked [about here][5]), which opens up so many other possibilities.

In reading Dr. Drang's article, I decided that I needed a simple way to track my mileage. Whenever I go in between schools at my new job, I can submit for a reimbursement for the gas and wear and tear on my car. They don't require a listing of miles driven, but from one building to another building (the school district dictates what the milage is between buildings, for those people who tend to drive circuitous routes). For last month, I went through my calendar and tried to pick out the days that I drove between different buildings. I'm excited about my new system using LCP and think I will save myself time. One of my co-workers told me that she never has time to fill out her form, so maybe I will have to share this with her.

For all of the non nerds out there, this might sound kind of complicated, but really it is not, and it's kind of fun to put together. I'll walk you through what I did. Basically I have an action in LCP that opens two lists which I select from which schools I'm drive from and to, sends those as a row in a Google spreadsheet, and then at the end of the month, IFTTT sends me an email with a link to the spreadsheet to remind me to copy and past it onto the correct from.

{% include feature_row %}

The first step is to create a new action in LCP. I just went through their action composer, found the IFTTT trigger, had it complete a Trigger Recipe with Values. I named my Recipe "Mileage Tracker" (I had to name it the same thing when creating my recipe on IFTTT). Then I set two values as "input with a list." I made list items of each of the schools that I might go from so that one list is the school building I was leaving and the second would be the school building I would be going to.

![My IFTTT recipe](/assets/media/ifttt-screenshot-launch-center-pro.png "My IFTTT recipe.")

My [IFTTT Recipe](https://ifttt.com/recipes/199280-create-mileage-entry-from-launch-center-pro-and-google-drive)

Then the IFTTT magic starts. It sends my answers to an IFTT recipe where it appends a spreadsheet in Google docs to add the new data (along with the date) to cells in the the spreadsheet. I made a second IFTT rule sending my work email an notification every month on the last day to complete copy and paste the values from the Google Docs to the appropriate spreadsheet and turn it in to receive my reimbursement.

After I got it all working, I was super excited. It feels amazing to know that I can track my mileage with a couple of clicks on my phone and I won't ever have to worry about it again. I might have to think about making it based on location... but we will see so that I don't even have to click anything on my phone.

[0]: http://jacobrcampbell.com/blog/2014/4/jump-in-the-stream-favorite-podcasts
[1]: http://www.macpowerusers.com/
[2]: http://contrast.co/launch-center-pro/
[3]: http://agiletortoise.com/drafts/
[4]: http://www.leancrew.com/all-this/2014/08/late-to-launch/
[5]: http://jacobrcampbell.com/blog/2013/1/new-and-fun-functionality