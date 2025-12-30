// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.1.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Agnes B. Riley",
  footer: context { [#emph[Agnes B. Riley -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Last updated in Dec 2025] ],
  locale-catalog-language: "en",
  page-size: "us-letter",
  page-top-margin: 0.7in,
  page-bottom-margin: 0.7in,
  page-left-margin: 0.7in,
  page-right-margin: 0.7in,
  page-show-footer: true,
  page-show-top-note: true,
  colors-body: rgb(0, 0, 0),
  colors-name: rgb(0, 79, 144),
  colors-headline: rgb(0, 79, 144),
  colors-connections: rgb(0, 79, 144),
  colors-section-titles: rgb(0, 79, 144),
  colors-links: rgb(0, 79, 144),
  colors-footer: rgb(128, 128, 128),
  colors-top-note: rgb(128, 128, 128),
  typography-line-spacing: 0.6em,
  typography-alignment: "justified",
  typography-date-and-location-column-alignment: right,
  typography-font-family-body: "Source Sans 3",
  typography-font-family-name: "Source Sans 3",
  typography-font-family-headline: "Source Sans 3",
  typography-font-family-connections: "Source Sans 3",
  typography-font-family-section-titles: "Source Sans 3",
  typography-font-size-body: 10pt,
  typography-font-size-name: 30pt,
  typography-font-size-headline: 10pt,
  typography-font-size-connections: 10pt,
  typography-font-size-section-titles: 1.4em,
  typography-small-caps-name: false,
  typography-small-caps-headline: false,
  typography-small-caps-connections: false,
  typography-small-caps-section-titles: false,
  typography-bold-name: true,
  typography-bold-headline: false,
  typography-bold-connections: false,
  typography-bold-section-titles: true,
  links-underline: false,
  links-show-external-link-icon: false,
  header-alignment: center,
  header-photo-width: 3.5cm,
  header-space-below-name: 0.7cm,
  header-space-below-headline: 0.7cm,
  header-space-below-connections: 0.7cm,
  header-connections-hyperlink: true,
  header-connections-show-icons: true,
  header-connections-display-urls-instead-of-usernames: false,
  header-connections-separator: "",
  header-connections-space-between-connections: 0.5cm,
  section-titles-type: "with_partial_line",
  section-titles-line-thickness: 0.5pt,
  section-titles-space-above: 0.5cm,
  section-titles-space-below: 0.3cm,
  sections-allow-page-break: true,
  sections-space-between-text-based-entries: 0.3em,
  sections-space-between-regular-entries: 1.2em,
  entries-date-and-location-width: 4.15cm,
  entries-side-space: 0.2cm,
  entries-space-between-columns: 0.1cm,
  entries-allow-page-break: false,
  entries-short-second-row: true,
  entries-summary-space-left: 0cm,
  entries-summary-space-above: 0cm,
  entries-highlights-bullet:  "•" ,
  entries-highlights-nested-bullet:  "•" ,
  entries-highlights-space-left: 0.15cm,
  entries-highlights-space-above: 0cm,
  entries-highlights-space-between-items: 0cm,
  entries-highlights-space-between-bullet-and-text: 0.5em,
  date: datetime(
    year: 2025,
    month: 12,
    day: 28,
  ),
)


= Agnes B. Riley

#connections(
  [#connection-with-icon("location-dot")[Sacramento, CA]],
  [#link("mailto:ariley@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[ariley\@gmail.com]]],
  [#link("tel:+1-917-660-7221", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[(917) 660-7221]]],
  [#link("https://www.credly.com/users/agnes-riley", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[www.credly.com\/users\/agnes-riley]]],
  [#link("https://linkedin.com/in/agnesriley", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[agnesriley]]],
)


== Summary

Seasoned IT professional with over twenty years of IT and process management experience. Change agent and problem solver with a passion for technology. Skilled at completing multiple projects on time and within budget.

== Skills

#strong[Core Competencies:] Business analysis, Project management, Process and standards definition, Software Engineering

#strong[Development:] FileMaker, HTML, CSS, JavaScript, SQL, Git, CI\/CD, NextJS, AstroJS, TailwindCSS

#strong[Infrastructure:] Servers (Mac, Linux, Windows), Networking, Firewalls, Google Cloud, AWS

#strong[Tools:] Adobe Suite, Photography, Video Editing, Project Management (Jira, Miro), Tableau

== Experience

#regular-entry(
  [
    #strong[Claris, An Apple Company], Sr. Product Manager (IC)

    - Lead product discovery and development for features enhancing security, user experience, and platform

    - Defined and prioritized product initiatives in collaboration with engineering, design, and cross-functional teams

    - Used customer feedback, analytics, and market research to guide roadmap decisions across the FileMaker platform

    - Executed product vision on analytics and providing updates to senior leadership to ensure alignment with strategic goals

  ],
  [
    Sunnyvale, CA

    Jan 2025 – Oct 2025

    10 months

  ],
)

#regular-entry(
  [
    #strong[Lawrence Livermore National Laboratory], Software Engineer (FileMaker, web developer)

    - Requirements Analysis: Conducted requirements analysis to identify business needs, document functional specifications, and ensure alignment with project objectives

    - Design Specifications Development: Created comprehensive design specifications and mind maps, along with schema designs and entity relationship models for apps

    - Charting and Metrics: Utilize HTML, JavaScript, and CSS to develop analytical tools that improve team efficiency

    - Tableau Integration: Seamlessly integrate analytical tools for enhanced data visualization from anywhere

    - Dynamic Website Development: Build modern, interactive websites featuring rotating schedules and maps using AstroJS, HTML, TailwindCSS with continuous deployment

    - Issue Resolution: Address user concerns, data discrepancies, and code defects efficiently

  ],
  [
    Livermore, CA

    June 2023 – Oct 2024

    1 year 5 months

  ],
)

#regular-entry(
  [
    #strong[Nutek Bravo], Director, Information Technology

    - General IT operations management (Meraki firewall, Microsoft 365, Ring Central, Zoho Google Cloud, etc.)

    - Process analysis and workflow creation (workflow charts, etc.)

    - FileMaker database Development (from concept to realization including 21 CFR Part 11 compliance and following FDA guidelines on principles of software validation)

    - Front-end development (NextJS, HTML, TailwindCSS, CI\/CD)

    - Google Cloud Apps (App Engine, Compute Engine, Cloud Storage, etc.)

    - Providing phone, chat, remote, or in-person support

    - Two-way data sync between FileMaker and Web Apps (FMBetterforms, JSON, JavaScript)

  ],
  [
    Hayward, CA

    Mar 2022 – Feb 2023

    1 year

  ],
)

#regular-entry(
  [
    #strong[DriveSavers], Solutions Architect

    - Improved work efficiency of sales team by at least 20\% via process automation

    - Improved shipping efficiency by mass-production of shipping labels and mobile app

    - Established improved process analysis and workflow management

    - Refinement and improvement of FileMaker-driven systems (desktop, mobile and web)

    - Data analysis, conversion, and normalization

    - Setup and maintenance of FileMaker Servers (Mac OS, Windows, Linux)

    - Providing phone, chat, remote, or in-person support

    - FileMaker to web Connectivity via ESS, JavaScript, JSON (FMBetterforms)

  ],
  [
    Novato, CA

    Dec 2018 – Feb 2022

    3 years 3 months

  ],
)

#regular-entry(
  [
    #strong[Soliant Consulting], Sr. Application Developer

    - Identified gaps in the process and improved workflow

    - Designed and implemented FileMaker-powered apps (mobile and desktop)

    - Data analysis, conversion of old systems, and normalization

    - Installation and maintenance of FileMaker Server

    - Web Connectivity via ESS or XML, JAVASCRIPT and JSON

  ],
  [
    Burlingame, CA

    Mar 2016 – Dec 2018

    2 years 10 months

  ],
)

#regular-entry(
  [
    #strong[ZeroBlue Technology Solutions], Owner

    - Drives process analysis to create better workflow

    - Designs and implements FileMaker Pro database-powered solutions

    - Performs data analysis, conversion, and normalization

    - Deploys and manages FileMaker Servers

    - Facilitates apps integration (WordPress, MySQL, SQL)

    - Has a FileMaker Server Hosting business (https:\/\/www.radfm.cloud)

  ],
  [
    Sacramento, CA

    Sept 2008 – present

    17 years 5 months

  ],
)

#regular-entry(
  [
    #strong[Beezwax Datatools], Consultant

    - FileMaker Pro database development for several Apple departments, as well as other clients

    - Expert in implementing SuperContainer and SimpleDialog-driven solutions and working in the FOCUS framework

  ],
  [
    Oakland, CA

    Oct 2008 – July 2010

    1 year 10 months

  ],
)

#regular-entry(
  [
    #strong[The Investor Relations Group], Chief Technology Officer

    - Improved worker efficiency by saving at least 2 hrs\/day\/employee resulting in over 1 million-dollar savings per year

    - Oversaw technical staff, contractors, and outsourced IT services

    - Developed and documented IT policies, processes, and procedures

    - Prioritization and allocation of IT resources to competing needs

    - Improved company efficiency by developing over 15 complex FileMaker Pro Databases (that reduce administrative time by 2 hours per employee per workday, achieving 25\% more productivity)

    - Designed, specified, managed, and led rich media content portal projects

    - Created and managed the MicroCaptivations® email campaign to over 190,000 investors, brokers, and money managers

    - Implemented new network configuration with 1000 BASE-T network, additional Cisco wireless APs, and PIX Firewall with VPN for remote office access

    - Produced websites; oversaw design and development from concept to launch

  ],
  [
    New York, NY

    Feb 2006 – Aug 2008

    2 years 7 months

  ],
)

#regular-entry(
  [
    #strong[New York Hotel Trades Council\/Local 6], Director, Information Technology

    - Oversaw all aspects of technology for the organization, including purchasing, initial setup and configuration; desktop, network, and server maintenance (2 OS X, Windows 2000, 2003, Linux AS and NAS)

    - Proactively improved server infrastructure by converting the FileMaker server from Mac to Linux, resulting in greater productivity, 100\% uptime, and enhanced stability for over a hundred users

    - Updated an obsolete mail server to one that handles three domains and flawlessly processes over 29,000 attempts at access a day

    - Produced the www.savetheplaza.com website and was responsible for all photography, imaging, design, formatting, and scripting, from concept to launch

    - Implemented new network configuration with 5 roaming wireless routers Cisco switches and PIX Firewall with VPN for remote office access

  ],
  [
    New York, NY

    July 2002 – July 2005

    3 years 1 month

  ],
)

#regular-entry(
  [
    #strong[Apple Computer, Inc.], Acting Mac Genius

    - Apple-certified technician in a fast-paced retail environment

    - Top-ranked hardware\/software salesperson

    - Consistently offered pre-sales advice and after-sales technical support and demonstrated technical knowledge that established solid client trust, bringing repeat clients, and increasing revenue

    - Performed photography training and held education presentations

  ],
  [
    New York, NY

    Nov 2001 – July 2002

    9 months

  ],
)

#regular-entry(
  [
    #strong[Budapest Business Journal], Advertising Executive\/Manager

    - \#1 sales rep for Book of Years publication yearly sales

    - Doubled revenue by doubling advertising area in publication

    - Solely responsible for hiring and training advertising staff

    - Created databases using ACT! and FileMaker Pro

  ],
  [
    Budapest, Hungary

    Jan 1996 – Dec 1999

    4 years

  ],
)

== Certifications

- AI For Everyone (Coursera) - 2024

- AWS Cloud Practitioner (AWS) - 2024

- FileMaker Desktop and Server (all latest) - 2024

- Apple Desktop Technician Certification - 2002

== Education

#education-entry(
  [
    #strong[AWS Cloud Institute], Cloud Computing

    - Part-time program

  ],
  [
    Online

    Jan 2024 – present

  ],
  degree-column: [
    
  ],
)

#education-entry(
  [
    #strong[Coursera], Google UX Design

  ],
  [
    Online

    Jan 2005 – Dec 2006

  ],
  degree-column: [
    
  ],
)

#education-entry(
  [
    #strong[Fashion Institute of Technology], Photography

  ],
  [
    New York, NY

    Jan 1998 – Dec 1999

  ],
  degree-column: [
    
  ],
)

#education-entry(
  [
    #strong[Euro-Contact Business School], Business Management, Marketing and Accounting

  ],
  [
    Budapest, Hungary

    Jan 1992 – Dec 1993

  ],
  degree-column: [
    
  ],
)

#education-entry(
  [
    #strong[Hungarian Journalists' Association], Journalism

  ],
  [
    Budapest, Hungary

    Jan 1992 – Dec 1993

  ],
  degree-column: [
    
  ],
)

#education-entry(
  [
    #strong[University of Miskolc], English and Asian Studies

  ],
  [
    Miskolc, Hungary

    Jan 1990 – Dec 1991

  ],
  degree-column: [
    
  ],
)
