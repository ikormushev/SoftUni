from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    INFLUENCER_TYPES = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    CAMPAIGN_TYPES = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            influencer = next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            self.influencers.append(self.INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate))
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:
            self.campaigns.append(self.CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement))
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = None
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        campaign = None
        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the "
                    f"eligibility criteria for the campaign with ID {campaign_id}.")

        if influencer.calculate_payment(campaign) > 0:
            influencer.campaigns_participated.append(campaign)
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment(campaign)
            return (f"Influencer '{influencer_username}' has successfully "
                    f"participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        campaign_dictionary = {}
        for campaign in self.campaigns:
            followers_sum = sum([y.reached_followers(campaign.__class__.__name__)
                                                 for y in campaign.approved_influencers])
            if followers_sum:
                campaign_dictionary[campaign] = followers_sum

        return campaign_dictionary

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda i: i.username == username, self.influencers))
        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = list(sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget)))
        result = "$$ Campaign Statistics $$\n"
        for campaign in sorted_campaigns:
            result += (f"  * Brand: {campaign.brand}, "
                       f"Total influencers: {len(campaign.approved_influencers)}, "
                       f"Total budget: ${campaign.budget:.2f}, ")
            if campaign in self.calculate_total_reached_followers():
                result += f"Total reached followers: {self.calculate_total_reached_followers()[campaign]}\n"
            else:
                result += "Total reached followers: 0\n"

        return result[:-1]

