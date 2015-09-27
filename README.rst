=====================
djangocms-fbcomments
=====================

.. image:: http://img.shields.io/travis/mishbahr/djangocms-fbcomments.svg?style=flat-square
    :target: https://travis-ci.org/mishbahr/djangocms-fbcomments/

.. image:: http://img.shields.io/pypi/v/djangocms-fbcomments.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-fbcomments/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/dm/djangocms-fbcomments.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-fbcomments/
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/djangocms-fbcomments.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-fbcomments/
    :alt: License

.. image:: http://img.shields.io/coveralls/mishbahr/djangocms-fbcomments.svg?style=flat-square
  :target: https://coveralls.io/r/mishbahr/djangocms-fbcomments?branch=master

The easiest way to integrate Facebook Comments for your django-cms powered site with lazy-loading, analytics and more.


Quickstart
----------

1. Install ``djangocms-fbcomments``::

    pip install djangocms-fbcomments

2. Add ``djangocms_fbcomments`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'djangocms_fbcomments',
        ...
    )

3. Sync database (requires south>=1.0.1 if you are using Django 1.6.x)::

    python manage.py migrate

4. To use the facebook moderation tool, you must include the following ``sekizai`` block in the ``<head>`` section of every template in which you want to use the comments plugin::

    {% load sekizai_tags %}

    <html>
        <head>
            {% render_block "meta" %}
        </head>
        <body>
        </body>
    </html>


Preview
-------

.. image:: http://mishbahr.github.io/assets/djangocms-fbcomments/thumbnail/djangocms-fbcomments-001.png
  :target: http://mishbahr.github.io/assets/djangocms-fbcomments/djangocms-fbcomments-001.png
  :width: 760px
  :align: center


.. image:: http://mishbahr.github.io/assets/djangocms-fbcomments/thumbnail/djangocms-fbcomments-002.png
  :target: http://mishbahr.github.io/assets/djangocms-fbcomments/djangocms-fbcomments-002.png
  :width: 760px
  :align: center
