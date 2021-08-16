from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from datacenter.models import get_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    leaved_at = localtime(visit.leaved_at)

    return leaved_at and (duration // 60) > minutes


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for passcard_visit in passcard_visits:
        entered_at = localtime(passcard_visit.entered_at)
        duration = format_duration(get_duration(passcard_visit))
        is_strange = is_visit_long(passcard_visit)

        visit = {
            "entered_at": entered_at,
            "duration": duration,
            "is_strange": is_strange,
        }

        this_passcard_visits.append(visit)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits,
    }
    return render(request, "passcard_info.html", context)
