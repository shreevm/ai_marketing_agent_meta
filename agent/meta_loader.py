from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import os
from dotenv import load_dotenv
from langchain_core.documents import Document  # Use langchain_core with newer versions

load_dotenv()

def fetch_meta_ads_data():
    access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
    ad_account_id = f"act_{os.getenv('FACEBOOK_AD_ACCOUNT_ID')}"

    FacebookAdsApi.init(access_token=access_token)
    account = AdAccount(ad_account_id)

    insights = account.get_insights(fields=["clicks", "impressions", "ctr"])

    docs = []
    for insight in insights:
        doc = f"Meta Ad Insights: Clicks: {insight.get('clicks', '0')}, Impressions: {insight.get('impressions', '0')}, CTR: {insight.get('ctr', '0')}"
        docs.append(Document(page_content=doc))

    return docs
