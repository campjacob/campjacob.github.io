---
title: Curriculum Vitae
permalink: /cv/
layout: foundation
author_sidebar: true
nav_group: projects
updated: 2026-08-01
# Teaching totals. Update when the CV is updated; ask Claude to recount
# from the class database in the Obsidian vault to verify.
teaching_courses: 18
teaching_sections: 65
teaching_since: 2013
---

<style>
/* Bootstrap defines --bs-orange but ships no orange utilities (orange is not a
   theme color), so these two fill the gap. */
.text-orange { color: var(--bs-orange); }
.bg-orange-subtle { background-color: rgba(253,126,20,0.05); }

/* Footnote markers: hover reveals the note via the native title attribute. */
.cv-fn { cursor: help; color: var(--bs-orange); font-weight: 700; }

/* Toggle label swaps on each button's own aria-expanded state, so both the top
   and bottom buttons stay in sync without any JavaScript. */
.cv-toggle .cv-toggle-label::after { content: "Show more details"; }
.cv-toggle[aria-expanded="true"] .cv-toggle-label::after { content: "Hide details"; }
.cv-toggle .fa-chevron-down { transition: transform .2s; }
.cv-toggle[aria-expanded="true"] .fa-chevron-down { transform: rotate(180deg); }

/* CSS analogue of LaTeX multicols. Bootstrap's grid splits items across
   columns; this flows content down one and up the next. */
.cv-cols-2 { columns: 2; column-gap: 2rem; }
.cv-cols-2 > li { break-inside: avoid; -webkit-column-break-inside: avoid; }
@media (max-width: 575.98px) { .cv-cols-2 { columns: 1; } }

.cv-compact { font-size: 0.93rem; line-height: 1.5; }
.cv-compact li { margin-bottom: 0.4rem; }

/* Years-of-experience band. auto-fit reflows to the available width, which
   Bootstrap's fixed-breakpoint row-cols cannot do. */
.cv-years { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 0.9rem 1.25rem; margin: 0; padding: 0; list-style: none; }
.cv-years li { margin: 0; display: flex; align-items: baseline; gap: 0.55rem; }
.cv-years .cv-num { font-size: 1.85rem; font-weight: 700; line-height: 1;
  color: var(--bs-orange); font-variant-numeric: tabular-nums; min-width: 2.1ch; text-align: right; }
.cv-years .cv-label { font-size: 0.88rem; line-height: 1.35; opacity: 0.8; }
</style>

# Jacob Campbell, Ph.D. LICSW

Curriculum Vitae
{: .lead .text-secondary .mb-4}

I am a social work educator and licensed independent clinical social worker. I approach social work from a generalist lens, with a broad and diverse set of expertise. My mission is to develop a place where resilience can grow, transformation can happen, and support the helpers who work for the same.


<div class="card mb-4">
  <h5 class="card-header">Professional Connections</h5>
  <div class="card-body">
    <ul class="list-unstyled mb-0">
      <li class="d-flex mb-3">
        <i class="fas fa-university fa-fw text-orange me-2 mt-1"></i>
        <span><strong>Associate Professor</strong> for Heritage University &amp; <strong>Associate Director</strong> of the Social Work Department</span>
      </li>
      <li class="d-flex mb-3">
        <i class="fas fa-briefcase fa-fw text-orange me-2 mt-1"></i>
        <span><strong>Owner</strong>, Locus of Transformation &mdash; LICSW supervision and consulting</span>
      </li>
      <li class="d-flex mb-3">
        <i class="fas fa-user-graduate fa-fw text-orange me-2 mt-1"></i>
        <span><strong>Ph.D. in Transformative Studies</strong> from California Institute of Integral Studies and a <strong>MSW</strong> from Eastern Washington University</span>
      </li>
      <li class="d-flex">
        <i class="fas fa-book-open fa-fw text-orange me-2 mt-1"></i>
        <span>Areas of professional interest include school social work, direct practice, adult education, policy practice, and program evaluation.</span>
      </li>
    </ul>
  </div>
</div>

<div class="card mb-4">
  <h5 class="card-header bg-transparent border-bottom-0">Years of Experience</h5>
  <div class="card-body bg-orange-subtle">
    <ul class="cv-years">
      <li><span class="cv-num" data-since="2002">{{ 'now' | date: "%Y" | minus: 2002 }}</span><span class="cv-label">years in the helping field</span></li>
      <li><span class="cv-num" data-since="2004">{{ 'now' | date: "%Y" | minus: 2004 }}</span><span class="cv-label">years working with youth</span></li>
      <li><span class="cv-num" data-since="2010">{{ 'now' | date: "%Y" | minus: 2010 }}</span><span class="cv-label">years in mental health</span></li>
      <li><span class="cv-num" data-since="2013">{{ 'now' | date: "%Y" | minus: 2013 }}</span><span class="cv-label">years teaching at university</span></li>
      <li><span class="cv-num" data-since="2019">{{ 'now' | date: "%Y" | minus: 2019 }}</span><span class="cv-label">years as a LICSW</span></li>
      <li><span class="cv-num" data-since="2022">{{ 'now' | date: "%Y" | minus: 2022 }}</span><span class="cv-label">years supervising clinicians toward licensure</span></li>
    </ul>
  </div>
</div>

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

<div class="card mb-4">
  <h5 class="card-header bg-transparent border-bottom-0">Places of Employment</h5>
  <div class="card-body pt-2">
    <div class="row g-0 align-items-center">
      <div class="col">
        <ul class="list-unstyled mb-0 cv-cols-2">
          <li><strong>Heritage University</strong> <span class="badge text-bg-light fw-normal">Current</span></li>
          <li><strong>Locus of Transformation</strong> <span class="badge text-bg-light fw-normal">Current</span></li>
          <li>Pasco School District</li>
          <li>Lourdes Counseling Center</li>
          <li>Tri-Cities Community Behavioral Health Services</li>
          <li>Universidad Nacional San Antonio Abad del Cusco</li>
        </ul>
      </div>
      <div class="col-auto ps-4 d-none d-sm-block">
        <i class="fas fa-building fa-5x text-orange opacity-25"></i>
      </div>
    </div>
  </div>
</div>

<div class="card mb-4">
  <h5 class="card-header bg-transparent border-bottom-0">Professional Contributions</h5>
  <div class="card-body pt-2">
    <div class="row g-0 align-items-center">
      <div class="col-auto pe-4 d-none d-sm-block">
        <i class="fas fa-bookmark fa-5x text-orange opacity-25"></i>
      </div>
      <div class="col">
        <ul class="list-unstyled mb-0 cv-cols-2">
          <li class="d-flex mb-2">
            <i class="fas fa-graduation-cap fa-fw text-orange me-2 mt-1"></i>
            <span>Taught {{ page.teaching_sections }} course sections across {{ page.teaching_courses }} different university classes since {{ page.teaching_since }}</span>
          </li>
          <li class="d-flex mb-2">
            <i class="fas fa-id-card fa-fw text-orange me-2 mt-1"></i>
            <span>Licensed Independent Clinical Social Worker (LICSW) in Washington State</span>
          </li>
          <li class="d-flex mb-2">
            <i class="fas fa-laptop fa-fw text-orange me-2 mt-1"></i>
            <span>Facilitated break-out sessions at many conferences and events</span>
          </li>
          <li class="d-flex mb-2">
            <i class="fas fa-certificate fa-fw text-orange me-2 mt-1"></i>
            <span>Certified to implement many evidence-based interventions</span>
          </li>
          <li class="d-flex mb-2">
            <i class="fas fa-users fa-fw text-orange me-2 mt-1"></i>
            <span>Leadership and engagement with community coalitions and organizations</span>
          </li>
          <li class="d-flex">
            <i class="fas fa-pen fa-fw text-orange me-2 mt-1"></i>
            <span>Published dissertation</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div class="card mb-4">
  <h5 class="card-header bg-transparent border-bottom-0">Professional Social Connections</h5>
  <div class="card-body pt-2">
    <ul class="list-unstyled mb-0 cv-cols-2">
      <li class="d-flex mb-2">
        <i class="fas fa-info-circle fa-fw text-orange me-2 mt-1"></i>
        <span><a href="https://jacobrcampbell.com/">jacobrcampbell.com</a></span>
      </li>
      <li class="d-flex mb-2">
        <i class="fab fa-mastodon fa-fw text-orange me-2 mt-1"></i>
        <span><a href="https://social.vsp.ink/@Jacob" rel="me">social.vsp.ink/@Jacob</a></span>
      </li>
      <li class="d-flex mb-2">
        <i class="fab fa-linkedin fa-fw text-orange me-2 mt-1"></i>
        <span><a href="https://linkedin.com/in/jacobrcampbell/">linkedin.com/in/jacobrcampbell</a></span>
      </li>
      <li class="d-flex">
        <i class="fab fa-youtube fa-fw text-orange me-2 mt-1"></i>
        <span><a href="https://www.youtube.com/@JacobCampbell82">youtube.com/@JacobCampbell82</a></span>
      </li>
    </ul>
  </div>
</div>

<div class="card mb-4">
  <div class="card-body d-flex flex-wrap align-items-center justify-content-between gap-2">
    <span>The following is a more detailed view of my CV.</span>
    <button class="btn btn-link p-0 cv-toggle" type="button"
            data-bs-toggle="collapse" data-bs-target=".cv-detail" aria-expanded="false">
      <span class="cv-toggle-label"></span><i class="fas fa-chevron-down ms-1"></i>
    </button>
  </div>
</div>

# Academic Appointments

<div class="border-start ps-3 mb-4" markdown="1">
### Heritage University
{: .h5 .mb-1}
<p class="small text-muted mb-2">Associate Professor <span class="float-end">Aug 2013–Current</span></p>

I served as an adjunct faculty member for several years, contracting to teach one to three classes per semester. While I have taught a wide range of courses in the social work program, my primary focus has been direct practice services. For a detailed list of courses, see the section <em>University Courses Taught</em>. In August 2024, I was hired as an Associate Professor in the MSW program.

<div class="collapse cv-detail" markdown="1">

I prioritize student-centered instruction in the classroom, fostering a safe yet rigorous learning environment, incorporating diverse and dynamic teaching methods, and providing hands-on opportunities for direct practice. I have consistently received positive student feedback in midterm and final evaluations.

The following are key aspects of my role at Heritage University:

- Developed course syllabi, designed content, and delivered a broad range of classes at graduate and undergraduate levels.
- Designed and developed new courses, including Social Work in Schools, Case Management, Working with Special Needs Populations, and Practice with Individuals, Families, and Groups.
- Facilitated courses using diverse instructional methods, including online learning, in-class discussions, lectures, role-plays, and interactive assignments.
- Secured approval for an Educational Staff Associate (ESA) credential through the Professional Educator Standards Board (PESB).
- Collaborated with social work faculty to meet the accreditation requirements of the Council for Social Work Education (CSWE).
- Coordinated with faculty across multiple campuses to align course content and objectives.
- Elected to and actively participated in faculty committees.
- Delivered professional development sessions during faculty training days.
- Created various grading rubrics to enhance assessment consistency and transparency.

</div>
</div>
<div class="border-start ps-3 mb-4" markdown="1">
### Universidad Nacional San Antonio Abad del Cusco (UNSAAC)
{: .h5 .mb-1}
<p class="small text-muted mb-2">English Professor <span class="float-end">Dec 2009–July 2010</span></p>

<div class="collapse cv-detail" markdown="1">

In the Language Center of UNSAAC in Peru, I worked as an English professor, teaching various English courses to students of various levels.

- Preparing and implementing effective courses to enhance students' learning
- Helping plan future curriculum for the intermediate courses and inclusion of new learning material

</div>
</div>
# Professional Experience

<div class="border-start ps-3 mb-4" markdown="1">
### Locus of Transformation
{: .h5 .mb-1}
<p class="small text-muted mb-2">Owner <span class="float-end">Aug 2014–Current</span></p>

I am the owner of Locus of Transformation, a business focused on providing LICSW supervision and educational consulting. Through this work, I support clinical professionals seeking licensure, assist organizations with training and development, help problem-solve interventions for clients with complex needs, and contribute to projects that enhance professional practice in social work and related fields.

<div class="collapse cv-detail" markdown="1">

The following are key aspects of my role at Locus of Transformation:

- Provide individual and group supervision for clinical social workers pursuing independent licensure.
- Develop and deliver training programs, curriculum design, and professional development workshops.
- Assist mental health practitioners and agencies in case consultations, ethical decision-making, and best practices.

</div>
</div>
<div class="border-start ps-3 mb-4" markdown="1">
### Pasco School District
{: .h5 .mb-1}
<p class="small text-muted mb-2">School Program Social Worker <span class="float-end">Aug 2014–Aug 2024</span></p>

I was initially hired as a mental health therapist for the Pasco School District in a newly created role designed to provide direct mental health services. However, through collaboration with the Assistant Director of Special Services and a program consultant, we redefined the position to focus primarily on brokering resources for students and families and coordinating with collateral contacts for students placed in the Bridges Program. Students in the Bridges Program receive special education services and have experienced significant behavioral challenges in school. I supported staff, students, and parents across seven K-12 school programs. I took a year of educational leave (2019–2020) to begin my Ph.D.~program. Upon returning, my role shifted to focus solely on the high school, with an additional staff member hired to support the middle school.

<div class="collapse cv-detail" markdown="1">

The following are key aspects of my role in the Pasco School District:

- Established the first social work role within the school district.
- Connected students and families to community resources and helped them navigate available services.
- Facilitated social skills instruction groups for students.
- Provided individual support and counseling for students.
- Designed and implemented service-learning projects for students.
- Developed a program-wide handbook in collaboration with Bridges Program teachers.
- Delivered presentations to strengthen collaboration between community organizations and school special services.
- Trained and certified staff in CPI non-violent crisis intervention techniques.
- Supervised social work practicum students placed in the district.
- Planned, coordinated, and implemented Review360, a data-driven behavior tracking software.
- Collected and analyzed data for program review using Participatory Evaluation and Expert Review for Programs Serving Students with EBD (PEER-EBD).
- Supported bilingual families, working with parents in both English and Spanish.
- Participated in multidisciplinary team meetings, including tier-1 behavior meetings, IEP meetings, WISe Child Family Team meetings
- Collaborated with parents and staff to develop team-based solutions for complex student cases.
- Facilitated staff training and team meetings.
- Maintained comprehensive documentation of student progress, interventions, and service coordination.

</div>
</div>
<div class="border-start ps-3 mb-4" markdown="1">
### Lourdes Counseling Center: Children's Day Program
{: .h5 .mb-1}
<p class="small text-muted mb-2">Social Services Counselor <span class="float-end">Oct 2019–June 2020</span></p>

<div class="collapse cv-detail" markdown="1">

I worked as a social services counselor at Lourdes Counseling Center's Children's Day Program. The program served students with mental health concerns who were unable to maintain placement at their home school. This was a temporary position while I was on educational leave from the Pasco School District. My role focused on supporting staff, students, and external partners involved with students in the program.

The following are key aspects of my role in the Children's Day Program:

- Planned and developed therapeutic group sessions for program staff to facilitate
- Provided individual support to students and deescalated crisis situations
- Coordinated services between school programs, parents, and external providers
- Conducted intake and referral meetings for new students
- Delivered professional development training for staff
- Maintained thorough documentation of student progress and interventions

</div>
</div>
<div class="border-start ps-3 mb-4" markdown="1">
### Tri-Cities Community Health: Behavioral Health Services (TCCH BHS)
{: .h5 .mb-1}
<p class="small text-muted mb-2">Mental Health Therapist &amp; Case Manager <span class="float-end">Nov 2010–Aug 2014</span></p>

<div class="collapse cv-detail" markdown="1">

At TCCH BHS, I worked as both a mental health therapist and a mental health case manager. As a therapist, I primarily focused on working with adolescents involved in the juvenile justice system, but I worked with a broad range of clientele. I completed mental health evaluations, often while they were incarcerated. I assessed the youth's eligibility for access to care, evaluated them for qualifying diagnosis, and assigned them to the appropriate provider.

As a case manager, I worked with a diverse range of cultural populations, developmental stages, and levels of chronicity in mental health concerns. This included individuals from various minority and mainstream populations, spanning from young children to geriatric clients. Their needs ranged from behavioral concerns and psychosocial stressors (as described on Axis IV of the DSM-IV-TR) to psychoeducational needs regarding mental health. My roles also provided the opportunity to collaborate with various community organizations.

The following are key aspects of my role at TCCH-BHS:

- Assisted clients in connecting with community organizations and understanding available services.
- Provided individual and family counseling using cognitive-behavioral therapy, solution-focused brief therapy, and motivational interviewing.
- Incorporated client voice and preferences in the development of treatment plans.
- Managed a caseload of clients with English or Spanish as their primary language, utilizing translation services for clients speaking another language.
- Received supervision from minority mental health specialists and participated in training on culturally competent care.
- Participated in multidisciplinary team meetings.
- Utilized a team-oriented approach in working with clients and planning for complex cases.
- Facilitated staff training sessions.
- Maintained thorough documentation of client progress and interventions.

</div>
</div>
<div class="collapse cv-detail" markdown="1">

<div class="border-start ps-3 mb-4" markdown="1">
### Safe Harbor Family Support Center
{: .h5 .mb-1}
<p class="small text-muted mb-2">Group Facilitator <span class="float-end">Sep 2010–Aug 2012</span></p>

<div class="collapse cv-detail" markdown="1">

Over the years, I have held several positions and worked on several projects at Safe Harbor Crisis Nursery. Most of these unpaid roles include consulting and providing recommendations for the teen homeless shelter, now called My Friends Place. My most recent paid position was as a group facilitator for adolescents who have experienced trauma in the Dragon Slayers Support Group. I developed the curriculum for this twelve-week program by adapting an evidence-based framework for working with individuals processing traumatic experiences.

- Developed a group curriculum tailored to the needs of youth served at Safe Harbor.
- Conducted intake assessments for youth and families participating in the Dragon Slayers Support Group.
- Implemented pre-test and post-test evaluations for each group session.
- Co-facilitated group sessions, ensuring a structured and supportive environment.
- Provided referrals to other agencies and assisted families in accessing needed resources.

</div>
</div>

</div>

<div class="collapse cv-detail" markdown="1">

<div class="border-start ps-3 mb-4" markdown="1">
### YFA Connections, Crisis Residential Center (CRC)
{: .h5 .mb-1}
<p class="small text-muted mb-2">Support Staff / Practicum Student / Shift Leader <span class="float-end">Mar 2008–Sep 2009</span></p>

<div class="collapse cv-detail" markdown="1">

The CRC works with youth who are homeless and runaway teenagers, along with their families. These families were experiencing various crises in their lives in Spokane County.

- Led shifts by deescalating volatile situations, assigning duties to staff, and managing complex cases
- Advocated within governmental organizations to secure resources for clients
- Provided individual, group, and family counseling
- Participated in multidisciplinary team meetings
- Facilitated staff training sessions
- Collaborated in team planning for high-risk cases
- Conducted a research project and applied for grants
- Designed new therapeutic group programs
- Created a database to maintain up-to-date client records
- Maintained thorough documentation of client interactions and case progress

</div>
</div>

</div>

<div class="collapse cv-detail" markdown="1">

<div class="border-start ps-3 mb-4" markdown="1">
### Spokane County Juvenile Correction Facility
{: .h5 .mb-1}
<p class="small text-muted mb-2">Aggression Replacement Training (ART) Facilitator <span class="float-end">Jun 2008–Jul 2008</span></p>

<div class="collapse cv-detail" markdown="1">

ART is an evidence-based program often implemented to work with adolescent criminal offenders. It focuses on developing cognitive skills through a group educational format. Key areas include teaching anger replacement skills, implementing the anger control chain, and fostering moral reasoning. I was trained to implement this intervention as part of my BASW practicum experience and was later offered a paid position post-graduation.

- Planned and facilitated group therapy sessions focused on behavior modification
- Implemented an evidence-based model program with a high success rate

</div>
</div>

</div>

<div class="collapse cv-detail" markdown="1">

<div class="border-start ps-3 mb-4" markdown="1">
### J. Ethan Construction
{: .h5 .mb-1}
<p class="small text-muted mb-2">Crewmember <span class="float-end">Jun 2007–Nov 2007</span></p>

<div class="collapse cv-detail" markdown="1">

J. Ethan Construction is a construction company in Spokane Washington that performs remodels and new residential construction.

</div>
</div>

</div>

<div class="collapse cv-detail" markdown="1">

<div class="border-start ps-3 mb-4" markdown="1">
### Jubilee Leadership Academy
{: .h5 .mb-1}
<p class="small text-muted mb-2">Residential Advisor / Shift Leader <span class="float-end">Aug 2004–Sep 2006</span></p>

<div class="collapse cv-detail" markdown="1">

Jubilee was a behavior modification-oriented boarding school for at-risk teens in Prescott, Washington. The facility included a school, vocational training, and residential programs. It is no longer operating.

- Led shifts by deescalating volatile situations, assigning duties to staff, managing complex cases, and completing documentation
- Worked with clients to develop detailed goal plans, provided support, and tracked progress toward completion
- Provided individual and group counseling
- Maintained communication and support for parents
- Established a behavior modification program called the Merit Store
- Developed a new program enabling youth to participate in community service

</div>
</div>

</div>

<div class="collapse cv-detail" markdown="1">

# Publications

- Campbell, J. (2023). *A professional learning community for developing trauma-informed practices using participatory action methods: Transforming school culture for students with emotional and behavioral disabilities* (Publication No. 30424801) [Doctoral dissertation, California Institute of Integral Studies]. ProQuest Dissertations and Theses. [View](https://www.proquest.com/dissertations-theses/professional-learning-community-developing-trauma/docview/2813493629/se-2)

# Selected Presentations

<ul class="cv-compact">
<li>Slonecker, A., <strong>Campbell, J.</strong>, &amp; Núñez, A. (2026, January 15). <em>Legislative write-in session: Advocating for HU students at the Washington State level</em> [General Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li><strong>Campbell, J.</strong> (2025, October 16). <em><a href="https://presentations.jacobrcampbell.com/aWNpQx/">Building connections through service-learning: Experiences and practice</a></em> [Featured Speaker]. Washington Association of School Social Workers Fall Conference, Vancouver, WA.
<div class="ratio ratio-16x9 my-3" style="max-width:720px;">
  <iframe src="https://presentations.jacobrcampbell.com/aWNpQx/embed" style="border:none;" loading="lazy" allowfullscreen title="Presentation slides"></iframe>
</div>
</li>
<li>Núñez, A., Slonecker, A., <strong>Campbell, J.</strong>, &amp; Jones-Dance, G. (2025, August 21). <em>Centering student voices: "How I learn best"</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li><strong>Campbell, J.</strong>, Aguilar, R., &amp; Vega, J. (2025, January 16). <em><a href="https://presentations.jacobrcampbell.com/I0pK2R/">Peace &amp; ease in changing times</a></em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.
<div class="ratio ratio-16x9 my-3" style="max-width:720px;">
  <iframe src="https://presentations.jacobrcampbell.com/I0pK2R/embed" style="border:none;" loading="lazy" allowfullscreen title="Presentation slides"></iframe>
</div>
</li>
<li>Vargas, K., &amp; <strong>Campbell, J.</strong> (2023, August 17). <em>Suicide and universities: What faculty should know</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li><strong>Campbell, J.</strong> (2023, March 3). <em><a href="https://presentations.jacobrcampbell.com/F4hwoF/">A professional learning community for developing trauma-informed practices using participatory action methods</a></em> [Dissertation Defense]. California Institute of Integral Studies. <a href="https://youtu.be/DD7X0XtrY1U">Recording</a>
<div class="ratio ratio-16x9 my-3" style="max-width:720px;">
  <iframe src="https://presentations.jacobrcampbell.com/F4hwoF/embed" style="border:none;" loading="lazy" allowfullscreen title="Presentation slides"></iframe>
</div>
</li>
<li><strong>Campbell, J.</strong>, Dance-Jones, G., &amp; Miguel, J. (2022, August 18). <em>ESCALA's 10 core responsibilities for Hispanic-serving institution instructors</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li>Wynn, W., &amp; <strong>Campbell, J.</strong> (2022, August 18). <em>Teaching in and beyond the classroom walls: Collaborative learning</em> [Conference Session]. Heritage University Faculty Day, Toppenish, WA.</li>
<li><strong>Campbell, J.</strong> (2019, May 23). <em><a href="https://presentations.jacobrcampbell.com/FhBMCJ/">Supporting students with emotional and behavioral disabilities: Foundational aspects of evidence-based classrooms</a></em> [Conference Session]. OSPI Student Support Conference, Wenatchee, WA.
<div class="ratio ratio-16x9 my-3" style="max-width:720px;">
  <iframe src="https://presentations.jacobrcampbell.com/FhBMCJ/embed" style="border:none;" loading="lazy" allowfullscreen title="Presentation slides"></iframe>
</div>
</li>
<li><strong>Campbell, J.</strong> (2017, April 23–24). <em>Bringing focus: Making your data match your strategies</em> and <em>Gaining perspective: How to make looking at data useful to you</em> [Conference Sessions]. Eastern Washington CPWI Sector Summit, Pasco, WA.</li>
<li><strong>Campbell, J.</strong> (2016, January 16). <em>¡Ayuda! Mi hijo tiene problemas de comportamiento: Ideas para los padres sobre cómo ayudar con comportamiento</em> [Conference Session]. Bilingual Parent Advisory Committee Conference, Pasco, WA.</li>
<li><strong>Campbell, J.</strong> (2015, April 27). <em>Interacting in the digital age: Social media and your coalition</em> [Conference Session]. Eastern Washington CPWI Sector Summit, Kennewick, WA.</li>
<li><strong>Campbell, J.</strong> (2015, January 17). <em>Acceso a los servicios: Información general sobre recursos de la comunidad</em> [Conference Session]. Bilingual Parent Advisory Committee Conference, Pasco, WA.</li>
</ul>

# Teaching

{{ page.teaching_courses }} distinct courses across {{ page.teaching_sections }} sections since {{ page.teaching_since }}, at both the undergraduate (BASW) and graduate (MSW) levels.

## Undergraduate

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 316: Social Policy I
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2015, 2016 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: In depth examination of the history of public welfare and social work; the function of social work - its mandates, values, and ethics and the fields of practice shaped by social welfare policies. Introduction to poverty and the nature of oppression. Offered fall semesters. Cross-listed as SOC 316.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 322<sup class="cv-fn" title="I developed and facilitated the first iteration of this course.">1</sup>: Practice with Persons with Special Needs
{: .h5 .mb-1}
<p class="small text-muted mb-2">Spring 2017, 2018, 2019, 2022, 2023, 2024 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Social workers often work with vulnerable populations, and these vulnerable populations often times include persons with special needs. Children with chronic conditions, developmental disorders, and birth defects commonly access services done by social workers. This course builds on the knowledge and skills for work with individuals to gain further insight into research, applied services, and policy perspectives reflecting the range of children's problems requiring special services.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 390<sup class="cv-fn" title="In the fall of 2013, I developed this course under the SOWK 390 code. In the fall of 2017, I taught this class in the psychology department under the code PSY 224">2</sup>: Introduction to Case Management
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2013, 2014, Spring 2015, 2016, Fall 2017 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: This course prepares the student to do generalist social work practice in a case management setting. The student develops knowledge and methods regarding best practices in case management through self-examination, learning effective communication skills, how to assess client's needs and strengths, and how to develop and implement a plan of treatment.

<strong>Course Description</strong><sup class="cv-fn" title="In 2017, when collaborated with the psychology department and taught this course as an elective under this description.">3</sup>: Explores definitions and practical application to inter-professional case management with an emphasis on relevant functions, including child and family needs assessment, development of case management plans, and case monitoring. Does not substitute for other psychology courses.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 430: History of Social Work &amp; Ethics in Practice
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2022 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: This course is required for all social work majors. Ethics are an integral component in all aspects of generalist social work practice. The National Association of Social Workers (NASW) Code of Ethics is the guide to direct practitioners' conduct. The NASW ethical standards provide guidelines for what is ethically acceptable and unacceptable behavior. The ethical standards help social workers identify ethical issues in practice. A brief history of the professions of social work will precede the study of the NASW Code of Ethics. Offered Fall Semester. This course is taken concurrently with SOWK 312 Human Behavior in the Social Environment I, SOWK 316 Social Policy I, and SOWK 486W Theory of Practice I. These courses are usually taken in the first semester of the junior year.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 459: Social Science Research Methods
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2019(2) <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Basic research methodologies for the social sciences; principles of qualitative and quantitative methodologies for collection and analysis of data. Development of research design. This course is the same as SOC 460W. Offered Fall semesters. Prerequisite(s): Senior standing; permission of the program chair. Cross-listed as SOC 460W.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 460W: Social Programs/Evaluation
{: .h5 .mb-1}
<p class="small text-muted mb-2">Spring 2020, 2024, 2025, 2026 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Basic evaluation methodologies for social programs; analysis of public and private social programs' effectiveness; policy design, implementation, and evaluation. Basic practice evaluation skills. Offered Spring semesters. Prerequisite(s): Limited to majors, Senior standing. Co-requisite(s): SOWK 491.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 486w: Theories of Practice I
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2014, 2015, 2016(2), 2017(2), 2018(2), 2019, 2020, 2021, 2022, 2023, 2024, 2025 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Generalist social work practice with micro systems. Knowledge and methods to bring about planned change with individuals and client-identified family systems practice in interpersonal skills. Offered Fall semester. Limited to majors Prerequisite(s): limited to majors or permission of program chair.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 487w: Theories of Practice II
{: .h5 .mb-1}
<p class="small text-muted mb-2">Spring 2015, 2016, 2017(2), 2018(2), 2019(2), 2020, 2021, 2022, 2023, 2024, 2025, 2026 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Generalist Social Work Practice with microsystems. Knowledge and methods to bring about planned change with individuals and client-identified family systems practice in interpersonal skills. Students must have completed PSY 101, SOC 101, and BIOL 111 or permission of the program chairperson. Course limited to majors.
</div>

## Graduate

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 530: Foundations of Social Work Practice I
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2025 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: This course provides students with the knowledge and skills for Generalist Social Work Practice with micro and mezzo systems. Utilizing foundational theoretical frameworks for social work, students will learn to bring about planned change with individuals and client-identified family systems. Practice in interpersonal skills, engagement, assessment, intervention, and evaluation will be incorporated throughout the course.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 581: Social Work Practice with Individuals, Families &amp; Groups
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2024 (2), 2025 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Students will use policy, research, and models to investigate advanced assessment and engagement methods, evidence-based practices, and service delivery. This course will include crisis intervention, elements of trauma informed practice, resilience, ethical decision making, and family systems practice. Students will analyze and evaluate their own social work practice with individuals, families, groups, organizations, and communities.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 590: Advanced Seminar I
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2024, 2025 <span class="float-end">1 Credit</span></p>

<strong>Course Description</strong>: Advanced seminar is taken concurrently with Advanced Practicum I. This course allows the student an environment to apply advanced field practicum experience to the program curriculum. Students are encouraged to critically reflect on theory, ethics, values, skills, knowledge, and cognitive and affective processes that shape social work practice. Designed as a supportive environment, students are encouraged to practice using peer supervision to manage both the challenges and successes in their field placement. This course is graded as Pass/No Pass.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 595: Advanced Practicum I
{: .h5 .mb-1}
<p class="small text-muted mb-2">Fall 2024, 2025 <span class="float-end">4 Credits</span></p>

<strong>Course Description</strong>: Practicum education provides the student with advanced generalist practice opportunities to demonstrate the nine social work competencies at all system levels. Students are given opportunities to apply knowledge gained from advanced course work and to integrate theory and practice in professional situations. At least 250 hours of placement are required. The course is graded as Pass/No Pass.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 531: Foundations of Social Work Practice II
{: .h5 .mb-1}
<p class="small text-muted mb-2">Spring 2026 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: This course provides students with the knowledge and skills for Generalist Social Work Practice with macro systems. Utilizing foundational theoretical frameworks for social work, students will learn to bring about planned change with organizations and communities through planning, administration, evaluation, advocacy, and community organizing.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 587: Social Work in Schools
{: .h5 .mb-1}
<p class="small text-muted mb-2">Spring 2025, 2026 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Social work in schools is a unique domain of practice. This course will prepare students to practice ethically in a school context with an understanding of national, state, and local laws and policies that affect decisions. Topics include collaboration with parents, teachers, administrators, and others; using professional social work knowledge, skills, and values to promote culturally responsive interventions in school settings; and utilizing human, community, and technological resources for more effective practice. The course meets the requirements for obtaining an Education Staff Associate (ESA) with social work endorsement in Washington State.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 591: Advanced Seminar II
{: .h5 .mb-1}
<p class="small text-muted mb-2">Spring 2025, 2026 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Advanced seminar is taken concurrently with Advanced Practicum II. This course allows the student an environment to apply advanced field practicum experience to the program curriculum.~ Students are encouraged to critically reflect on theory, ethics, values, skills, knowledge, and cognitive and affective processes that shape social work practice. Designed as a supportive environment, students are encouraged to practice using peer supervision to manage both the challenges and successes in their field placement.~ This course is graded as Pass/No Pass.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 596: Advanced Practicum II
{: .h5 .mb-1}
<p class="small text-muted mb-2">Spring 2025, 2026 <span class="float-end">4 Credits</span></p>

<strong>Course Description</strong>: Field education provides the student with advanced generalist practice opportunities to demonstrate the nine social work competencies at all system levels.~ Students are given opportunities to apply knowledge gained from advanced course work and to integrate theory and practice in professional situations. At least 250 hours of placement are required. The course is graded as Pass/No Pass.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### SOWK 588: Advanced Policy Practice
{: .h5 .mb-1}
<p class="small text-muted mb-2">Summer 2025 <span class="float-end">3 Credits</span></p>

<strong>Course Description</strong>: Students will acquire a deeper understanding of social policies at the local, state, tribal, and federal levels in the context of policy implementation and advocacy impacts on oppressed and marginalized populations. Students will identify and explain social policy theories such as social construction, political economy, cost-benefit analysis, and feminist perspectives to analyze cases; understand diverse client populations; create culturally tailored interventions; predict results; and evaluate outcomes. They will compare the Universal Declaration of Human Rights with the National Association of Social Workers (NASW) Code of Ethics, and social welfare policies in United States.

</div>

# Service &amp; Professional Engagement

Selected committee membership, evidence-based practice training, and other engagements.

<div class="border-start ps-3 mb-4" markdown="1">
### Faculty Professional Development Committee
{: .h5 .mb-1}
<p class="small text-muted mb-2">Faculty Representative <span class="float-end">August 2022–Current</span></p>

I started on this committee as the adjunct faculty representative. This Committee recommends policies and programs to advance the professional development of the Heritage University faculty. It also advises the Provost/Vice President for Academic Affairs regarding funding needs and procedures for faculty applications for professional development opportunities sponsored by the University.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Committee on Evaluation &amp; Multi-Year Appointment
{: .h5 .mb-1}
<p class="small text-muted mb-2">Faculty Representative <span class="float-end">January 2025–Current</span></p>

The Committee on Evaluation and Multi-year Appointments is charged with evaluating and affirming faculty achievement in teaching, scholarship, and service as related to evaluation and multi-year appointments by applying policies stated in the faculty handbook. The Committee maintains standards for faculty excellence with consistency and objectivity, enabling the University to fulfill and enhance its educational mission.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Academic Affairs
{: .h5 .mb-1}
<p class="small text-muted mb-2">Faculty Representative <span class="float-end">August 2024–Current</span></p>

The Academic Affairs Assembly is responsible for academic policy formulation, including admissions and graduation requirements, academic advising, program quality assurance, and approval of new majors, programs, sites, and/or degrees. It receives recommendations from the Undergraduate and Graduate Curriculum Committee and also acts on academic policy matters referred by other units of the University. The President of the University and the Provost/Vice President for the academic Affairs give monthly reports. This Committee is advisory to the President and the Provost/Vice President for the Academic Affairs. The President forwards the committee's recommendations to the Board of Directors when appropriate.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Faculty Senate
{: .h5 .mb-1}
<p class="small text-muted mb-2">Faculty Representative <span class="float-end">August 2024–Current</span></p>

Faculty Senate is the official faculty organization and part of the University's governance structure. It conveys formal statements of decisions, recommendations, and opinions to the Academic Affairs Assembly, administrators, the President of the University, and other appropriate bodies.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Community of HOPE
{: .h5 .mb-1}
<p class="small text-muted mb-2">Coalition Member <span class="float-end">October 2023–Current</span></p>

The community of HOPE is a coalition facilitated by the Benton-Franklin Health Department. The coalition convenes stakeholders to take a community-based approach to address the root causes of trauma and ACEs by promoting healthy outcomes from positive experiences and environments to build resilience, promote healing, and advance equity on a community level.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Pasco Prevention Network (PPN)
{: .h5 .mb-1}
<p class="small text-muted mb-2">Coalition Member, Former Chair <span class="float-end">Feb 2012–Current</span></p>

The PPN, formerly the Pasco Discovery Coalition, is a CPWI community coalition made up of community members who work together collaboratively to create and sustain a healthy, safe, alcohol and drug-free community through the transformation of attitudes and norms. I have taken on several roles over the years, including acting as chair, co-chair, and executive team member.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Mid Valley Provider Consortium
{: .h5 .mb-1}
<p class="small text-muted mb-2">Coalition Member <span class="float-end">September 2024–Current</span></p>

The MVPC is designed to promote and coordinate a community-wide strategy that is collaborative and expeditious. The consortium will provide services based on an individual's identified needs while reducing barriers. The result will be a systems change of cooperation among agencies and school districts and a proactive linkage between the individual and provider.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Tier 1 Behavior Team
{: .h5 .mb-1}
<p class="small text-muted mb-2">Committee Member <span class="float-end">March 2022–August 2024</span></p>

Pasco High School implements multi-teared systems of support (MTSS) through a positive behavior interventions and supports (PBIS) system. The behavior team meets to review building data and potential interventions to implement a consistent and equitable behavior system.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Crisis Prevention Institute (CPI) Non-violent Crisis Intervention
{: .h5 .mb-1}
<p class="small text-muted mb-2">Certified Trainer <span class="float-end">Oct 2014–August 2024</span></p>

As a part of my duties for the Pasco School District, I train and certify district staff multiple times per year in CPI Non-violent Crisis Intervention. This provides staff information on how to intervene with another person to address behavior that may escalate into a disruptive or even violent incident. This certification requires participation in regular professional development to keep from facilitator drift.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### First Aid Certification Class
{: .h5 .mb-1}
<p class="small text-muted mb-2">Certified <span class="float-end">Oct 2008–Current</span></p>

I have completed training in first aid on an ongoing basis.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Strengthening Families Program for Parents and Youth 10-14
{: .h5 .mb-1}
<p class="small text-muted mb-2">Certified Facilitator <span class="float-end">June 2019</span></p>

Strengthening Families Program for Parents and Youth 10-14 is an evidence-based prevention intervention and parenting program developed by the University of Iowa. It is designed to engage both caregivers and youth in learning new skills.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Guiding Good Choices Facilitator
{: .h5 .mb-1}
<p class="small text-muted mb-2">Certified Facilitator <span class="float-end">Aug 2015</span></p>

Guiding Good Choices is a science-based, ATOD-prevention program that gives parents the skills they need to ensure the future well-being of their children.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Why Try Facilitator
{: .h5 .mb-1}
<p class="small text-muted mb-2">Training Participant <span class="float-end">Sep 2014</span></p>

WhyTry is a resilience education curriculum that provides simple, hands-on solutions for dropout prevention, violence prevention, truancy reduction, and increased academic success.
</div>

<div class="border-start ps-3 mb-4" markdown="1">
### Aggression Replacement Training Facilitator Training Course
{: .h5 .mb-1}
<p class="small text-muted mb-2">Certified Facilitator <span class="float-end">Jan 2008</span></p>

Aggression Replacement Training is a cognitive behavioral intervention for the reduction of aggressive and violent behavior, originally focused on adolescents.
</div>

# Education

<div class="table-responsive" markdown="0">
<table class="table table-sm align-middle">
  <tr><td><strong>Ph.D. in Transformative Studies</strong><br><span style="opacity:.7">California Institute of Integral Studies &mdash; Department of Transformative Inquiry</span></td><td class="text-end text-nowrap">Aug 2019 &ndash; May 2023</td></tr>
  <tr><td><strong>Master of Social Work (MSW)</strong><br><span style="opacity:.7">Eastern Washington University &mdash; School of Social Work</span></td><td class="text-end text-nowrap">Aug 2008 &ndash; Jun 2009</td></tr>
  <tr><td><strong>Bachelor of Social Work (BASW)</strong><br><span style="opacity:.7">Eastern Washington University &mdash; School of Social Work</span></td><td class="text-end text-nowrap">Sep 2006 &ndash; Jun 2008</td></tr>
  <tr><td><strong>Associate of Arts (AA)</strong><br><span style="opacity:.7">Columbia Basin College</span></td><td class="text-end text-nowrap">Sep 2004 &ndash; Jun 2006</td></tr>
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

# Professional Qualifications

## Skills

<ul class="cv-compact">
<li>Facilitate groups, inform using psychoeducational techniques, manage a university classroom, and other skills associated with teaching</li>
<li>Collaborate with peers &amp; quickly pick up new skills</li>
<li>Developing a research proposal, gaining approval, implementing, analyzing, and disseminating findings</li>
<li>Work with at-risk youth, facilitate groups, and family counseling</li>
<li>Plan &amp; organize large events and various group curriculum</li>
<li>Utilizing the counseling techniques of motivational interviewing &amp; solution-focused brief therapy</li>
<li>Utilize the DSM-5 to diagnose mental health issues</li>
<li>Speaking Spanish at an intermediate level</li>
</ul>

## Computer Skills

<ul class="cv-compact">
<li>Operate Microsoft Office [Word, PowerPoint, Excel, and Outlook] with proficiency</li>
<li>General computer literacy</li>
<li>Graphic and web design</li>
</ul>

# Professional Memberships

<ul class="cv-compact">
<li><strong>National Association of Social Workers (NASW)</strong> <span style="opacity:.6">— 2009–Present</span></li>
<li><strong>Washington State Association of School Social Workers (WSASSW)</strong> <span style="opacity:.6">— 2018–Present</span></li>
</ul>

</div>

<p class="text-center mb-4">
  <button class="btn btn-sm btn-outline-secondary cv-toggle" type="button"
          data-bs-toggle="collapse" data-bs-target=".cv-detail" aria-expanded="false">
    <i class="fas fa-chevron-down me-1"></i><span class="cv-toggle-label"></span>
  </button>
</p>

<p class="border rounded p-3 small text-body-secondary mt-5">
  <i class="fas fa-history text-orange me-1"></i><strong>Last updated:</strong>
  {% if page.updated %}{{ page.updated | date: "%B %-d, %Y" }}{% else %}{{ site.time | date: "%B %-d, %Y" }}{% endif %}.
  Also available as a <a href="{{ '/assets/media/2026-01-03-curriculum-vitae.pdf' | relative_url }}">formatted PDF</a>, last updated January 3, 2026.
</p>
