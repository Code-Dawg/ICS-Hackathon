# -*- coding: utf-8 -*-
"""
==============================================================================
FOOTPRINT QUEST - 110+ SCENARIOS QUESTION BANK
Groups detailed scenarios with choices, effects, correct answers, and feedback.
==============================================================================
"""

SCENARIOS = {
    # Chapter 1 / Level 1 — Create Account
    1: [
        {
            "id": "L1_Q1",
            "story": "You are creating your Footprint Quest account. Which password choice best protects your new account?",
            "choices": [
                "Use your name and birth year so it is easy to remember.",
                "Reuse the password from your social media account.",
                "Create a unique, long passphrase and enable two-factor authentication when available."
            ],
            "correct_idx": 2,
            "effects": {"xp": 10, "coins": 5, "privacy": 5, "security": 15, "trust": 5},
            "feedback": "A unique passphrase prevents one leaked password from unlocking several accounts. Two-factor authentication adds another layer of protection."
        }
    ],

    # Level 2 — First Steps Online
    2: [
        {
            "id": "L2_Q1",
            "story": "You want to research a school project about space exploration. A pop-up asks you to 'Allow Notifications' to view the content.",
            "choices": [
                "Allow notifications to read the content immediately.",
                "Deny notifications and look for the information elsewhere.",
                "Minimize the window and leave it open in the background."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "security": 5, "trust": -2},
            "feedback": "Allowing notifications lets untrusted websites send spam and fake alerts to your device, compromising security."
        },
        {
            "id": "L2_Q2",
            "story": "You find a free game download on an unfamiliar forum. The uploader says it is safe, but your browser blocks the download.",
            "choices": [
                "Bypass the browser warning and download it anyway.",
                "Look for the game on an official, trusted distribution platform.",
                "Disable your antivirus temporarily to let the download finish."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 15, "trust": 5, "reputation": 2},
            "feedback": "Browser security warnings protect you from malware. Disabling protection is a high risk."
        },
        {
            "id": "L2_Q3",
            "story": "A website offers to shorten your URLs, but it asks for your email address to log in first.",
            "choices": [
                "Use your primary personal email address.",
                "Use a temporary mask email address or find a service that does not require sign-up.",
                "Register using your school email account."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "security": 5},
            "feedback": "Masking your email prevents spam databases from correlating your web searches to your identity."
        },
        {
            "id": "L2_Q4",
            "story": "While reading a blog, you see a banner stating 'Your PC is infected! Click here to scan and remove virus.'",
            "choices": [
                "Click the banner to run the scan immediately.",
                "Close the browser tab and run your local, installed antivirus scanner.",
                "Ignore the banner but keep reading the website."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 15, "privacy": 5},
            "feedback": "Scareware popups try to trick users into downloading malicious software by simulating virus warnings."
        },
        {
            "id": "L2_Q5",
            "story": "A site terms of service pop-up appears. It is 50 pages long. What do you do?",
            "choices": [
                "Click 'Accept' without looking at any text.",
                "Use a browser tool to summarize key sections (like data selling and tracking) before accepting.",
                "Decline and never use any website that has a terms of service agreement."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "trust": 5},
            "feedback": "Summarizing terms helps you catch bad clauses like 'we share your browsing behavior with third parties.'"
        },
        {
            "id": "L2_Q6",
            "story": "You want to bookmark a site. The bookmark manager asks to sync your search history with an advertising partner.",
            "choices": [
                "Agree to sync to make bookmarks access easier.",
                "Decline the sync and save bookmarks locally.",
                "Change bookmarker to an open-source, private alternative."
            ],
            "correct_idx": 2,
            "effects": {"xp": 15, "coins": 8, "privacy": 15, "trust": 10},
            "feedback": "Choosing private utilities keeps your browsing habits out of marketing databases."
        },
        {
            "id": "L2_Q7",
            "story": "You see a cool image on a blog and want to share it. How should you attribute it?",
            "choices": [
                "Save and post it as your own work.",
                "Find the source, check the license (e.g. Creative Commons), and attribute properly.",
                "Use it without attribution because it is on the public web."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 15, "trust": 10},
            "feedback": "Respecting digital copyright and licensing builds your reputation as a responsible digital citizen."
        },
        {
            "id": "L2_Q8",
            "story": "A research site asks for your physical address to mail a free informational poster.",
            "choices": [
                "Provide your home address without checking the privacy policy.",
                "Download a digital copy of the poster instead, avoiding sharing your physical address.",
                "Enter a random, fake address to see if they still ship it."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "security": 8},
            "feedback": "Digital alternatives protect your physical coordinates from data harvesting databases."
        },
        {
            "id": "L2_Q9",
            "story": "You notice your web browser is starting up with a strange homepage you did not set.",
            "choices": [
                "Ignore it as long as searches still work.",
                "Check browser settings for extensions you did not install, remove them, and reset homepage.",
                "Reinstall your entire operating system immediately."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 12, "privacy": 8},
            "feedback": "Unwanted extensions can hijack searches, inject advertisements, and spy on inputs."
        },
        {
            "id": "L2_Q10",
            "story": "You are logging into a learning portal at a public library computer.",
            "choices": [
                "Save your password in the browser so it is easier for next time.",
                "Use incognito mode, uncheck 'Remember Me', and log out fully when done.",
                "Leave the browser tab open when you walk away."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 15, "privacy": 10},
            "feedback": "Public computers cache credentials. Failing to sign out allows the next user to compromise your account."
        }
    ],

    # Level 3 — Your First Social Media Account
    3: [
        {
            "id": "L3_Q1",
            "story": "You are creating a profile on a new social network. It asks for your full name, birthdate, and school.",
            "choices": [
                "Provide all details accurately so friends can locate you.",
                "Use a nickname and omit sensitive fields like birthdate and school name.",
                "Enter fake credentials of a popular celebrity."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "reputation": 5},
            "feedback": "Limiting profile fields protects you from identity theft and social engineering profiling."
        },
        {
            "id": "L3_Q2",
            "story": "Your profile picture default setting is public. What adjustments should you make?",
            "choices": [
                "Leave it public so anyone can follow you.",
                "Change it to 'Friends Only' and use an illustrated avatar instead of a close-up photo.",
                "Delete the account completely."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 15, "reputation": 8},
            "feedback": "Avatar images prevent facial recognition databases from harvesting your physical appearance."
        },
        {
            "id": "L3_Q3",
            "story": "A school acquaintance you barely know sends a friend request on your private account.",
            "choices": [
                "Accept them immediately to increase your follower count.",
                "Decline or ignore the request, keeping your network to trusted friends.",
                "Accept and share your phone number in a direct message."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "trust": 8},
            "feedback": "Limiting friends lists keeps your personal posts within a trusted circle, minimizing leaks."
        },
        {
            "id": "L3_Q4",
            "story": "You want to comment on a public post. You disagree strongly with the creator. How do you respond?",
            "choices": [
                "Post a harsh comment calling them names.",
                "State your perspective calmly using facts, or scroll past without replying.",
                "Report their post immediately using multiple fake reports."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 15, "trust": 10},
            "feedback": "Public comments build your permanent digital reputation. Keeping discussions civil prevents future backlashes."
        },
        {
            "id": "L3_Q5",
            "story": "An app asks to connect to your social media account to 'personalize your experience.'",
            "choices": [
                "Grant connection without checking what data it accesses.",
                "Refuse the connection and create a separate login using a masked email.",
                "Click allow but delete the app after five minutes."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 14, "security": 8},
            "feedback": "Third-party authorization connections often leak lists of friends and personal histories."
        },
        {
            "id": "L3_Q6",
            "story": "You want to upload a funny video of your sibling. They do not know you recorded it.",
            "choices": [
                "Post it anyway, it will get a lot of likes.",
                "Ask for their consent first before sharing any media containing them.",
                "Send it to a public group chat."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 12, "trust": 15},
            "feedback": "Respecting other people's digital privacy is a key aspect of healthy digital citizenship."
        },
        {
            "id": "L3_Q7",
            "story": "A new platform trend asks you to share '10 Fun Facts About Yourself' to unlock a profile badge.",
            "choices": [
                "Participate and list your hometown, first pet, and mother's maiden name.",
                "Decline to participate, as these facts are common security verification questions.",
                "Make up completely fake facts that are funny."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 15, "privacy": 10},
            "feedback": "Social media viral trends are frequently engineered to collect answers to common password reset questions."
        },
        {
            "id": "L3_Q8",
            "story": "You receive a message from a popular brand offering a sponsorship if you post their link.",
            "choices": [
                "Post the link immediately to lock in the deal.",
                "Verify the account status (check mark, official website) and avoid sharing unverified URLs.",
                "Ignore it and block the account."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 10, "reputation": 5},
            "feedback": "Spam accounts offer fake sponsorships to distribute phishing URLs through compromised user accounts."
        },
        {
            "id": "L3_Q9",
            "story": "You decide to delete an old social account you no longer use. What is the best method?",
            "choices": [
                "Just delete the app from your phone.",
                "Log into the account, request full account deletion/data removal, then delete the app.",
                "Leave it active in case you want to check it next year."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 15, "security": 10},
            "feedback": "Leaving unused accounts active increases your attack surface if a data breach leaks old passwords."
        },
        {
            "id": "L3_Q10",
            "story": "A social app changes its privacy policy, sending you a notification to review it.",
            "choices": [
                "Dismiss the notification.",
                "Check the summary of changes, specifically looking for additions to tracking or data broker sharing.",
                "Delete your device settings."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "trust": 5},
            "feedback": "Monitoring policy updates ensures you know when platforms start sharing user data with corporate partners."
        }
    ],

    # Level 4 — Active vs Passive Digital Footprints
    4: [
        {
            "id": "L4_Q1",
            "story": "You open a news site and notice ads for shoes you searched for on another site ten minutes ago.",
            "choices": [
                "Assume it is a coincidence.",
                "Install a tracker blocker and clear your browser cookies.",
                "Report the website to the police."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 15, "trust": 8},
            "feedback": "Cross-site tracking cookies collect a passive footprint of your browsing path to deliver targeted ads."
        },
        {
            "id": "L4_Q2",
            "story": "An online game asks to collect telemetry reports to 'improve server performance.'",
            "choices": [
                "Allow it without review.",
                "Decline permission, or read the telemetry policy to ensure it excludes personal device identifiers.",
                "Disable your internet connection."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "security": 5},
            "feedback": "Telemetry logs can build a passive trail of your device specifications, location details, and active hours."
        },
        {
            "id": "L4_Q3",
            "story": "You post a tweet expressing your opinion on a movie. What kind of footprint is this?",
            "choices": [
                "An active digital footprint.",
                "A passive digital footprint.",
                "No footprint at all."
            ],
            "correct_idx": 0,
            "effects": {"xp": 10, "coins": 5, "reputation": 5},
            "feedback": "Any deliberate action you take to publish content online builds your active digital footprint."
        },
        {
            "id": "L4_Q4",
            "story": "You visit an online shop. The shop logs your IP address, browser canvas fingerprint, and screen resolution.",
            "choices": [
                "These details cannot identify you.",
                "This forms a passive footprint that can identify your device uniquely, even without cookies.",
                "This is illegal and cannot happen."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "security": 5},
            "feedback": "Device fingerprinting compiles screen settings, fonts, and device specs to trace you silently."
        },
        {
            "id": "L4_Q5",
            "story": "You use search engines that log your queries to build an interest profile of you.",
            "choices": [
                "Switch to a privacy-centric search engine that does not track queries.",
                "Ignore it; customized searches are helpful.",
                "Delete your search history from your computer every five minutes."
            ],
            "correct_idx": 0,
            "effects": {"xp": 12, "coins": 6, "privacy": 15, "trust": 10},
            "feedback": "Privacy search engines route requests without logging query terms or IP identifiers."
        },
        {
            "id": "L4_Q6",
            "story": "A mobile navigation app asks for 'Always Allow' location tracking.",
            "choices": [
                "Grant 'Always Allow' to ensure accurate maps.",
                "Change to 'Only While Using App' to limit background location traces.",
                "Deny location tracking completely."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 15, "security": 10},
            "feedback": "Background location coordinates build a detailed passive footprint of your physical routines."
        },
        {
            "id": "L4_Q7",
            "story": "You write a public review for a local business on a map platform.",
            "choices": [
                "Use your full name and list the exact dates and times you visit.",
                "Write the review under a pseudonym, focusing on the service, without exposing routine times.",
                "Upload photos containing your friends' faces."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "reputation": 10},
            "feedback": "Public reviews build active footprints. Pseudonyms protect your schedule and identity."
        },
        {
            "id": "L4_Q8",
            "story": "You notice your phone connects to public Wi-Fi access points automatically as you walk down the street.",
            "choices": [
                "Keep it enabled to save mobile data charges.",
                "Turn off 'Auto-Join' and Wi-Fi scanning in public areas to prevent tracing.",
                "Change your phone's screen lock."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 15, "privacy": 12},
            "feedback": "Automatic connection signals broadcast your unique MAC address, allowing local physical tracking."
        },
        {
            "id": "L4_Q9",
            "story": "A fitness tracker band asks to upload your heart rate logs to the cloud.",
            "choices": [
                "Allow it without review.",
                "Check their data sharing agreements and limit tracking sharing settings where possible.",
                "Throw away the tracker."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "trust": 5},
            "feedback": "Biometric data uploaded to the cloud is permanent metadata that is highly valued by health advertisers."
        },
        {
            "id": "L4_Q10",
            "story": "What is the primary difference between active and passive footprints?",
            "choices": [
                "Active footprints are stored on your device; passive footprints are on servers.",
                "Active is intentional data sharing; passive is background tracking without active consent.",
                "Active footprints expire; passive footprints are permanent."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 10, "trust": 10},
            "feedback": "Active footprints require your click-to-publish action, while passive footprints compile silently."
        }
    ],

    # Level 5 — Sharing Photos
    5: [
        {
            "id": "L5_Q1",
            "story": "You want to post a group photo from a birthday party. A friend in the photo is uncomfortable with their image online.",
            "choices": [
                "Post it anyway, they look fine.",
                "Crop them out, blur their face, or don't post the photo.",
                "Tag them in the photo to show they attended."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 15, "trust": 15},
            "feedback": "Always respect others' consent. Posting photos of friends against their wishes compromises trust."
        },
        {
            "id": "L5_Q2",
            "story": "You want to share a picture of your cool new gaming desk, which has your school ID sitting on it.",
            "choices": [
                "Post the photo directly.",
                "Crop the ID out of the picture or blur the name and barcode before posting.",
                "Post it, but tell people not to zoom in."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 15, "privacy": 12},
            "feedback": "High-resolution photos allow zoom-ins that can harvest barcode numbers, school names, and details."
        },
        {
            "id": "L5_Q3",
            "story": "Your phone camera attaches GPS coordinates (EXIF metadata) to your photos automatically.",
            "choices": [
                "Leave it enabled to remember where photos were taken.",
                "Disable location tags in camera settings and clear metadata before posting to public sites.",
                "Never share photos online again."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 15, "security": 10},
            "feedback": "EXIF metadata tags preserve precise GPS coordinates, revealing home and school locations."
        },
        {
            "id": "L5_Q4",
            "story": "A friend posts a funny photo of you sleeping and tags your account. What do you do?",
            "choices": [
                "Comment with an angry reply.",
                "Untag yourself, check profile tag-approval settings, and ask them to take the photo down.",
                "Ignore it completely."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 12, "trust": 10},
            "feedback": "Managing your tagged photos protects your public digital reputation from unflattering records."
        },
        {
            "id": "L5_Q5",
            "story": "You want to post a picture of your house keys to show you finally got your own set.",
            "choices": [
                "Post the key picture.",
                "Avoid posting pictures of keys, as bad actors can duplicate physical keys from photographs.",
                "Post it but make sure the background is dark."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 18, "privacy": 10},
            "feedback": "Physical security can be bypassed by duplicating keys using high-resolution images."
        },
        {
            "id": "L5_Q6",
            "story": "You want to share a picture of a concert ticket barcode to show you are going tonight.",
            "choices": [
                "Post the barcode clearly.",
                "Blur or cover the barcode and order number completely before posting.",
                "Send it to a public chat group."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 15, "trust": 5},
            "feedback": "Exposed ticket barcodes can be copied and scanned, locking you out of the concert."
        },
        {
            "id": "L5_Q7",
            "story": "A photo platform asks for access to your entire contact list to 'find your friends.'",
            "choices": [
                "Allow full contact access.",
                "Deny access, or search for friends manually to prevent sharing their private contact details.",
                "Type fake phone numbers."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 14, "trust": 10},
            "feedback": "Sharing contact lists compromises the privacy of friends who did not sign up for the platform."
        },
        {
            "id": "L5_Q8",
            "story": "You want to upload photos to a cloud backup. The default setting is set to public share link active.",
            "choices": [
                "Leave it public to share links easily.",
                "Verify sharing parameters and set directory folder status to private restricted access.",
                "Delete your cloud backup software."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 15, "security": 10},
            "feedback": "Public cloud folders are indexed by custom search engines, exposing private photos to the web."
        },
        {
            "id": "L5_Q9",
            "story": "You want to post a picture of a package you received. The shipping label is visible.",
            "choices": [
                "Post the picture directly.",
                "Cover or blur the shipping label containing your full name, barcode, and home address.",
                "Post it but write a comment telling people to ignore the label."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "security": 8},
            "feedback": "Label metadata includes barcodes and address lines that expose your physical home location."
        },
        {
            "id": "L5_Q10",
            "story": "You want to post photos of a school field trip. Some children are visible in the background.",
            "choices": [
                "Post the photos anyway, they are just background details.",
                "Select photos where background faces are blurred, out of focus, or not visible.",
                "Post it but do not tag the location."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 10, "privacy": 12},
            "feedback": "Protecting minor children from public identification is a key ethical standard of photo sharing."
        }
    ],

    # Level 8 — Online Shopping
    8: [
        {
            "id": "L8_Q1",
            "story": "You are shopping online and see an ad for designer hoodies at 90% off on a website you have never heard of.",
            "choices": [
                "Buy it immediately before the deal ends.",
                "Check for trust indicators (reviews, official contacts, HTTPS) or search if the site is a known scam.",
                "Enter your login credentials to get a bigger discount."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 15, "trust": 10},
            "feedback": "Fake online stores advertise unrealistic discounts to steal credit card details and emails."
        },
        {
            "id": "L8_Q2",
            "story": "An online checkout form asks if you want to 'Save card details for future purchases.'",
            "choices": [
                "Save details to checkout faster next time.",
                "Decline to save, or use a temporary virtual credit card number to shield your account.",
                "Save details but write down your CVV on a post-it note."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 15, "privacy": 10},
            "feedback": "Stored credit card details increase risk if the shop's server database is compromised in a breach."
        },
        {
            "id": "L8_Q3",
            "story": "You receive a text message claiming your package cannot be delivered until you pay a $1.50 address correction fee.",
            "choices": [
                "Click the link and input your credit card details.",
                "Check the official tracking status page directly through the postal provider's verified website.",
                "Ignore the message but reply with your address."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 18, "trust": 12},
            "feedback": "Smishing (SMS Phishing) scams use minor delivery fees to steal full credit card credentials."
        },
        {
            "id": "L8_Q4",
            "story": "You want to buy a game from a seller on a social media forum who asks you to pay via 'Friends & Family' transfer.",
            "choices": [
                "Pay using Friends & Family to avoid transaction fees.",
                "Insist on Goods & Services payment which has buyer protection, or buy from a certified shop.",
                "Send cash in an envelope."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "trust": 10, "security": 12},
            "feedback": "Paying via Friends & Family removes all purchase protection, allowing scammers to take coins without delivering products."
        },
        {
            "id": "L8_Q5",
            "story": "A shopping app asks for permissions to access your calendar, contacts, and photos to run.",
            "choices": [
                "Allow permissions so the app works smoothly.",
                "Deny non-essential permissions, keeping access restricted to basic network details.",
                "Provide all permissions but write a bad review."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 14, "security": 8},
            "feedback": "Shopping apps frequently collect background contacts and calendars to sell to advertising brokers."
        },
        {
            "id": "L8_Q6",
            "story": "You want to buy a product but the website url shows 'http://' instead of 'https://'.",
            "choices": [
                "Buy it anyway; the store looks professional.",
                "Avoid submitting any payment information over unencrypted HTTP connections.",
                "Try refreshing the page multiple times."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 16, "trust": 8},
            "feedback": "Unencrypted HTTP connections allow middle-man attackers to intercept payment card details in transit."
        },
        {
            "id": "L8_Q7",
            "story": "You see a site review score of 5.0 with 1,000 identical reviews saying 'Excellent product buy now!'",
            "choices": [
                "Trust the reviews completely.",
                "Recognize this as a potential bot farm review wave and crosscheck third-party forums for reviews.",
                "Assume the product is sold out."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "trust": 12, "security": 5},
            "feedback": "Fake stores buy synthetic positive reviews to trick search filters and consumers."
        },
        {
            "id": "L8_Q8",
            "story": "You want to buy a gift. What is the safest network connection to use for shopping?",
            "choices": [
                "Public library Wi-Fi without VPN.",
                "Your secure home Wi-Fi or cellular connection.",
                "Free airport Wi-Fi hotspot."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 15, "privacy": 10},
            "feedback": "Unsecured public networks allow attackers to read unencrypted data packets transmitted by your device."
        },
        {
            "id": "L8_Q9",
            "story": "You want to purchase a membership. The site asks for your Social Security or National ID number to verify your age.",
            "choices": [
                "Provide the ID number to get access.",
                "Decline to provide core national identity details for basic commercial transactions.",
                "Provide a fake number that you made up."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 18, "security": 10},
            "feedback": "Commercial websites do not need national identifiers. Providing them increases identity theft risks."
        },
        {
            "id": "L8_Q10",
            "story": "After purchasing from an online shop, you receive a spam email welcoming you to 10 partner newsletters.",
            "choices": [
                "Ignore the emails.",
                "Unsubscribe from each, and check the shop settings to opt-out of marketing sharing.",
                "Create a new email address immediately."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "trust": 5},
            "feedback": "Pre-checked checkboxes on check-out pages often sign you up for spam partners by default."
        }
    ],

    # Level 14 — Online Gaming Safety
    14: [
        {
            "id": "L14_Q1",
            "story": "A player in an online lobby offers to give you free high-tier weapons if you click a link and log in to a trading site.",
            "choices": [
                "Click the link and log in with your account credentials.",
                "Ignore the offer and avoid entering credentials on unverified third-party websites.",
                "Give them your password directly in chat so they can log in and trade it for you."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 18, "privacy": 12},
            "feedback": "Fake trade links are phishing setups designed to steal steam/gaming credentials and inventory skins."
        },
        {
            "id": "L14_Q2",
            "story": "You are playing voice chat. A player asks you which school you go to and what town you live in.",
            "choices": [
                "Tell them the school name and town, it is just friendly banter.",
                "Keep conversation limited to game mechanics and avoid sharing real-world coordinates.",
                "Give them your friends' home address instead."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 15, "reputation": 5},
            "feedback": "Social engineering in online games targets physical locations to carry out doxxing or swatting."
        },
        {
            "id": "L14_Q3",
            "story": "You want to download a 'mod cheat' that promises infinite health in a multiplayer game.",
            "choices": [
                "Download and run the installer.",
                "Avoid downloads from unverified sources, as game cheats frequently carry hidden trojans and stealers.",
                "Run it on your parents' work computer."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 16, "reputation": 10},
            "feedback": "Game hacks and cheats are prime vectors for keyloggers and info-stealers targeting saved passwords."
        },
        {
            "id": "L14_Q4",
            "story": "Your game account password has been compromised. What is the best course of action?",
            "choices": [
                "Keep playing until they lock you out.",
                "Change password to a secure passphrase, enable Multi-Factor Authentication (MFA), and check recovery emails.",
                "Create a new account and abandon the old one."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 18, "privacy": 10},
            "feedback": "Enabling MFA stops attackers from accessing your inventory even if they know your active password."
        },
        {
            "id": "L14_Q5",
            "story": "A player is constantly typing toxic insults and threats in your direction during match play.",
            "choices": [
                "Trash talk them back with harsher insults.",
                "Mute them, block their account, and report their profile using the game's abuse reporting systems.",
                "Dox them using their username."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 15, "trust": 10},
            "feedback": "Muting and reporting toxic behavior protects your mental space and keeps your gaming record clean."
        },
        {
            "id": "L14_Q6",
            "story": "A game asks to link your profile to a public community leaderboard. What data is shared?",
            "choices": [
                "Only game stats.",
                "It can expose email lists, online status indicators, and gameplay times publicly.",
                "Nothing at all."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "trust": 5},
            "feedback": "Connecting accounts to community leaderboards exposes your online habits to scrapers and trackers."
        },
        {
            "id": "L14_Q7",
            "story": "You want to sell a virtual skin for real cash. A buyer asks you to send the skin first.",
            "choices": [
                "Trust them and trade the item first.",
                "Use an official, trusted marketplace middleman escrow system to prevent trade scams.",
                "Give them your login password to let them verify the skin."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 14, "trust": 10},
            "feedback": "Direct trading scams exploit trust to steal items without transferring money."
        },
        {
            "id": "L14_Q8",
            "story": "A gaming application launcher asks to run with 'Administrator Privileges' on every startup.",
            "choices": [
                "Click yes to ensure maximum game performance.",
                "Investigate why the launcher needs deep system rights, and only grant it if it is a verified official package.",
                "Format your hard drive."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "security": 15, "privacy": 8},
            "feedback": "Running applications as administrator allows hidden update payloads to compromise the entire OS."
        },
        {
            "id": "L14_Q9",
            "story": "A gaming server you play on requires you to download custom sound files to connect.",
            "choices": [
                "Download the files directly without scan.",
                "Only download if the server host is verified, and check files using an active scanner.",
                "Decline and play on official matchmaking servers."
            ],
            "correct_idx": 2,
            "effects": {"xp": 10, "coins": 5, "security": 16, "trust": 10},
            "feedback": "Custom community server files can contain embedded malicious scripts that trigger when executed."
        },
        {
            "id": "L14_Q10",
            "story": "You want to set a username for your gaming profile. What should you choose?",
            "choices": [
                "Your real name and birth year (e.g. Liam_Smith_2011).",
                "A creative alias that contains zero references to your real identity.",
                "Your school name and mascot."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 15, "security": 10},
            "feedback": "Real names in usernames let crawlers link your gameplay records to your public profiles."
        }
    ],

    # Level 15 — Digital Reputation
    15: [
        {
            "id": "L15_Q1",
            "story": "You posted an embarrassing comment on a video four years ago. You want to make sure it doesn't affect your future applications.",
            "choices": [
                "Ignore it; nobody checks old comments.",
                "Search your history, delete the comment, and set your older profiles to private.",
                "Create a new social account and change your name."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 18, "privacy": 10},
            "feedback": "Proactively auditing old comments cleans up your digital footprint before recruiters check it."
        },
        {
            "id": "L15_Q2",
            "story": "A university admissions officer is scanning candidates' public social media pages.",
            "choices": [
                "They are not allowed to do that.",
                "It is a common practice; keeping public profiles positive and professional is crucial.",
                "They only check official emails."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 15, "trust": 10},
            "feedback": "Many institutions verify candidates' digital reputation by review of public profiles and logs."
        },
        {
            "id": "L15_Q3",
            "story": "You want to build a positive digital reputation. What should you post?",
            "choices": [
                "Complaints about teachers or former classmates.",
                "A portfolio of your coding projects, art, volunteer work, or science awards.",
                "Every minor thought you have throughout the day."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "reputation": 20, "trust": 15},
            "feedback": "A positive footprint highlights achievements, showing leadership and professional capabilities."
        },
        {
            "id": "L15_Q4",
            "story": "You notice your name appears in a Google Search next to a post you did not write.",
            "choices": [
                "Submit a request to Google or the site host to remove the incorrect association details.",
                "Hope no one notices the search result.",
                "Sue the search engine immediately."
            ],
            "correct_idx": 0,
            "effects": {"xp": 12, "coins": 6, "reputation": 15, "privacy": 12},
            "feedback": "Under privacy rules, you can request search engines to delink incorrect, harmful, or outdated results."
        },
        {
            "id": "L15_Q5",
            "story": "You want to share a project link. How should you format your profile bios?",
            "choices": [
                "List your phone number and email publicly so they can contact you.",
                "Provide a clean overview, using secure forms or masked emails for public contact.",
                "Leave all description sections blank."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "reputation": 10},
            "feedback": "Secure contact forms filter out spam bots while preserving professional outreach paths."
        },
        {
            "id": "L15_Q6",
            "story": "What is the role of web archives (like archive.org) in digital reputation?",
            "choices": [
                "They delete pages automatically when you delete them from your server.",
                "They capture snapshots of pages that remain visible even if you delete the original site.",
                "They encrypt internet pages so no one can read them."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "security": 5},
            "feedback": "Archive engines preserve public web history, meaning deleted posts can still be retrieved."
        },
        {
            "id": "L15_Q7",
            "story": "Your classmate asks you to sign an online petition that has highly aggressive, hateful language.",
            "choices": [
                "Sign it, it's just supporting a friend.",
                "Refuse to sign, as your name on hateful public petitions damages your digital reputation.",
                "Sign it using your school account details."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 16, "trust": 12},
            "feedback": "Public alignments and petition signatures create permanent search records linked to your identity."
        },
        {
            "id": "L15_Q8",
            "story": "You want to comment on a video, stating constructive criticism. How should you write it?",
            "choices": [
                "Write 'This video is trash, delete your account.'",
                "State what was good, suggest improvement areas respectfully, and avoid toxic language.",
                "Report the video using multiple fake accounts."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 15, "trust": 10},
            "feedback": "Constructive feedback demonstrates communication skills and maturity in public records."
        },
        {
            "id": "L15_Q9",
            "story": "You are applying for a scholarship. The application form asks for your public handles.",
            "choices": [
                "Give them fake handles or delete your accounts before applying.",
                "Provide handles of clean, professionally curated profiles.",
                "Leave the handles blank and hope they do not search your name."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 12, "trust": 10},
            "feedback": "Curating professional accounts prepares you for audit reviews by application boards."
        },
        {
            "id": "L15_Q10",
            "story": "A friend offers to sell you automated follower bots to boost your profile reputation metrics.",
            "choices": [
                "Buy the bots to look more popular.",
                "Decline, as bot followers violate terms, risk account bans, and damage authentic reputation.",
                "Buy the bots but report the seller."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "reputation": 14, "trust": 8},
            "feedback": "Synthetic metrics are easily detected, reducing trust and violating platform safety guidelines."
        }
    ],

    # Level 16 — Cyberbullying
    16: [
        {
            "id": "L16_Q1",
            "story": "You witness a classmate being targeted with cruel, threatening comments in a group chat.",
            "choices": [
                "Join in the jokes so you don't become the next target.",
                "Save screenshots of the abuse, tell the victim they have your support, and report it to a trusted adult.",
                "Ignore the chat and mute notifications."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "reputation": 18, "trust": 20},
            "feedback": "Bullying escalates when bystanders remain silent. Documentation helps school authorities intervene."
        },
        {
            "id": "L16_Q2",
            "story": "An anonymous user sends you threatening direct messages. What is your first step?",
            "choices": [
                "Argue with them and send threats back.",
                "Capture screenshots, block the user account immediately, and report the behavior to the host platform.",
                "Delete your email account."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 15, "privacy": 12},
            "feedback": "Engaging feeds toxic behavior. Saving evidence and blocking is the safest protocol."
        },
        {
            "id": "L16_Q3",
            "story": "A group of kids creates a fake profile of a classmate, posting embarrassing, manipulated photos.",
            "choices": [
                "Follow the page and share it with classmates.",
                "Report the profile for impersonation and bullying to the platform, and support the classmate.",
                "Do nothing."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 15, "trust": 15},
            "feedback": "Impersonation and distribution of modified images violates platform rules and local safety regulations."
        },
        {
            "id": "L16_Q4",
            "story": "You want to help a friend who is feeling anxious because of harassment on a gaming server.",
            "choices": [
                "Tell them to stop crying and deal with it.",
                "Listen to them, help them turn on mute/privacy settings, and encourage them to report the abuse.",
                "Target the bullies in real life."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "trust": 18, "reputation": 12},
            "feedback": "Empathetic support and practical platform filters help victims manage digital stress."
        },
        {
            "id": "L16_Q5",
            "story": "What is the best way to handle comments that target your appearance in your feed?",
            "choices": [
                "Delete the comments, block the accounts, and use the filter settings to auto-hide toxic keywords.",
                "Reply with details explaining why they are wrong.",
                "Make your account public to ask others for help."
            ],
            "correct_idx": 0,
            "effects": {"xp": 10, "coins": 5, "privacy": 15, "reputation": 10},
            "feedback": "Keyword filters automatically intercept toxic comments, preserving a clean workspace."
        },
        {
            "id": "L16_Q6",
            "story": "You realize a joke comment you posted was taken as offensive by a classmate. They are upset.",
            "choices": [
                "Tell them they are too sensitive.",
                "Apologize directly, clarify your intent, and delete the post immediately.",
                "Leave it online and stop talking to them."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 15, "trust": 15},
            "feedback": "Owning mistakes and clearing misunderstandings preserves peer relationships and reputation."
        },
        {
            "id": "L16_Q7",
            "story": "A messaging app lets users submit anonymous feedback. The feed turns into a space for insult matches.",
            "choices": [
                "Participate in the matches.",
                "Decline to use anonymous rating platforms and delete the app to protect your peace.",
                "Report the app to search engines."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "reputation": 12},
            "feedback": "Anonymous feedback tools frequently foster toxic spaces due to lack of accountability structures."
        },
        {
            "id": "L16_Q8",
            "story": "You see an option to 'Expose' another student's secret in a local community channel.",
            "choices": [
                "Post it anonymously.",
                "Refuse to engage in gossip and report the channel for harassment.",
                "Share it in private chats only."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 16, "trust": 14},
            "feedback": "Spreading private secrets damages student communities and leaves active database traces."
        },
        {
            "id": "L16_Q9",
            "story": "A platform lacks moderating structures and abuse reporting options.",
            "choices": [
                "Continue using it; it's free speech.",
                "Limit your usage and find platforms that actively moderate harassment and threats.",
                "Spam the server with bots."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 12, "privacy": 10},
            "feedback": "Unmoderated spaces carry higher exposure to security hacks, malware, and cyberbullying."
        },
        {
            "id": "L16_Q10",
            "story": "How does digital harassment compare to physical bullying?",
            "choices": [
                "It is less harmful because it is just text.",
                "It can be more persistent, as it spreads globally and traces remain online permanently.",
                "It is exactly the same."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "reputation": 10, "trust": 10},
            "feedback": "Digital abuse reaches victims at any hour, and archived records prolong the distress."
        }
    ],

    # Level 17 — Data Brokers
    17: [
        {
            "id": "L17_Q1",
            "story": "You type your name into a people-search site and find your phone number, email, and family names listed publicly.",
            "choices": [
                "Hope no one finds it.",
                "Submit an official opt-out request form to the data broker site to delete your record.",
                "Change your phone number immediately."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 18, "security": 10},
            "feedback": "Data brokers gather details from public databases. You can submit opt-outs to remove them."
        },
        {
            "id": "L17_Q2",
            "story": "A sweepstakes site offers a free gaming laptop if you fill out a survey detailing your family's purchases.",
            "choices": [
                "Fill it out; it only takes 5 minutes.",
                "Decline to share personal details for prizes, as these forms sell your profiles to database brokers.",
                "Fill it out with fake details."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 15, "security": 10},
            "feedback": "High-value giveaways are catalog collection schemes designed to compile household profiles."
        },
        {
            "id": "L17_Q3",
            "story": "A store loyalty card gives you 5% off, but tracks all items you purchase to create a retail profile.",
            "choices": [
                "Use the card every time.",
                "Evaluate if the tracking trade-off is worth the discount, and opt-out of marketing sharing.",
                "Never buy groceries again."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "trust": 5},
            "feedback": "Loyalty programs monetize purchase records by selling compiled shopping profiles to data consolidators."
        },
        {
            "id": "L17_Q4",
            "story": "You get repeated marketing calls from companies you have never heard of.",
            "choices": [
                "Yell at the callers.",
                "Register your phone on national 'Do Not Call' lists and request brokers delete your number.",
                "Throw away your phone."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 15, "security": 8},
            "feedback": "Cold marketing calls indicate your contact details have been packaged and sold by data brokers."
        },
        {
            "id": "L17_Q5",
            "story": "You want to protect your digital footprint from being sold. What setting should you check on your mobile device?",
            "choices": [
                "Disable 'Personalized Ads' and reset your advertising identifier regularly.",
                "Turn off Wi-Fi completely.",
                "Keep Bluetooth disabled at home."
            ],
            "correct_idx": 0,
            "effects": {"xp": 12, "coins": 6, "privacy": 15, "security": 8},
            "feedback": "Mobile OS systems attach an ad ID to track user activity across applications."
        },
        {
            "id": "L17_Q6",
            "story": "A website registration form lists optional fields like income, education, and hobbies.",
            "choices": [
                "Fill them all out to get better recommendations.",
                "Leave all optional demographic profile fields blank to minimize footprint data points.",
                "Type fake information."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 14, "trust": 5},
            "feedback": "Optional registration details are compiled directly to build advertising personas."
        },
        {
            "id": "L17_Q7",
            "story": "You see a button on a dashboard that says 'Opt-Out of Interest-Based Advertising.'",
            "choices": [
                "Click it to request advertising trackers stop indexing your active profile.",
                "Ignore it as it will not work.",
                "Assume it makes ads disappear completely."
            ],
            "correct_idx": 0,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "trust": 10},
            "feedback": "Opting out signals marketing networks to replace custom profiling tracking with generic ads."
        },
        {
            "id": "L17_Q8",
            "story": "How do data brokers purchase your digital footprint records?",
            "choices": [
                "They steal files directly using software hacks.",
                "They acquire it legally from voter lists, public profiles, survey entries, and credit cards.",
                "They only buy it from search engines."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "trust": 8},
            "feedback": "Brokers compile footprints legally using aggregated public filings and marketing forms."
        },
        {
            "id": "L17_Q9",
            "story": "You receive a newsletter subscription verification email you did not sign up for.",
            "choices": [
                "Click the unsubscribe link directly without checking it.",
                "Mark it as spam, or verify the sender link address safety before clicking unsubscribe.",
                "Ignore the email completely."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 14, "privacy": 8},
            "feedback": "Fake unsubscribe links in unrecognized emails are phishing tricks to verify active email addresses."
        },
        {
            "id": "L17_Q10",
            "story": "Under GDPR/CCPA regulations, what right do you have regarding data brokers?",
            "choices": [
                "The right to shut down their website.",
                "The right to request access to and deletion of your personal data index.",
                "The right to demand payment for your data."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 16, "trust": 12},
            "feedback": "Privacy laws empower citizens to demand corporate aggregators delete personal files."
        }
    ],

    # Level 18 — Search Engines
    18: [
        {
            "id": "L18_Q1",
            "story": "You want to find private medical details online. What search method protects your privacy?",
            "choices": [
                "Use a standard search engine while logged into your primary profile account.",
                "Use a privacy search engine that does not track your search keywords or associate queries with your IP address.",
                "Use incognito mode on your standard browser."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 16, "security": 10},
            "feedback": "Incognito mode only hides local history, not server tracking. Privacy engines decouple queries from IP details."
        },
        {
            "id": "L18_Q2",
            "story": "You notice search results for political topics are vastly different on your laptop compared to your friend's laptop.",
            "choices": [
                "One laptop is broken.",
                "Search engines use profile history to personalize results, creating a filter bubble.",
                "It is a network glitch."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 10, "trust": 12},
            "feedback": "Filter bubbles limit the viewpoints you see by tailoring search feeds based on active tracking."
        },
        {
            "id": "L18_Q3",
            "story": "A search engine portal asks to save your search history to 'give you faster results.'",
            "choices": [
                "Agree to save all historical queries.",
                "Decline to save search history on the cloud, or clear your history logs regularly.",
                "Delete your browser."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 14, "security": 8},
            "feedback": "Cloud history databases compile interests, location histories, and personal health habits."
        },
        {
            "id": "L18_Q4",
            "story": "You accidentally searched for something embarrassing while logged in. How do you clean this footprint?",
            "choices": [
                "You cannot clean search logs.",
                "Go to your search account settings page and delete the specific queries from your cloud activity history.",
                "Reboot your router."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 15, "reputation": 10},
            "feedback": "Large search providers let you delete query profiles from your active cloud account settings."
        },
        {
            "id": "L18_Q5",
            "story": "You see search results that contain your home address and telephone number.",
            "choices": [
                "Submit a removal request directly to the search provider to de-index personal identification pages.",
                "Hope no one search lists your name.",
                "Change search engine providers."
            ],
            "correct_idx": 0,
            "effects": {"xp": 12, "coins": 6, "privacy": 18, "security": 10},
            "feedback": "Search providers have specialized forms to request deletion of personally identifying parameters."
        },
        {
            "id": "L18_Q6",
            "story": "A search engine extension offers to help you find discount coupons while logging your search activities.",
            "choices": [
                "Install it to save money.",
                "Decline, as coupon search extensions track and sell search pathways to advertising networks.",
                "Install it but use it only in private tabs."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "privacy": 12, "security": 8},
            "feedback": "Coupon utility extensions operate by collecting all search parameters and URLs to monetize them."
        },
        {
            "id": "L18_Q7",
            "story": "You want to find an un-indexed source. What search syntax helps bypass general search sorting algorithms?",
            "choices": [
                "Use quotes for exact matches and filters (e.g. site:, filetype:).",
                "Type the exact sentence in capital letters.",
                "Ask a friend."
            ],
            "correct_idx": 0,
            "effects": {"xp": 10, "coins": 5, "reputation": 10, "trust": 10},
            "feedback": "Exact search syntax and file filters refine results, retrieving specific records without logging broad query trends."
        },
        {
            "id": "L18_Q8",
            "story": "You search a topic and see the top 4 results are labeled 'Sponsored link'.",
            "choices": [
                "Click the first sponsored link immediately.",
                "Recognize these as paid advertising spots, scroll down to the organic results, and compare sources.",
                "Assume sponsored links are the only safe sites."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "security": 12, "trust": 10},
            "feedback": "Sponsored links are paid advertisements. Scammers buy them to push fake mirror login portals."
        },
        {
            "id": "L18_Q9",
            "story": "A search provider lets you turn on 'SafeSearch'. What is the security function?",
            "choices": [
                "It blocks hackers from access.",
                "It filters out explicit and unsafe content from search engine result lists.",
                "It encrypts your search requests."
            ],
            "correct_idx": 1,
            "effects": {"xp": 10, "coins": 5, "reputation": 8, "trust": 5},
            "feedback": "SafeSearch filters explicit graphic results, reducing risks of downloading bad malware attachments."
        },
        {
            "id": "L18_Q10",
            "story": "What is the primary privacy advantage of using search engines that do not log history?",
            "choices": [
                "They block spam pop-ups.",
                "They prevent the creation of an interest-based profile that is sold to advertising brokers.",
                "They make web pages load twice as fast."
            ],
            "correct_idx": 1,
            "effects": {"xp": 12, "coins": 6, "privacy": 15, "trust": 10},
            "feedback": "Zero-log search engines prevent corporate profiling networks from monetizing your daily searches."
        }
    ],

    # Level 20 — Final Cyber Challenge (Grand Scenario Mix)
    20: [
        {
            "id": "L20_Q1",
            "story": "You receive a phone call from 'Security Department' saying your banking password has compromised. They ask you to confirm your current login detail to reset it.",
            "choices": [
                "Provide the current password to secure the account.",
                "Hang up, and contact the official security number printed on the back of your debit card.",
                "Give them a fake password to troll them."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 20, "privacy": 15},
            "feedback": "Support callers are often social engineers trying to bypass security barriers by scaring you."
        },
        {
            "id": "L20_Q2",
            "story": "You find a USB flash drive labeled 'Final Exam Answer Key' lying on the ground in the school hallway.",
            "choices": [
                "Plug it into your personal computer to see the answers.",
                "Give the drive to the school office or IT department without plugging it in.",
                "Plug it into your friend's laptop to check it."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 25, "reputation": 15},
            "feedback": "Found USB drives can run automated keystroke script injections (Rubber Ducky attacks) to drop trojans."
        },
        {
            "id": "L20_Q3",
            "story": "A friend shares a QR code on a messaging app saying it gives free food delivery vouchers.",
            "choices": [
                "Scan it immediately using your banking app.",
                "Verify the source separately, inspect the destination URL before logging in, and avoid scanning unverified codes.",
                "Scan it on a public computer."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 20, "privacy": 12},
            "feedback": "Quishing (QR Code Phishing) bypasses standard link filters to route devices to malicious phishing portals."
        },
        {
            "id": "L20_Q4",
            "story": "Your phone carrier alerts you that a request to transfer your phone number to a new SIM card has been initialized. You did not request this.",
            "choices": [
                "Ignore it; it's a routine update.",
                "Contact your phone carrier immediately to lock your account, reporting an active SIM swap attack.",
                "Turn off your phone for 24 hours."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 25, "privacy": 15},
            "feedback": "SIM swap attacks hijack phone numbers to bypass SMS-based Multi-Factor Authentication codes."
        },
        {
            "id": "L20_Q5",
            "story": "You receive a message from your parent's profile asking you to send them money because they are locked out of their house. The language is slightly formal.",
            "choices": [
                "Transfer the money immediately.",
                "Call your parent directly on their phone number to verify their voice and safety details.",
                "Report their account for hacking."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "trust": 20, "security": 15},
            "feedback": "Compromised profiles are used by social engineers to send urgent requests to close family members."
        },
        {
            "id": "L20_Q6",
            "story": "An app asks for permission to 'access local devices and network computers' on startup.",
            "choices": [
                "Click yes to ensure connection.",
                "Deny local network permissions unless it is a verified local game or cast utility, reducing tracking risk.",
                "Restart your router."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 18, "privacy": 12},
            "feedback": "Local network permissions allow tracking code to scan and build profiles of other devices in your home."
        },
        {
            "id": "L20_Q7",
            "story": "You notice your laptop webcam has a tiny green light glowing when you are not running any camera app.",
            "choices": [
                "Ignore it as a system glitch.",
                "Run a malware scan, check background app camera access details, and cover the lens.",
                "Delete your camera drivers."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 22, "privacy": 20},
            "feedback": "Spyware/Remote Access Trojans (RATs) activate camera hardware silently to monitor targets."
        },
        {
            "id": "L20_Q8",
            "story": "You want to buy cryptocurrency on a peer-to-peer exchange. The other party suggests taking the trade off-platform.",
            "choices": [
                "Agree, as it will reduce fees.",
                "Refuse, keeping the trade on the exchange escrow system to protect transaction coins.",
                "Cancel your trade account."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "trust": 15, "security": 15},
            "feedback": "Off-platform trades are common setups to take coins without forwarding payment, with no recourse."
        },
        {
            "id": "L20_Q9",
            "story": "You see an option to download a 'VPN patch' that bypasses school firewall blocks on games.",
            "choices": [
                "Download and run it.",
                "Avoid unverified network patches, as they frequently route network traffic through malicious proxy nodes.",
                "Report the game host."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 20, "privacy": 12},
            "feedback": "Firewall patches carry hidden trojans and can monitor traffic to harvest credentials."
        },
        {
            "id": "L20_Q10",
            "story": "You want to write a security question answer for account recovery. The prompt is 'Where did your parents meet?'",
            "choices": [
                "Type the exact town name, since it's easy to remember.",
                "Type a long random passphrase or an unrelated answer that is stored securely in a password manager.",
                "Type your school mascot's name."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 25, "privacy": 15},
            "feedback": "Real security answers can be easily researched on public data broker directories or social posts."
        },
        {
            "id": "L20_Q11",
            "story": "What is the most secure method to log in to high-security platforms (like email or banking)?",
            "choices": [
                "Username and password only.",
                "Username, password, and a hardware security key (FIDO2) or authenticator app (TOTP).",
                "Username, password, and SMS text code verification."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "security": 25, "privacy": 15},
            "feedback": "Hardware keys and TOTP apps are highly resistant to phishing, unlike SMS verification codes."
        },
        {
            "id": "L20_Q12",
            "story": "You want to clear your digital footprint before taking a job in a highly secure environment.",
            "choices": [
                "Delete your browsing history.",
                "Run a comprehensive privacy audit, opt-out of data brokers, secure active profiles, and enforce deletion rights.",
                "Deactivate your internet router."
            ],
            "correct_idx": 1,
            "effects": {"xp": 15, "coins": 10, "reputation": 20, "privacy": 20},
            "feedback": "Digital sovereignty requires active review of old logs, cookie settings, and data broker catalogs."
        }
    ]
}
