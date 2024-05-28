from rest_framework import serializers
from dateutil.relativedelta import relativedelta

class FormattedDurationField(serializers.DurationField):
    def to_representation(self, value):
        days = value.days
        hours, remainder = divmod(value.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        duration_str = ""
        if days:
            duration_str += f"{days}d "
        if hours:
            duration_str += f"{hours}h "
        if minutes:
            duration_str += f"{minutes}m "
        if seconds:
            duration_str += f"{seconds}s"
        return duration_str.strip()