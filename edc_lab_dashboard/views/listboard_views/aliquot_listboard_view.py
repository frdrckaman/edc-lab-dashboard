from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ...model_wrappers import AliquotModelWrapper
from ..listboard_filters import AliquotListboardViewFilters
from .base_listboard_view import BaseListboardView

edc_lab_app_config = django_apps.get_app_config('edc_lab')


class AliquotListboardView(BaseListboardView):

    navbar_selected_item = 'aliquot'
    model = edc_lab_app_config.aliquot_model
    model_wrapper_cls = AliquotModelWrapper
    listboard_url = 'aliquot_listboard_url'
    listboard_template = 'aliquot_listboard_template'
    show_all = True
    listboard_view_filters = AliquotListboardViewFilters()
    form_action_url = 'aliquot_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
