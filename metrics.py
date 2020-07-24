import pandas as pd

#todo - takes a few seconds to run, research what's written inefficiently
#todo - can just be one get_metrics function with type input

def get_ad_news_metrics(file, keyword):

    df = pd.read_csv(file, keep_default_na=False)

    entered = df.apply(lambda x: keyword in x['utm_source'], axis=1)
    weekly_optin = df.apply(lambda x: keyword in x['utm_source'] and x['second_optin'] == 'yes_news' and x['parenting_feed'] == 'yes', axis=1)
    monthly_optin = df.apply(lambda x: keyword in x['utm_source'] and x['second_optin'] == 'yes_news' and x['parenting_feed'] == 'yes_lite', axis=1)
    total_optin = df.apply(lambda x: keyword in x['utm_source'] and x['second_optin'] == 'yes_news', axis=1)
    nothanks_optin = df.apply(lambda x: keyword in x['utm_source'] and x['parenting_feed'] == 'superlite', axis=1)
    zip = df.apply(lambda x: keyword in x['utm_source'] and x['userstate'] != '', axis=1)
    unsub = df.apply(lambda x: keyword in x['utm_source'] and x['permission_status'] == 'no', axis=1)
    blocked = df.apply(lambda x: keyword in x['utm_source'] and x['status'] == 'blocked', axis=1)

    entered_num = len(entered[entered == True].index)
    weekly_optin_num = len(weekly_optin[weekly_optin == True].index)
    monthly_optin_num = len(monthly_optin[monthly_optin == True].index)
    total_optin_num = len(total_optin[total_optin == True].index)
    nothanks_optin_num = len(nothanks_optin[nothanks_optin == True].index)
    zip_num = len(zip[zip == True].index)
    unsub_num = len(unsub[unsub == True].index)
    blocked_num = len(blocked[blocked == True].index)

    metrics = {}
    metrics['entered'] = entered_num
    metrics['weekly_optin'] = weekly_optin_num
    metrics['monthly_optin'] = monthly_optin_num
    metrics['total_optin'] = total_optin_num
    metrics['nothanks_optin'] = nothanks_optin_num
    metrics['zip'] = zip_num
    metrics['unsub'] = unsub_num
    metrics['blocked'] = blocked_num

    return metrics



def get_ad_petition_metrics(file, keyword, petition_name):
    df = pd.read_csv(file, keep_default_na=False)
    #viral_str = 'viral_ad_petition_' + keyword
    #todo will have to update how file is exported to get viral sigs here

    entered = df.apply(lambda x: keyword in x['utm_source'], axis=1)
    signed = df.apply(lambda x: x[petition_name] == 'yes', axis=1)
    #viral_signed = df.apply(lambda x: x[petition_name] == 'yes' and viral_str in x['utm_source'], axis=1)
    zip = df.apply(lambda x: keyword in x['utm_source'] and x['userstate'] != '', axis=1)
    still_sub = unsub = df.apply(lambda x: keyword in x['utm_source'] and x['permission_status'] == 'yes' and x['status'] == 'reachable', axis=1)
    unsub = df.apply(lambda x: keyword in x['utm_source'] and x['permission_status'] == 'no', axis=1)
    blocked = df.apply(lambda x: keyword in x['utm_source'] and x['status'] == 'blocked', axis=1)

    entered_num = len(entered[entered == True].index)
    signed_num = len(signed[signed == True].index)
    #viral_signed_num = len(viral_signed[viral_signed == True].index)
    zip_num = len(zip[zip == True].index)
    still_sub_num = len(still_sub[still_sub == True].index)
    unsub_num = len(unsub[unsub == True].index)
    blocked_num = len(blocked[blocked == True].index)

    metrics = {}
    metrics['entered'] = entered_num
    metrics['signed'] = signed_num
    metrics['still subscribed'] = still_sub_num
    metrics['zip'] = zip_num
    metrics['unsub'] = unsub_num
    metrics['blocked'] = blocked_num

    return metrics




def get_ad_totals_metrics(file):
    df = pd.read_csv(file, keep_default_na=False)

    total_news_entered = df.apply(lambda x: 'ad_news_corona_' in x['utm_source'], axis=1)
    total_news_still_subscribed = df.apply(lambda x: 'ad_news_corona_' in x['utm_source'] and x['status'] == 'reachable' and x['permission_status'] == 'yes', axis=1)
    total_news_blocks = df.apply(lambda x: 'ad_news_corona_' in x['utm_source'] and x['status'] == 'blocked', axis=1)
    total_news_unsub = df.apply(lambda x: 'ad_news_corona_' in x['utm_source'] and x['permission_status'] == 'no',axis=1)

    total_news_entered_num = len(total_news_entered[total_news_entered == True].index)
    total_news_still_subscribed_num = len(total_news_still_subscribed[total_news_still_subscribed == True].index)
    total_news_blocks_num = len(total_news_blocks[total_news_blocks == True].index)
    total_news_unsub_num = len(total_news_unsub[total_news_unsub == True].index)

    metrics = {}
    metrics['total news entered'] = total_news_entered_num
    metrics['total news still subscribed'] = total_news_still_subscribed_num
    metrics['total news blocks'] = total_news_blocks_num
    metrics['total news unsub'] = total_news_unsub_num

    return metrics


def get_petition_metrics(file, keyword, saw_str, petition_name):

    df = pd.read_csv(file, keep_default_na=False) #keep_default_na is key or empty cells get NaN -> type errors
    share_str = keyword + '_ask_agreed'

    broadcast = df.apply(lambda x: keyword in x[saw_str], axis=1)
    broadcast_sig = df.apply(lambda x: keyword in x[saw_str] and x[petition_name] == 'yes', axis=1)
    total_sig = df.apply(lambda x: x[petition_name] == 'yes', axis=1)
    shared = df.apply(lambda x: keyword in x[saw_str] and x[petition_name] == 'yes' and share_str in x['test_attribute_10'], axis=1)
    viral_sig = df.apply(lambda x: keyword in x['utm_source'] and x[petition_name] == 'yes', axis=1)
    blocked = df.apply(lambda x: keyword in x[saw_str] and x['status'] == 'blocked', axis=1)
    unsub = df.apply(lambda x: keyword in x[saw_str] and x['permission_status'] == 'no', axis=1)
    soft_unsub = df.apply(lambda x: keyword in x[saw_str] and x['advocacy_feed'] == 'superlite', axis=1)
    remaining = df.apply(lambda x: keyword in x[saw_str] and x['permission_status'] == 'yes' and x['status'] == 'reachable', axis=1)

    broadcast_num = len(broadcast[broadcast == True].index)
    total_sig_num = len(total_sig[total_sig == True].index)
    broadcast_sig_num = len(broadcast_sig[broadcast_sig == True].index)
    shared_num = len(shared[shared == True].index)
    viral_sig_num = len(viral_sig[viral_sig == True].index)
    soft_unsub_num = len(soft_unsub[soft_unsub == True].index)
    unsub_num = len(unsub[unsub == True].index)
    blocked_num = len(blocked[blocked == True].index)
    remaining_num = len(remaining[remaining == True].index)

    metrics = {}
    metrics['broadcast'] = broadcast_num
    metrics['total sigs'] = total_sig_num
    metrics['broadcast sigs'] = broadcast_sig_num
    metrics['shared'] = shared_num
    metrics['viral sigs'] = viral_sig_num
    metrics['soft unsub'] = soft_unsub_num
    metrics['unsub'] = unsub_num
    metrics['blocked'] = blocked_num
    metrics['remaining'] = remaining_num

    return metrics
