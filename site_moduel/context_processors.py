from .models import SiteSetting


def site_settings(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    return {'site_setting': setting}