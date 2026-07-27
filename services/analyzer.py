import pandas as pd


class BusinessAnalyzer:
    def __init__(self, deals_df: pd.DataFrame, work_orders_df: pd.DataFrame):
        self.deals = deals_df
        self.work_orders = work_orders_df

    def total_deals(self):
        return len(self.deals)

    def total_work_orders(self):
        return len(self.work_orders)

    def deals_by_status(self):
        return self.deals["deal_status"].value_counts(dropna=False).to_dict()

    def deals_by_stage(self):
        return self.deals["deal_stage"].value_counts(dropna=False).to_dict()

    def work_orders_by_status(self):
        return self.work_orders["execution_status"].value_counts(dropna=False).to_dict()

    def work_orders_by_sector(self):
        return self.work_orders["sector"].value_counts(dropna=False).to_dict()

    def summary(self):
        return {
            "total_deals": self.total_deals(),
            "total_work_orders": self.total_work_orders(),
            "deal_status": self.deals_by_status(),
            "deal_stage": self.deals_by_stage(),
            "execution_status": self.work_orders_by_status(),
            "sector_distribution": self.work_orders_by_sector(),
        }