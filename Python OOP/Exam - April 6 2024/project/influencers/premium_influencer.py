from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    CAMPAIGNS_MULTIPLIERS = {"HighBudgetCampaign": 1.5, "LowBudgetCampaign": 0.8}

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * 0.85

    def reached_followers(self, campaign_type: str):
        if campaign_type in self.CAMPAIGNS_MULTIPLIERS:
            return int(self.followers * self.engagement_rate * self.CAMPAIGNS_MULTIPLIERS[campaign_type])
