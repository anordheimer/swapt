from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_swaptadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]