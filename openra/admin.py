from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from openra.models import Maps
from openra.models import MapCategories
from openra.models import Lints
from openra.models import Screenshots
from openra.models import Reports
from openra.models import Rating
from openra.models import Comments
from openra.models import UnsubscribeComments

admin.site.register(MapCategories)

class MapsAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted'
    list_display = ('map_hash', 'title', 'user', 'posted', 'game_mod', 'amount_reports', 'mapformat', 'parser', 'advanced_map', 'lua', 'downloading')
    list_filter = ('game_mod', 'mapformat', 'advanced_map', 'lua')
admin.site.register(Maps, MapsAdmin)

class UnsubscribeCommentsAdmin(admin.ModelAdmin):
    date_hierarchy = 'unsubscribed'
    list_display = ('item_id', 'user', 'unsubscribed')
admin.site.register(UnsubscribeComments, UnsubscribeCommentsAdmin)

class CommentsAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted'
    list_display = ('item_id', 'user', 'posted', 'content', 'item_type', 'is_removed')
admin.site.register(Comments, CommentsAdmin)

class LintsAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted'
    list_display = ('map_id', 'version_tag', 'posted', 'pass_status')
    list_filter = ('pass_status',)
admin.site.register(Lints, LintsAdmin)

class ReportsAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted'
    list_display = ('ex_id', 'user', 'posted', 'reason', 'infringement')
    list_filter = ('infringement',)
admin.site.register(Reports, ReportsAdmin)

class RatingAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted'
    list_display = ('ex_id', 'user', 'posted', 'rating')
admin.site.register(Rating, RatingAdmin)

class ScreenshotsAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted'
    list_display = ('ex_id', 'user', 'posted', 'map_preview')
admin.site.register(Screenshots, ScreenshotsAdmin)

# Add the registration date to the user list
UserAdmin.list_display = list(UserAdmin.list_display) + ['date_joined']
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
