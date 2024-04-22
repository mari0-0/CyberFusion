from celery import shared_task
from saa import cyberFusion
import time

@shared_task
def runCyberFusion():
    cyberFusion()
