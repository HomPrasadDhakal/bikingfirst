# Generated by Django 2.2.2 on 2021-09-22 11:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutusDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('about_cover', models.FileField(upload_to='about_cover_image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.FileField(upload_to='trip_photos')),
                ('Itinerary', ckeditor.fields.RichTextField()),
                ('region', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('Availability', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField()),
                ('rating', models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'THREE'), ('4', 'FOUR'), ('5', 'FIVE')], max_length=25)),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('all_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.AllCategory')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Category')),
                ('inclusion', models.ManyToManyField(blank=True, related_name='package_inclusion', to='travel.Inclusion')),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, null=True)),
                ('image', models.FileField(upload_to='slider_image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PackagesGallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='packages/images')),
                ('packages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Packages')),
            ],
        ),
        migrations.AddField(
            model_name='packages',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.SubCategory'),
        ),
        migrations.CreateModel(
            name='BookPackages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=255)),
                ('no_of_adults', models.CharField(max_length=255)),
                ('no_of_children', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Packages')),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500)),
                ('content', ckeditor.fields.RichTextField()),
                ('cover_image', models.FileField(upload_to='blogs_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user')),
            ],
        ),
        migrations.AddField(
            model_name='allcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Category'),
        ),
        migrations.AddField(
            model_name='allcategory',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.SubCategory'),
        ),
    ]
