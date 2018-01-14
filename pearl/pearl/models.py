from django.db import models
from django.db.models import (
    CASCADE,
    Model,
)


class CurrentModel(Model):
    created_time = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Coin(Model):
    name = models.CharField(max_length=16)
    name_verbose = models.CharField(max_length=64, null=True)
    name_coingecko = models.CharField(max_length=64, null=True)
    algorithm = models.CharField(max_length=64, null=True)


class Repo(Model):
    coin = models.ForeignKey(Coin, on_delete=CASCADE)
    url = models.CharField(max_length=80, null=True)


class Developer(Model):
    repo = models.ManyToManyField(Repo)

    name = models.CharField(max_length=64, null=True)
    name_verbose = models.CharField(max_length=64, null=True)


#################################################################

class GeckoGeneralScore(CurrentModel):
    coin = models.ForeignKey(Coin, on_delete=CASCADE)

    price = models.FloatField(default=0)
    cap = models.BigIntegerField(default=0)
    liquidity = models.BigIntegerField(default=0)

    rank = models.IntegerField()
    developer = models.IntegerField(default=0)
    community = models.IntegerField(default=0)
    public = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    class Meta:
        unique_together = ('coin', 'created_time')


class GeckoRepoMetrics(CurrentModel):
    repo = models.ForeignKey(Repo, on_delete=CASCADE)

    stars = models.IntegerField(default=0)
    watchers = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    pull_requests = models.IntegerField(default=0)
    total_issues = models.IntegerField(default=0)
    closed_issues = models.IntegerField(default=0)
    contributors = models.IntegerField(default=0)
    new_commits = models.IntegerField(default=0)

    class Meta:
        unique_together = ('repo', 'created_time')
