from django.core.checks import Error
from spacecrafts.components.models import Component
from asgiref.sync import sync_to_async
import logging


def example_check_main_engine(app_configs=None, **kwargs):
    '''
    Check for existance of the main engine in the database
    '''

    # your check logic here
    errors = []
    logging.info("Our check actully works!")
    # we need to wrap all sync calls to the database into a sync_to_async wrapper for hurricane to use it in async way
    if not sync_to_async(Component.objects.filter(title="Main engine").exists):
        errors.append(
            Error(
                'an error',
                hint='There is no main engine in the spacecraft.',
                id='components.E001',
            )
        )

    return errors
