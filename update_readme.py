import re
import os

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Let's just find the indices of the sections
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if line.startswith("### Featured Projects"):
        start_idx = i
    if line.startswith("**Tip**: Use **PX4**"):
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    featured_projects = """### Featured Projects

- **[F Prime (F')](https://github.com/nasa/fprime)** [![GitHub stars](https://img.shields.io/github/stars/nasa/fprime?style=social&color=white)](https://github.com/nasa/fprime/stargazers) — NASA's open-source, component-based flight software framework for small satellites and embedded systems.
- **[Zephyr RTOS](https://zephyrproject.org)** [![GitHub stars](https://img.shields.io/github/stars/zephyrproject-rtos/zephyr?style=social&color=white)](https://github.com/zephyrproject-rtos/zephyr/stargazers) — Modern, secure RTOS with excellent embedded support and safety features.
- **[PX4 Autopilot](https://px4.io)** [![GitHub stars](https://img.shields.io/github/stars/PX4/PX4-Autopilot?style=social&color=white)](https://github.com/PX4/PX4-Autopilot/stargazers) — Widely used open-source autopilot for drones, with simulation and hardware support.
- **[Core Flight System (cFS)](https://github.com/nasa/cFS)** [![GitHub stars](https://img.shields.io/github/stars/nasa/cFS?style=social&color=white)](https://github.com/nasa/cFS/stargazers) — NASA's reusable flight software architecture with OS abstraction for portability.

### Additional Open-Source Tools
- **[ArduPilot](https://ardupilot.org)** [![GitHub stars](https://img.shields.io/github/stars/ArduPilot/ardupilot?style=social&color=white)](https://github.com/ArduPilot/ardupilot/stargazers) — Versatile open-source autopilot for copters, planes, rovers, and submarines.
- **Betaflight / iNAV** [![GitHub stars](https://img.shields.io/github/stars/betaflight/betaflight?style=social&color=white)](https://github.com/betaflight/betaflight/stargazers) — High-performance open-source firmware for racing and navigation drones.
- RTOS options: **FreeRTOS**, **NuttX**, **RIOT OS**. [![GitHub stars](https://img.shields.io/github/stars/FreeRTOS/FreeRTOS?style=social&color=white)](https://github.com/FreeRTOS/FreeRTOS/stargazers)
- **[Paparazzi UAV](https://wiki.paparazziuav.org)** [![GitHub stars](https://img.shields.io/github/stars/paparazzi/paparazzi?style=social&color=white)](https://github.com/paparazzi/paparazzi/stargazers) — Open-source drone autopilot and ground station software.
- **[LibrePilot](https://librepilot.org)** [![GitHub stars](https://img.shields.io/github/stars/librepilot/librepilot?style=social&color=white)](https://github.com/librepilot/librepilot/stargazers) — Open-source flight control for multi-rotors and fixed-wing.

"""
    lines = lines[:start_idx] + [featured_projects] + lines[end_idx:]

content = "".join(lines)

# Emojis and SEO
seo_text = "> A comprehensive, SEO-optimized curated guide to the best embedded flight software frameworks, RTOS, drone autopilots, and open-source alternatives.\n\n"
content = content.replace("## Top Embedded Flight Softwares & Open-Source Alternatives", "## 🌟 Top Embedded Flight Softwares & Open-Source Alternatives\n\n" + seo_text)

content = content.replace("# Awesome-Embedded-Flight-Softwares", "# 🚀 Awesome-Embedded-Flight-Softwares")
content = content.replace("## SaaS / Cloud-Hosted or Commercial Flight Software", "## ☁️ SaaS / Cloud-Hosted or Commercial Flight Software")
content = content.replace("## Open-Source / Self-Hosted Alternatives", "## 🛠️ Open-Source / Self-Hosted Alternatives")
content = content.replace("## Comparison", "## ⚖️ Comparison")
content = content.replace("## Getting Started", "## 🚀 Getting Started")
content = content.replace("## Contributing", "## 🤝 Contributing")

# Badges and Banner
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
right_badges = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

badges_html = f'<div align="center">\n{left_badges}\n{right_badges}\n</div>\n\n'
banner_md = "![Banner](assets/banner.svg)\n\n"

# Replace heading with heading + banner + badges
content = content.replace("# 🚀 Awesome-Embedded-Flight-Softwares\n", "# 🚀 Awesome-Embedded-Flight-Softwares\n\n" + banner_md + badges_html)

# Star history
star_history = """
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Embedded-Flight-Softwares&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Embedded-Flight-Softwares&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Embedded-Flight-Softwares&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Embedded-Flight-Softwares&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content += star_history

# Fixes
content = content.replace("chartrepos", "chart?repos")
content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

# Write banner
os.makedirs("assets", exist_ok=True)
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(10,10,30);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(30,10,50);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)" />
  <text x="400" y="100" font-family="Arial" font-size="30" fill="white" text-anchor="middle" dominant-baseline="middle">Awesome Embedded Flight Softwares</text>
  <circle cx="100" cy="100" r="10" fill="white">
    <animate attributeName="cy" values="90;110;90" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="700" cy="100" r="10" fill="white">
    <animate attributeName="cy" values="110;90;110" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>'''
with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
