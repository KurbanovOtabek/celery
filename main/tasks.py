from celery import shared_task
import requests as r
import uuid
from django.conf import settings

CAT_URL = "https://cataas.com/cat"


@shared_task
def download_a_cat():
    resp = r.get(CAT_URL)
    file_exp = resp.headers.get('Content-Type').split('/')[1]
    file_name = settings.BASE_DIR / 'cats' / (str(uuid.uuid4()) + "." + file_exp)
    with open(file_name, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=128):
            f.write(chunk)
    return True
