from __future__ import unicode_literals
# not sure yet exactly what this is!!

from django.contrib import admin
from blog.models import Post

# added from another tutorial
import datetime
import calendar
from django.core.urlresolvers import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe

class PostAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'text']
    change_list_template = 'blog/change_list.html'

admin.site.register(Post)
