# Generated by Django 2.0.1 on 2018-01-14 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('name_verbose', models.CharField(max_length=64, null=True)),
                ('name_coingecko', models.CharField(max_length=64, null=True)),
                ('algorithm', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('name_verbose', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeckoGeneralScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(auto_now_add=True)),
                ('price', models.FloatField(default=0)),
                ('cap', models.BigIntegerField(default=0)),
                ('liquidity', models.BigIntegerField(default=0)),
                ('rank', models.IntegerField()),
                ('developer', models.IntegerField(default=0)),
                ('community', models.IntegerField(default=0)),
                ('public', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pearl.Coin')),
            ],
        ),
        migrations.CreateModel(
            name='GeckoRepoMetrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(auto_now_add=True)),
                ('stars', models.IntegerField(default=0)),
                ('watchers', models.IntegerField(default=0)),
                ('forks', models.IntegerField(default=0)),
                ('pull_requests', models.IntegerField(default=0)),
                ('total_issues', models.IntegerField(default=0)),
                ('closed_issues', models.IntegerField(default=0)),
                ('contributors', models.IntegerField(default=0)),
                ('new_commits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=80, null=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pearl.Coin')),
            ],
        ),
        migrations.AddField(
            model_name='geckorepometrics',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pearl.Repo'),
        ),
        migrations.AddField(
            model_name='developer',
            name='repo',
            field=models.ManyToManyField(to='pearl.Repo'),
        ),
        migrations.AlterUniqueTogether(
            name='geckorepometrics',
            unique_together={('repo', 'created_time')},
        ),
        migrations.AlterUniqueTogether(
            name='geckogeneralscore',
            unique_together={('coin', 'created_time')},
        ),
    ]
