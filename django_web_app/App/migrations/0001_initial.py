# Generated by Django 3.1.2 on 2021-04-06 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ChestPain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Electrocardiographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='St_segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ThalliumResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Paitent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=3)),
                ('blood_pressure', models.IntegerField(max_length=3)),
                ('cholestorol', models.IntegerField(max_length=3)),
                ('blood_sugar', models.IntegerField(max_length=3)),
                ('heart_rate', models.IntegerField(max_length=3)),
                ('st_depression', models.FloatField(max_length=5)),
                ('vessels', models.IntegerField(max_length=2)),
                ('angina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.angina')),
                ('chest_pain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.chestpain')),
                ('electrocardiographic_resulter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.electrocardiographic')),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.sex')),
                ('st_segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.st_segment')),
                ('thallium_test_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.thalliumresult')),
            ],
        ),
    ]
