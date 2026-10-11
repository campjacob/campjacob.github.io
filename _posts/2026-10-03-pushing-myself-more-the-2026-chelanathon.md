---
title: Pushing Myself More - The 2026 Chelanathon
name: 2026-10-03-pushing-myself-more-the-2026-chelanathon.md
date: 2026-10-03 12:00:00
tags:
  - Personal
  - Health
  - Self Care
  - L-- Lake Chelan Washington
  - L-- Leavenworth Washington
  - L-- Tri-Cities Washington
locations:
  - Lake Chelan Washington
  - Leavenworth Washington
  - Pasco Washington
categories:
  - Personal Blog
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/media/2026-10-03-chelanathon-header-1600x600.png
  teaser: /assets/media/2026-10-03-chelanathon-teaser-500x300.jpg
  caption: "My 2026 Chelanathon finisher medal, with Lake Chelan behind it in Manson."
excerpt: "On September 19th I swam half a mile in Lake Chelan, biked 12 miles through the orchards above Manson, and ran a 5K to the finish line of the Chelanathon Sprint Triathlon. Three months earlier I had sat down and started a planning document."
gallery:
  - url: https://fitpub.social/activities/d4d38d71-7b94-41b9-b1e4-4ce823bce555
    image_path: /assets/media/2026-09-19-chelanathon-swim-fitpub.png
    alt: "FitPub summary of the Chelanathon swim: 1.30 km by watch in 34:13, average heart rate 139 bpm, Lake Chelan"
    title: "Swim on FitPub"
  - url: https://fitpub.social/activities/155082a0-bf10-41f8-8493-168e079b172d
    image_path: /assets/media/2026-09-19-chelanathon-bike-fitpub.png
    alt: "FitPub summary of the Chelanathon bike: 21.19 km loop around Manson past Wapato and Roses Lakes in 1:31:58, 203 m of climbing"
    title: "Bike on FitPub"
  - url: https://fitpub.social/activities/94ea2e9e-6c8e-4594-8cdb-d6d29cb652dd
    image_path: /assets/media/2026-09-19-chelanathon-run-fitpub.png
    alt: "FitPub summary of the Chelanathon run: 5.13 km in 46:40, average heart rate 150 bpm"
    title: "Run on FitPub"
---

In mid-June, I started thinking about what felt like a crazy idea. I have a [niece who is also a therapist](https://www.hanancounseling.com), and she is very involved in the connection between mental health and physical health. She does races and does some health influencer activities. We were at my concuña's birthday party. Hearing about some of her experiences, I think, started me thinking (even though I didn't immediately decide I wanted to do my own race).

I have also honestly felt very stagnant with my health and fitness. I have been feeling like I can't make any real or meaningful change. While I'm very active, I really need to lose some weight to be as healthy as I can be. I started thinking about trying something new. My weight has been increasing slowly over the last few years even though I consistently go and walk in the evenings and very inconsistently go to the gym. I decided I needed something to motivate myself. 

So I started planning to do a race, and I decided I wanted to do a triathlon. As I started looking into options, I realized there are different lengths. An Ironman is crazy: it includes a full marathon (42.2 km) run, along with a 3.9 km swim and a 180.2 km bike ride. While I would like to build up to doing an Olympic race (a 1.5 km swim, a 40 km bike ride, and a 10 km run), there is a smaller length that can be done as well, the sprint. This is what I did, but I definitely did not sprint through it as it took me 2 hours, 52 minutes, and 1 second to finish.

The race distances for the Chelanathon Sprint were:

- **Swim**: 0.5 mile (805 m)
- **Bike**: 12.1 miles (19.5 km)
- **Run**: 3.1 miles (5.0 km)

## Training and Working Toward It

Just under 90 days before the race, I decided that I wanted to do it and started a planning document. While I watched some videos and read some articles, a lot of my planning and thinking about this event was done with the support of AI. I had no idea how to train, how to think about things, or what I might need to do. Questions like how the transition works or how to build up my training really helped me conceptualize this.

I wanted to push myself harder than I normally do, with a goal to just finish the race. My hope is that this can jump-start my efforts to improve my physical fitness and health. Although I've only lost a small amount of weight in the last couple of months, I am still really glad to have participated. I've always loved swimming as exercise (though I didn't get to do it as much during this summer's training), but I've now decided that I do like running. I logged every workout from June 22 (when I made the final decision to do the event) through race day, and it added up to:

| | Sessions | Distance |
| --- | --- | --- |
| Swim | 5 | about 5,800 m |
| Bike | 18 | about 190 miles |
| Run | 19 | about 49 miles |
| Walk | 44 | about 58 miles |
| Hike | 2 | about 5.7 miles |
| **Total logged workouts** | **99**[^1] | |

[^1]: These include the race itself and a handful of strength and yoga sessions in the workout count.

Comparing early summer to the four weeks before the race showed real progress:

| | May–June | Late Aug – early Sep | Change |
| --- | --- | --- | --- |
| Swim pace | ~3:10 /100m | **2:52 /100m** | about 18 seconds faster per 100 m |
| Bike speed | ~7.1 mph | **10.0 mph** | about 41% faster |
| Run pace | ~16:06 /mile | **14:32 /mile** | about 1.5 minutes faster per mile |

## Race Day

Here is the course as my watch recorded it: the swim along the Manson shoreline, the bike loop up past Wapato and Roses Lakes, and the run back to the finish. Hover over a leg for its official time.

<div id="chelanathon-map" style="height: 460px; border-radius: 8px; margin: 1em 0 0.25em;"></div>
<p style="font-size: 0.75em; color: #777; margin-top: 0;">GPS tracks from my Apple Watch via <a href="https://fitpub.social/users/campjacob">FitPub</a>. Watch distances run a little long, especially in open water.</p>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function () {
  var tracks = {"swim":[[47.87803,-120.12867],[47.87783,-120.12863],[47.87768,-120.12849],[47.87753,-120.1284],[47.87747,-120.12839],[47.87741,-120.12841],[47.87738,-120.12904],[47.87764,-120.1296],[47.8775,-120.13],[47.87755,-120.13033],[47.87752,-120.13033],[47.87752,-120.13038],[47.8776,-120.13047],[47.87774,-120.13052],[47.87781,-120.1308],[47.87779,-120.13108],[47.87773,-120.13112],[47.87767,-120.13124],[47.87767,-120.13166],[47.87773,-120.13164],[47.87779,-120.13156],[47.87769,-120.13178],[47.87765,-120.132],[47.87766,-120.13207],[47.87758,-120.13201],[47.87761,-120.13209],[47.87775,-120.13224],[47.87777,-120.13231],[47.8777,-120.13282],[47.87772,-120.13287],[47.87771,-120.13281],[47.87765,-120.13298],[47.87763,-120.13299],[47.87763,-120.13276],[47.87768,-120.13252],[47.8776,-120.13234],[47.87753,-120.13204],[47.87756,-120.13177],[47.87749,-120.13142],[47.87747,-120.1312],[47.87749,-120.13114],[47.87746,-120.13084],[47.87748,-120.13065],[47.87735,-120.12995],[47.87734,-120.12955],[47.87727,-120.12925],[47.87729,-120.12906],[47.87724,-120.12879],[47.87726,-120.12867],[47.8773,-120.12861],[47.87737,-120.12857],[47.8775,-120.12859],[47.8776,-120.12868],[47.87794,-120.12858],[47.87806,-120.1286],[47.8781,-120.1287],[47.87819,-120.12873],[47.87848,-120.12871],[47.87864,-120.12872],[47.87892,-120.12869],[47.87897,-120.12864],[47.87897,-120.12853],[47.87897,-120.12857],[47.879,-120.12851],[47.87899,-120.12855],[47.87901,-120.12853]],"bike":[[47.88004,-120.12768],[47.88043,-120.12786],[47.88071,-120.12822],[47.88083,-120.12861],[47.88074,-120.1293],[47.88097,-120.12954],[47.88109,-120.1293],[47.88112,-120.12629],[47.88015,-120.1229],[47.87804,-120.11895],[47.87433,-120.11017],[47.87441,-120.10988],[47.87638,-120.11038],[47.87732,-120.11134],[47.88118,-120.11455],[47.88178,-120.11556],[47.88237,-120.1178],[47.88316,-120.11746],[47.88344,-120.11764],[47.8836,-120.11859],[47.88499,-120.12105],[47.88511,-120.12177],[47.88488,-120.12307],[47.88496,-120.12454],[47.88542,-120.12635],[47.88592,-120.12725],[47.887,-120.12804],[47.88759,-120.12959],[47.88835,-120.12974],[47.88868,-120.13009],[47.88896,-120.13079],[47.8892,-120.13246],[47.88942,-120.13299],[47.89057,-120.13378],[47.89318,-120.13496],[47.89358,-120.13503],[47.89463,-120.1348],[47.89489,-120.13492],[47.8987,-120.14053],[47.89868,-120.14097],[47.89629,-120.1454],[47.89586,-120.14796],[47.89598,-120.14916],[47.89797,-120.15377],[47.89933,-120.15435],[47.90013,-120.1555],[47.90256,-120.16049],[47.90393,-120.16267],[47.90486,-120.1647],[47.90551,-120.1656],[47.90631,-120.16779],[47.90829,-120.17229],[47.91019,-120.17596],[47.91119,-120.17709],[47.91501,-120.18032],[47.91756,-120.18333],[47.92113,-120.18903],[47.92241,-120.18986],[47.92481,-120.19033],[47.9253,-120.19073],[47.9257,-120.1923],[47.92625,-120.19362],[47.92595,-120.19513],[47.92472,-120.19629],[47.92356,-120.19653],[47.92216,-120.19603],[47.92142,-120.19553],[47.92062,-120.1955],[47.91991,-120.19525],[47.9191,-120.19635],[47.91808,-120.19734],[47.91772,-120.19756],[47.91723,-120.19757],[47.91462,-120.19595],[47.90758,-120.19199],[47.90634,-120.19104],[47.90404,-120.18882],[47.90218,-120.18811],[47.89844,-120.18782],[47.89833,-120.18714],[47.89876,-120.1855],[47.90047,-120.18368],[47.90035,-120.18209],[47.89704,-120.17698],[47.89635,-120.17517],[47.89563,-120.17215],[47.89442,-120.16956],[47.89319,-120.16858],[47.89126,-120.16774],[47.8903,-120.16787],[47.88669,-120.16953],[47.88607,-120.1692],[47.88565,-120.16844],[47.88557,-120.16766],[47.88624,-120.16557],[47.88627,-120.1643],[47.88104,-120.14008],[47.88108,-120.12975],[47.88077,-120.12934],[47.88077,-120.12833],[47.88022,-120.12769],[47.87947,-120.12752],[47.87906,-120.12811],[47.87841,-120.12865],[47.8789,-120.12871],[47.879,-120.12855]],"run":[[47.87911,-120.12843],[47.87929,-120.12806],[47.87937,-120.12774],[47.87972,-120.1276],[47.88021,-120.12775],[47.88033,-120.12782],[47.88056,-120.12806],[47.88074,-120.12836],[47.8808,-120.12867],[47.88071,-120.12912],[47.88072,-120.12938],[47.88078,-120.12952],[47.88094,-120.12965],[47.88102,-120.12982],[47.88106,-120.13239],[47.88097,-120.13998],[47.88093,-120.14002],[47.8794,-120.13999],[47.87896,-120.14004],[47.8779,-120.14001],[47.87771,-120.14012],[47.87762,-120.14028],[47.87762,-120.14043],[47.87985,-120.15085],[47.87999,-120.15106],[47.88011,-120.15111],[47.88139,-120.15109],[47.88136,-120.15117],[47.88124,-120.15121],[47.88007,-120.15119],[47.87989,-120.15113],[47.87981,-120.15103],[47.87755,-120.14049],[47.87755,-120.14024],[47.8776,-120.14006],[47.8777,-120.13996],[47.87784,-120.13991],[47.88065,-120.13995],[47.88094,-120.13994],[47.88099,-120.13989],[47.88107,-120.13266],[47.88106,-120.13036],[47.88099,-120.12971],[47.88096,-120.12965],[47.88081,-120.12955],[47.88075,-120.12941],[47.88084,-120.12873],[47.88083,-120.12844],[47.88072,-120.12817],[47.88049,-120.12787],[47.8802,-120.12765],[47.87927,-120.12742],[47.87911,-120.1275],[47.87896,-120.12768]]};
  var legs = [
    ["swim", "Swim · 805 m · 28:23", "#1f9bd1"],
    ["bike", "Bike · 12.1 mi · 1:31:48", "#e5007e"],
    ["run",  "Run · 3.1 mi · 46:27",  "#ff8c1a"]
  ];
  var map = L.map("chelanathon-map", { scrollWheelZoom: false });
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: "&copy; <a href=\"https://www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors"
  }).addTo(map);
  var group = L.featureGroup().addTo(map);
  legs.forEach(function (leg) {
    L.polyline(tracks[leg[0]], { color: "#fff", weight: 8, opacity: 0.8 }).addTo(group);
    L.polyline(tracks[leg[0]], { color: leg[2], weight: 5, opacity: 0.95 })
      .bindTooltip(leg[1], { sticky: true }).addTo(group);
  });
  L.circleMarker(tracks.run[tracks.run.length - 1], { radius: 8, color: "#fff", weight: 2, fillColor: "#222", fillOpacity: 1 })
    .bindTooltip("Finish · 2:52:01").addTo(group);
  map.fitBounds(group.getBounds(), { padding: [20, 20] });
  var legend = L.control({ position: "bottomright" });
  legend.onAdd = function () {
    var div = L.DomUtil.create("div");
    div.style.cssText = "background: rgba(255,255,255,0.92); padding: 6px 10px; border-radius: 6px; font: 12px/1.6 system-ui, sans-serif; box-shadow: 0 1px 4px rgba(0,0,0,0.3);";
    div.innerHTML = legs.map(function (leg) {
      return '<span style="display:inline-block;width:14px;height:4px;background:' + leg[2] + ';vertical-align:middle;margin-right:6px;"></span>' + leg[1];
    }).join("<br>");
    return div;
  };
  legend.addTo(map);
})();
</script>

I wasn't super happy with my final swim time. I only practiced once with a wetsuit before the race. The water was also very cold (64°F). For the first 400 m, I couldn't really swim normally. Not only was it chaotic being in the middle of everyone, but I also felt like I couldn't catch my breath (because of the cold). I actually thought I might not be able to make it and I might have to quit. But as I got closer to the place where we had to start coming back, I started feeling more comfortable and like I could actually swim.

After swimming my half mile in Lake Chelan, I biked 12 miles through the vineyards and orchards around Manson. There were a lot more hills than I trained on, and I am still slow on the bike. My bike is a gravel bike, not really the type used for these kinds of races, but I loved seeing all of the little lakes that we passed through. There was one hill I had to get off and walk part of the way up, but for the rest I kept a steady pace. It was also sad that we passed somebody (who appeared much more fit than me) who was receiving CPR from emergency responders at the top of the last hill overlooking the lake. After pulling into the transition space, I parked my bike and started running (more like a jog and a bit of a limp to start off with). It was 5K to the finish line. 

The first time I recorded a 5K run on my watch was about two months earlier. [First time running 5K...](https://social.vsp.ink/@Jacob/116933722892527559)

<blockquote class="mastodon-embed" data-embed-url="https://social.vsp.ink/@Jacob/116933722892527559/embed" style="background: #FCF8FF; border-radius: 8px; border: 1px solid #C9C4DA; margin: 0; max-width: 540px; min-width: 270px; overflow: hidden; padding: 0;"> <a href="https://social.vsp.ink/@Jacob/116933722892527559" target="_blank" style="align-items: center; color: #1C1A25; display: flex; flex-direction: column; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Roboto, sans-serif; font-size: 14px; justify-content: center; letter-spacing: 0.25px; line-height: 20px; padding: 24px; text-decoration: none;"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32" viewBox="0 0 79 75"><path d="M63 45.3v-20c0-4.1-1-7.3-3.2-9.7-2.1-2.4-5-3.7-8.5-3.7-4.1 0-7.2 1.6-9.3 4.7l-2 3.3-2-3.3c-2-3.1-5.1-4.7-9.2-4.7-3.5 0-6.4 1.3-8.6 3.7-2.1 2.4-3.1 5.6-3.1 9.7v20h8V25.9c0-4.1 1.7-6.2 5.2-6.2 3.8 0 5.8 2.5 5.8 7.4V37.7H44V27.1c0-4.9 1.9-7.4 5.8-7.4 3.5 0 5.2 2.1 5.2 6.2V45.3h8ZM74.7 16.6c.6 6 .1 15.7.1 17.3 0 .5-.1 4.8-.1 5.3-.7 11.5-8 16-15.6 17.5-.1 0-.2 0-.3 0-4.9 1-10 1.2-14.9 1.4-1.2 0-2.4 0-3.6 0-4.8 0-9.7-.6-14.4-1.7-.1 0-.1 0-.1 0s-.1 0-.1 0 0 .1 0 .1 0 0 0 0c.1 1.6.4 3.1 1 4.5.6 1.7 2.9 5.7 11.4 5.7 5 0 9.9-.6 14.8-1.7 0 0 0 0 0 0 .1 0 .1 0 .1 0 0 .1 0 .1 0 .1.1 0 .1 0 .1.1v5.6s0 .1-.1.1c0 0 0 0 0 .1-1.6 1.1-3.7 1.7-5.6 2.3-.8.3-1.6.5-2.4.7-7.5 1.7-15.4 1.3-22.7-1.2-6.8-2.4-13.8-8.2-15.5-15.2-.9-3.8-1.6-7.6-1.9-11.5-.6-5.8-.6-11.7-.8-17.5C3.9 24.5 4 20 4.9 16 6.7 7.9 14.1 2.2 22.3 1c1.4-.2 4.1-1 16.5-1h.1C51.4 0 56.7.8 58.1 1c8.4 1.2 15.5 7.5 16.6 15.6Z" fill="currentColor"/></svg> <div style="color: #787588; margin-top: 16px;">Post by @Jacob@social.vsp.ink</div> <div style="font-weight: 500;">View on Mastodon</div> </a> </blockquote> <script data-allowed-prefixes="https://social.vsp.ink/" async src="https://social.vsp.ink/embed.js"></script>


The night after the race, I posted each leg to [FitPub](https://fitpub.social/users/campjacob):

{% include gallery caption="My three race legs on FitPub: swim, bike, and run. Click a card to see the activity." %}

> **Swim:** "I wasn't very happy with my swimming time. The first bit I felt like I couldn't breathe or catch my breath. I almost quit but kept going."
>
> **Bike:** "There were a bunch of ups and downs and hills. Most of my practice was flat. So beautiful going through several small lakes."
>
> **Run:** "I actually felt pretty good about the run and my pace. Still lots of room for growth but good. Overall I just wanted to be able to finish."

I finished **10th of 11** in my age group (men 40–44). More importantly, I met the only goal I set back in June: **I finished.** Full results are on the [Pacific Multisports results page](https://register.pacificmultisports.com/Events/Results/1333).

My daughter participated in the Splash & Dash as well. Afterwards, we went to Leavenworth and spent the afternoon wandering around the shops there and eating some Bavarian-style food. It made for a fun weekend and wonderful experience.

