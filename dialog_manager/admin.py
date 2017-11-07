from django.contrib import admin
from .models import *


class InputSentenceInline(admin.StackedInline):
    # показывать текст предложений
    model = InputSentence
    extra = 1


class IntentAdmin(admin.ModelAdmin):
    # показывать входящие в интент предложения
    inlines = [InputSentenceInline, ]


class PairAdmin(admin.ModelAdmin):
    pass


class DialogHistoryAdmin(admin.ModelAdmin):
    # просто отображать поля
    readonly_fields = ("chat_id", "text", "source", "date",)
    actions = None


admin.site.register(Intent, IntentAdmin)
admin.site.register(Pair, PairAdmin)
admin.site.register(DialogHistory, DialogHistoryAdmin)
# Register your models here.
