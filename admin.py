from django.contrib import admin
from .models import Articles, CustomUser, TV, Twitch, Telegram, VK, YouTube

admin.site.register(CustomUser)
admin.site.register(Articles)
admin.site.register(TV)
admin.site.register(Twitch)
admin.site.register(Telegram)
admin.site.register(VK)
admin.site.register(YouTube)

