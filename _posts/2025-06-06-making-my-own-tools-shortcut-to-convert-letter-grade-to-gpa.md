---
title: "Making My Own Tools: Shortcut to Convert Letter Grade to GPA"
name: 2025-06-06-making-my-own-tools-shortcut-to-convert-letter-grade-to-gpa.md
date: 2025-06-06 14:55:36
tags:
  - Shortcuts
  - Heritage University
  - Nerd
  - Professional
  - L-- Tri-Cities Washington
locations: 
  - Tri-Cities Washington
categories:
  - Personal Blog
  - Professional Blo
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/media/2025-06-06-shortcut-to-convert-letter-grade-to-gpa-header-1900x600.jpg
  teaser: /assets/media/2025-06-06-shortcut-to-convert-letter-grade-to-gpa-header-500x300.jpg
  caption: "Photo credit: Image by [**Jacob Campbell**](https://vsp.ink/hub)."
excerpt: "Making my own tools to do my work is so satisfying."
---

I would argue that social workers and university faculty align well with the concept of being a [Knowledge Worker](https://en.wikipedia.org/wiki/Knowledge_worker). A lot of the work that we do, apart from the directly engaged in practice, requires assessment, making connections, developing and modifying strategies, and more. We have a lot of information that we receive and must do something with it. Over the years, the writing of [Cal Newport](https://calnewport.com) has been impactful in thinking about how I should be working (especially Slow Productivity and Deep Work). When I was going through my Ph.D. program, I talked about these approaches [as necessary skills for completing my program](/resources/essays/a-look-into-personality-self-creation-and-self-care/).

One way I manage information is by developing my systems and methods for organizing my data, tasks, and sharing and planning. My systems are [sometimes convoluted and complicated](https://jacobrcampbell.com/blog/2025/03/building-services-for-my-students/). I find it gratifying and valuable to build my tools and systems. Sometimes, these can be quick little things. These little helper tools probably provide me the most return on the investment of time and effort than anything that is a much larger project (as those I might sink hours, days, and even sometimes weeks) into making something work.

![Photo of 3D Printed Cardboard Construction Tools](/assets/media/2025-06-06-3d-printed-cardboard-crafting-tools.jpeg "Photo of 3D Printed Cardboard Construction Tools")
It can even be fun to build my own tools out of plastic, like you can see these cardboard construction tools I printed for making things with my daughter (find the file on Makerworld [Cardboard Crafting Tools](https://makerworld.com/en/models/829210-cardboard-crafting-tools)).

This week, I have had a few meetings with students to talk about grades. Our advising views only provide letter grades (e.g., A, A-, B, etc.). At a master's level, students are expected to maintain a **3.0 or higher**, and their graduate-level career GPA must also meet that same standard. Because they only provide letter grades and the average for the GPA, it is hard to discuss how future grades (or retaking a class to improve your grade) might impact a student's career GPA.

I made a [shortcut](https://support.apple.com/guide/shortcuts/welcome/ios) to be able to provide an input of letter grades, and it will provide a GPA score. It isn't an overly complicated Shortcut. It does the following:

- Create a dictionary that defines each letter grade with its GPA value
- Asks for me to provide a list of grades, each on a new line
- Converts those to uppercase (if I don't add the letter grade in the proper format)
- Splits each line of letter grades so they can be reviewed individually
- Gets the value of the letter grade from the dictionary
- Split each line of GPA values so they can be calculated into an average
- Shows the results

It was super simple to create. Because I decided to share this with my colleagues in case they find it useful, I wanted to try to make it error-free (I suppose they could not enter the grades as new lines, but the directions instruct you to do so). But what happens if they enter one and it isn't uppercase to match the dictionary key? I accounted for that. I thought I would need to do something in case they add something that isn't a usable letter grade (consider P for pass or I for incomplete). I started to try to have ChatGPT assist me in writing out some complicated [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) to do this. Still, I figured out that because I am only getting the values from the dictionary, only letters included in the keys get passed to the next step, so it automatically removes them.

You can find the [Calculate GPA from Letter Grades](https://www.icloud.com/shortcuts/ef595853395747378f078c9a9b664c20). It does feel gratifying to have a simple tool that I can use to do this.