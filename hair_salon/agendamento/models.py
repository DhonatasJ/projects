from django.db import models

class Topics(models.Model):
    topic = models.CharField(max_length=20)

    def __str__(self):
        return self.topic
    

class Options(models.Model):
    option = models.CharField(max_length=20)

    def __str__(self):
        return self.option


class Relation_tpc_opt(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    option = models.ForeignKey(Options, on_delete=models.CASCADE)
