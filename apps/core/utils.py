from django.conf import settings


def get_name_from_host(host: str) -> str:
    """
    Returns a titled name from a URL host.
    """
    # Strip port if it's there
    name = host.split(":")[0]
    
    # Strip domain suffix
    name = name.replace(settings.DOMAIN_SUFFIX, "")

    return name.title()
