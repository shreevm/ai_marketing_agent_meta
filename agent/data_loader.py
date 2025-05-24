
from agent.meta_loader import fetch_meta_ads_data

def load_all_ad_data():
    meta_docs = fetch_meta_ads_data()
    return meta_docs
