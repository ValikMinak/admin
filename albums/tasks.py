import requests

from io import BytesIO

from admin.celery import app
from items.models import Image
from PIL import Image as pil_image
from django.core.files import File


@app.task
def get_image(url, pk):
    # print(dir(response))  show response methods

    response = requests.get(url).content
    with open('comic.png', 'wb') as f:
        f.write(response)

    res_image = pil_image.open(BytesIO(response)).size
    Image.objects.filter(pk=pk).update(image_width=res_image[1], image_height=res_image[0],
                                       image=File(open('media/photos/comic.png', 'r')))
