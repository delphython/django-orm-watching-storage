from django.db import models
from django.utils.timezone import localtime


def format_duration(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    return "%02d:%02d" % (hours, minutes)


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at)
    location_time = leaved_at - entered_at
    return int(location_time.total_seconds())


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
