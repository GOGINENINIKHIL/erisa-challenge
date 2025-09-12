from django.db import models
from django.contrib.auth.models import User

class Claim(models.Model):
    patient_name = models.CharField(max_length=255)
    billed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    insurer_name = models.CharField(max_length=255)
    discharge_date = models.DateField()

    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"Claim {self.id} for {self.patient_name}"

class ClaimDetail(models.Model):
    claim = models.OneToOneField(Claim, on_delete=models.CASCADE, related_name='details')
    cpt_codes = models.CharField(max_length=255) 
    denial_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Details for Claim {self.claim.id}"

class Note(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE, related_name='notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Note on Claim {self.claim.id} by {self.user.username}"