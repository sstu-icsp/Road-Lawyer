from django.contrib import admin
from .models import*

class InputSentenceAdmin (admin.StackedInline):
    # показывать текст предложений
    fields = ("text",)
    model = InputSentence
    extra = 1

class IntentAdmin(admin.ModelAdmin):
    # показывать входящие в интент предложения
    inlines = [InputSentenceAdmin,]

class IntentInLine(admin.StackedInline):
    model = Intent
    extra = 1

class ResponseInLine (admin.StackedInline):
    # показывать текст ответа
    fields = ("text",)
    model = Pair
    extra = 1

class PairAdmin (admin.ModelAdmin):
# показывать связанные интенты и ответы
    inlines = [ResponseInLine,  IntentInLine,]

class DialogHistoryAdmin(admin.ModelAdmin):
    # просто отображать поля
    readonly_fields =("chat_id", "text","source","date",)
    actions = None

admin.site.register(Intent, IntentAdmin)
admin.site.register(Pair, PairAdmin)
admin.site.register(DialogHistory)
#admin.site.register(Users)
#admin.site.register(DisplayedMessages)
#admin.site.register(NotAnsweredMessage)
# Register your models here.
