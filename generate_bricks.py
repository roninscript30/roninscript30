#!/usr/bin/env python3
import math
import random
import base64

with open('assets/pfp.jpeg', 'rb') as f:
    pfp_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode('utf-8')

FONT_FAMILY = "'JetBrains Mono', 'Fira Code', 'Space Mono', 'DejaVu Sans Mono', Consolas, monospace"
WIDTH = 680

# ========================================================
# 1. HEADER BRICK (assets/header.svg)
# ========================================================
header_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} 36" width="100%" height="36">
  <defs>
    <style>
      .mono {{ font-family: {FONT_FAMILY}; }}
    </style>
  </defs>

  <!-- Container with Top Rounded Corners -->
  <rect x="0.5" y="0.5" width="{WIDTH - 1}" height="35.5" rx="8" ry="8" fill="#080d1a" stroke="#162238" stroke-width="1"/>
  <line x1="0" y1="35.5" x2="{WIDTH}" y2="35.5" stroke="#162238" stroke-width="1"/>

  <!-- Left Prompt -->
  <text x="20" y="23" class="mono" font-size="12.5" font-weight="700">
    <tspan fill="#10b981">&gt; </tspan>
    <tspan fill="#e2e8f0">roninscript30 </tspan>
    <tspan fill="#10b981">&gt; </tspan>
    <tspan fill="#f8fafc">init</tspan>
  </text>

  <!-- Right Tags -->
  <text x="{WIDTH - 20}" y="23" text-anchor="end" class="mono" font-size="11.5" font-weight="500">
    <tspan fill="#526e88">[ </tspan>
    <tspan fill="#94a3b8">learning</tspan>
    <tspan fill="#38bdf8"> / </tspan>
    <tspan fill="#94a3b8">building</tspan>
    <tspan fill="#38bdf8"> / </tspan>
    <tspan fill="#94a3b8">exploring</tspan>
    <tspan fill="#526e88"> ]</tspan>
  </text>
</svg>
'''

with open('assets/header.svg', 'w') as f:
    f.write(header_svg)

# ========================================================
# 2. CELESTIAL SOLAR SYSTEM (assets/solar-system.svg)
# SYNCHRONIZED LOCKED-PHASE NON-COLLIDING ORBIT REVOLUTION
# ========================================================
CX = 340
CY = 110
N_STEPS = 72
PERIOD = 40.0

planets_cfg = [
    {
        "id": "planet-linux",
        "rx": 100, "ry": 36, "phi": math.pi / 2, # 90 deg (Top)
        "label": '<text y="24" text-anchor="middle" class="mono" font-size="8" font-weight="700" fill="#f8fafc" letter-spacing="0.06em">LINUX</text>',
        "icon": '''
        <g transform="translate(-7, -9) scale(0.58)">
          <path fill="#f8fafc" d="M12 2C8 2 6 5 6 9c0 2.5 1 5 1 8 0 2-1 3-2 4 0 1 2 1 4 1 1 0 1.5-.5 3-2 1.5 1.5 2 2 3 2 2 0 4 0 4-1-1-1-2-2-2-4 0-3 1-5.5 1-8 0-4-2-7-6-7z"/>
          <path fill="#080d1a" d="M12 4c-2.5 0-3.5 2-3.5 5 0 2.5.5 5 .5 8 0 1-.5 1.5-1 2 1 .5 2 .5 3-.5.5-.5 1-1 1-1s.5.5 1 1c1 1 2 1 3 .5-.5-.5-1-1-1-2 0-3 .5-5.5.5-8 0-3-1-5-3.5-5z"/>
          <ellipse cx="12" cy="14" rx="2.5" ry="4" fill="#f8fafc"/>
          <polygon points="10.5,8 13.5,8 12,10" fill="#f59e0b"/>
          <circle cx="10.5" cy="6.5" r="0.6" fill="#000000"/>
          <circle cx="13.5" cy="6.5" r="0.6" fill="#000000"/>
          <ellipse cx="9" cy="21" rx="2" ry="0.8" fill="#f59e0b"/>
          <ellipse cx="15" cy="21" rx="2" ry="0.8" fill="#f59e0b"/>
        </g>'''
    },
    {
        "id": "planet-systems",
        "rx": 138, "ry": 52, "phi": 5 * math.pi / 6, # 150 deg (Top-Left)
        "label": '''<text y="23" text-anchor="middle" class="mono" font-size="7" font-weight="700" fill="#f8fafc" letter-spacing="0.03em">SYSTEMS</text>
                    <text y="30" text-anchor="middle" class="mono" font-size="6" font-weight="700" fill="#f8fafc" letter-spacing="0.02em">PROGRAMMING</text>''',
        "icon": '''
        <g transform="translate(-7, -7) scale(0.58)">
          <path stroke="#a855f7" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" fill="none" d="M8 7L3 12L8 17M16 7L21 12L16 17M14 4L10 20"/>
        </g>'''
    },
    {
        "id": "planet-opensource",
        "rx": 176, "ry": 68, "phi": 7 * math.pi / 6, # 210 deg (Bottom-Left)
        "label": '''<text y="23" text-anchor="middle" class="mono" font-size="7" font-weight="700" fill="#f8fafc" letter-spacing="0.03em">OPEN</text>
                    <text y="30" text-anchor="middle" class="mono" font-size="7" font-weight="700" fill="#f8fafc" letter-spacing="0.03em">SOURCE</text>''',
        "icon": '''
        <g transform="translate(-7, -7) scale(0.58)">
          <path fill="#f8fafc" fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
        </g>'''
    },
    {
        "id": "planet-ai",
        "rx": 214, "ry": 84, "phi": 3 * math.pi / 2, # 270 deg (Bottom)
        "label": '<text y="24" text-anchor="middle" class="mono" font-size="8.5" font-weight="700" fill="#f8fafc" letter-spacing="0.08em">AI</text>',
        "icon": '''
        <g transform="translate(-7, -7) scale(0.58)">
          <path fill="#f8fafc" d="M12 2L14.4 8.6L21 11L14.4 13.4L12 20L9.6 13.4L3 11L9.6 8.6Z"/>
          <path fill="#c084fc" d="M19 16L20 18.2L22.2 19.2L20 20.2L19 22.4L18 20.2L15.8 19.2L18 18.2Z"/>
        </g>'''
    },
    {
        "id": "planet-technology",
        "rx": 252, "ry": 100, "phi": 11 * math.pi / 6, # 330 deg (Bottom-Right)
        "label": '<text y="24" text-anchor="middle" class="mono" font-size="7" font-weight="700" fill="#f8fafc" letter-spacing="0.05em">TECHNOLOGY</text>',
        "icon": '''
        <g transform="translate(-7, -7) scale(0.58)">
          <path fill="#22d3ee" d="M19 15v-2h2v-2h-2V9h2V7h-2c0-1.1-.9-2-2-2h-2V3h-2v2h-2V3H9v2H7c-1.1 0-2 .9-2 2v2H3v2h2v2H3v2h2v2c0 1.1.9 2 2 2h2v2h2v-2h2v2h2v-2h2c1.1 0 2-.9 2-2v-2h2v-2h-2v-2zm-4 4H9c-.55 0-1-.45-1-1V9c0-.55.45-1 1-1h6c.55 0 1 .45 1 1v8c0 .55-.45 1-1 1zm-4-7h2v2h-2v-2z"/>
        </g>'''
    },
    {
        "id": "planet-engineering",
        "rx": 290, "ry": 116, "phi": math.pi / 6, # 30 deg (Top-Right)
        "label": '<text y="24" text-anchor="middle" class="mono" font-size="7" font-weight="700" fill="#f8fafc" letter-spacing="0.05em">ENGINEERING</text>',
        "icon": '''
        <g transform="translate(-7, -7) scale(0.58)">
          <path fill="#38bdf8" d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58a.49.49 0 0 0 .12-.61l-1.92-3.32a.488.488 0 0 0-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54A.484.484 0 0 0 14 2h-4c-.25 0-.46.18-.49.42l-.36 2.54c-.59.24-1.13.56-1.62.94l-2.39-.96a.488.488 0 0 0-.59.22L2.63 8.47c-.13.22-.08.49.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58a.49.49 0 0 0-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h4c.25 0 .46-.18.49-.42l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.49-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/>
        </g>'''
    }
]

planets_svg_blocks = []
for p in planets_cfg:
    pts = []
    for k in range(N_STEPS + 1):
        t = k / float(N_STEPS) * 2 * math.pi
        angle = p["phi"] + t
        x = round(CX + p["rx"] * math.cos(angle), 1)
        y = round(CY - p["ry"] * math.sin(angle), 1)
        pts.append(f"{x} {y}")
    val_str = "; ".join(pts)

    block = f'''
  <g id="{p['id']}">
    <animateTransform attributeName="transform" type="translate" values="{val_str}" dur="{PERIOD}s" repeatCount="indefinite" />
    <circle cx="0" cy="0" r="13.5" class="planet-disc"/>
    <circle cx="0" cy="0" r="11" class="planet-inner"/>
    {p['icon']}
    {p['label']}
  </g>'''
    planets_svg_blocks.append(block)

all_planets_svg = "\n".join(planets_svg_blocks)

solar_system_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} 220" width="100%" height="220">
  <defs>
    <clipPath id="avatar-clip">
      <circle cx="{CX}" cy="{CY}" r="24"/>
    </clipPath>

    <radialGradient id="discGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#141e33"/>
      <stop offset="100%" stop-color="#070c18"/>
    </radialGradient>

    <style>
      .mono {{ font-family: {FONT_FAMILY}; }}
      .orbit-line {{
        fill: none;
        stroke: #162942;
        stroke-width: 1.1px;
        stroke-dasharray: 4 5;
      }}
      .planet-disc {{
        fill: url(#discGrad);
        stroke: #38bdf8;
        stroke-width: 1.2px;
      }}
      .planet-inner {{
        fill: none;
        stroke: #ffffff;
        stroke-width: 0.6px;
        stroke-dasharray: 2 2.5;
        opacity: 0.3;
      }}
    </style>
  </defs>

  <rect x="0.5" y="0" width="{WIDTH - 1}" height="220" fill="#080d1a" stroke="#162238" stroke-width="1"/>

  <!-- Static Starfield -->
  <g fill="#38bdf8" opacity="0.6">
    <circle cx="45" cy="35" r="0.9"/>
    <circle cx="110" cy="95" r="1.1"/>
    <circle cx="630" cy="45" r="0.9"/>
    <circle cx="640" cy="180" r="1.1"/>
    <circle cx="230" cy="25" r="0.8"/>
    <circle cx="460" cy="205" r="1"/>
    <circle cx="560" cy="190" r="0.9"/>
    <circle cx="70" cy="185" r="1"/>
    <circle cx="410" cy="20" r="0.8"/>
  </g>

  <!-- 6 Orbit Tracks -->
  <g>
    <ellipse cx="{CX}" cy="{CY}" rx="100" ry="36" class="orbit-line" stroke-opacity="0.85"/>
    <ellipse cx="{CX}" cy="{CY}" rx="138" ry="52" class="orbit-line" stroke-opacity="0.80"/>
    <ellipse cx="{CX}" cy="{CY}" rx="176" ry="68" class="orbit-line" stroke-opacity="0.75"/>
    <ellipse cx="{CX}" cy="{CY}" rx="214" ry="84" class="orbit-line" stroke-opacity="0.70"/>
    <ellipse cx="{CX}" cy="{CY}" rx="252" ry="100" class="orbit-line" stroke-opacity="0.65"/>
    <ellipse cx="{CX}" cy="{CY}" rx="290" ry="116" class="orbit-line" stroke-opacity="0.55"/>
  </g>

  <!-- Central Luffy Avatar (Sun) -->
  <g id="center-sun">
    <circle cx="{CX}" cy="{CY}" r="30" fill="none" stroke="#38bdf8" stroke-width="1.1" stroke-dasharray="3 3" opacity="0.5"/>
    <circle cx="{CX}" cy="{CY}" r="26" fill="#080d1a" stroke="#38bdf8" stroke-width="1.6"/>
    
    <image href="{pfp_b64}" x="{CX - 24}" y="{CY - 24}" width="48" height="48" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>

    <text x="{CX}" y="{CY + 40}" text-anchor="middle" class="mono" font-size="11" font-weight="800" fill="#f8fafc" letter-spacing="0.16em">MARUDHU</text>
  </g>

  <!-- 6 Revolving Planets -->
  {all_planets_svg}

  <line x1="0" y1="219.5" x2="{WIDTH}" y2="219.5" stroke="#162238" stroke-width="1"/>
</svg>
'''

with open('assets/solar-system.svg', 'w') as f:
    f.write(solar_system_svg)

# ========================================================
# 3. WHOAMI BRICK (assets/whoami.svg)
# ========================================================
whoami_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} 142" width="100%" height="142">
  <defs>
    <style>
      .mono {{ font-family: {FONT_FAMILY}; }}
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; }}
    </style>
  </defs>

  <rect x="0.5" y="0" width="{WIDTH - 1}" height="142" fill="#080d1a" stroke="#162238" stroke-width="1"/>

  <!-- Prompt -->
  <text x="20" y="22" class="mono" font-size="12.5" font-weight="700">
    <tspan fill="#10b981">&gt; </tspan>
    <tspan fill="#38bdf8">whoami</tspan>
  </text>

  <!-- Title -->
  <text x="20" y="47" class="sans" font-size="22" font-weight="800">
    <tspan fill="#f8fafc">Hey, I'm </tspan>
    <tspan fill="#a855f7">Marudhu.</tspan>
  </text>

  <!-- Subtitle -->
  <text x="20" y="65" class="mono" font-size="11.5" font-weight="500" fill="#94a3b8">
    Engineering Student / Curious by Nature
  </text>

  <!-- Accent Bar -->
  <rect x="20" y="77" width="2.5" height="52" rx="1.2" fill="#10b981"/>

  <!-- Bio Quote Text -->
  <text x="32" y="89" class="mono" font-size="11.5" fill="#cbd5e1" font-weight="400">
    <tspan x="32" dy="0">I'm an engineering student, figuring things out</tspan>
    <tspan x="32" dy="14">one step at a time. I like understanding how</tspan>
    <tspan x="32" dy="14">things work, exploring new ideas, and going</tspan>
    <tspan x="32" dy="14">deeper than the surface.</tspan>
  </text>

  <line x1="0" y1="141.5" x2="{WIDTH}" y2="141.5" stroke="#162238" stroke-width="1"/>
</svg>
'''

with open('assets/whoami.svg', 'w') as f:
    f.write(whoami_svg)

# ========================================================
# 4. QUESTS & EXPLORATION LOG (assets/quests-and-log.svg)
# ========================================================
quests_and_log_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} 160" width="100%" height="160">
  <defs>
    <style>
      .mono {{ font-family: {FONT_FAMILY}; }}
    </style>
  </defs>

  <rect x="0.5" y="0" width="{WIDTH - 1}" height="160" fill="#080d1a" stroke="#162238" stroke-width="1"/>
  <line x1="325" y1="8" x2="325" y2="152" stroke="#162238" stroke-width="1"/>

  <!-- ================= LEFT: QUESTS ================= -->
  <text x="20" y="22" class="mono" font-size="12.5" font-weight="700">
    <tspan fill="#10b981">&gt; </tspan>
    <tspan fill="#f8fafc">quests </tspan>
    <tspan fill="#64748b" font-weight="400">(ongoing)</tspan>
  </text>

  <!-- Quest 1 -->
  <g transform="translate(20, 36)">
    <rect x="0" y="0" width="11" height="11" rx="2" fill="none" stroke="#64748b" stroke-width="1.4"/>
    <text x="20" y="9.5" class="mono" font-size="11.5" font-weight="500" fill="#f8fafc">Deepen Core Understanding</text>
  </g>

  <!-- Quest 2 -->
  <g transform="translate(20, 63)">
    <rect x="0" y="0" width="11" height="11" rx="2" fill="none" stroke="#64748b" stroke-width="1.4"/>
    <text x="20" y="9.5" class="mono" font-size="11.5" font-weight="500" fill="#f8fafc">Build Meaningful Things</text>
  </g>

  <!-- Quest 3 -->
  <g transform="translate(20, 90)">
    <rect x="0" y="0" width="11" height="11" rx="2" fill="none" stroke="#64748b" stroke-width="1.4"/>
    <text x="20" y="9.5" class="mono" font-size="11.5" font-weight="500" fill="#f8fafc">Contribute to Open Source</text>
  </g>

  <!-- Quest 4 -->
  <g transform="translate(20, 117)">
    <rect x="0" y="0" width="11" height="11" rx="2" fill="none" stroke="#64748b" stroke-width="1.4"/>
    <text x="20" y="9.5" class="mono" font-size="11.5" font-weight="500" fill="#f8fafc">Prepare for Bigger Goals</text>
  </g>

  <!-- Active Quest 5 -->
  <g transform="translate(20, 143)">
    <polygon points="0,1 9,6 0,11" fill="#a855f7"/>
    <text x="20" y="10" class="mono" font-size="12" font-weight="700" fill="#c084fc">Keep Exploring ...</text>
  </g>

  <!-- ================= RIGHT: EXPLORATION LOG ================= -->
  <text x="345" y="22" class="mono" font-size="12.5" font-weight="700">
    <tspan fill="#10b981">&gt; </tspan>
    <tspan fill="#f8fafc">exploration log</tspan>
  </text>

  <line x1="352" y1="40" x2="352" y2="145" stroke="#1e2d42" stroke-width="1.8"/>

  <!-- Step 1: Learn -->
  <g transform="translate(352, 40)">
    <circle cx="0" cy="0" r="4" fill="#080d1a" stroke="#38bdf8" stroke-width="2"/>
    <text x="14" y="3.5" class="mono" font-size="10.5">
      <tspan font-weight="700" fill="#f8fafc">Learn</tspan>
      <tspan fill="#475569">   &#8212;   </tspan>
      <tspan fill="#94a3b8">Understand the basics, ask a lot of questions.</tspan>
    </text>
  </g>

  <!-- Step 2: Build -->
  <g transform="translate(352, 66)">
    <circle cx="0" cy="0" r="4" fill="#080d1a" stroke="#34d399" stroke-width="2"/>
    <text x="14" y="3.5" class="mono" font-size="10.5">
      <tspan font-weight="700" fill="#f8fafc">Build</tspan>
      <tspan fill="#475569">   &#8212;   </tspan>
      <tspan fill="#94a3b8">Turn ideas into working things.</tspan>
    </text>
  </g>

  <!-- Step 3: Break -->
  <g transform="translate(352, 92)">
    <circle cx="0" cy="0" r="4" fill="#080d1a" stroke="#fbbf24" stroke-width="2"/>
    <text x="14" y="3.5" class="mono" font-size="10.5">
      <tspan font-weight="700" fill="#f8fafc">Break</tspan>
      <tspan fill="#475569">   &#8212;   </tspan>
      <tspan fill="#94a3b8">Find and fix what doesn't work.</tspan>
    </text>
  </g>

  <!-- Step 4: Experiment -->
  <g transform="translate(352, 118)">
    <circle cx="0" cy="0" r="4" fill="#080d1a" stroke="#c084fc" stroke-width="2"/>
    <text x="14" y="3.5" class="mono" font-size="10.5">
      <tspan font-weight="700" fill="#f8fafc">Experiment</tspan>
      <tspan fill="#475569"> &#8212; </tspan>
      <tspan fill="#94a3b8">Try new tools, new approaches, new perspectives.</tspan>
    </text>
  </g>

  <!-- Step 5: Go Deeper -->
  <g transform="translate(352, 144)">
    <circle cx="0" cy="0" r="4" fill="#080d1a" stroke="#ec4899" stroke-width="2"/>
    <text x="14" y="3.5" class="mono" font-size="10.5">
      <tspan font-weight="700" fill="#f8fafc">Go Deeper</tspan>
      <tspan fill="#475569">  &#8212;  </tspan>
      <tspan fill="#94a3b8">Explore beyond the obvious.</tspan>
    </text>
  </g>

  <line x1="0" y1="159.5" x2="{WIDTH}" y2="159.5" stroke="#162238" stroke-width="1"/>
</svg>
'''

with open('assets/quests-and-log.svg', 'w') as f:
    f.write(quests_and_log_svg)

# ========================================================
# 5. INTERESTS BRICK (assets/interests.svg)
# ========================================================
interests_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} 76" width="100%" height="76">
  <defs>
    <style>
      .mono {{ font-family: {FONT_FAMILY}; }}
    </style>
  </defs>

  <rect x="0.5" y="0" width="{WIDTH - 1}" height="76" fill="#080d1a" stroke="#162238" stroke-width="1"/>

  <!-- Header -->
  <text x="20" y="20" class="mono" font-size="12.5" font-weight="700">
    <tspan fill="#10b981">&gt; </tspan>
    <tspan fill="#f8fafc">interests</tspan>
  </text>

  <!-- Dividers -->
  <line x1="113" y1="28" x2="113" y2="68" stroke="#162238" stroke-width="1"/>
  <line x1="226" y1="28" x2="226" y2="68" stroke="#162238" stroke-width="1"/>
  <line x1="340" y1="28" x2="340" y2="68" stroke="#162238" stroke-width="1"/>
  <line x1="453" y1="28" x2="453" y2="68" stroke="#162238" stroke-width="1"/>
  <line x1="566" y1="28" x2="566" y2="68" stroke="#162238" stroke-width="1"/>

  <!-- 1. Linux -->
  <g transform="translate(56, 38)">
    <g transform="translate(-8, -10) scale(0.68)">
      <path fill="#f8fafc" d="M12 2C8 2 6 5 6 9c0 2.5 1 5 1 8 0 2-1 3-2 4 0 1 2 1 4 1 1 0 1.5-.5 3-2 1.5 1.5 2 2 3 2 2 0 4 0 4-1-1-1-2-2-2-4 0-3 1-5.5 1-8 0-4-2-7-6-7z"/>
      <path fill="#080d1a" d="M12 4c-2.5 0-3.5 2-3.5 5 0 2.5.5 5 .5 8 0 1-.5 1.5-1 2 1 .5 2 .5 3-.5.5-.5 1-1 1-1s.5.5 1 1c1 1 2 1 3 .5-.5-.5-1-1-1-2 0-3 .5-5.5.5-8 0-3-1-5-3.5-5z"/>
      <ellipse cx="12" cy="14" rx="2.5" ry="4" fill="#f8fafc"/>
      <polygon points="10.5,8 13.5,8 12,10" fill="#f59e0b"/>
      <ellipse cx="9" cy="21" rx="2" ry="0.8" fill="#f59e0b"/>
      <ellipse cx="15" cy="21" rx="2" ry="0.8" fill="#f59e0b"/>
    </g>
    <text y="24" text-anchor="middle" class="mono" font-size="10.5" font-weight="600" fill="#f1f5f9">Linux</text>
  </g>

  <!-- 2. Systems -->
  <g transform="translate(170, 38)">
    <g transform="translate(-9, -9) scale(0.75)">
      <path stroke="#a855f7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" d="M8 7L3 12L8 17M16 7L21 12L16 17M14 4L10 20"/>
    </g>
    <text y="24" text-anchor="middle" class="mono" font-size="10.5" font-weight="600" fill="#f1f5f9">Systems</text>
  </g>

  <!-- 3. AI & ML -->
  <g transform="translate(283, 38)">
    <g transform="translate(-10, -10) scale(0.78)">
      <path fill="#ec4899" d="M12 3C8.5 3 6 5.5 6 8.5c0 1.2.4 2.3 1.1 3.2-.7.8-1.1 1.9-1.1 3.1 0 2.6 1.8 4.7 4.2 5.1V21h3.6v-1.1c2.4-.4 4.2-2.5 4.2-5.1 0-1.2-.4-2.3-1.1-3.1.7-.9 1.1-2 1.1-3.2C18 5.5 15.5 3 12 3zm-1 15.1c-1.7-.4-3-2-3-3.9 0-.8.3-1.5.8-2.1l.7-.8-.7-.8c-.5-.6-.8-1.3-.8-2.1 0-1.7 1.3-3.1 3-3.3v13zm5.6-3.9c0 1.9-1.3 3.5-3 3.9v-13c1.7.2 3 1.6 3 3.3 0 .8-.3 1.5-.8 2.1l-.7.8.7.8c.5.6.8 1.3.8 2.1z"/>
    </g>
    <text y="24" text-anchor="middle" class="mono" font-size="10.5" font-weight="600" fill="#f1f5f9">AI &amp; ML</text>
  </g>

  <!-- 4. Open Source -->
  <g transform="translate(396, 38)">
    <g transform="translate(-9, -9) scale(0.75)">
      <path fill="#10b981" fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
    </g>
    <text y="24" text-anchor="middle" class="mono" font-size="10.5" font-weight="600" fill="#f1f5f9">Open Source</text>
  </g>

  <!-- 5. Technology -->
  <g transform="translate(510, 38)">
    <g transform="translate(-9, -9) scale(0.75)">
      <path fill="#22d3ee" d="M19 15v-2h2v-2h-2V9h2V7h-2c0-1.1-.9-2-2-2h-2V3h-2v2h-2V3H9v2H7c-1.1 0-2 .9-2 2v2H3v2h2v2H3v2h2v2c0 1.1.9 2 2 2h2v2h2v-2h2v2h2v-2h2c1.1 0 2-.9 2-2v-2h2v-2h-2v-2zm-4 4H9c-.55 0-1-.45-1-1V9c0-.55.45-1 1-1h6c.55 0 1 .45 1 1v8c0 .55-.45 1-1 1zm-4-7h2v2h-2v-2z"/>
    </g>
    <text y="24" text-anchor="middle" class="mono" font-size="10.5" font-weight="600" fill="#f1f5f9">Technology</text>
  </g>

  <!-- 6. Engineering -->
  <g transform="translate(623, 38)">
    <g transform="translate(-9, -9) scale(0.75)">
      <path fill="#3b82f6" d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58a.49.49 0 0 0 .12-.61l-1.92-3.32a.488.488 0 0 0-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54A.484.484 0 0 0 14 2h-4c-.25 0-.46.18-.49.42l-.36 2.54c-.59.24-1.13.56-1.62.94l-2.39-.96a.488.488 0 0 0-.59.22L2.63 8.47c-.13.22-.08.49.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58a.49.49 0 0 0-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h4c.25 0 .46-.18.49-.42l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.49-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/>
    </g>
    <text y="24" text-anchor="middle" class="mono" font-size="10.5" font-weight="600" fill="#f1f5f9">Engineering</text>
  </g>

  <line x1="0" y1="75.5" x2="{WIDTH}" y2="75.5" stroke="#162238" stroke-width="1"/>
</svg>
'''

with open('assets/interests.svg', 'w') as f:
    f.write(interests_svg)

# ========================================================
# 6. NOW PLAYING BRICK (assets/now-playing.svg)
# ========================================================
eq_bars_svg = ""
eq_keyframes = ""
bar_count = 24

for i in range(bar_count):
    h_min = random.randint(3, 5)
    h_mid = random.randint(11, 20)
    dur = round(random.uniform(0.7, 1.3), 2)
    delay = round(random.uniform(0.0, 0.7), 2)

    eq_keyframes += f'''
      @keyframes eq_{i} {{
        0%, 100% {{ height: {h_min}px; y: {38 - h_min // 2}px; }}
        50% {{ height: {h_mid}px; y: {38 - h_mid // 2}px; }}
      }}
      .bar-{i} {{
        animation: eq_{i} {dur}s ease-in-out infinite {delay}s;
      }}
    '''
    # Waveform from x=260 to x=450
    x_pos = 260 + i * 8.0
    eq_bars_svg += f'<rect class="bar-{i}" x="{x_pos}" y="{38 - h_min // 2}" width="3" height="{h_min}" rx="1.5" fill="url(#waveGrad)"/>\n'

now_playing_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} 74" width="100%" height="74">
  <defs>
    <linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#22d3ee"/>
    </linearGradient>

    <linearGradient id="albumCoverGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2e1065"/>
      <stop offset="45%" stop-color="#a21caf"/>
      <stop offset="70%" stop-color="#fb7185"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>

    <clipPath id="albumClip">
      <rect x="20" y="14" width="46" height="46" rx="6"/>
    </clipPath>

    <style>
      .mono {{ font-family: {FONT_FAMILY}; }}
      {eq_keyframes}
    </style>
  </defs>

  <rect x="0.5" y="0" width="{WIDTH - 1}" height="74" fill="#080d1a" stroke="#162238" stroke-width="1"/>

  <!-- Left: Album Art -->
  <g clip-path="url(#albumClip)">
    <rect x="20" y="14" width="46" height="46" fill="url(#albumCoverGrad)"/>
    <rect x="24" y="38" width="5" height="22" fill="#090d16" opacity="0.8"/>
    <rect x="31" y="33" width="7" height="27" fill="#090d16" opacity="0.9"/>
    <rect x="40" y="41" width="5" height="19" fill="#090d16" opacity="0.7"/>
    <rect x="51" y="36" width="6" height="24" fill="#090d16" opacity="0.8"/>
    <circle cx="43" cy="37" r="8" fill="#020617"/>
    <path d="M35 37 C35 32 39 28 43 28 C47 28 51 32 51 37" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
    <rect x="33.5" y="35" width="3" height="5.5" rx="1.2" fill="#38bdf8"/>
    <rect x="49.5" y="35" width="3" height="5.5" rx="1.2" fill="#38bdf8"/>
    <path d="M36 49 C38 45 48 45 50 49" fill="#020617"/>
  </g>
  <rect x="20" y="14" width="46" height="46" rx="6" fill="none" stroke="#334155" stroke-width="1"/>

  <!-- Track Info -->
  <g transform="translate(76, 17)">
    <text x="0" y="12" class="mono" font-size="10.5" font-weight="700" fill="#10b981">Now Playing</text>
    <text x="0" y="31" class="mono" font-size="12" font-weight="600" fill="#f1f5f9">
      Lofi Beats <tspan fill="#94a3b8" font-size="10.5">(ChilledCow)</tspan>
    </text>
  </g>

  <!-- Live Equalizer Bars -->
  <g id="soundwave">
    {eq_bars_svg}
  </g>

  <!-- Timestamp at x=475 -->
  <text x="475" y="42" class="mono" font-size="11" font-weight="500" fill="#94a3b8">
    02:14 / 03:56
  </text>

  <!-- Pause Button (⏸) at x=585 -->
  <g transform="translate(585, 32)">
    <rect x="0" y="0" width="3" height="13" rx="1.2" fill="#f8fafc"/>
    <rect x="5.5" y="0" width="3" height="13" rx="1.2" fill="#f8fafc"/>
  </g>

  <!-- Volume Button (🔊) at x=625 -->
  <g transform="translate(625, 31)">
    <polygon points="0,4.5 3.5,4.5 7.5,1 7.5,13.5 3.5,10 0,10" fill="#94a3b8"/>
    <path d="M10 3.5 C11.5 5.5 11.5 8.5 10 11" stroke="#94a3b8" stroke-width="1.3" fill="none" stroke-linecap="round"/>
    <path d="M12.5 1.5 C15 4.5 15 10 12.5 13" stroke="#94a3b8" stroke-width="1.3" fill="none" stroke-linecap="round"/>
  </g>

  <line x1="0" y1="73.5" x2="{WIDTH}" y2="73.5" stroke="#162238" stroke-width="1"/>
</svg>
'''

with open('assets/now-playing.svg', 'w') as f:
    f.write(now_playing_svg)

# ========================================================
# 7. FOOTER BRICK (assets/footer.svg)
# ========================================================
footer_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} 34" width="100%" height="34">
  <defs>
    <style>
      .mono {{ font-family: {FONT_FAMILY}; }}
    </style>
  </defs>

  <!-- Bottom Rounded Corners -->
  <rect x="0.5" y="0" width="{WIDTH - 1}" height="33.5" rx="8" ry="8" fill="#080d1a" stroke="#162238" stroke-width="1"/>

  <text x="20" y="21" class="mono" font-size="11.5" font-weight="500">
    <tspan fill="#10b981">&gt; </tspan>
    <tspan fill="#cbd5e1">Still curious. Always evolving.</tspan>
  </text>

  <text x="{WIDTH - 20}" y="21" text-anchor="end" class="mono" font-size="13" font-weight="700" fill="#38bdf8" letter-spacing="0.1em">
    ///
  </text>
</svg>
'''

with open('assets/footer.svg', 'w') as f:
    f.write(footer_svg)

print("Generated pixel-perfect 680px bricks!")
