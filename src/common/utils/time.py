from datetime import timedelta


def get_elapsed_time_with_message(
    elapsed_time: timedelta,
) -> tuple[int, str, str]:
    """
    Calculate the time elapsed since the object's creation.

    Returns a tuple containing three elements:
    - An integer representing the time elapsed
    - A string indicating the time unit (e.g., days, months)
    - A string message that describes the elapsed time
    """
    if elapsed_time.days >= 30:
        months = elapsed_time.days // 30
        return (
            months,
            'months',
            f'{months} month{"s" if months > 1 else ""} ago',
        )
    elif elapsed_time.days >= 1:
        return (
            elapsed_time.days,
            'days',
            f'{elapsed_time.days} day{"s" if elapsed_time.days > 1 else ""} ago',
        )
    elif elapsed_time.seconds >= 3600:
        hours = elapsed_time.seconds // 3600
        return (hours, 'hours', f'{hours} hour{"s" if hours > 1 else ""} ago')
    elif elapsed_time.seconds >= 60:
        minutes = elapsed_time.seconds // 60
        return (
            minutes,
            'minutes',
            f'{minutes} minute{"s" if minutes > 1 else ""} ago',
        )
    else:
        return (
            elapsed_time.seconds,
            'seconds',
            f'{elapsed_time.seconds} second{"s" if elapsed_time.seconds > 1 else ""} ago',
        )
