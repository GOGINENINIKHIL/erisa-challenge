from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.db.models import Count, Avg, F
from django.contrib.auth.decorators import login_required
from .models import Claim, Note
from django.contrib.auth.models import User

@login_required
def claim_list_view(request):
    query_status = request.GET.get('status', '')
    query_insurer = request.GET.get('insurer', '')

    claims_list = Claim.objects.all().order_by('id')
    if query_status:
        claims_list = claims_list.filter(status__iexact=query_status)
    if query_insurer:
        claims_list = claims_list.filter(insurer_name__icontains=query_insurer)

    paginator = Paginator(claims_list, 25)
    page_number = request.GET.get('page')
    claims_page = paginator.get_page(page_number)
    
    context = {
        'claims_page': claims_page,
        'selected_status': query_status,
        'selected_insurer': query_insurer
    }

    if 'HX-Request' in request.headers:
        return render(request, 'claims/partials/claim_results.html', context)
    
    context['statuses'] = Claim.objects.values_list('status', flat=True).distinct()
    context['insurers'] = Claim.objects.values_list('insurer_name', flat=True).distinct()
    return render(request, 'claims/claim_list.html', context)

@login_required
def claim_detail_view(request, pk):
    claim = get_object_or_404(Claim, pk=pk)
    context = {
        'claim': claim,
        'csrf_token_value': get_token(request)
    }
    return render(request, 'claims/partials/claim_detail.html', context)

def toggle_flag_view(request, pk):
    claim = get_object_or_404(Claim, pk=pk)
    if request.method == 'POST':
        claim.is_flagged = not claim.is_flagged
        claim.save()
    context = {'claim': claim}
    return render(request, 'claims/partials/flag_toggle_response.html', context)


def add_note_view(request, pk):
    claim = get_object_or_404(Claim, pk=pk)
    if request.method == 'POST':
        note_text = request.POST.get('note_text')
        if note_text:
            Note.objects.create(claim=claim, text=note_text, user=request.user)
    context = {'claim': claim}
    return render(request, 'claims/partials/notes_list.html', context)


def delete_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    claim = note.claim
    if request.method == 'POST':
        note.delete()
        context = {'claim': claim}
        return render(request, 'claims/partials/notes_list.html', context)
    return HttpResponse(status=405)

@login_required
def dashboard_view(request):
    total_flagged_claims = Claim.objects.filter(is_flagged=True).count()
    
    total_claims = Claim.objects.count()
    underpayment_stats = Claim.objects.aggregate(
        avg_underpayment=Avg(F('billed_amount') - F('paid_amount'))
    )
    average_underpayment = underpayment_stats.get('avg_underpayment', 0)

    context = {
        'total_flagged_claims': total_flagged_claims,
        'total_claims': total_claims,
        'average_underpayment': average_underpayment,
    }
    return render(request, 'claims/dashboard.html', context)