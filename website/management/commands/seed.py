from datetime import time
from django.core.management.base import BaseCommand
from website.models import (
    SiteSettings, Program, ScheduleItem, StaffMember,
    Testimonial, FeeItem, FAQ,
)


class Command(BaseCommand):
    help = "Seed the database with sample content"

    def handle(self, *args, **options):
        # Site Settings
        settings = SiteSettings.load()
        settings.site_name = "The Garden of Children"
        settings.tagline = "Nurturing growth, one child at a time"
        settings.ages_served = "30 months to kindergarten"
        settings.about_text = (
            "The Garden of Children is a warm, welcoming daycare nestled in the heart of "
            "Vancouver, BC. Founded with a passion for early childhood education, we provide "
            "a safe and stimulating environment where children aged 30 months to kindergarten "
            "can explore, learn, and grow at their own pace.\n\n"
            "Our experienced and caring educators are committed to building strong foundations "
            "for lifelong learning through play-based activities, creative expression, and "
            "meaningful connections with nature and community."
        )
        settings.philosophy_text = (
            "We believe every child is unique, capable, and full of potential. Our play-based "
            "curriculum is inspired by a deep respect for childhood and guided by the belief "
            "that children learn best when they feel safe, valued, and free to explore.\n\n"
            "At The Garden of Children, learning happens everywhere — in the garden, at the "
            "art table, during story time, and through everyday moments of wonder. We nurture "
            "the whole child: social, emotional, physical, and cognitive development go hand "
            "in hand."
        )
        settings.address = "123 Garden Lane"
        settings.city = "Vancouver, BC"
        settings.phone = "(604) 555-0199"
        settings.email = "hello@gardenofchildren.ca"
        settings.hours_weekday = "7:00 AM – 6:00 PM"
        settings.save()
        self.stdout.write(self.style.SUCCESS("Site settings created"))

        # Programs
        programs_data = [
            {
                "title": "Toddler Program",
                "age_range": "30 months – 3 years",
                "description": (
                    "Our Toddler Program provides a gentle introduction to group care. "
                    "Through sensory play, music, art, and outdoor exploration, toddlers build "
                    "confidence and develop key social and motor skills in a nurturing setting. "
                    "Activities are designed to encourage curiosity and independence while providing "
                    "plenty of comfort and reassurance."
                ),
                "order": 1,
            },
            {
                "title": "Preschool Program",
                "age_range": "3 – 5 years",
                "description": (
                    "Our Preschool Program builds on children's natural curiosity with a rich, "
                    "play-based curriculum. Children engage in hands-on activities including art, "
                    "science experiments, storytelling, dramatic play, and nature walks. We focus "
                    "on developing literacy, numeracy, and social skills to prepare children for "
                    "a confident start to kindergarten."
                ),
                "order": 2,
            },
            {
                "title": "Kindergarten Readiness",
                "age_range": "4 – 5 years",
                "description": (
                    "Designed for children entering kindergarten the following year, this program "
                    "focuses on school readiness skills including letter and number recognition, "
                    "self-regulation, following routines, and collaborative play. Children practice "
                    "independence and build the social confidence they'll need for their big transition."
                ),
                "order": 3,
            },
        ]
        for data in programs_data:
            Program.objects.get_or_create(title=data["title"], defaults=data)
        self.stdout.write(self.style.SUCCESS("Programs created"))

        # Schedule
        schedule_data = [
            (time(7, 0), time(8, 30), "Arrival & Free Play", "Welcome time with open-ended play activities", 1),
            (time(8, 30), time(9, 0), "Morning Snack", "Healthy snack and group conversation", 2),
            (time(9, 0), time(10, 0), "Circle Time & Learning", "Songs, stories, calendar, and group activities", 3),
            (time(10, 0), time(11, 0), "Outdoor Play", "Fresh air and active play in our garden and playground", 4),
            (time(11, 0), time(11, 45), "Creative Activities", "Art, sensory play, science, or music", 5),
            (time(11, 45), time(12, 30), "Lunch", "Nutritious meal served family-style", 6),
            (time(12, 30), time(14, 30), "Rest Time", "Quiet time with stories and soft music", 7),
            (time(14, 30), time(15, 0), "Afternoon Snack", "Light snack and waking-up activities", 8),
            (time(15, 0), time(16, 0), "Outdoor Play", "Afternoon outdoor exploration and games", 9),
            (time(16, 0), time(17, 0), "Free Play & Activities", "Child-led play, puzzles, and small-group activities", 10),
            (time(17, 0), time(18, 0), "Quiet Play & Pickup", "Calm activities as families arrive", 11),
        ]
        for ts, te, act, desc, order in schedule_data:
            ScheduleItem.objects.get_or_create(
                activity=act, order=order,
                defaults={"time_start": ts, "time_end": te, "description": desc, "order": order},
            )
        self.stdout.write(self.style.SUCCESS("Schedule created"))

        # Staff
        staff_data = [
            {
                "name": "Sarah Mitchell",
                "role": "Director & Lead Educator",
                "bio": "With over 15 years in early childhood education, Sarah founded The Garden of Children to create a space where every child can thrive. She holds an ECE diploma and a passion for nature-based learning.",
                "order": 1,
            },
            {
                "name": "Emily Chen",
                "role": "Preschool Teacher",
                "bio": "Emily brings creativity and warmth to the preschool classroom. She specializes in arts-based learning and loves watching children discover new ways to express themselves.",
                "order": 2,
            },
            {
                "name": "Marcus Johnson",
                "role": "Toddler Room Educator",
                "bio": "Marcus is known for his calm presence and gentle approach. With a background in child development, he creates activities that spark curiosity while keeping little ones feeling safe and supported.",
                "order": 3,
            },
        ]
        for data in staff_data:
            StaffMember.objects.get_or_create(name=data["name"], defaults=data)
        self.stdout.write(self.style.SUCCESS("Staff created"))

        # Testimonials
        testimonials_data = [
            {
                "parent_name": "Lisa W.",
                "child_age_at_time": "3 years old",
                "quote": "The Garden of Children has been such a blessing for our family. My daughter absolutely loves going every day, and I can see how much she's growing socially and creatively. The staff are incredibly caring and communicative.",
                "is_featured": True,
            },
            {
                "parent_name": "David & Priya K.",
                "child_age_at_time": "4 years old",
                "quote": "We looked at many daycares in Vancouver and this one stood out immediately. The environment is warm, the outdoor space is wonderful, and our son is so well prepared for kindergarten. Highly recommend!",
                "is_featured": True,
            },
            {
                "parent_name": "James T.",
                "child_age_at_time": "3.5 years old",
                "quote": "What I appreciate most is the genuine care the educators show. They know my child by name and by heart. The daily updates and photos help me feel connected even while I'm at work.",
                "is_featured": True,
            },
        ]
        for data in testimonials_data:
            Testimonial.objects.get_or_create(parent_name=data["parent_name"], defaults=data)
        self.stdout.write(self.style.SUCCESS("Testimonials created"))

        # Fees
        fees_data = [
            {"title": "Full-Time (5 days/week)", "age_group": "30 months – kindergarten", "amount": 1200, "period": "monthly", "description": "Monday to Friday, 7:00 AM – 6:00 PM", "order": 1},
            {"title": "Part-Time (3 days/week)", "age_group": "30 months – kindergarten", "amount": 850, "period": "monthly", "description": "Choose any 3 days per week", "order": 2},
            {"title": "Part-Time (2 days/week)", "age_group": "30 months – kindergarten", "amount": 600, "period": "monthly", "description": "Choose any 2 days per week", "order": 3},
            {"title": "Drop-In", "age_group": "30 months – kindergarten", "amount": 75, "period": "daily", "description": "Subject to availability", "order": 4},
        ]
        for data in fees_data:
            FeeItem.objects.get_or_create(title=data["title"], defaults=data)
        self.stdout.write(self.style.SUCCESS("Fees created"))

        # FAQs
        faqs_data = [
            {
                "question": "What ages do you accept?",
                "answer": "We accept children from 30 months (2.5 years) through to kindergarten age. Children must be at least 30 months old at the time of enrollment.",
                "order": 1,
            },
            {
                "question": "What are your hours of operation?",
                "answer": "We are open Monday through Friday from 7:00 AM to 6:00 PM. We are closed on statutory holidays and for two weeks during the winter holiday break.",
                "order": 2,
            },
            {
                "question": "Do you provide meals and snacks?",
                "answer": "Yes! We provide a morning snack, a nutritious lunch, and an afternoon snack daily. Our menu is balanced and allergy-conscious. Please let us know about any dietary restrictions or allergies when you enroll.",
                "order": 3,
            },
            {
                "question": "What is your child-to-staff ratio?",
                "answer": "We maintain low ratios that exceed BC licensing requirements. Our toddler room maintains a 4:1 ratio, and our preschool room maintains an 8:1 ratio, ensuring personalized attention for every child.",
                "order": 4,
            },
            {
                "question": "How can I enroll my child?",
                "answer": "Simply fill out the inquiry form on our Contact page or give us a call. We'll schedule a tour so you can see our space and meet the team. Once you decide we're the right fit, we'll walk you through the enrollment paperwork.",
                "order": 5,
            },
            {
                "question": "Is there outdoor play every day?",
                "answer": "Absolutely! We believe in the importance of outdoor play and nature connection. Children go outside at least twice a day, rain or shine (we are in Vancouver, after all!). Our outdoor space includes a garden, sandbox, climbing structures, and open play areas.",
                "order": 6,
            },
            {
                "question": "Are you licensed?",
                "answer": "Yes, we are fully licensed by the BC Ministry of Health through Community Care Facilities Licensing. All of our educators hold valid Early Childhood Education (ECE) certifications and current first aid training.",
                "order": 7,
            },
        ]
        for data in faqs_data:
            FAQ.objects.get_or_create(question=data["question"], defaults=data)
        self.stdout.write(self.style.SUCCESS("FAQs created"))

        self.stdout.write(self.style.SUCCESS("\nAll seed data created successfully!"))
