from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('classroom', 'Subject')
    Subject.objects.create(name='Завдання 1 клас', color='#343a40')
    Subject.objects.create(name='Завдання 2 клас', color='#007bff')
    Subject.objects.create(name='Завдання 3 клас', color='#28a745')
    Subject.objects.create(name='Завдання 4 клас', color='#17a2b8')
    Subject.objects.create(name='Завдання 5 клас', color='#ffc107')


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]
