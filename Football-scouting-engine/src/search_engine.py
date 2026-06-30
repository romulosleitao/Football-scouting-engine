import pandas as pd

class SearchEngine:
    def __init__(self,data_frame):
        self.data_frame = data_frame

    def apply_filters (self, user_choices):
        for metric_name, min_value in user_choices.items():
            mask = self.data_frame[metric_name] >= min_value
            self.data_frame = self.data_frame[mask]
        return self.data_frame

    def sort_results (self, sort_by, ascending = False):
        self.data_frame = self.data_frame.sort_values(
            sort_by, ascending = ascending)
        return self.data_frame

    def get_summary (self):
        return self.data_frame.head()
