
from celery.task import task
import logging
from some_name.models import *
import random
logger = logging.getLogger(__name__)
#logging.getLogger().setLevel(logging.INFO)


from celery.task.schedules import crontab
from celery.decorators import periodic_task


@task(name='background_task')
def background_task():
    print('I am in Background Task')
    logger.info('some task is running')


@periodic_task(run_every=(crontab(minute='*/1')), name="periodic_background_task")
def periodic_background_task():
    logger.info('Periodic task executed')


@task(name="create_transaction")
def create_transaction():
    print("jfiqejqwijqif")
    Payment.objects.create(
        amount=random.randint(15, 15000),
        payment_id=str(random.randint(1, 100)),
        status=random.choice([True, None]),
        user=User.objects.all()[random.randint(0, User.objects.all().count()-1)]
    )
    logger.info('created transaction')
