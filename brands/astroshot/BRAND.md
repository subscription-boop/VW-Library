# Astroshot

Source of this brand file: the two reference boards supplied by the user on 2026-10-21 (`D:\AS\insta videos\output`), copied to `examples/`. The boards mark each item as **verified** (from the website/CSS), **observed** (sampled from Astroshot's own posts and videos) or **proposed**. This file keeps those labels. Nothing here is an official brand manual; items marked missing must be asked for.

- `examples/astroshot-brand-reference-4k.png`: visual identity / technical reference (website-verified foundation).
- `examples/astroshot-visual-motion-reference-8k.png`: visual & motion identity from Instagram content (photo + video + AI production).

## Identity
Astroshot Media: production studio for film, CGI, VFX, mixed reality and AI production (services verified on the website). Audience: Kuwait and GCC brands. Personality: premium, cinematic, high-contrast, modern, bold, clean; tech-forward, VFX/CGI-inspired. Tagline seen on the board: "Bold ideas. Cinematic content. Clear impact."

## Colors
| Role | Value | Status | Notes |
| :- | :- | :- | :- |
| Primary green | #01F17C | verified (website) | The brand accent. CTAs, emphasis words, "SHOT" in the split wordmark |
| Green as seen in videos | #00EE7A | observed | Same green after encoding/bloom; use #01F17C as the token |
| Black | #000000 / #050505 | verified (#050505), observed (#000000) | Main background |
| Dark surfaces | #0D0D0D, #111111, #171717 | verified (#0D0D0D, #111111), observed (#171717) | Cards, panels |
| Additional neutral | #141414 | proposed | |
| Light surface | #FFFFFF / #FAFAFA | verified | Light slides/CTA (rare) |
| White lettering | #F7FFFB | observed | Slightly green-tinted white in videos |
| Muted text | white at 60% opacity | verified | Secondary copy |
| Muted gray | #9C9C9C | observed | |
| Context only | orange #FB9C4C, blue #839BBA | observed | From client footage; NOT brand colours |
| Secondary accent | none | verified as absent | Do not invent one |

## Color treatment for video
- Dark wrappers with controlled green accents; green bloom/glow around key shapes and text ("sharp text + soft surrounding glow").
- Keep the client footage's own colours and believable lighting inside the work; do not apply a blanket green grade.
- Metallic highlights and dark textures in branded graphics; daylight, blue sky and client colours inside embedded work.

## Typography
| Use | Font | Weight | Case | Notes |
| :- | :- | :- | :- | :- |
| Wordmark | Montserrat | 900 | uppercase | verified (observed website wordmark) |
| Headlines / hero | Montserrat | 800 (900 for punch) | uppercase or sentence | verified family; hero 96 px desktop observed |
| Body | Montserrat | 400 | sentence | verified; 16–18 px web |
| Navigation / UI / labels | Montserrat | 600 (400–700) | sentence or spaced uppercase for tags | verified / proposed |
| Arabic | unknown | – | – | **missing**: Arabic overlays exist in videos (green + white) but the typeface is unverified; ask for the font |

Font files: `fonts/Montserrat-{Regular,SemiBold,Bold,ExtraBold,Black}.ttf` (open-source OFL, Latin subset, added for production; see `fonts/README.md`).

Typical hierarchy seen in posts: oversized heavy uppercase headline, often split white + green ("MILLIONAIRES" green / "VIEWS CLUB" white; "How we got / 15.8 MILLION / Views"), then a regular-weight body line with one green emphasis phrase.

## Logo usage
- **Logo masters are missing.** Only raster crops from the boards exist (`examples/observed-*.png`). Do not use these crops as production logos, do not redraw or AI-generate the logo. Ask the user for SVG/PNG masters before any edit that needs the logo.
- Observed lockups: white inline wordmark (P01), split wordmark "ASTRO" green + "SHOT" white (P02), black on light (P08), stacked icon over "ASTROSHOT / PROJECT MANAGEMENT COMPANY" (P11), icon only: white upward chevron/arrow (P14). Current primary vs legacy status is not established.
- Website wordmark: "ASTRO" white + "SHOT" green, Montserrat 900.
- Clear space: proposed 1x cap height on all sides. Minimum size: not published.
- Observed logo animation (V04 end): oversized dark 3D icon → scale down → white fill + glow → stacked lockup → hold (~17.5–19.5 s).
- Small wordmark often sits bottom-left on posts with the website "astroshotmedia.com".

## Graphic elements
- Rounded cards and containers (16 px radius), dark surface, fine 1 px border; pills/tags 12 px radius, dark with fine border, spaced uppercase label (verified/observed web style).
- Buttons: green fill + black text (primary); transparent with 1 px green border + green text (secondary).
- Glass cards / translucent rounded rows with green icon squares; luminous card edges; green bloom; fine perspective grid; rings; plus signs; swipe line + chevrons ">>" (observed in posts).
- Metric-led covers: huge number, metallic/green gradient type.

## Motion (observed in Astroshot videos, not specifications)
- Pacing: client logos flashed ~0.2 s each; role/word cards held ~0.9 s; work shots ~0.4–1.1 s; portfolio tiles play inside a steady layout.
- Transitions: hard cuts in proof montages; expanding/contracting green circle; perspective tile travel; fade before a closing line. No common easing curve.
- Camera: virtual push/tilt through card grids; animated objects and product reveals.
- Text: staggered two-line reveal with reflection; incremental word reveal with alternating black/white emphasis on full-screen green; kinetic Arabic type; green/white Arabic captions on dark backing.
- Full-screen flat green cards with bold white or black uppercase words ("CREATIVE", "SOCIAL MEDIA RETAINER"), black end card with small green line ("Let's have a talk.").
- Narrative models: (A) English service promo: 1 s two-line hook → angled portfolio mosaic → work clips → sector cards → fade + short closing line. (B) Arabic explainer: object + Arabic title → green wave → rapid montage → portfolio corridor + CTA. (C) CGI showreel: montage → 3D icon resolves to white lockup → end hold. (D) Portfolio loops ~5–11 s.
- Format: 9:16 for promos; ~4:5 stills and card loops.
- Sound: music, VO, beat sync and sound signature were not verified (not listened to).

## Tone
Confident, short and clear. Large metrics, short headings, clear body copy. English and Arabic (Gulf) audiences. "Bold ideas. Cinematic content. Clear impact."

## Do / Don't
- Do: strong hierarchy; controlled green accents; generous negative space; keep identity and client footage distinct; use approved source artwork; design for portrait viewing; choose the format from the brief.
- Don't: crowded compositions; decorative space clichés (no recurring space/astro motif verified); unapproved logo variants; regenerating logos with AI; blanket green grade; inventing a secondary colour; inventing performance numbers or claims (view counts in artwork are source claims only); certifying a font by appearance.

## Files
- `examples/astroshot-brand-reference-4k.png`: identity/technical reference board.
- `examples/astroshot-visual-motion-reference-8k.png`: visual & motion board.
- `examples/observed-lockup-*.png`, `examples/observed-icon-P14.png`: reference crops of observed logos (NOT masters).
- `examples/motion-grammar-strip.png`: timed frames from the V02 service promo.
- `examples/reels-editing-model.png`: the four observed narrative models.
- `fonts/`: Montserrat 400/600/700/800/900 (OFL).
- `logos/README.md`: what is missing.

## Missing information
- SVG/PNG logo masters (inline, split-colour, stacked, icon), light-background version, official clear space and minimum size.
- Approved master HEX palette (green varies between #01F17C and #00EE7A).
- Arabic typeface (name + files).
- Brand sound / music direction (nothing verified).
- Instagram post exports (the boards say the Instagram style could not be fully reviewed).
