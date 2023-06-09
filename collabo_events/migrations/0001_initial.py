# Generated by Django 2.0.7 on 2019-04-25 10:59

import collabo_events.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import places.fields
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_operator', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=collabo_events.models.user_directory_artist)),
                ('slug', models.SlugField(max_length=100)),
                ('fb_followers', models.IntegerField(blank=True, null=True)),
                ('inst_followers', models.IntegerField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('about', tinymce.models.HTMLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30, verbose_name='Photo Title')),
                ('upload', models.FileField(upload_to=collabo_events.models.user_directory_path_artistimage, verbose_name='Upload Photo')),
            ],
            options={
                'verbose_name_plural': 'Artists Photos',
            },
        ),
        migrations.CreateModel(
            name='ArtistSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30, verbose_name='Song Title')),
                ('upload', models.URLField(blank=True, null=True, verbose_name='Paste Url')),
            ],
            options={
                'verbose_name_plural': 'Artists Songs',
            },
        ),
        migrations.CreateModel(
            name='ButtonText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Button Text',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('upload', models.ImageField(upload_to=collabo_events.models.user_directory_path_category)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(choices=[('VDO', 'Video'), ('IMG', 'Image')], default='IMG', max_length=128)),
                ('category_name', models.CharField(max_length=30)),
                ('upload', models.FileField(upload_to=collabo_events.models.user_directory_path_categoryimage)),
            ],
            options={
                'verbose_name_plural': 'Category Image',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('short_name', models.CharField(blank=True, max_length=30, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('host_details', tinymce.models.HTMLField(blank=True, null=True)),
                ('itinerary', tinymce.models.HTMLField(blank=True, null=True)),
                ('cancellation_policy', tinymce.models.HTMLField(blank=True, null=True)),
                ('booking_type', models.CharField(choices=[('B', 'Bookable'), ('NB', 'External/Non-Bookable'), ('P', 'Promotion/URL')], default='B', max_length=128)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('image_original', models.FileField(default='', upload_to='Events/1556189949/', verbose_name='original file upload')),
                ('image_medium', models.CharField(blank=True, max_length=255)),
                ('image_thumb', models.CharField(blank=True, max_length=255)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('ticket_type', models.CharField(choices=[('S', 'Single Ticket'), ('M', 'Multiple Ticket')], default='S', max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Promotion Events',
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True)),
                ('weight', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Promotion Category',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('item_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField(max_length=90)),
                ('item_price', models.FloatField()),
                ('upload', models.FileField(upload_to=collabo_events.models.user_directory_path)),
                ('tax', models.PositiveIntegerField(blank=True, default=2)),
                ('discounted_price', models.FloatField(blank=True, null=True)),
                ('discount_rate', models.PositiveIntegerField(blank=True, default=0)),
                ('duration', models.DurationField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Sub Category',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('genre', models.ManyToManyField(to='collabo_events.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OfferGeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('goal', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', places.fields.PlacesField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Price_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('false_price', models.FloatField(default=0.0)),
                ('max_size', models.IntegerField(blank=True, null=True)),
                ('additional_charge', models.FloatField(default=0.0)),
                ('additional_charge_label', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RoutePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', places.fields.PlacesField(max_length=255)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collabo_events.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Seo_Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(max_length=30)),
                ('seo_keyword', models.CharField(max_length=30)),
                ('seo_description', models.TextField(blank=True, max_length=100, null=True)),
                ('footer_title', models.CharField(max_length=30)),
                ('footer_type', models.CharField(choices=[('I', 'Internal'), ('E', 'External')], default='I', max_length=32)),
                ('footer_url', models.URLField(blank=True, max_length=100, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='collabo_events.City')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('max_size', models.PositiveIntegerField(default=1000)),
            ],
            options={
                'verbose_name': 'SLOT',
                'verbose_name_plural': 'SLOTS',
            },
        ),
        migrations.CreateModel(
            name='SlotPC',
            fields=[
                ('booked_seats', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('remaining_seats', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('limitCategory', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('limitSlot', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('totalSlot', models.PositiveIntegerField(default=0)),
                ('seating_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slot_event', to='collabo_events.Event')),
                ('price_cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='collabo_events.Price_Category')),
                ('slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='collabo_events.Slot')),
            ],
            options={
                'verbose_name_plural': 'SLOTPC',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Venue Type',
            },
        ),
        migrations.CreateModel(
            name='Venue1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', places.fields.PlacesField(blank=True, max_length=255)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('label', models.TextField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(max_length=100)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('about', tinymce.models.HTMLField(blank=True, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='venue1', to='collabo_events.City')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venue1', to='collabo_events.Type')),
            ],
            options={
                'verbose_name_plural': 'Venue',
            },
        ),
        migrations.CreateModel(
            name='VImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(blank=True, max_length=30)),
                ('upload', models.FileField(upload_to=collabo_events.models.user_directory_path_venueimage)),
            ],
            options={
                'verbose_name_plural': 'Venue Photos',
            },
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='venue1',
            name='upload',
            field=models.ManyToManyField(blank=True, related_name='venue1', to='collabo_events.VImage', verbose_name='Venue Photos'),
        ),
        migrations.AddField(
            model_name='offer',
            name='geo',
            field=models.ManyToManyField(related_name='offers', to='collabo_events.OfferGeo'),
        ),
        migrations.AddField(
            model_name='event',
            name='address_venue',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collabo_events.Venue1'),
        ),
        migrations.AddField(
            model_name='event',
            name='artists',
            field=models.ManyToManyField(related_name='events', to='collabo_events.Artist', verbose_name='Artists Name'),
        ),
        migrations.AddField(
            model_name='event',
            name='button_text',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='collabo_events.ButtonText'),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='collabo_events.EventCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='categoryImage',
            field=models.ManyToManyField(related_name='events', to='collabo_events.CategoryImage', verbose_name='Category Image'),
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='collabo_events.City'),
        ),
        migrations.AddField(
            model_name='event',
            name='pricing_category',
            field=models.ManyToManyField(related_name='events', to='collabo_events.Price_Category'),
        ),
        migrations.AddField(
            model_name='event',
            name='slots',
            field=models.ManyToManyField(related_name='events', to='collabo_events.Slot', verbose_name='Slot time'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='collabo_events.State'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_items',
            field=models.ManyToManyField(to='collabo_events.item'),
        ),
        migrations.AddField(
            model_name='artist',
            name='artistImage',
            field=models.ManyToManyField(related_name='atrists', to='collabo_events.ArtistImage', verbose_name='Artists Photos and videos'),
        ),
        migrations.AddField(
            model_name='artist',
            name='artistSong',
            field=models.ManyToManyField(related_name='artists', to='collabo_events.ArtistSong', verbose_name='ArtistSong'),
        ),
        migrations.AddField(
            model_name='artist',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artist', to='collabo_events.City'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collabo_events.Owners'),
        ),
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collabo_events.Owners'),
        ),
    ]
