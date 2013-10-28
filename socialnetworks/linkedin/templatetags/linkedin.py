from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


register = template.Library()


@register.simple_tag(takes_context=True)
def facebook_login(context, label=None, css_class=None, icon_class=None):
    """
    Renders a 'Sign in with LinkedIn' button.

    """
    context['label'] = label or _('Sign in with LinkedIn')
    context['action'] = reverse('socialnetworks:linkedin:login')
    context['css_class'] = css_class
    context['icon_class'] = icon_class

    return template.loader.render_to_string(
        'linkedin/login_button.html', context)
