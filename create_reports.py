client_id = "xxx"
scope = "xxx"

REPORT_CONFIGURATION_TEMPLATE = {
    "adProduct": "SPONSORED_PRODUCTS",
    "groupBy": ["advertiser"],
    "columns": [
            "startDate", "endDate", "campaignName", "campaignId", "adGroupName", "adGroupId", "adId",
            "portfolioId", "impressions", "clicks", "costPerClick", "clickThroughRate", "cost", "spend",
            "campaignBudgetCurrencyCode", "campaignBudgetAmount", "campaignBudgetType", "campaignStatus",
            "advertisedAsin", "advertisedSku", "purchases1d", "purchases7d", "purchases14d", "purchases30d",
            "purchasesSameSku1d", "purchasesSameSku7d", "purchasesSameSku14d", "purchasesSameSku30d",
            "unitsSoldClicks1d", "unitsSoldClicks7d", "unitsSoldClicks14d", "unitsSoldClicks30d", "sales1d",
            "sales7d", "sales14d", "sales30d", "attributedSalesSameSku1d", "attributedSalesSameSku7d",
            "attributedSalesSameSku14d", "attributedSalesSameSku30d", "salesOtherSku7d", "unitsSoldSameSku1d",
            "unitsSoldSameSku7d", "unitsSoldSameSku14d", "unitsSoldSameSku30d", "unitsSoldOtherSku7d",
            "kindleEditionNormalizedPagesRead14d", "kindleEditionNormalizedPagesRoyalties14d", "acosClicks7d",
            "acosClicks14d", "roasClicks7d", "roasClicks14d"
        ],
    "reportTypeId": "spAdvertisedProduct",
    "timeUnit": "SUMMARY",
    "format": "GZIP_JSON"
}
access_token = access_token
api = AmazonAPI(client_id, scope, access_token)
configuration = REPORT_CONFIGURATION_TEMPLATE.copy()

response = api.create_report('Report Name', '2023-10-01', '2023-10-30', configuration)
print(response)

report_id = response["reportId"]
status_response = api.get_report_status(report_id)
print(status_response["status"])


report_ids=[]
report_ids.append(report_id)
import time

reports_urls = []
