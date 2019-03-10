---
title: Tracking Trainings Using Drafts and Launch Center Pro
date: 2014-11-14 23:55
permalink: /blog/2014/8/mileage-tracking-form-and-launch-center-pro
tags:
    - Technology
    - Personal
    - Professional
    - Drafts
    - Launch Center Pro
    - L-- Tri-Cities Washington
categories:
    - Personal Blog
    - Professional Blog
locations:
    - Tri-Cities Washington
---

![Graphic of Blocks Saying Learn](/assets/media/track-your-trainings-learn-blocks.jpg "Track Trainings for CEUs and Clock Hours Using Drafts 4 & Launch Center Pro")

A couple of weeks ago, I spent some times further diving into [Drafts][0] and [Launch Center Pro][1]. Both are amazing applications for iOS, and have greatly improved my productivity and ability to get things done. I have been absolutely loving my [Milage Tracker][2] that I put together, and use it multiple times a day (and find that it makes it so I don't forget to track). As I have written before, I'm a big fan of using plain [text files and Markdown][3].

Several years ago, when I started working at Tri-Cities Community Health Behavioral Health Services, and attending various trainings post MSW I started keeping a word document listing all of the various trainings that I attend. If you work in an industry that requires documentation regarding trainings received, hopefully you have started doing that too. I since have change my system around. I now have a plain text file that I keep on dropbox which has a listing of every training that I have received (whether that be in agency or for some sort of professional development certificate). As I have been looking towards applying for my [LICSW][4] and having my [ESA][5] which requires so many clock hours, I decided that I wanted to also have an easy way to calculate how many CEU's or Clock Hours without combing through my long text file of all my trainings. I created two [CSV files][6] which I could open in Excel or Numbers and have calculate the total number of hours easily. The problem is, I didn't want to have to write entries sometimes three times. I also wanted to be able to add these entries either from my phone or from my iPad easily when I get to the training. Never having to worry about it again.

With so many iOS automation tasks that I do, it starts in Launch Center Pro (LCP) for me. I have a main entry that collects data in several prompts (you [can install it][7]). The content is as follows:

    launch://x-callback-url/clipboard?text=[prompt:Review=[prompt:Date], [prompt:Training Title], [prompt-num:Number of CEUs or Clock Hours] [list:Type|Clock Hours=Clock Hours|CEUs=CEUs|Both=Clock Hours and CEUs], [list:Type of Units|Ethics= Professional Law and Ethics|Suicide=Suicide Assessment Treatment and Management|General=General Continuing Education Credits|None=|ESA Suicide=ESA Suicide Prevention Intervention Training]]
    

It creates a final review prompt that includes text regarding the training date, the title of the training, the number of hours, and the type of hours (i.e. Professional Law and Ethics or Suicide Assessment Treatment and Management). 

I have this LCP action in my "base" actions folder along with a couple of different actions related to my trainings. All of them send the contents to Drafts for different actions. One action posts the clipboard to an action that appends it to my Clock Hour CSV, one to my CEU CSV, and one to my text file. I then have a main action that calls all of the other actions and let me select if I want to post it to one, two or all three of the actions.

The two actions that I have which append to my Clock Hour CSV and my CEU CSV files are very simple and just append to the files. There are two actions to append to my overall text file. One action takes the comma separated data and uses some JavaScript to split the text at each ", " and return the text with each section as a new line. You can [install the drafts action][8] or see the JavaScript below:

    // Function to Parse Comma Separated Value Text
    // Jacob Campbell -- http://jacobrcampbell.com/
    
    function parseText(s){
        var temp = new Array();
        temp = s.split(', ');
          var result = "";
          var i;
        for(i=0; i<temp.length; i++) {
            result += temp[i] + "\n";
        }
    return result;
    }
    
    // Commit content to draft
    
    var text = draft.content;
    draft.content = parseText(text);
    commit(draft);
    

The drafts action then passes that data to another action which takes those new lines and adds it to a template page that has the following information:

    ## [[line|2]]
    * __Date__: [[line|1]]  
    * __Location__:   
    * __Facilitator__:   
    * __CEU / Clock Hours__: [[line|3]], [[line|4]]  
    * __Duration__:   
    * __Certificate of Completion__:

Each of the the parts that say `[[line|n]]` takes that line from the draft and puts it there. I then add the last little bit of information (i.e. location, who facilitated it... etc) and I'm all done.

What is amazing, is I can write it once in LCP, have it post to both CSV files and then prepare it for posting it to my text file with only typing minimal text. I have taken it to another level, and have made some OmniFocus task templates that I can post and remember to follow up and see if I have received my confirmation form for my clock hours.

If you have the need to track your clock hours or CEU's its a pretty awesome system, and I'd highly encourage you steal what I have put together and change it for your own needs. 

[0]: http://agiletortoise.com/drafts/
[1]: http://contrast.co/launch-center-pro/
[2]: /blog/2014/8/mileage-tracking-form-and-launch-center-pro
[3]: /blog/2014/3/review-of-david-sparkss-markdown-book-an-investigation-to-formatting-documents
[4]: http://www.doh.wa.gov/LicensesPermitsandCertificates/ProfessionsNewReneworUpdate/SocialWorker/LicenseRequirements/LicensedIndependentClinicalSocialWorker
[5]: https://www.k12.wa.us/certification/ESAMain.aspx
[6]: http://en.m.wikipedia.org/wiki/Comma-separated_values
[7]: https://launchcenterpro.com/t4zs0x
[8]: http://drafts4-actions.agiletortoise.com/a/1NF