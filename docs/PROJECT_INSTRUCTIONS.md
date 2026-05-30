# Mr. Do Ultra - Project Instructions

**Repository:** https://github.com/erkkilai/mr-do-ultra  
**Working Title:** Mr. Do Ultra (or Mr. Do! Modern / Clown Dig 2026)  
**Status:** Active iterative development  
**Last Updated:** May 29, 2026

## 1. Project Overview

This is a modern reimagining of the 1982 Universal arcade classic *Mr. Do!*. The goal is to create a faithful yet elevated experience that preserves the addictive core loop of digging tunnels, collecting cherries, using physics-based apples, and the signature bouncing Powerball, while adding modern production values, deeper strategy, accessibility, and replayability.

**Target Platforms (future):** PC (Steam), handheld (Steam Deck, Legion Go), mobile, web export.

**Core Philosophy:** Arcade-tight sessions (2–8 minutes per run) with "just one more try" addiction, whimsical circus/clown theme suitable for all ages, and strategic depth for experienced players.

## 2. Current Status (v0.1 Prototype)

- **Engine:** Python + Pygame (rapid prototyping phase)
- **Location of code:** `src/` directory
- **Playable features:**
  - Destructible dirt grid with pre-dug tunnels (letter/number inspired layouts)
  - Smooth player movement and real-time digging
  - Cherry collection with scoring
  - Basic glowing Powerball stub (straight-line throw in facing direction)
  - Multiple cherries and level-clear condition (collect all)
  - Simple but expressive clown visual representation
- **Files:**
  - `src/constants.py` – Screen, grid, colors, speeds, timings
  - `src/level.py` – Dirt grid logic, tunnel generation, cherry placement and collection
  - `src/player.py` – Movement, digging, facing direction, basic Powerball
  - `src/main.py` – Game loop, rendering, UI, input handling
- **Supporting files:** `requirements.txt`, `.gitignore`, `docs/PROJECT_INSTRUCTIONS.md` (this file)

The prototype is fully functional and can be run with:
```bash
git clone https://github.com/erkkilai/mr-do-ultra.git
cd mr-do-ultra
pip install -r requirements.txt
python src/main.py
```

## 3. Development Workflow (Grok Build + Terminal)

**Primary collaboration model:**
1. In this conversation, request specific features, bug fixes, code reviews, or design decisions using clear, precise language.
2. Grok will respond with:
   - Complete, ready-to-paste code (full files or diffs)
   - Explanations of implementation choices
   - Testing recommendations
   - Suggestions for follow-up iterations
3. On your local machine:
   - Apply changes to the appropriate files in `src/`
   - Use terminal for version control:
     ```bash
     git add src/
     git commit -m "feat: descriptive message following conventional commits"
     git push origin main
     ```
4. For larger features, create a feature branch:
   ```bash
   git checkout -b feature/apple-physics
   # ... work ...
   git push origin feature/apple-physics
   ```
   Then request a PR description if needed.

**Commit message convention (recommended):** Use Conventional Commits (feat, fix, docs, refactor, test, chore).

**When to use direct repo updates vs local workflow:** Local terminal workflow is preferred for your control and learning. Grok can also directly update files in the repository via secure tools when rapid seeding or complex multi-file changes are required.

## 4. Core Faithfulness Requirements (Non-Negotiable)

The following mechanics from the 1982 original must be faithfully recreated with modern precision and feel:

- Single-screen (or optional camera-follow for larger levels) colorful underground environment with destructible dirt and pre-dug tunnel patterns.
- Primary win conditions per level: Collect all cherries **OR** defeat all enemies **OR** spell "EXTRA" **OR** (rare) collect special Diamond.
- Apples as interactive physics objects: pushable along tunnels, fall when undermined, crush enemies (and risk self-crush). Enemies can push apples. Support chain reactions.
- Powerball: Throwable bouncing "superball" that ricochets unpredictably at junctions. One-kill per use + cooldown. High skill expression and risk/reward.
- Enemies ("Creeps"): Red chasers emerging from central doorway/hive. They become aggressive diggers later. Escalating waves.
- Alphamonster event: After all regular enemies appear, doorway becomes prize → spawns Alphamonster + 4 henchmen (tougher, apple-resistant). Killing Alpha converts henchmen to apples.
- Multiple viable strategies and scoring depth per level.

Levels must feel arcade-tight with high replayability.

## 5. Art Direction & Juice

- **Visual style:** Vibrant, saturated retro-modern. Bright 80s arcade colors (cherry reds, electric blues, sunny yellows) combined with clean modern pixel art or high-clarity 2D cartooning. Expressive animations for Mr. Do (digging poses, wind-up throws, victory dances).
- **Juice:** Screen shake on impacts, flying dirt particles/clods, satisfying pop animations on collection, dynamic lighting/glow on Powerball, impact effects.
- **Theme:** Cheerful circus clown (big red nose, colorful striped outfit, floppy shoes). Enemies are whimsical-but-threatening weird creatures (Muppet-adjacent energy, not nightmare fuel). Layered colorful dirt with depth.
- **Family-friendly:** Whimsical tone suitable for all ages while offering strategic depth.

## 6. Planned Modern Enhancements (Prioritized for MVP)

1. **Physics & Emergence** (High priority next): Full 2D physics for apples (rolling, slight bounce, stacking, chain crushing). Varied dirt density or temporary structures in later levels.
2. **Enemy Variety & Smart AI**: Core creeps + diggers + new types (cherry thieves, tunnel-filling builders, flyers). Reactive AI. Alphamonster as proper mini-boss.
3. **Powerball Evolution**: Core bouncing + temporary upgrades/power-ups (multi-ball, charged shot, short homing, freeze). Make it a skill centerpiece.
4. **Progression & Variety**: 30–50+ levels across themed circus zones. Hand-crafted campaign + procedural/endless mode with modifiers. Unlockable Mr. Do costumes/skins. Meta systems (high scores, challenges, letter/Diamond hunting).
5. **Polish & Accessibility**: 60+ FPS, gamepad/keyboard/touch controls, trajectory preview or assist modes (without removing challenge), colorblind support, adjustable difficulty, practice arena.
6. **Audio & Feel**: Catchy chiptune or modern-remixed circus/underground soundtrack that intensifies. Juicy sound effects for every action. Expanded intermission animations.
7. **Multiplayer (Post-MVP)**: Local co-op (two clowns) and hotseat competitive modes.

## 7. Technical Guidelines

- **Initial prototyping:** Python + Pygame. Keep code clean, modular, and well-commented. Separate concerns (player, level, entities, UI, constants).
- **Future migration:** Once core loop feels excellent, plan migration to Godot 4 (excellent 2D tools, particles, animation, export to multiple platforms).
- **Performance:** Efficient grid-based operations. Target stable 60 FPS even with many entities.
- **Code quality:** Use meaningful variable names, avoid magic numbers (use constants), add docstrings for classes/functions. Type hints encouraged for larger systems.
- **Assets:** Start with procedural/simple shapes. Later integrate generated pixel art or hand-crafted sprites (use image generation tools for concepts).
- **Version control:** Main branch for stable prototype. Feature branches for new systems. Clear commit messages.

## 8. How to Request Work from Grok

Provide requests in this format for best results:
- Clear goal (e.g., "Implement full apple physics with pushing, falling, and chain reactions")
- Any specific constraints or desired behavior
- Preferred file(s) to modify
- Testing focus (e.g., "Test with multiple apples stacked near enemies")

I will deliver:
- Complete updated code ready to paste
- Explanation of key decisions and trade-offs
- Potential follow-up improvements
- Suggested test scenarios

## 9. Immediate Next Steps (Proposed)

1. Test v0.1 locally and provide feedback on movement feel, digging weight, collection feedback, and any bugs.
2. v0.2: Implement realistic apple physics + improved Powerball (bouncing logic that respects tunnels).
3. Add basic enemy spawning and simple chase AI.
4. Expand win conditions (kill all enemies, EXTRA letters).
5. Generate concept art for Mr. Do, enemies, and improved visuals.
6. Create initial Game Design Document (GDD) expansion if desired.

## 10. Notes

- Keep the experience whimsical and family-friendly while adding strategic depth.
- All changes should maintain the "one more credit" arcade addiction.
- This document serves as the single source of truth for project direction. Update it as major decisions are made.

**Let's continue building.** Provide your feedback on v0.1 or specify the next feature to implement.