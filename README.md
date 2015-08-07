# Simple Social Login
a django single page social login, using python-social-auth.


## Database Setup

In your **settings.py**, edit your **DATABASES** setting to your needs.
For some more information, follow this [link](https://docs.djangoproject.com/en/1.7/howto/legacy-databases/) or this [one](https://docs.djangoproject.com/en/1.8/intro/tutorial01/).
Here's an example:
<pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',  # Or path to database file if using sqlite3.
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}</code></pre>

Then open a terminal, set your working directory to the project's manage.py file and execute:
<pre><code>python manage.py migrate</code></pre>

In order to have access to your admin, you'll need to create a superuser:
<pre><code>./manage.py createsuperuser</code></pre>
If you want to learn more about this, click [here](https://docs.djangoproject.com/en/1.7/ref/django-admin/).


## Facebook Backend

Continuing on **settings.py**, seek for the Social Auth section.

Once there, edit **SOCIAL_AUTH_FACEBOOK_KEY** and **SOCIAL_AUTH_FACEBOOK_SECRET** with the App ID and App secret
that facebook will provide in your [dashboard](https://developers.facebook.com/) after you add an app for this purpose.

Still at your facebook app page, select **Settings**, right below **Dashboard**, and provide facebook with a valid email in *Contact Email*. 

Now, it is possible to enable *Do you want to make this app and all its live features available to the general public?*, which allows you to gather information about the user.
