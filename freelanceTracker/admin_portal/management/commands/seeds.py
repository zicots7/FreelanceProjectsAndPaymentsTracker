from datetime import timedelta, datetime
from Project.models import Project
from Milestone.models import Milestone
from Payment.models import Payment
from accounts.models import Customer
from Logs.mongoDB import collection
from Client.models import Client
from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
from django.core.management import BaseCommand
import random

from django.contrib.auth import get_user_model


# 2. Initialize Django

Customer = get_user_model()
fake = Faker('en_IN')


class Command(BaseCommand):
    help = "Seeds SQL and MongoDB with Indian client data based on provided models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning existing data...")
        collection.delete_many({})
        Payment.objects.all().delete()
        Milestone.objects.all().delete()
        Project.objects.all().delete()
        Client.objects.all().delete()
        Customer.objects.filter(role='client').delete()

        self.stdout.write("Generating data...")

        for _ in range(12):
            # 1. Create Customer (User)
            f_name = fake.first_name()
            l_name = fake.last_name()
            user = Customer.objects.create_user(
                username=f"{f_name.lower()}_{random.randint(100, 999)}",
                email=fake.unique.email(),
                password="password123",
                role='client'
            )

            # 2. Create Client Profile
            client = Client.objects.create(
                user=user,
                first_name=f_name,
                last_name=l_name,
                email=user.email,
                platform=random.choice(["Fiverr", "Upwork", "Direct"]),
                company=fake.company(),
                added_date=timezone.now()
            )

            # 3. Create Projects
            for _ in range(random.randint(2, 3)):
                start = fake.date_between(start_date='-1y', end_date='today')
                val = random.randint(15000, 100000)
                project = Project.objects.create(
                    title=random.choice(["REST API Dev", "Flask Dashboard", "Portfolio Site"]),
                    client=client,
                    description=fake.sentence(nb_words=12),
                    start_date=start,
                    deadline=start + timedelta(days=45),
                    status=random.choice(["Complete", "Pending", "Delivered"]),
                    total_value=val
                )

                # 4. Create Milestones
                num_milestones = random.randint(3, 4)
                for i in range(num_milestones):
                    is_paid = random.choice(["Yes", "No"])
                    milestone_amt = val // num_milestones

                    milestone = Milestone.objects.create(
                        project_name=project,
                        description=f"Phase {i + 1} implementation",
                        amount=milestone_amt,
                        due_date=project.deadline,
                        is_paid=is_paid
                    )

                    # 5. Create Payment
                    if is_paid == "Yes":
                        Payment.objects.create(
                            milestone=milestone,
                            amount_paid=milestone_amt,
                            date_paid=fake.date_this_month(),
                            payment_method=random.choice(["UPI", "CARD", "NET BANKING"])
                        )

                # 6. MongoDB Interaction Logs
                self.seed_mongo_log(project.Pid)

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))

    def seed_mongo_log(self, project_id):
        interaction_type = random.choice(['revision_request', 'contract', 'requirement', 'general_note'])

        log_entry = {
            "log_id": fake.uuid4(),
            "project_id": project_id,
            "messages": fake.sentence(),
            "timestamp": datetime.now(),
            "tags": "development,feedback",
            "interaction_type": interaction_type,
        }

        if interaction_type == "revision_request":
            log_entry["details"] = {
                "message": "Please change the brand colors",
                "revision_number": random.randint(1, 3),
                "affected_pages": ["Landing", "Contact"],
                "priority": "High"
            }
        elif interaction_type == 'contract':
            log_entry['details'] = {
                "contract_value": str(random.randint(20000, 50000)),
                "payment_terms": "Net-15",
                "deliverables": ["Codebase", "Video Tutorial"],
                "signed_date": str(datetime.now().date()),
            }
        elif interaction_type == 'requirement':
            log_entry['details'] = {
                "description": "Needs AWS integration",
                "tech_preference": "Python/Django",
                "budget_flexible": random.choice([True, False]),
                "deadline_flexible": True,
            }
        else:  # general_note
            log_entry['details'] = {
                "message": "Client requested a call next Monday",
                "tags": ["call", "follow-up"]
            }

        collection.insert_one(log_entry)