from django.db import models


class Intent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        input_sentences = ", ".join(self.inputsentence_set.all())
        return "Response: [ sentences: {} ]".format(input_sentences)


class InputSentence(models.Model):
    text = models.CharField(max_length=150)
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)


class Response(models.Model):
    text = models.CharField(max_length=150)
    # article = models.ForeignKey(Article)

# #class IntentNode(models.Model):
#   nextNodes = models.PositiveIntegerField
#  flow = models.PositiveIntegerField
# node = models.ForeignKey(Flow)


# class Flow (models.Model):

class Pair(models.Model):
    list_respons = models.ManyToManyField(Response)
    intent = models.ManyToManyField(Intent)

# class Article(models.Model):
#   articleName = models.CharField(max_length=150)
#  articleText = models.TextField()


class Users(models.Model):
    name_user = models.CharField(max_length=60)
    #  userState = models.ForeignKey(UserState)


class DisplayedMessages(models.Model):
    user = models.ForeignKey(Users)
    adv_or_train = models.ForeignKey(Response)
    date_disp = models.DateField()



# class UserState(models.Model):
# flow
#  intent


class NotAnswerMessege(models.Model):
    user = models.ForeignKey(Users)
    text_answ = models.TextField()
    date_answ = models.DateField()
