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
