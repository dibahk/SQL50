import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity['timestamp'] = activity.apply(lambda x: x.timestamp * -1 if x.activity_type == 'start' else x.timestamp, axis=1)
    sum_time = activity.groupby(['machine_id', 'process_id'],  as_index=False).sum()
    avg_time = sum_time.groupby(['machine_id'], as_index= False)['timestamp'].mean().round(3).rename(columns={'timestamp':'processing_time'})
    return avg_time
        
