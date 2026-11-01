---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# 👋 About

I am a senior student at Beijing University of Posts and Telecommunications, majoring in Internet of Things Engineering. Before that, I studied at Shenzhen Middle School. I am currently seeking research collaborations and MPhil/PhD opportunities. Feel free to contact me!

My research interests lie primarily in **AI Security & Safety** and **Robotics**. On the security & safety side, I currently focus on **Agent Security & Safety**, particularly external attacks aimed at extracting sensitive information and risks arising during instruction following and action execution, as well as defense mechanisms against such threats. My long-term goal is to build efficient agents that preserve sensitive information and operate within explicitly granted permissions. On the robotics side, I am interested in **Agents for Embodied Intelligence**, and I hope to bring these directions together to develop secure and trustworthy embodied systems.

Outside of research, I enjoy playing basketball as a SG/PG. I am a fan of Kevin Durant and Anthony Edwards. Looking forward to seeing the Minnesota Timberwolves 🐺 and the Houston Rockets 🚀 to meet in the Western Conference Finals this year!

<span class="anchor" id="news"></span>

# 🔥 News
- Coming soon.

<span class="anchor" id="publications"></span>

# 📝 Publications 

<p class="publication-note"><small>* Equal contribution</small></p>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/PrivGNN.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Auditing Privacy Risks in LLM-Enhanced Graph Neural Networks](https://arxiv.org/pdf/2608.25727)

Longzhu He<sup>*</sup>, **Zelang Wen**<sup>*</sup>, Chaozhuo Li, Sen Su

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='{{ "/images/MIRAGE.png" | relative_url }}' alt="Overview of the MIRAGE topology-concealment framework" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Concealing LLM-Based Multi-Agent Topology via Phantom Structure Injection](https://arxiv.org/pdf/2609.37567)

Longzhu He, **Zelang Wen**, Xinfeng Li, Sen Su, XiaoFeng Wang

</div>
</div>

<span class="anchor" id="honors-and-awards"></span>

# 🎖 Honors and Awards
- **"Three Good Student", BUPT**, Freshman year
- **BUPT University Scholarship - Third Class**, Academic year 2023-2024 & 2024-2025
- **Embodied AI Application Scenario Challenge in 2025 International Humanoid Robot Skills Competition (Zhangjiang Launch Tournament) - Innovation Award**, 2025.06
- **Beijing Division - Second Prize** Mathematics competition of Chinese College Students, 2025.12

<span class="anchor" id="education"></span>

# 📖 Educations

<div class="education-list">
  <section class="education-item">
    <span class="education-item__logo institution-logo institution-logo--bupt"><img src="{{ '/images/education/bupt-logo.png' | relative_url }}" alt="Beijing University of Posts and Telecommunications emblem" width="40" height="40" loading="lazy"></span>
    <div class="education-item__details">
      <h2 class="education-item__school">Beijing University of Posts and Telecommunications</h2>
      <p class="education-item__degree">B.Eng. in Internet of Things Engineering</p>
    </div>
    <p class="education-item__period">Sep. 2023 - Jun. 2027 (Expected)</p>
  </section>

  <section class="education-item">
    <span class="education-item__logo institution-logo"><img src="{{ '/images/education/shenzhen-middle-school-logo.png' | relative_url }}" alt="Shenzhen Middle School emblem" width="40" height="40" loading="lazy"></span>
    <div class="education-item__details">
      <h2 class="education-item__school">Shenzhen Middle School</h2>
      <p class="education-item__degree">High School Diploma</p>
    </div>
    <p class="education-item__period">Sep. 2020 - Jun. 2023</p>
  </section>
</div>

<span class="anchor" id="research-experiences"></span>

# 💻 Research Experiences

<div class="experience-list">
  <section class="experience-item">
    <span class="experience-item__logo institution-logo"><img src="{{ '/images/education/hkust-gz-logo.png' | relative_url }}" alt="The Hong Kong University of Science and Technology (Guangzhou) emblem" width="40" height="40" loading="lazy"></span>
    <div class="experience-item__details">
      <h2 class="experience-item__school">The Hong Kong University of Science and Technology (Guangzhou)</h2>
      <p class="experience-item__role">Research Assistant - supervised by Prof. Yixin Wu</p>
    </div>
    <p class="experience-item__period">Oct. 2026 - Present</p>
  </section>

  <section class="experience-item">
    <span class="experience-item__logo institution-logo"><img src="{{ '/images/education/tsinghua-university-logo.png' | relative_url }}" alt="Tsinghua University emblem" width="40" height="40" loading="lazy"></span>
    <div class="experience-item__details">
      <h2 class="experience-item__school">State Key Laboratory of Intelligent Technology and Systems, Tsinghua University</h2>
      <p class="experience-item__role">Research Assistant - supervised by Prof. Huaping Liu</p>
    </div>
    <p class="experience-item__period">Jun. 2026 - Oct. 2026</p>
  </section>

  <section class="experience-item">
    <span class="experience-item__logo institution-logo institution-logo--bupt"><img src="{{ '/images/education/bupt-logo.png' | relative_url }}" alt="Beijing University of Posts and Telecommunications emblem" width="40" height="40" loading="lazy"></span>
    <div class="experience-item__details">
      <h2 class="experience-item__school">State Key Laboratory of Networking and Switching Technology, Beijing University of Posts and Telecommunications</h2>
      <p class="experience-item__role">Research Assistant - supervised by Prof. Sen Su</p>
    </div>
    <p class="experience-item__period">Jan. 2026 - Jun. 2026</p>
  </section>

  <section class="experience-item">
    <span class="experience-item__logo institution-logo institution-logo--bupt"><img src="{{ '/images/education/bupt-logo.png' | relative_url }}" alt="Beijing University of Posts and Telecommunications emblem" width="40" height="40" loading="lazy"></span>
    <div class="experience-item__details">
      <h2 class="experience-item__school">DeepTouch Lab, Beijing University of Posts and Telecommunications</h2>
      <p class="experience-item__role">Research Assistant, supervised by Prof. Bin Fang</p>
    </div>
    <p class="experience-item__period">Mar. 2025 - Sep. 2025</p>
  </section>
</div>

<span class="anchor" id="invited-talks"></span>

# 💬 Invited Talks
- Coming soon.
