import datetime

from django.utils.safestring import mark_safe

def get_color():
    today = datetime.date.today().day
    if today % 2 == 0:
        return "bleu"
    else:
        return "rouge"


def get_random_image():
    url = "https://www.google.com/search?q=random+image&rlz=1C1GCEA_enUS832US832&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiA_4OzvMzjAhUJyDgGHcS9BPQQ_AUIEigB&biw=1366&bih=657"
    return url


def get_table_data():
    name = "Alexandre"
    color = get_color()
    image_url = get_random_image()
    html = f"<span style='color:{color}'>{color}</span>"
    image_html = f"<img src='{image_url}' width='100'>"
    
    context = {
        "name": "Jean"
    }
    return context