from django.contrib import admin
from .models import *



class InputSentenceInline(admin.StackedInline):
    # показывать текст предложений

    model = InputSentence
    extra = 1


class IntentAdmin(admin.ModelAdmin):
    # показывать входящие в интент предложение
    list_display = ('name', 'inner_sentences',)
    inlines = [InputSentenceInline, ]
    ordering = ('pk',)

class PairAdmin(admin.ModelAdmin):
    list_display = ('inner_intents','inner_responses',)
    pass


class DialogHistoryAdmin(admin.ModelAdmin):
    # просто отображать поля
    readonly_fields = ("chat_id", "text", "source", "date",)
    actions = None
    list_display = ('chat_id','text','source','date',)
    ordering = ('date',)


admin.site.register(Intent, IntentAdmin)
admin.site.register(Pair, PairAdmin)
admin.site.register(DialogHistory, DialogHistoryAdmin)
admin.site.register(Response)
# Register your models here.
