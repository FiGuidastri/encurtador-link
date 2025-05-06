import string
import random
from models.url_model import save_url, get_original_url

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(original_url):
    short_id = generate_short_id()
    save_url(short_id, original_url)
    return short_id

def resolve_short_url(short_id):
    return get_original_url(short_id)

