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


def name_to_subdomain(name: str) -> str:
    """
    Takes a name and strips it down to just a valid subdomain.
    """
    name = name.lower()

    # Strip non-alphanumeric or dash
    name = "".join([x for x in name if x.isalpha() or x.isnumeric() or x == "-"])

    return name
