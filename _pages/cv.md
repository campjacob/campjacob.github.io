---
title: Curriculum Vitae
permalink: /cv/
layout: foundation
author_sidebar: true
nav_group: about
updated: 2026-08-01
---

{% comment %}
  Teaching data is loaded once here, at the top of the page, rather than
  inline beside the Teaching heading. Liquid's whitespace-trimming tag
  delimiters (the hyphenated ones) swallow the newline after a Markdown
  heading, which glues the following paragraph onto the "# Teaching" line
  and makes kramdown render the whole thing as one giant heading. Keep
  these assigns up here and use plain, non-hyphenated delimiters.

  The section total is only asserted once every course carries a sections
  count, so the page never claims a number the data cannot support.
{% endcomment %}
{% assign courses = site.data.cv_teaching %}
{% assign grad = courses | where: "level", "graduate" %}
{% assign undergrad = courses | where: "level", "undergraduate" %}
{% assign first_year = courses | map: "year_start" | sort | first %}
{% assign counted = courses | where_exp: "c", "c.sections" %}
{% assign section_total = 0 %}
{% for c in counted %}{% assign section_total = section_total | plus: c.sections %}{% endfor %}

<style>
.cv-lede { font-size: 1.05rem; line-height: 1.6; margin-bottom: 1.75rem; }

.cv-glance { display: flex; flex-wrap: wrap; gap: 0.75rem; margin: 0 0 2rem; padding: 0; list-style: none; }
.cv-glance li {
  flex: 1 1 240px; margin: 0; padding: 0.85rem 1rem;
  border-left: 3px solid #6b8f9c; background: rgba(107,143,156,0.07);
  border-radius: 0 4px 4px 0; font-size: 0.94rem; line-height: 1.45;
}
.cv-glance i { color: #6b8f9c; margin-right: 0.5rem; }
.cv-glance strong { display: block; font-size: 0.78rem; letter-spacing: 0.06em;
  text-transform: uppercase; opacity: 0.65; margin-bottom: 0.2rem; }

.cv-entry { margin: 0 0 1.6rem; padding-left: 1rem; border-left: 2px solid rgba(128,128,128,0.22); }
.cv-entry h3 { margin: 0 0 0.15rem; font-size: 1.06rem; }
.cv-meta { font-size: 0.87rem; opacity: 0.72; margin: 0 0 0.5rem; }
.cv-meta .cv-date { float: right; font-variant-numeric: tabular-nums; }
.cv-entry p { margin: 0 0 0.5rem; font-size: 0.95rem; line-height: 1.55; }
.cv-entry ul { font-size: 0.93rem; margin-bottom: 0; }

.cv-table { width: 100%; font-size: 0.92rem; border-collapse: collapse; }
.cv-table th { text-align: left; font-size: 0.76rem; letter-spacing: 0.06em;
  text-transform: uppercase; opacity: 0.6; border-bottom: 1px solid rgba(128,128,128,0.3);
  padding: 0.4rem 0.6rem 0.4rem 0; }
.cv-table td { padding: 0.42rem 0.6rem 0.42rem 0; border-bottom: 1px solid rgba(128,128,128,0.13);
  vertical-align: top; }
.cv-table td:last-child { text-align: right; white-space: nowrap; opacity: 0.7;
  font-variant-numeric: tabular-nums; }
.cv-scroll { overflow-x: auto; margin-bottom: 1.5rem; }

.cv-compact { font-size: 0.93rem; line-height: 1.5; }
.cv-compact li { margin-bottom: 0.4rem; }

/* Years-of-experience band — mirrors the \yearsworked cover page block */
.cv-years { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 0.9rem 1.25rem; margin: 0 0 2rem; padding: 1.25rem 1.4rem; list-style: none;
  border: 1px solid rgba(128,128,128,0.22); border-radius: 6px;
  background: rgba(107,143,156,0.05); }
.cv-years li { margin: 0; display: flex; align-items: baseline; gap: 0.55rem; }
.cv-years .cv-num { font-size: 1.85rem; font-weight: 700; line-height: 1;
  color: #6b8f9c; font-variant-numeric: tabular-nums; min-width: 2.1ch; text-align: right; }
.cv-years .cv-label { font-size: 0.88rem; line-height: 1.35; opacity: 0.8; }

.cv-updated { margin: 2.5rem 0 1rem; padding: 0.85rem 1.1rem; font-size: 0.86rem;
  border: 1px solid rgba(128,128,128,0.22); border-radius: 6px;
  background: rgba(128,128,128,0.05); opacity: 0.85; }
.cv-updated i { color: #6b8f9c; margin-right: 0.45rem; }

@media (max-width: 640px) {
  .cv-meta .cv-date { float: none; display: block; }
}
</style>

# Curriculum Vitae

<p class="cv-lede">I am a social work educator and licensed independent clinical social worker. My work centers on direct practice, trauma-informed systems change, and preparing students to practice ethically in schools and community settings. As a generalist practitioner, I help individuals, groups, and systems transform through careful assessment and cooperative planning.</p>

<ul class="cv-glance">
  <li><i class="fas fa-university"></i><strong>Position</strong> Associate Professor, MSW Program, Heritage University</li>
  <li><i class="fas fa-graduation-cap"></i><strong>Doctorate</strong> Ph.D. in Transformative Studies, California Institute of Integral Studies</li>
  <li><i class="fas fa-id-card"></i><strong>Licensure</strong> Licensed Independent Clinical Social Worker (LICSW), Washington</li>
  <li><i class="fas fa-chalkboard-teacher"></i><strong>Teaching</strong> {{ courses | size }} distinct courses{% if counted.size == courses.size %} across {{ section_total }} sections{% endif %} since {{ first_year }}</li>
</ul>

# Years of Experience

<ul class="cv-years">
  <li><span class="cv-num" data-since="2002">{{ 'now' | date: "%Y" | minus: 2002 }}</span><span class="cv-label">years in the helping field</span></li>
  <li><span class="cv-num" data-since="2004">{{ 'now' | date: "%Y" | minus: 2004 }}</span><span class="cv-label">years working with youth</span></li>
  <li><span class="cv-num" data-since="2010">{{ 'now' | date: "%Y" | minus: 2010 }}</span><span class="cv-label">years in mental health</span></li>
  <li><span class="cv-num" data-since="2013">{{ 'now' | date: "%Y" | minus: 2013 }}</span><span class="cv-label">years teaching at university</span></li>
  <li><span class="cv-num" data-since="2019">{{ 'now' | date: "%Y" | minus: 2019 }}</span><span class="cv-label">years as a LICSW</span></li>
  <li><span class="cv-num" data-since="2022">{{ 'now' | date: "%Y" | minus: 2022 }}</span><span class="cv-label">years supervising clinicians toward licensure</span></li>
</ul>

<script>
  // Recompute years-of-experience client side so the numbers stay correct
  // between site builds. Liquid renders a build-time value as the fallback.
  (function () {
    var year = new Date().getFullYear();
    document.querySelectorAll('.cv-num[data-since]').forEach(function (el) {
      el.textContent = year - parseInt(el.dataset.since, 10);
    });
  })();
</script>

# Education

<div class="cv-scroll" markdown="0">
<table class="cv-table">
  <tr><td><strong>Ph.D., Transformative Studies</strong><br><span style="opacity:.7">California Institute of Integral Studies — Center for Consciousness Studies</span></td><td>2019–2023</td></tr>
  <tr><td><strong>Master of Social Work (MSW)</strong><br><span style="opacity:.7">Eastern Washington University — School of Social Work</span></td><td>2008–2009</td></tr>
  <tr><td><strong>Bachelor of Social Work (BASW)</strong><br><span style="opacity:.7">Eastern Washington University — School of Social Work</span></td><td>2006–2008</td></tr>
  <tr><td><strong>Associate of Arts (AA)</strong><br><span style="opacity:.7">Columbia Basin College</span></td><td>2004–2006</td></tr>
</table>
</div>

# Academic Appointments

<div class="cv-entry" markdown="1">
### Heritage University
<p class="cv-meta">Associate Professor, MSW Program <span class="cv-date">Aug 2013 – Present</span></p>

I served as an adjunct faculty member for eleven years, contracting to teach one to three classes per semester, and in August 2024 was hired as an Associate Professor in the MSW program. While I have taught across the social work curriculum, my primary focus is direct practice.

I prioritize student-centered instruction — a safe but rigorous learning environment, varied teaching methods, and hands-on opportunities for direct practice.

- Developed syllabi, designed content, and delivered courses at both graduate and undergraduate levels
- Designed new courses including Social Work in Schools, Case Management, Working with Special Needs Populations, and Practice with Individuals, Families, and Groups
- Secured approval for an Educational Staff Associate (ESA) credential through the Professional Educator Standards Board
- Collaborate with faculty to meet Council on Social Work Education (CSWE) accreditation requirements
- Elected to and actively serve on faculty committees
- Deliver professional development sessions during faculty training days
</div>

<div class="cv-entry" markdown="1">
### Universidad Nacional San Antonio Abad del Cusco
<p class="cv-meta">English Professor — Cusco, Peru <span class="cv-date">Dec 2009 – Jul 2010</span></p>
</div>

# Professional Experience

<div class="cv-entry" markdown="1">
### Locus of Transformation
<p class="cv-meta">Owner <span class="cv-date">Aug 2014 – Present</span></p>

A practice providing LICSW supervision and educational consulting. I support clinicians seeking licensure, assist organizations with training and development, and consult on interventions for clients with complex needs.

- Provide individual and group supervision for clinical social workers pursuing independent licensure
- Develop and deliver training programs, curriculum design, and professional development workshops
- Assist practitioners and agencies with case consultation, ethical decision-making, and best practices
</div>

<div class="cv-entry" markdown="1">
### Pasco School District
<p class="cv-meta">School Program Social Worker <span class="cv-date">Aug 2014 – Aug 2024</span></p>

Hired as a mental health therapist into a newly created role, then — working with the Assistant Director of Special Services and a program consultant — redefined the position toward brokering resources for students and families and coordinating collateral contacts for students in the Bridges Program, which serves students receiving special education services who have experienced significant behavioral challenges. I supported staff, students, and parents across seven K–12 programs.

- Established the first social work role within the district
- Connected students and families to community resources and helped them navigate services
- Facilitated social skills instruction groups
</div>

<div class="cv-entry" markdown="1">
### Lourdes Counseling Center — Children's Day Program
<p class="cv-meta">Social Services Counselor <span class="cv-date">Oct 2019 – Jun 2020</span></p>
</div>

<div class="cv-entry" markdown="1">
### Tri-Cities Community Health — Behavioral Health Services
<p class="cv-meta">Mental Health Therapist &amp; Case Manager <span class="cv-date">Nov 2010 – Aug 2014</span></p>
</div>

<div class="cv-entry" markdown="1">
### Safe Harbor Family Support Center
<p class="cv-meta">Group Facilitator <span class="cv-date">Sep 2010 – Aug 2012</span></p>
</div>

<div class="cv-entry" markdown="1">
### YFA Connections — Crisis Residential Center
<p class="cv-meta">Support Staff / Practicum Student / Shift Leader <span class="cv-date">Mar 2008 – Sep 2009</span></p>
</div>

<div class="cv-entry" markdown="1">
### Jubilee Leadership Academy
<p class="cv-meta">Residential Advisor / Shift Leader <span class="cv-date">Aug 2004 – Sep 2006</span></p>
</div>

# Teaching

{{ courses | size }} distinct courses{% if counted.size == courses.size %} across {{ section_total }} sections{% endif %} since {{ first_year }}, at both the undergraduate (BASW) and graduate (MSW) levels.

## Graduate — MSW

<div class="cv-scroll" markdown="0">
<table class="cv-table">
  <tr><th>Course</th><th>Number</th><th>Years</th></tr>
  {%- for c in grad %}
  <tr><td>{{ c.title }}</td><td>{{ c.number }}</td><td>{{ c.year_start }}{% if c.year_end %}–{{ c.year_end }}{% endif %}</td></tr>
  {%- endfor %}
</table>
</div>

## Undergraduate — BASW

<div class="cv-scroll" markdown="0">
<table class="cv-table">
  <tr><th>Course</th><th>Number</th><th>Years</th></tr>
  {%- for c in undergrad %}
  <tr><td>{{ c.title }}</td><td>{{ c.number }}</td><td>{{ c.year_start }}{% if c.year_end %}–{{ c.year_end }}{% endif %}</td></tr>
  {%- endfor %}
</table>
</div>

# Publications

- Campbell, J. (2023). *A professional learning community for developing trauma-informed practices using participatory action methods: Transforming school culture for students with emotional and behavioral disabilities* (Publication No. 30424801) [Doctoral dissertation, California Institute of Integral Studies]. ProQuest Dissertations and Theses. [View](https://www.proquest.com/dissertations-theses/professional-learning-community-developing-trauma/docview/2813493629/se-2)

# Selected Presentations

<ul class="cv-compact">
<li>Slonecker, A., <strong>Campbell, J.</strong>, &amp; Núñez, A. (2026, January 15). <em>Legislative write-in session: Advocating for HU students at the Washington State level</em> [General Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li><strong>Campbell, J.</strong> (2025, October 16). <em>Building connections through service-learning: Experiences and practice</em> [Featured Speaker]. Washington Association of School Social Workers Fall Conference, Vancouver, WA.</li>
<li>Núñez, A., Slonecker, A., <strong>Campbell, J.</strong>, &amp; Jones-Dance, G. (2025, August 21). <em>Centering student voices: "How I learn best"</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li><strong>Campbell, J.</strong>, Aguilar, R., &amp; Vega, J. (2025, January 16). <em>Peace &amp; ease in changing times</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li>Vargas, K., &amp; <strong>Campbell, J.</strong> (2023, August 17). <em>Suicide and universities: What faculty should know</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li><strong>Campbell, J.</strong> (2023, March 3). <em>A professional learning community for developing trauma-informed practices using participatory action methods</em> [Dissertation Defense]. California Institute of Integral Studies. <a href="https://youtu.be/DD7X0XtrY1U">Recording</a></li>
<li><strong>Campbell, J.</strong>, Dance-Jones, G., &amp; Miguel, J. (2022, August 18). <em>ESCALA's 10 core responsibilities for Hispanic-serving institution instructors</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li>Wynn, W., &amp; <strong>Campbell, J.</strong> (2022, August 18). <em>Teaching in and beyond the classroom walls: Collaborative learning</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li><strong>Campbell, J.</strong> (2019, May 23). <em>Supporting students with emotional and behavioral disabilities: Foundational aspects of evidence-based classrooms</em> [Conference Session]. OSPI Student Support Conference, Wenatchee, WA.</li>
<li><strong>Campbell, J.</strong> (2017, April 23–24). <em>Bringing focus: Making your data match your strategies</em> and <em>Gaining perspective: How to make looking at data useful to you</em> [Conference Sessions]. Eastern Washington CPWI Sector Summit, Pasco, WA.</li>
<li><strong>Campbell, J.</strong> (2016, January 16). <em>¡Ayuda! Mi hijo tiene problemas de comportamiento: Ideas para los padres sobre cómo ayudar con comportamiento</em> [Conference Session]. Bilingual Parent Advisory Committee Conference, Pasco, WA.</li>
<li><strong>Campbell, J.</strong> (2015, April 27). <em>Interacting in the digital age: Social media and your coalition</em> [Conference Session]. Eastern Washington CPWI Sector Summit, Kennewick, WA.</li>
<li><strong>Campbell, J.</strong> (2015, January 17). <em>Acceso a los servicios: Información general sobre recursos de la comunidad</em> [Conference Session]. Bilingual Parent Advisory Committee Conference, Pasco, WA.</li>
</ul>

# Service &amp; Professional Engagement

<div class="cv-scroll" markdown="0">
<table class="cv-table">
  <tr><th>Role</th><th>Organization</th><th>Years</th></tr>
  <tr><td>Faculty Representative</td><td>Faculty Senate, Heritage University</td><td>2024–Present</td></tr>
  <tr><td>Faculty Representative</td><td>Academic Affairs, Heritage University</td><td>2024–Present</td></tr>
  <tr><td>Faculty Representative</td><td>Committee on Evaluation &amp; Multi-Year Appointment</td><td>2025–Present</td></tr>
  <tr><td>Faculty Representative</td><td>Faculty Professional Development Committee</td><td>2022–Present</td></tr>
  <tr><td>Coalition Member</td><td>Community of HOPE</td><td>2023–Present</td></tr>
  <tr><td>Coalition Member</td><td>Mid Valley Provider Consortium</td><td>2024–Present</td></tr>
  <tr><td>Coalition Member, Former Chair</td><td>Pasco Prevention Network</td><td>2012–Present</td></tr>
  <tr><td>Coalition Member</td><td>Council for Children</td><td>2015–2018</td></tr>
</table>
</div>

# Certifications &amp; Licensure

<ul class="cv-compact">
<li><strong>Licensed Independent Clinical Social Worker (LICSW)</strong> — Washington State <span style="opacity:.6">(2019)</span></li>
<li><strong>Crisis Prevention Institute (CPI)</strong> Non-Violent Crisis Intervention Certified Trainer <span style="opacity:.6">(2014–2024)</span></li>
<li><strong>Strengthening Families Program</strong> for Parents and Youth 10–14, Certified Instructor <span style="opacity:.6">(2019)</span></li>
<li><strong>Certificate of College Teaching and Learning</strong> for Hispanic-Serving Institutions <span style="opacity:.6">(2018)</span></li>
<li><strong>Guiding Good Choices</strong> Certified Facilitator <span style="opacity:.6">(2015)</span></li>
<li><strong>Life Space Crisis Intervention (LSCI)</strong> Certified <span style="opacity:.6">(2015)</span></li>
<li><strong>Aggression Replacement Training (ART)</strong> Certified Washington State Facilitator <span style="opacity:.6">(2008)</span></li>
</ul>

# Professional Memberships

<ul class="cv-compact">
<li><strong>National Association of Social Workers (NASW)</strong> <span style="opacity:.6">— 2009–Present</span></li>
<li><strong>Washington State Association of School Social Workers (WSASSW)</strong> <span style="opacity:.6">— 2018–Present</span></li>
</ul>

# Areas of Practice &amp; Skill

<ul class="cv-compact">
<li>Group facilitation, psychoeducation, and university classroom instruction</li>
<li>Work with at-risk youth, group work, and family counseling</li>
<li>Motivational interviewing and solution-focused brief therapy</li>
<li>DSM-5 diagnostic assessment</li>
<li>Program planning, curriculum development, and large event organization</li>
<li>Conversational Spanish (intermediate)</li>
</ul>

<p class="cv-updated">
  <i class="fas fa-history"></i><strong>Last updated:</strong>
  {% if page.updated %}{{ page.updated | date: "%B %-d, %Y" }}{% else %}{{ site.time | date: "%B %-d, %Y" }}{% endif %}.
  Also available as a <a href="{{ '/assets/media/2026-01-03-curriculum-vitae.pdf' | relative_url }}">formatted PDF</a> and last updated January 3, 2026.
</p>
