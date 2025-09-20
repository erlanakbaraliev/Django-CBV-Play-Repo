from django.db.models import Count
from django.views.generic import ListView, TemplateView
import datetime

from dmx_admin.models import MfiSsaRmlException

# class DmxAdminHomeView(TemplateView):
#     template_name = 'dmx_admin/dmx_admin_home.html'

#     def get_context_data(self, )


class DmxAdminSummaryView(ListView):
    template_name = 'dmx_admin/dmx_admin_summary_list.html'

    def get_queryset(self):
        queryset = MfiSsaRmlException.objects.filter(universe_date=datetime.datetime(2025,9,3)).values('error_descr', 'error_code').annotate(error_count=Count("error_descr")).order_by("error_count")
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parentParams'] = self.request.GET.urlencode()
        context['columns'] = ['Error Descr', 'Error Count']
        return context
