from django.core.management.base import BaseCommand
from home.models import Scenario, Choice, Achievement

class Command(BaseCommand):
    help = 'Seeds 25 comprehensive educational scenarios and achievements about Digital Footprints.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Seeding scenarios and achievements...'))

        # Clear existing to allow clean re-seeding
        Choice.objects.all().delete()
        Scenario.objects.all().delete()
        Achievement.objects.all().delete()

        # Seed Achievements
        achievements_data = [
            {
                'title': 'First Digital Step',
                'description': 'Completed your very first digital footprint scenario.',
                'icon_emoji': '👣',
                'badge_code': 'FIRST_STEP',
                'criteria_type': 'SCENARIO_1'
            },
            {
                'title': 'Privacy Guardian',
                'description': 'Maintained a score of 50+ points in your journey.',
                'icon_emoji': '🛡️',
                'badge_code': 'PRIVACY_GUARDIAN',
                'criteria_type': 'SCORE_50'
            },
            {
                'title': 'Footprint Master',
                'description': 'Reached 150+ total digital footprint score.',
                'icon_emoji': '👑',
                'badge_code': 'FOOTPRINT_MASTER',
                'criteria_type': 'SCORE_150'
            },
            {
                'title': 'Cautious Communicator',
                'description': 'Made 5 consecutive safe decisions.',
                'icon_emoji': '🔒',
                'badge_code': 'CAUTIOUS_COMMUNICATOR',
                'criteria_type': 'SAFE_5'
            },
            {
                'title': 'Digital Citizen',
                'description': 'Successfully completed all 25 digital footprint scenarios!',
                'icon_emoji': '🎓',
                'badge_code': 'DIGITAL_CITIZEN',
                'criteria_type': 'COMPLETED_ALL'
            }
        ]

        for ach in achievements_data:
            Achievement.objects.create(**ach)

        # Seed Scenarios (25 Scenarios)
        scenarios_data = [
            # 1. Tagged Photos
            {
                'order': 1,
                'title': 'The Embarrassing Party Tag',
                'category': 'Tagged Photos',
                'situation_text': 'A friend tags you in a public photo from a weekend gathering where you look silly and out of control. Your school teachers and future employers could see it.',
                'choices': [
                    {
                        'text': 'Leave it public and ignore it; it is just a joke.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Leaving public tagged photos unaddressed lets search engines index them under your full name, shaping public perceptions permanently.',
                        'consequences': 'College admissions officers and hiring managers often search tagged photos. An unaddressed questionable photo remains visible on your public record.',
                        'tip': 'Regularly review tagged posts and act immediately if photos reflect poorly on your character.'
                    },
                    {
                        'text': 'Kindly ask your friend to remove the photo and untag yourself immediately.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Untagging breaks the direct link to your profile, and asking your friend to take it down stops it from circulating publicly.',
                        'consequences': 'Demonstrates proactive control over your digital footprint, ensuring search results for your name remain positive.',
                        'tip': 'Enable profile settings that require your explicit approval before tagged photos appear on your profile.'
                    },
                    {
                        'text': 'Untag yourself, but say nothing to your friend.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Untagging removes the direct link from your profile, but the photo still exists on your friend\'s public profile.',
                        'consequences': 'Reduces visibility on your timeline, though persistent searchers might still find it on your friend\'s feed.',
                        'tip': 'Follow up untagging with a friendly private message to ensure total removal.'
                    },
                    {
                        'text': 'Share the photo on your own story with a sarcastic caption.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Re-sharing amplifies the broadcast of the photo and increases its engagement rate, pushing it higher in feed algorithms.',
                        'consequences': 'Turns a minor tag into a post directly created and endorsed by you on your own digital footprint.',
                        'tip': 'Never re-post content you would not want framed on your living room wall.'
                    }
                ]
            },
            # 2. Location Sharing
            {
                'order': 2,
                'title': 'Real-Time Vacation Check-In',
                'category': 'Location Sharing',
                'situation_text': 'You are at the airport leaving for a 2-week family vacation. You want to post an exciting update on social media.',
                'choices': [
                    {
                        'text': 'Post a public story: "Heading to Paris for 2 weeks! House is empty!" with live location.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Broadcasting real-time locations and empty homes exposes physical security risks and creates geotagged data trails visible to anyone.',
                        'consequences': 'Burglars scan location tags for empty houses, and live coordinates are recorded permanently by ad networks.',
                        'tip': 'Wait until you return home before posting vacation photos and highlights.'
                    },
                    {
                        'text': 'Save your photos and post a trip highlight album after returning home.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Posting after returning protects your physical safety while still allowing you to share memories with friends safely.',
                        'consequences': 'Prevents property risks and allows you to curate high-quality photos intentionally rather than impulse posting.',
                        'tip': 'Always post vacation memories in retrospect ("Throwback to last week!").'
                    },
                    {
                        'text': 'Share a photo with close private friends only, without precise GPS tagging.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Restricting audience limits exposure, though close friends list settings should be routinely audited.',
                        'consequences': 'Dramatically narrows your exposure risk compared to public broadcasts.',
                        'tip': 'Disable automated camera geotagging in your phone settings.'
                    },
                    {
                        'text': 'Check in at the airport publicly but omit how long you will be away.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Public airport check-ins still broadcast that you are traveling away from your home city.',
                        'consequences': 'Leaves digital breadcrumbs linking your identity to flight schedules and locations.',
                        'tip': 'Turn off default location permissions for social media apps.'
                    }
                ]
            },
            # 3. Public vs Private Profiles
            {
                'order': 3,
                'title': 'Setting Up Your Main Social Account',
                'category': 'Public vs Private Profiles',
                'situation_text': 'You are creating a new social media profile for sharing daily life, hobbies, and personal photos.',
                'choices': [
                    {
                        'text': 'Keep the profile completely public so anyone can follow and view your life.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Public profiles allow web crawlers, strangers, and data brokers to harvest your pictures, status updates, and daily routine.',
                        'consequences': 'Your personal photos and updates become part of the public search domain forever.',
                        'tip': 'Use public profiles only for professional portfolios, not personal daily life.'
                    },
                    {
                        'text': 'Set the profile to private and approve only people you know personally in real life.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Private accounts create a boundary around your personal footprint, ensuring only verified contacts see your updates.',
                        'consequences': 'Prevents unauthorized scraping of your images and keeps your personal life contained within a trusted circle.',
                        'tip': 'Audit your follower list twice a year to remove acquaintances you no longer interact with.'
                    },
                    {
                        'text': 'Keep profile public, but refrain from putting your real name in the bio.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'Hiding your real name helps, but photos, metadata, and friend interactions can easily reveal your real identity.',
                        'consequences': 'Offers a false sense of anonymity while still exposing media content publicly.',
                        'tip': 'Anonymity online is rarely absolute; profile privacy settings offer stronger control.'
                    },
                    {
                        'text': 'Accept every follow request you receive to build a massive follower count.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Accepting strangers negates privacy settings, opening your footprint to malicious accounts and impersonators.',
                        'consequences': 'Exposes your location, school, and family details to unvetted strangers.',
                        'tip': 'A follower count is temporary; your digital footprint and security are permanent.'
                    }
                ]
            },
            # 4. Comments & Heat of the Moment
            {
                'order': 4,
                'title': 'Responding to an Online Argument',
                'category': 'Comments',
                'situation_text': 'Someone posts an opinion online that strongly offends you. You feel angry and want to reply.',
                'choices': [
                    {
                        'text': 'Write an angry comment attacking their intelligence and calling them names.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Angry comments leave a permanent paper trail of hostility indexed under your name or username.',
                        'consequences': 'Ranting comments are screenshot and stored, reflecting negatively on your emotional maturity.',
                        'tip': 'Never post online when emotionally triggered. Take a 15-minute break first.'
                    },
                    {
                        'text': 'Pause, step away from the screen, and choose not to engage in toxic arguments.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Choosing not to engage prevents unnecessary digital drama and keeps your public comment record clean and positive.',
                        'consequences': 'Saves mental energy and keeps your digital footprint free of flame wars.',
                        'tip': 'Ask yourself: "Will I be proud of this comment in 5 years?"'
                    },
                    {
                        'text': 'Post a calm, respectful response citing facts without personal attacks.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Constructive dialogue shows maturity, provided the forum itself is respectful.',
                        'consequences': 'Demonstrates civil discourse, though public forums can still drag you into extended debates.',
                        'tip': 'Keep public discussions polite, objective, and brief.'
                    },
                    {
                        'text': 'Delete your comment 10 minutes after posting an angry reply.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Deleting content does not guarantee removal; screenshots or archive scrapers may capture it within seconds.',
                        'consequences': 'False belief in deletion leads to careless posting behavior.',
                        'tip': 'Assume everything you type online is captured immediately by someone.'
                    }
                ]
            },
            # 5. Online Gaming Usernames
            {
                'order': 5,
                'title': 'Choosing a Gaming Username',
                'category': 'Online Gaming Usernames',
                'situation_text': 'You are creating an account on a popular online multiplayer gaming platform.',
                'choices': [
                    {
                        'text': 'Use your real full name and birth year (e.g. Alex_Smith_2008).',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Combining full names and birth years in gaming tags allows strangers across global servers to search and locate your social profiles.',
                        'consequences': 'Links gaming activity, voice chat behavior, and stats directly to your real-world offline identity.',
                        'tip': 'Keep gaming handles separate from real-world identities and official documents.'
                    },
                    {
                        'text': 'Create a fun, anonymous handle unrelated to your real name or personal details.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Anonymized usernames insulate your personal life while letting you enjoy online gaming fully.',
                        'consequences': 'Keeps your gaming identity distinct from your academic and professional digital footprint.',
                        'tip': 'Use pseudonyms that contain no personal identifiers (name, age, location, school).'
                    },
                    {
                        'text': 'Use your school name and nickname in the username.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Revealing your school location narrows down your geographic footprint to strangers.',
                        'consequences': 'Enables location-tracking and unwanted contact from online players.',
                        'tip': 'Never include school names, sports teams, or towns in public usernames.'
                    },
                    {
                        'text': 'Use the exact same username and password across all your gaming and personal accounts.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Reusing identical usernames across platforms links all your disparate accounts into one easily traceable web.',
                        'consequences': 'Data breaches on one gaming forum will expose your entire online presence.',
                        'tip': 'Vary your handles across unrelated hobbies and platforms.'
                    }
                ]
            },
            # 6. Old Posts & Digital Audits
            {
                'order': 6,
                'title': 'Reviewing Your Early Middle School Posts',
                'category': 'Old Posts',
                'situation_text': 'You look back at social media posts you made 4 years ago. Some contain cringe humor, offensive slang, or childish complaints.',
                'choices': [
                    {
                        'text': 'Leave them alone; nobody looks at old posts anyway.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Old posts stay indexable forever and are frequently dredged up during college applications or job background checks.',
                        'consequences': 'Past immature statements can be judged against your current character.',
                        'tip': 'Conduct an annual "digital footprint cleanup" to remove outdated or questionable content.'
                    },
                    {
                        'text': 'Delete or archive inappropriate past posts and clean up your public timeline history.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Cleaning up past timelines ensures your current digital footprint reflects your current maturity and values.',
                        'consequences': 'Protects your reputation from past errors while maintaining control over your online identity.',
                        'tip': 'Use built-in archive features or privacy filters to restrict visibility of past years.'
                    },
                    {
                        'text': 'Make your entire account private while keeping old questionable posts on it.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Privating limits public viewing, though existing followers can still view and screenshot old posts.',
                        'consequences': 'Reduces public search risk, but internal follower risk remains.',
                        'tip': 'Private accounts still need internal content cleanup.'
                    },
                    {
                        'text': 'Repost the old cringe posts to laugh about them publicly.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Re-sharing brings past questionable content back to the top of current feeds.',
                        'consequences': 'Signals to your current audience that you still endorse the content.',
                        'tip': 'Let past mistakes fade away rather than renewing their broadcast.'
                    }
                ]
            },
            # 7. Deleted Content Myths
            {
                'order': 7,
                'title': 'The "Disappearing" Photo App',
                'category': 'Deleted Content',
                'situation_text': 'An app promises that photos sent through it auto-delete after 5 seconds. You are tempted to send a risky photo.',
                'choices': [
                    {
                        'text': 'Send the photo assuming it disappears completely after 5 seconds.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'No digital content truly disappears. Recipients can take screenshots, screen recordings, or use another phone camera to save it.',
                        'consequences': 'Risky photos can be saved permanently and redistributed without your consent.',
                        'tip': 'Remember the golden rule: Once digital, always permanent.'
                    },
                    {
                        'text': 'Refrain from sending any photo that you would not want stored permanently.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Understanding that ephemeral apps still generate permanent digital data protects you from severe reputational damage.',
                        'consequences': 'Keeps your digital trail completely clean and prevents extortion or embarrassment.',
                        'tip': 'Assume every receiver has a screen recorder active.'
                    },
                    {
                        'text': 'Send the photo only to your best friend whom you trust completely.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Trust can break, phones get stolen, and backup drives get synced to cloud services outside your control.',
                        'consequences': 'Puts your digital reputation into someone else\'s hands indefinitely.',
                        'tip': 'Even close friendships change; never store sensitive collateral on devices.'
                    },
                    {
                        'text': 'Send it with a text warning: "Do not screenshot this!"',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Asking someone not to screenshot often prompts curiosity or malicious screenshots.',
                        'consequences': 'Guarantees the receiver knows the content is sensitive and valuable to save.',
                        'tip': 'Warnings do not prevent screen captures or data logging.'
                    }
                ]
            },
            # 8. Online Quizzes & Data Collection
            {
                'order': 8,
                'title': 'The Fun "Which Superhero Are You?" Quiz',
                'category': 'Online Quizzes',
                'situation_text': 'A viral quiz asks for your mother\'s maiden name, childhood street, first pet\'s name, and birthday to reveal your superhero alter-ego.',
                'choices': [
                    {
                        'text': 'Fill out all answers accurately and share the result on your profile.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Viral quizzes are frequently engineered by data brokers to mine security questions used for account recovery.',
                        'consequences': 'Builds a public profile of secret security answers that can be used to breach your email or bank accounts.',
                        'tip': 'Never answer security question prompts on social media quizzes.'
                    },
                    {
                        'text': 'Recognize the security risk and skip the quiz entirely.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Avoiding data-harvesting traps keeps your personal identifiers and recovery credentials safe from data mining.',
                        'consequences': 'Prevents third-party trackers from building a detailed dossier on your personal identity.',
                        'tip': 'Treat personal history details as confidential credentials.'
                    },
                    {
                        'text': 'Take the quiz but put fake made-up answers for all personal questions.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Using fake data protects your real identity, though the site may still track IP address and cookies.',
                        'consequences': 'Avoids revealing authentic personal answers on your public footprint.',
                        'tip': 'Be mindful that quiz apps may still request broad profile permissions.'
                    },
                    {
                        'text': 'Tag 5 friends in the comments to take the quiz as well.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Tagging friends spreads data-harvesting schemes across your network footprint.',
                        'consequences': 'Exposes your contacts to identity mining traps.',
                        'tip': 'Do not amplify quizzes that request personal memory data.'
                    }
                ]
            },
            # 9. Email Communication
            {
                'order': 9,
                'title': 'Emailing Your Teacher or Future Director',
                'category': 'Email Communication',
                'situation_text': 'You need to email your instructor about a project deadline from your personal email address.',
                'choices': [
                    {
                        'text': 'Use your casual email "party_boy99x@coolmail.com" with subject "hey answer me".',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Unprofessional email addresses and slang leave a permanent record of poor decorum in institutional archives.',
                        'consequences': 'Creates a negative professional digital footprint in school or employer record archives.',
                        'tip': 'Create a professional email (firstname.lastname@domain.com) for official communications.'
                    },
                    {
                        'text': 'Use your student/formal email, include a clear subject line, polite greeting, and signature.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Formal emails establish a positive, respectable digital paper trail in academic and career records.',
                        'consequences': 'Builds a trail of professional competence that recommendations and reference checks rely upon.',
                        'tip': 'Structure official emails with Greeting, Clear Message, and Professional Sign-off.'
                    },
                    {
                        'text': 'Send a quick one-line message with no greeting or subject line.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Abrupt emails appear dismissive and reflect poorly on your digital communication skills.',
                        'consequences': 'Leaves an impression of carelessness in archived school exchanges.',
                        'tip': 'Always fill in the Subject field with a concise description of the topic.'
                    },
                    {
                        'text': 'Send the email from a shared family account without putting your name in the text.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'Unidentified emails cause confusion and clutter, though they avoid unprofessional handles.',
                        'consequences': 'Delays response times and creates disorganized communication records.',
                        'tip': 'Identify yourself clearly whenever communicating from non-standard accounts.'
                    }
                ]
            },
            # 10. School & Discussion Forums
            {
                'order': 10,
                'title': 'Posting on an Online Class Board',
                'category': 'School Forums',
                'situation_text': 'Your online class forum requires students to post peer critiques on a group project.',
                'choices': [
                    {
                        'text': 'Post: "This project is terrible and group 3 clearly put no effort in."',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Harsh insults on educational portals become part of your permanent academic record stored by school servers.',
                        'consequences': 'Can be flagged by administrators for code-of-conduct violations.',
                        'tip': 'Constructive feedback critiques the work, never the person.'
                    },
                    {
                        'text': 'Provide specific, encouraging critique highlighting strengths and gentle areas for improvement.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Polite, constructive forum contributions foster a leadership reputation on recorded academic databases.',
                        'consequences': 'Establishes a digital record of strong collaboration and maturity.',
                        'tip': 'Use the "Praise-Critique-Praise" sandwich method for peer reviews.'
                    },
                    {
                        'text': 'Copy-paste someone else\'s critique word-for-word to finish quickly.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Plagiarism tools automatically index and flag copied text across digital learning management systems.',
                        'consequences': 'Leaves a clear digital marker of academic dishonesty.',
                        'tip': 'Write authentic thoughts; plagiarism checkers retain permanent comparison logs.'
                    },
                    {
                        'text': 'Post only the bare minimum one-word answer "Good" to satisfy requirements.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'Low-effort responses do not damage your ethical record, but they show minimal engagement.',
                        'consequences': 'Misses an opportunity to build a strong academic track record.',
                        'tip': 'Engage meaningfully on public academic platforms.'
                    }
                ]
            },
            # 11. Search History & Browser Privacy
            {
                'order': 11,
                'title': 'Understanding Search Log Footprints',
                'category': 'Search History',
                'situation_text': 'You are logged into your primary Google account on a public library computer while researching topics for a paper.',
                'choices': [
                    {
                        'text': 'Leave your account logged in when walking away from the public computer.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Leaving accounts logged in on public terminals allows the next user to access your search history, cloud files, and identity.',
                        'consequences': 'Exposes your entire personal account ecosystem to strangers.',
                        'tip': 'Always log out and clear browser data when using shared computers.'
                    },
                    {
                        'text': 'Log out of your account, use Private/Incognito mode, and clear cookies before leaving.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Logging out and clearing local cache ensures no residual session tokens or history remain stored on the machine.',
                        'consequences': 'Keeps your browsing session contained to your eyes only.',
                        'tip': 'Incognito mode prevents local history saving, but account logouts are vital.'
                    },
                    {
                        'text': 'Close the browser window without logging out of your Google account.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Simply closing a browser window leaves active session cookies alive for whoever re-opens the browser.',
                        'consequences': 'Allows subsequent users to restore your active logged-in session.',
                        'tip': 'Closing a tab is NOT logging out.'
                    },
                    {
                        'text': 'Use Incognito mode while staying logged into your personal profile.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'Logging into your profile inside Incognito still syncs search activity directly to your cloud account history.',
                        'consequences': 'Does not stop search activity from accumulating on your main user dashboard.',
                        'tip': 'Incognito hides history from the local computer, not from the logged-in service.'
                    }
                ]
            },
            # 12. Online Reviews & Feedback
            {
                'order': 12,
                'title': 'Writing a Public Business Review',
                'category': 'Online Reviews',
                'situation_text': 'You had poor service at a local restaurant and want to post a review on Google or Yelp.',
                'choices': [
                    {
                        'text': 'Write an abusive review cursing at the staff and lying about food poisoning.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Exaggerated or abusive public reviews posted under your name can expose you to defamation liability and bad digital optics.',
                        'consequences': 'Legal risks and a permanent record of malicious public behavior.',
                        'tip': 'Public reviews are legal documents; stick strictly to truthful facts.'
                    },
                    {
                        'text': 'Write an objective, honest review describing what happened without insults or fabrication.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Truthful, measured feedback provides helpful consumer information while demonstrating responsible digital citizenship.',
                        'consequences': 'Builds a credible, helpful reviewer profile that reflects constructive communication.',
                        'tip': 'Describe the specific problem calmly and suggest how the service could improve.'
                    },
                    {
                        'text': 'Post 5 fake 1-star reviews from alternate accounts you created.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Review platforms use IP tracking and algorithms to detect and permanently flag review manipulation rings.',
                        'consequences': 'Associates your network IP with fraudulent spam activity.',
                        'tip': 'Never create sock-puppet accounts to manipulate public ratings.'
                    },
                    {
                        'text': 'Decide it is not worth posting publicly and email the manager directly instead.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Private communication resolves customer service issues directly without creating unnecessary public friction.',
                        'consequences': 'Solves the issue efficiently without inflating public drama.',
                        'tip': 'Direct private messages often yield faster solutions than public complaints.'
                    }
                ]
            },
            # 13. Photo Uploads & Metadata
            {
                'order': 13,
                'title': 'Uploading High-Res Photos of Your Home',
                'category': 'Photo Uploads',
                'situation_text': 'You snap photos of your new laptop desk setup at home to share on a hobby site.',
                'choices': [
                    {
                        'text': 'Upload raw camera photos with visible mail containing your address and unstripped EXIF GPS metadata.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Raw camera photos contain hidden EXIF data (exact GPS latitude/longitude, device serials) and visual private details.',
                        'consequences': 'Reveals your precise home location and expensive electronics to online thieves.',
                        'tip': 'Check photo backgrounds for documents, house numbers, or sensitive items before uploading.'
                    },
                    {
                        'text': 'Crop out private mail/documents and strip metadata before uploading.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Stripping metadata and scrubbing background details ensures you share your setup without leaking geographic credentials.',
                        'consequences': 'Allows safe sharing while shielding your home address and identity details.',
                        'tip': 'Turn off location services in your camera app when taking photos at home.'
                    },
                    {
                        'text': 'Blur out your address on the mail but leave camera location EXIF data intact.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Visual blurring is good, but tech-savvy users can extract exact GPS coordinates directly from the image file headers.',
                        'consequences': 'Leaks home location despite visual censoring.',
                        'tip': 'File metadata can reveal what the eye cannot see.'
                    },
                    {
                        'text': 'Share the photo only in a private group chat.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Group chats reduce audience exposure, but members can still save and re-share images.',
                        'consequences': 'Safer than open forums, though group privacy depends on member discretion.',
                        'tip': 'Even in group chats, avoid capturing sensitive paperwork in photos.'
                    }
                ]
            },
            # 14. Cloud Storage & Shareable Links
            {
                'order': 14,
                'title': 'Sharing Google Drive / Cloud Documents',
                'category': 'Cloud Storage',
                'situation_text': 'You are sharing a folder containing school notes, personal journal entries, and ID copies with a classmate.',
                'choices': [
                    {
                        'text': 'Set folder permissions to "Anyone with the link can edit" and post link in a group chat.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Setting open link permissions to folders with personal IDs exposes your private records to anyone who forwards the link.',
                        'consequences': 'Risk of data corruption, identity theft, and indexing by search engines.',
                        'tip': 'Never combine personal sensitive IDs in the same folder as shareable class notes.'
                    },
                    {
                        'text': 'Create a dedicated notes folder, set access to "Restricted", and invite your classmate\'s specific email as "Viewer".',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Specific email invitations under View-Only permissions enforce least-privilege access and protect sensitive files.',
                        'consequences': 'Keeps your private documents completely segregated and protected.',
                        'tip': 'Always restrict cloud file access to specific email addresses rather than open links.'
                    },
                    {
                        'text': 'Share the whole folder as "View Only" via open link.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Even View-Only open links allow anyone with the link to download personal documents if shared further.',
                        'consequences': 'Sensitive IDs inside the folder remain exposed to anyone who receives the link.',
                        'tip': 'Separate public files from private personal records.'
                    },
                    {
                        'text': 'Email all personal IDs and notes as raw unencrypted email attachments.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Unencrypted attachments stay in sent folders and server archives indefinitely.',
                        'consequences': 'Increases your cloud footprint of sensitive documents.',
                        'tip': 'Avoid storing copies of government IDs in unorganized cloud folders.'
                    }
                ]
            },
            # 15. Personal Info Sharing (PII)
            {
                'order': 15,
                'title': 'Posting Your First Driver\'s License',
                'category': 'Personal Information Sharing',
                'situation_text': 'You just passed your driving test! You want to celebrate by taking a picture with your new driver\'s license.',
                'choices': [
                    {
                        'text': 'Post a close-up photo of the license showing your full name, birth date, address, and license number.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Driver\'s licenses contain prime Personally Identifiable Information (PII) that scammers use to forge IDs or open credit lines.',
                        'consequences': 'High risk of identity theft, synthetic identity fraud, and physical address tracking.',
                        'tip': 'NEVER post pictures of official ID cards, passports, tickets, or credit cards.'
                    },
                    {
                        'text': 'Post a photo holding the steering wheel or car keys (with key teeth hidden) with a happy caption.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Sharing the joy of passing without displaying official documentation keeps your PII completely secure.',
                        'consequences': 'Celebrates the milestone publicly while maintaining zero exposure of critical identity credentials.',
                        'tip': 'Celebrate achievements through symbolic items (keys, thumbs up) rather than paperwork.'
                    },
                    {
                        'text': 'Post the license photo but place an emoji sticker over your license number only.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Covering only one field still leaves your full name, photo, birth date, and home address readable.',
                        'consequences': 'Provides enough PII for bad actors to locate your address or match data breaches.',
                        'tip': 'Stickers over photos can often be removed or leave surrounding data exposed.'
                    },
                    {
                        'text': 'Send the license photo in a group chat of 20 acquaintances.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Large group chats are informal public spaces where media is saved locally to multiple phone galleries.',
                        'consequences': 'Spreads your PII across 20 unverified phone storage devices.',
                        'tip': 'Treat your PII as high-value currency; do not send it in group chats.'
                    }
                ]
            },
            # 16. Permanent Online Records
            {
                'order': 16,
                'title': 'The News Article Mention',
                'category': 'Permanent Online Records',
                'situation_text': 'A local community newspaper publishes an online article mentioning your participation in a youth community service project.',
                'choices': [
                    {
                        'text': 'Embrace the article; it creates a positive, verifiable public record of your community involvement.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Positive press releases and community achievements form the foundation of a stellar public digital footprint.',
                        'consequences': 'When admissions or employers search your name, reputable news coverage highlights your good character.',
                        'tip': 'Build your digital footprint intentionally with positive achievements, volunteering, and published work.'
                    },
                    {
                        'text': 'Demand the newspaper take it down because you want zero internet presence.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'While privacy is important, eliminating all positive records leaves your footprint blank or defined by others.',
                        'consequences': 'Misses an opportunity to populate top search engine results with verified positive accomplishments.',
                        'tip': 'A good digital footprint is not an invisible one—it is a well-curated positive one.'
                    },
                    {
                        'text': 'Comment on the article using an anonymous account bragging about yourself.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Self-aggrandizing comments can look tacky if connected back to your IP or identity.',
                        'consequences': 'Adds unnecessary commentary to a clean press record.',
                        'tip': 'Let third-party news coverage speak for itself.'
                    },
                    {
                        'text': 'Link the article on your LinkedIn or professional academic profile.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Curating positive news links on professional portals showcases your civic contributions directly.',
                        'consequences': 'Solidifies your reputation as an active, engaged community member.',
                        'tip': 'Use professional networks to showcase your verified milestones.'
                    }
                ]
            },
            # 17. Likes & Social Signals
            {
                'order': 17,
                'title': ' Liking Bullying or Hate Posts',
                'category': 'Likes & Reactions',
                'situation_text': 'A popular classmate posts a meme making fun of a fellow student\'s physical appearance. Many people are liking it.',
                'choices': [
                    {
                        'text': 'Like the post so you do not feel left out by the popular crowd.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Social media platforms log your "Likes" publicly. Liking abusive content signals your endorsement of cyberbullying.',
                        'consequences': 'Your public profile activity log shows you supported harmful content, damaging your reputation.',
                        'tip': 'Your "Likes" are public endorsements. Never like content that hurts others.'
                    },
                    {
                        'text': 'Do not like or react to the post; report it for harassment if appropriate.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Refusing to engage stops the spread of toxic content and keeps your personal activity log free of harassment signals.',
                        'consequences': 'Demonstrates digital integrity and empathy.',
                        'tip': 'Algorithms reward engagement. Starve toxic posts of likes and views.'
                    },
                    {
                        'text': 'Leave a laughing emoji comment to fit in.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Commenting emojis actively boosts the post\'s algorithmic reach and creates permanent evidence of participation.',
                        'consequences': 'Directly connects your name to bullying behavior.',
                        'tip': 'Stand up against cyberbullying by withholding engagement.'
                    },
                    {
                        'text': 'Share the meme in a private chat asking "Isn\'t this mean?"',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Sharing harmful media spreads it further, regardless of your intent caption.',
                        'consequences': 'Further distributes hurtful content across private channels.',
                        'tip': 'If content is mean, do not forward or re-upload it anywhere.'
                    }
                ]
            },
            # 18. Digital Reputation & Job Searching
            {
                'order': 18,
                'title': 'Preparing for College / Job Applications',
                'category': 'Digital Reputation',
                'situation_text': 'You are applying for a prestigious internship or university program next month. You want your online presence ready.',
                'choices': [
                    {
                        'text': 'Conduct a thorough search of your full name on search engines and review all public social profiles.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Self-auditing allows you to discover what admissions officers see and fix any unintended public disclosures.',
                        'consequences': 'Ensures your public digital footprint matches your resume and application credentials.',
                        'tip': 'Search your name in quotation marks ("First Last") on Google and Bing periodically.'
                    },
                    {
                        'text': 'Assume admissions officers will only read your written application essay.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Over 70% of hiring managers and admissions staff check applicants\' public social media footprints.',
                        'consequences': 'Unchecked public profiles might contain red flags that contradict your essay.',
                        'tip': 'Your digital footprint IS part of your application.'
                    },
                    {
                        'text': 'Delete all social accounts completely 2 days before submitting the application.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'Panicking and deleting accounts last-minute does not instantly remove cached search results or archive logs.',
                        'consequences': 'Creates an abrupt absence rather than a well-maintained professional image.',
                        'tip': 'Build a clean footprint over time rather than attempting emergency wipeouts.'
                    },
                    {
                        'text': 'Create a professional LinkedIn or online portfolio showcasing your projects.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Proactively creating professional profiles places high-quality, positive links at the top of your search results.',
                        'consequences': 'Outranks old or irrelevant search results with verified accomplishments.',
                        'tip': 'Fill the first page of Google results with your own positive web assets.'
                    }
                ]
            },
            # 19. Online Petition & Activism Footprints
            {
                'order': 19,
                'title': 'Signing an Online Public Petition',
                'category': 'Digital Reputation',
                'situation_text': 'You see a controversial online petition about a local political dispute and want to add your support.',
                'choices': [
                    {
                        'text': 'Sign with your full name, email, home address, and check "Display my name publicly".',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Public petition sites rank very high on search engines. Signing controversial petitions publicly links your name to political stances forever.',
                        'consequences': 'Your name becomes permanently searchable alongside the petition topic on search engines.',
                        'tip': 'If signing petitions, opt to uncheck "Display signature publicly" unless you intend to stand by it publicly.'
                    },
                    {
                        'text': 'Sign the petition but uncheck public display of your name and personal details.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Unchecking public display allows your vote to count while protecting your public search results from permanent indexing.',
                        'consequences': 'Supports the cause without attaching a permanent search result to your identity.',
                        'tip': 'Protect your search results by keeping civic signatures private.'
                    },
                    {
                        'text': 'Share the petition on all your profiles urging everyone to sign immediately.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'Sharing advocacy is a personal right, but be mindful that controversial topics remain part of your permanent footprint.',
                        'consequences': 'Establishes a public political footprint.',
                        'tip': 'Be prepared to stand behind any cause you champion publicly.'
                    },
                    {
                        'text': 'Use a fake stolen name to sign the petition multiple times.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Falsifying identities on digital forms violates terms of service and compromises integrity.',
                        'consequences': 'Invalidates the petition and creates fraud records.',
                        'tip': 'Digital activism requires authenticity and privacy awareness.'
                    }
                ]
            },
            # 20. Smart Devices & Voice Search Logs
            {
                'order': 20,
                'title': 'Smart Assistant Voice History',
                'category': 'Search History',
                'situation_text': 'You use smart home speakers and mobile voice assistants daily for questions, songs, and personal notes.',
                'choices': [
                    {
                        'text': 'Never check or delete your voice assistant recording logs in account settings.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Voice assistants store audio clips and transcripts of everything recorded after wake words on cloud servers indefinitely.',
                        'consequences': 'Accumulates thousands of private voice snippets and ambient recordings in cloud history.',
                        'tip': 'Set auto-delete schedules (e.g. delete after 3 months) in your account privacy dashboard.'
                    },
                    {
                        'text': 'Regularly review voice logs, enable auto-delete features, and turn off mic when not in use.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Managing audio history settings ensures convenience without leaving years of unmonitored audio recordings stored.',
                        'consequences': 'Minimizes cloud telemetry data linked to your profile.',
                        'tip': 'Explore Google/Apple/Amazon Privacy Dashboards to manage voice recordings.'
                    },
                    {
                        'text': 'Scream personal secrets into the voice speaker for fun.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Audio files are stored as digital audio clips on server databases.',
                        'consequences': 'Stores sensitive spoken audio in cloud logs.',
                        'tip': 'Treat smart speakers as open recording microphones.'
                    },
                    {
                        'text': 'Disable voice recording storage altogether in privacy settings.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Opting out of voice storage halts audio log collection completely.',
                        'consequences': 'Prevents audio telemetry from building up on your account footprint.',
                        'tip': 'Disable "Save audio recordings" in account settings.'
                    }
                ]
            },
            # 21. Secondary "Finsta" Accounts
            {
                'order': 21,
                'title': 'The Secret "Finsta" Account',
                'category': 'Public vs Private Profiles',
                'situation_text': 'You decide to create a secret secondary account ("Finsta") to post unfiltered rants and embarrassing photos.',
                'choices': [
                    {
                        'text': 'Believe the account is 100% untraceable because you used a fake handle.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Secondary accounts link to your phone number, IP address, device ID, and contact lists. Apps suggest your account to friends automatically.',
                        'consequences': 'Secret accounts are routinely exposed via "People You May Know" algorithms or follower screenshots.',
                        'tip': 'Never rely on secondary accounts for toxic or risky posting.'
                    },
                    {
                        'text': 'Understand that secondary accounts still leave technical footprints and refrain from posting inappropriate content.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Recognizing that platform algorithms link phone numbers and contacts across accounts prevents false security assumptions.',
                        'consequences': 'Keeps your entire online presence clean and avoids accidental exposure.',
                        'tip': 'Assume any alt account can be linked back to you by phone or email sync.'
                    },
                    {
                        'text': 'Link your main phone number to the Finsta for easy password reset.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Linking your main phone number lets social platforms suggest your secret account to all your phone contacts.',
                        'consequences': 'Exposes your secret handle to school friends and family via contact matching.',
                        'tip': 'Phone contact syncing is the #1 way secret accounts get discovered.'
                    },
                    {
                        'text': 'Allow contacts sync on the alt account.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Syncing contacts instantly broadcasts your secondary profile to everyone in your address book.',
                        'consequences': 'Immediately unmasks your alt account to real-world acquaintances.',
                        'tip': 'Deny contact permissions for secret or hobby profiles.'
                    }
                ]
            },
            # 22. Fitness Trackers & Map Data
            {
                'order': 22,
                'title': 'Publishing Running Routes on Fitness Apps',
                'category': 'Location Sharing',
                'situation_text': 'You use a fitness app to track your daily jog around your neighborhood and share workout maps.',
                'choices': [
                    {
                        'text': 'Publish workout maps publicly showing the exact start and end point at your front door.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Public workout maps reveal exact home locations, daily routines, and times when you are away from home.',
                        'consequences': 'Allows strangers to map your daily schedule and physical residence.',
                        'tip': 'Use "Privacy Zones" in fitness apps to hide 1/2 mile radius around your home address.'
                    },
                    {
                        'text': 'Enable privacy zones around your home/school and set workout sharing to private.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Privacy zones obscure the start/end points of fitness maps, hiding your home location while tracking workouts.',
                        'consequences': 'Protects physical safety while enjoying fitness app features.',
                        'tip': 'Always obscure start/end locations on public GPS workout logs.'
                    },
                    {
                        'text': 'Share workout stats (distance/time) without the GPS route map.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Sharing text metrics celebrates progress without exposing geographic location footprints.',
                        'consequences': 'Keeps location hidden while participating in fitness communities.',
                        'tip': 'Text stats share achievements safely.'
                    },
                    {
                        'text': 'Post workout maps with your home address labeled in the title.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Explicitly labeling home addresses on public maps creates severe physical safety risks.',
                        'consequences': 'Directly publishes sensitive home location data.',
                        'tip': 'Never label home or school addresses on public maps.'
                    }
                ]
            },
            # 23. Wi-Fi Networks & Footprints
            {
                'order': 23,
                'title': 'Connecting to Unsecured Mall Wi-Fi',
                'category': 'Search History',
                'situation_text': 'You are at a shopping mall and connect to "Free_Mall_WiFi" without a password to log into your school portal.',
                'choices': [
                    {
                        'text': 'Log into unencrypted sensitive accounts while on open public Wi-Fi.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Open Wi-Fi networks allow network administrators and packet sniffers to log visited domain names and unencrypted traffic.',
                        'consequences': 'Exposes browsing activity logs and potential session data to network operators.',
                        'tip': 'Avoid logging into sensitive accounts on open public Wi-Fi networks.'
                    },
                    {
                        'text': 'Use cellular data or connect through a trusted VPN when on public Wi-Fi.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'VPN encryption or cellular data shields your network footprint and DNS requests from local network monitoring.',
                        'consequences': 'Ensures your data stream remains encrypted and hidden from local eavesdroppers.',
                        'tip': 'Use HTTPS and trusted VPNs when using public wireless access points.'
                    },
                    {
                        'text': 'Turn off Wi-Fi auto-connect in your device settings when out in public.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Disabling auto-connect prevents your device from constantly broadcasting probing requests with past connected Wi-Fi names (SSIDs).',
                        'consequences': 'Stops devices from broadcasting past location histories to nearby Wi-Fi sniffers.',
                        'tip': 'Turn off Wi-Fi auto-join to prevent automatic logging on public networks.'
                    },
                    {
                        'text': 'Ignore security warnings on HTTPS certificate errors to access a site.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Bypassing SSL/TLS certificate warnings on public Wi-Fi exposes your login credentials directly to man-in-the-middle attacks.',
                        'consequences': 'Immediate risk of credential theft and session hijacking.',
                        'tip': 'NEVER bypass browser security warnings on public Wi-Fi.'
                    }
                ]
            },
            # 24. Unsubscribing & Data Deletion Rights
            {
                'order': 24,
                'title': 'Unused Accounts on Old Websites',
                'category': 'Permanent Online Records',
                'situation_text': 'You have 15 unused accounts from old games, forums, and shopping sites you used 3 years ago.',
                'choices': [
                    {
                        'text': 'Leave the old unused accounts open and forgotten indefinitely.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Forgotten accounts are vulnerable to data breaches. If an old site suffers a leak, your old passwords and data get exposed.',
                        'consequences': 'Expands your unnecessary digital attack surface and leaves lingering data on old servers.',
                        'tip': 'Delete unused accounts to shrink your passive digital footprint.'
                    },
                    {
                        'text': 'Log into old accounts, request account deletion, and remove your personal data.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Actively deleting unused accounts removes your stored data from third-party databases, reducing breach exposure.',
                        'consequences': 'Shrinks your digital footprint and protects old personal records.',
                        'tip': 'Use "Right to be Forgotten" or account deletion options on old services.'
                    },
                    {
                        'text': 'Change password to a random string but leave the account active.',
                        'score_impact': 5,
                        'quality_type': 'GOOD',
                        'explanation': 'Securing the account helps, but your stored personal data remains in their database.',
                        'consequences': 'Prevents account takeover, though data retains on server databases.',
                        'tip': 'Full account deletion is cleaner than abandoning secured accounts.'
                    },
                    {
                        'text': 'Mark all notification emails from old sites as spam without deleting accounts.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'Hiding emails removes them from inbox sight, but the underlying account and data trail remain active on their servers.',
                        'consequences': 'Out of sight does not mean out of their database.',
                        'tip': 'Unsubscribing from emails is different from deleting an account.'
                    }
                ]
            },
            # 25. The Final Digital Legacy
            {
                'order': 25,
                'title': 'Defining Your Digital Legacy',
                'category': 'Digital Reputation',
                'situation_text': 'You are reflecting on how your overall digital footprint will represent you to future colleges, employers, and family.',
                'choices': [
                    {
                        'text': 'Commit to being an active, respectful digital citizen who posts intentionally and protects privacy.',
                        'score_impact': 10,
                        'quality_type': 'EXCELLENT',
                        'explanation': 'Digital footprints are not just about avoiding mistakes—they are about building a positive, inspiring legacy of your life and work.',
                        'consequences': 'Creates an online presence that opens doors to academic, career, and personal opportunities.',
                        'tip': 'Your digital footprint is your lifelong online resume. Build it with purpose and pride!'
                    },
                    {
                        'text': 'Decide internet safety does not matter and post whatever pops into your head.',
                        'score_impact': -10,
                        'quality_type': 'DANGEROUS',
                        'explanation': 'Careless posting creates a chaotic digital footprint that can hinder future educational and professional ambitions.',
                        'consequences': 'Long-term reputational damage across search engines and social archives.',
                        'tip': 'Think before you click, post, like, or share.'
                    },
                    {
                        'text': 'Hide from the internet completely and never create any online work or portfolio.',
                        'score_impact': 0,
                        'quality_type': 'NEUTRAL',
                        'explanation': 'A completely blank footprint leaves you invisible in a digital world where achievements are verified online.',
                        'consequences': 'Misses out on showcasing genuine talents, creative projects, and leadership.',
                        'tip': 'Aim for a positive footprint, not an invisible one.'
                    },
                    {
                        'text': 'Pay a shady service $500 to "wipe" your internet history.',
                        'score_impact': -5,
                        'quality_type': 'RISKY',
                        'explanation': 'Third-party "wipe" services are often scams and cannot delete third-party archives or news coverage.',
                        'consequences': 'Wastes money while leaving actual web archives intact.',
                        'tip': 'Authentic digital habits build a better reputation than quick-fix promises.'
                    }
                ]
            }
        ]

        for s_data in scenarios_data:
            choices_list = s_data.pop('choices')
            scenario = Scenario.objects.create(**s_data)
            for c_data in choices_list:
                Choice.objects.create(scenario=scenario, **c_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(scenarios_data)} scenarios and {len(achievements_data)} achievements!'))
