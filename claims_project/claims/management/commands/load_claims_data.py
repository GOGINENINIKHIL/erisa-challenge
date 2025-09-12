# claims/management/commands/load_claims_data.py
import csv
from django.core.management.base import BaseCommand
from claims.models import Claim, ClaimDetail
from datetime import datetime

class Command(BaseCommand):
    help = 'Loads data from CSV files into the database'

    def handle(self, *args, **options):
        # Clear existing data to prevent duplicates on re-runs
        Claim.objects.all().delete()
        self.stdout.write("Cleared existing claim data.")

        # --- Load Claim List Data ---
        try:
            with open('data/claim_list_data.csv', 'r') as file:
                # IMPORTANT: Specify the pipe delimiter
                reader = csv.DictReader(file, delimiter='|')
                for row in reader:
                    Claim.objects.create(
                        id=row['id'],
                        patient_name=row['patient_name'],
                        billed_amount=row['billed_amount'],
                        paid_amount=row['paid_amount'],
                        status=row['status'],
                        insurer_name=row['insurer_name'],
                        discharge_date=datetime.strptime(row['discharge_date'], '%Y-%m-%d').date()
                    )
            self.stdout.write(self.style.SUCCESS('Successfully loaded claim list data.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found: data/claim_list_data.csv'))
            return

        # --- Load Claim Detail Data ---
        try:
            with open('data/claim_detail_data.csv', 'r') as file:
                # IMPORTANT: Specify the pipe delimiter
                reader = csv.DictReader(file, delimiter='|')
                for row in reader:
                    # Find the parent Claim object
                    try:
                        parent_claim = Claim.objects.get(id=row['claim_id'])
                        ClaimDetail.objects.create(
                            id=row['id'],
                            claim=parent_claim,
                            cpt_codes=row['cpt_codes'],
                            denial_reason=row['denial_reason']
                        )
                    except Claim.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f"Claim with id={row['claim_id']} not found. Skipping detail record."))
            self.stdout.write(self.style.SUCCESS('Successfully loaded claim detail data.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found: data/claim_detail_data.csv'))