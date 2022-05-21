from django.contrib.sites.shortcuts import get_current_site


def request_domain(request):
    current_site = get_current_site(request)
    return current_site.domain
