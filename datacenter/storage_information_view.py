from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render
from django.utils.timezone import localtime, now


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    location_time = now() - entered_at
    return int(location_time.total_seconds())


def storage_information_view(request):
    not_leaved_guards = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for not_leaved_guard in not_leaved_guards:
        who_entered = not_leaved_guard.passcard
        entered_at = localtime(not_leaved_guard.entered_at)
        duration = format_duration(get_duration(not_leaved_guard))

        visit = {
            "who_entered": who_entered,
            "entered_at": entered_at,
            "duration": duration,
        }

        non_closed_visits.append(dict(visit))

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
