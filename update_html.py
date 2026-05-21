import os
import glob
import re
from bs4 import BeautifulSoup

blog_texts = [
    {
        "title": "Saphira’s “Listen To Me” Turns Seduction Into a Form of Healing",
        "description": "The dark-pop artist explores emotional intimacy, obsession, and the strange comfort of feeling emotionally consumed by someone.",
        "content": [
            "The dark-pop artist explores emotional intimacy, obsession, and the strange comfort of feeling emotionally consumed by someone.",
            "“I wanted this song to feel like someone crawling inside your mind softly instead of breaking the door down.”",
            "There’s a specific kind of intimacy that doesn’t feel loud or explosive. It feels hypnotic. Slow. Dangerous but in a comforting way. That emotional space is exactly where Saphira’s upcoming single “Listen To Me” lives. Blending dark pop production with vulnerable lyricism, the track explores what it feels like to become emotionally intertwined with another person so deeply that their voice, touch, and presence begin to feel almost medicinal.",
            "Rather than writing a traditional love song, Saphira approaches romance from a more psychologically intimate angle. Throughout the track, affection becomes something immersive — almost consuming. In the chorus, she repeats:",
            "“Listen to me, my voice is your medicine.”",
            "The line captures the emotional core of the song: wanting to soothe someone while simultaneously becoming impossible for them to escape.",
            "In the bridge, Saphira leans further into the song’s hypnotic atmosphere with lyrics like:",
            "“Tonight, drown with me / Haunt me endlessly.”",
            "Instead of portraying love as safe or perfect, “Listen To Me” presents intimacy as something haunting, addictive, and emotionally transformative.",
            "Fans have already started comparing the track’s cinematic atmosphere to darker alternative-pop artists, though Saphira’s writing remains distinctly personal. The singer has previously spoken about writing all of her lyrics herself in order to preserve emotional authenticity in her music.",
            "Rather than chasing perfectly polished pop writing, Saphira seems more interested in emotional precision. Many of her lyrics feel less like traditional songwriting and more like fragmented inner thoughts whispered out loud. Intimate, slightly dangerous, and deeply self-aware.",
            "That emotional honesty becomes especially visible in “Listen To Me,” where desire and healing constantly blur into each other. Throughout the track, affection isn’t presented as soft or innocent. Instead, it feels consuming, hypnotic, almost addictive.",
            "Even the song’s central lyric “My voice is your medicine” leaves room for interpretation. Is the narrator comforting someone emotionally, or becoming something they emotionally depend on? Saphira never fully answers that question, and that ambiguity gives the track much of its haunting power.",
            "Sonically, the production mirrors that emotional tension. Dark textures, slow-burning intensity, and breath-like vocal layering create the feeling of being pulled deeper and deeper into someone else’s emotional world.",
            "If “Listen To Me” is any indication of where Saphira’s artistry is heading, she may be building a lane that feels less like mainstream pop and more like psychological storytelling wrapped inside music."
        ]
    },
    {
        "title": "Saphira’s “Collective Hypnosis” Was Designed to Pull Listeners Into an Emotional Trance",
        "description": "The upcoming EP blends dark pop, emotional vulnerability, and hypnotic atmosphere into something designed to be deeply immersive.",
        "content": [
            "The upcoming EP blends dark pop, emotional vulnerability, and hypnotic atmosphere into something designed to be deeply immersive.",
            "“I wanted people to put headphones on, close their eyes, and feel psychologically pulled somewhere else for a moment.”",
            "Saphira didn’t choose the title Collective Hypnosis randomly. According to the artist, the phrase sat in her mind for months before eventually becoming the emotional center of the project.",
            "The upcoming EP explores the invisible emotional programming people absorb throughout their lives, ideas about love, identity, femininity, self-worth, and desire that often feel personal, even when they were quietly inherited from the world around them.",
            "“We’re all under some kind of hypnosis already,” Saphira explains. “By culture. By expectations. By the versions of ourselves we learned to perform before we were old enough to question them.”",
            "Rather than confronting those ideas aggressively, Collective Hypnosis approaches them through atmosphere, vulnerability, and emotional immersion. The project’s production and intimate writing are designed to feel almost psychologically invasive at times, less like passive listening and more like slipping into an emotional trance.",
            "That tension between comfort and discomfort appears repeatedly throughout the EP. Across multiple tracks, Saphira blurs the line between healing and seduction, emotional dependency and empowerment, softness and psychological control.",
            "“I wasnt trying to hypnotize one person,” she says. “I wanted the music to feel collective. Like everyone listening was entering the same atmosphere together.”",
            "Unlike traditional concept albums built around linear storytelling, Collective Hypnosis feels more fragmented and emotionally instinctive. Memories, desires, fears, and inner monologues drift in and out of focus like scenes from a half-remembered dream.",
            "Saphira wrote every song on the EP herself, something she considers essential to maintaining emotional authenticity in her work.",
            "“Every word came from somewhere real,” she says. “I think people can feel when music is emotionally lived-in versus emotionally performed.”",
            "If the project succeeds in what it sets out to do, Collective Hypnosis may become less of an EP and more of an experience — one designed to leave listeners feeling slightly unsettled, emotionally exposed, and strangely understood at the same time."
        ]
    },
    {
        "title": "“No One Else Could Tell My Story”: Saphira on Writing Her Own Lyrics",
        "description": "The dark-pop artist opens up about authorship, identity, and why every word in her music comes directly from lived experience.",
        "content": [
            "The dark-pop artist opens up about authorship, identity, and why every word in her music comes directly from lived experience.",
            "People sometimes ask Saphira whether she has ever considered working with outside songwriters ,co-writers, industry veterans, people who could potentially “refine” her ideas into something more commercially polished.",
            "She understands the question. Collaboration has shaped some of the most iconic songs in music history, and she speaks about that process with genuine respect.",
            "But for her, songwriting has never been just a technical craft. It has always been something closer to emotional documentation.",
            "Long before music, there was writing, journals, fragmented thoughts, observations she didn’t yet know how to translate into meaning. Writing was how she processed the world. How she made sense of things she couldn’t say out loud. How she stayed connected to herself when everything else felt unclear.",
            "When music entered her life, that instinct didn’t disappear. It simply evolved.",
            "And the idea of handing that process over to someone else, even partially doesn’t feel like collaboration to her. It feels like distortion.",
            "Not because of ego. But because of precision.",
            "The emotions she writes about are deeply specific: the disorientation of belonging to more than one culture at once, the invisible pressure of being perceived before being understood, the strange duality of love as both comfort and confinement. These are not abstract themes for her. They are lived experiences that exist in layered emotional detail.",
            "“No one else could describe it better than me,” she says. “Not because others could not do it, but because they weren’t there.”",
            "For Saphira, authorship is not about control. It is about fidelity to experience. Every lyric becomes a record of something felt in real time, translated without interference.",
            "And in a music landscape often shaped by collaboration rooms and external writers, that singular voice becomes part of what defines her artistry: unfiltered, intimate, and deliberately unshared."
        ]
    },
    {
        "title": "Behind the Music: How Saphira’s Mixed Identity Shapes Her Sound and Storytelling",
        "description": "The dark-pop artist reflects on growing up between Türkiye and Germany, and how her mixed cultural background became the emotional foundation of her music.",
        "content": [
            "The dark-pop artist reflects on growing up between Türkiye and Germany, and how her mixed cultural background became the emotional foundation of her music.",
            "Music has always been one of the few places where identity doesn’t need to be simplified. For Saphira, that idea is not theoretical, it comes from lived experience.",
            "Raised within a multicultural family spanning Türkiye and Germany, she grew up surrounded by different languages, traditions, and emotional codes that often coexisted in the same space without ever fully merging into one.",
            "“I exist between things,” she says.",
            "Between Turkish emotional intensity and German structure. Between different expectations of womanhood, expression, and ambition. Between ways of communicating that don’t always translate directly, but still shape how she feels and creates.",
            "Her family background meant that identity was never singular. It was layered from the beginning shaped by contrasting cultures that each carried their own emotional logic.",
            "In one environment, expression was expansive and deeply emotional. In another, clarity, discipline, and restraint were emphasized. Growing up between these worlds meant constantly learning how to move through different emotional languages.",
            "At first, that meant adaptation , adjusting how she spoke, how she expressed emotion, how much of herself she revealed depending on where she was.",
            "But over time, something shifted.",
            "What once felt like adjustment became awareness. And that awareness became creative language.",
            "Instead of choosing between cultural identities, Saphira began working within both. That duality now shapes her music in a very specific way: emotional intensity paired with controlled delivery, vulnerability balanced with structure.",
            "“It stopped feeling like I had to pick a side,” she explains. “It started feeling like I had access to more than one way of expressing the same emotion.”",
            "That sense of multiplicity is central to her songwriting. Her music often feels emotionally layered — never fully one tone, never fully resolved. Intimate, but slightly distant. Direct, but cinematic. Personal, but universally readable.",
            "Rather than presenting her background as contrast or conflict, Saphira treats it as texture something that naturally exists inside her work without needing explanation or justification.",
            "For her, being shaped by more than one culture doesn’t make her “in-between” in a fragmented sense. It creates range, emotional, linguistic, and creative.",
            "And that range continues to define the way she writes, sings, and builds her sonic world: structured, emotional, and quietly unplaceable in any single category."
        ]
    },
    {
        "title": "The Aesthetic Universe of Saphira",
        "description": "Sahsenem Saphira may be preparing to open the doors to her upcoming era, Collective Hypnosis, but one thing is already clear: she isn’t just releasing music, she’s building an entire world.",
        "content": [
            "Sahsenem Saphira may be preparing to open the doors to her upcoming era, Collective Hypnosis, but one thing is already clear: she isn’t just releasing music, she’s building an entire world.",
            "And while fans are likely to focus on the sound first, Saphira is making it very clear that the visuals are not secondary, not decorative, and definitely not an afterthought. In fact, they’re inseparable from the music itself.",
            "“Sound is only one layer of what I’m building,” she says.",
            "From the beginning, Saphira has envisioned her artistry as something that exists inside a fully formed universe ,one that is visual, emotional, and conceptual all at once. Dark, but never cold. Sensual, but never predictable. Rooted in something that feels almost ancient, yet always reaching toward something undefined.",
            "When she describes the visual language of her world, she speaks in contrasts: light sources in dark rooms, gold against shadow, ornate textures placed beside restraint. Nothing exists in isolation, everything is tension, balance, and atmosphere.",
            "“I’m involved in every visual decision,” she says. “The art direction, the styling, the imagery. Not because I need control, but because the visual and the sonic have to breathe together. They’re the same story told in different languages.”",
            "That philosophy becomes especially clear in her upcoming project, Collective Hypnosis. The EP is designed not just to be heard, but experienced, as something immersive, atmospheric, and slightly disorienting in its emotional intimacy.",
            "When listeners enter her world, Saphira says, they aren’t just stepping into a collection of songs. They’re stepping into a constructed environment with its own emotional logic, its own aesthetic rules, and its own internal gravity.",
            "“I’ve been building it for a long time,” she says. “It’s almost time to open the door.”"
        ]
    },
    {
        "title": "Why Saphira’s “Listen To Me” Feels Like a Breaking Point",
        "description": "There’s a specific emotional tension running through Saphira’s latest single, “Listen To Me” the kind that doesn’t sound manufactured for virality, but pulled directly from internal pressure.",
        "content": [
            "There’s a specific emotional tension running through Saphira’s latest single, “Listen To Me” the kind that doesn’t sound manufactured for virality, but pulled directly from internal pressure.",
            "Built on atmospheric production and emotionally restrained vocals, the track explores isolation, emotional exhaustion, and the feeling of speaking without truly being heard. Rather than leaning into polished pop catharsis, Saphira allows the discomfort to remain unresolved — which is exactly what gives the song its weight.",
            "“I didn’t want it to sound perfect,” she explains. “I wanted it to feel like someone trying to hold themselves together while saying something they’ve kept buried for too long.”",
            "That tension exists throughout the entire record. The production simmers instead of exploding, creating the sense that something is constantly building underneath the surface. The result is intimate without becoming overly confessional, a balance many artists struggle to maintain early in their careers.",
            "For Saphira, songwriting has always been personal. Every lyric she releases is self-written, something she sees less as a creative choice and more as necessity.",
            "“No one else fully understands the emotional contradictions I grew up with,” she says. “Music became the place where I could finally translate them.”",
            "There’s also a cinematic quality to the track that aligns with the dark, nocturnal aesthetic Saphira has slowly been building around her music and visual identity, mysterious, emotionally charged, and intentionally distant from conventional pop presentation.",
            "“Listen To Me” doesn’t ask for sympathy. It asks for attention.",
            "And that distinction matters."
        ]
    },
    {
        "title": "Saphira Says Vulnerability Became Impossible to Ignore",
        "description": "The “Collective Hypnosis” artist opens up about emotional exposure, delayed releases and the fear of staying silent for too long.",
        "content": [
            "The “Collective Hypnosis” artist opens up about emotional exposure, delayed releases and the fear of staying silent for too long.",
            "Saphira says she spent years postponing the music she was always meant to release.",
            "Not because the songs weren’t finished but because they felt too personal.",
            "“There’s a certain level of vulnerability that changes you once it’s public,” Saphira says. “People hear the song, but you remember exactly what it cost to write it.”",
            "The dark-pop artist, currently developing her upcoming project Collective Hypnosis, describes the music as emotionally exposed, intimate and intentionally unfiltered.",
            "According to Saphira, many of the records were written during periods of isolation, emotional overstimulation and internal conflict, themes that continue shaping the sonic and visual identity of the project.",
            "But despite delaying multiple releases over the years, the artist says fear eventually stopped being a reason to stay silent.",
            "“I realized I was more afraid of becoming older and never sharing it,” she explains. “That regret felt heavier than vulnerability.”",
            "That realization reportedly became a turning point in how Saphira approached both songwriting and artistic identity.",
            "Instead of trying to appear emotionally untouchable, the singer says she became more interested in documenting uncomfortable truths in real time.",
            "“I don’t want my music to sound emotionally safe,” Saphira says. “I want it to feel real enough that people recognize themselves inside it.”",
            "The artist has gradually built a world around hypnotic visuals, psychological themes and emotionally charged lyricism, elements expected to define the Collective Hypnosis era moving forward.",
            "And according to Saphira, the goal was never perfection.",
            "“It was honesty,” she says. “Even when honesty leaves a mark.”"
        ]
    },
    {
        "title": "Saphira Says the Best Songs Feel “Dangerously True”",
        "description": "The “Collective Hypnosis” artist opens up about deleting perfect versions, surrendering control and following emotion instead of ego.",
        "content": [
            "The “Collective Hypnosis” artist opens up about deleting perfect versions, surrendering control and following emotion instead of ego.",
            "Saphira says songwriting rarely begins with certainty.",
            "According to the dark-pop artist, the strongest records often reveal themselves slowly pulling her away from polished ideas and toward something far more emotionally exposed.",
            "“I think the song already knows what it wants before I do,” Saphira says. “My job is just to stop fighting it.”",
            "The singer-songwriter, currently developing her upcoming project Collective Hypnosis, describes her creative process as less about control and more about emotional surrender.",
            "While working on several tracks for the project, Saphira says she initially tried building songs around carefully planned concepts and “safe” emotional narratives.",
            "But despite sounding technically complete, something felt missing.",
            "“The first versions were perfect in all the wrong ways,” she explains. “They sounded polished, but emotionally empty.”",
            "According to the artist, many of those early drafts were eventually deleted entirely.",
            "“I realized I was writing toward what looked good instead of what felt true,” Saphira says. “And people can hear the difference immediately.”",
            "That realization reportedly reshaped the direction of Collective Hypnosis, a project centered around obsession, emotional conflict, vulnerability and psychological tension.",
            "Rather than forcing songs into predetermined structures, Saphira says she now follows emotional instinct first, even when it leads somewhere uncomfortable.",
            "“The resistance usually tells me exactly where the real song is hiding,” she says.",
            "The artist also credits her personal background for shaping the emotional intensity behind her writing process.",
            "Growing up between multiple cultures, languages and expectations, Saphira says she learned early on to filter herself carefully, something music eventually challenged her to unlearn.",
            "“I spent years trying to soften what I really felt,” she explains. “Music became the one place where I stopped editing myself.”",
            "That emotional honesty has gradually become one of the defining elements behind Saphira’s artistic identity, alongside hypnotic visuals, dark femininity and cinematic production.",
            "And according to the singer, vulnerability is no longer something she wants to avoid.",
            "“The older I get,” Saphira says, “the more I fear silence more than exposure.”"
        ]
    }
]

target_dirs = ['atwoodmagazine', 'clashmusic', 'earmilk', 'famemagazine', 'flaunt', 'musicrow', 'notiononline', 'eighth_template']

html_files = []
for ext in ('*.html', '*.htm'):
    html_files.extend(glob.glob(f'./**/{ext}', recursive=True))

html_files = sorted([f for f in html_files if any(d in f for d in target_dirs)])
html_files = sorted(list(set(html_files)))

def find_main_content(soup, file_path):
    if 'atwoodmagazine' in file_path:
        return soup.find('div', class_='entry-content') or soup.find('div', class_='site-content') or soup.find('article')
    elif 'clashmusic' in file_path:
        return soup.find('div', class_='pane-node-content') or soup.find('article')
    elif 'earmilk' in file_path:
        return soup.find('div', class_='entry-content') or soup.find('article')
    elif 'famemagazine' in file_path:
        div = soup.find('div', class_='entry-content')
        if div: return div
    elif 'flaunt' in file_path:
        return soup.find('div', class_='content-block-1') or soup.find('div', class_='rich-text-block-1')
    elif 'musicrow' in file_path:
        return soup.find('div', class_='entry-content')
    elif 'notiononline' in file_path or 'eighth_template' in file_path:
        div = soup.find('div', class_='elementor-widget-theme-post-content')
        if not div: div = soup.find('div', class_='show-hide-content-wrapper')
        if div: return div
    return soup.find('article')

for i in range(8):
    file_path = html_files[i]
    blog = blog_texts[i]

    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # 5. SADECE SEO (lang, title, meta desc)
    html_tag = soup.find('html')
    if html_tag:
        html_tag['lang'] = 'en'

    if soup.title:
        soup.title.string = blog['title']

    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        meta_desc['content'] = blog['description']
    else:
        new_meta = soup.new_tag('meta', attrs={'name': 'description', 'content': blog['description']})
        if soup.head:
            soup.head.append(new_meta)

    # Open Graph & Twitter
    og_title = soup.find('meta', property='og:title')
    if og_title: og_title['content'] = blog['title']
    og_desc = soup.find('meta', property='og:description')
    if og_desc: og_desc['content'] = blog['description']

    twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
    if twitter_title: twitter_title['content'] = blog['title']
    twitter_desc = soup.find('meta', attrs={'name': 'twitter:description'})
    if twitter_desc: twitter_desc['content'] = blog['description']

    main_content = find_main_content(soup, file_path)

    # 1. SADECE METİN DEĞİŞECEK. (Only text will change)
    if main_content:
        def is_meta_node(node):
            parent = node.parent
            while parent and parent != main_content:
                classes = parent.get('class', [])
                if not isinstance(classes, list):
                    classes = [classes]
                if any(c and ('author' in c.lower() or 'date' in c.lower() or 'time' in c.lower() or 'meta' in c.lower() or 'tags' in c.lower() or 'category' in c.lower() or 'share' in c.lower() or 'post-meta' in c.lower()) for c in classes):
                    return True
                parent = parent.parent
            return False

        valid_tags = []
        for tag in main_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote']):
            if not is_meta_node(tag):
                valid_tags.append(tag)

        content_idx = 0
        for tag in valid_tags:
            # Check safely to prevent AttributeError if parent is None
            if tag.parent and tag.parent.name in ['a', 'script', 'style', 'img', 'iframe', 'button', 'time', 'span']:
                continue

            if not tag.find(['a', 'img', 'iframe', 'video', 'embed']):
                if content_idx < len(blog['content']):
                    tag.string = blog['content'][content_idx]
                    content_idx += 1
                else:
                    tag.string = " "

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Processed: {file_path}")

print("Done parsing HTML files.")
