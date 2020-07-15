import pandas as pd
#todo - takes a few seconds to run, research what's written inefficiently
#todo - can just be one get_metrics function with type input

def get_ad_metrics(file, keyword):

    #todo - this only works for news ads. Add functionality for petition ads and type arguments to differentiate
    #todo - add functionality to get total news ad entrants
    #todo - add functionality to get total still subscribed (ps + s) from all news and all petition ads
    #todo - add functionality for total blocks and total unsubs from all petition and all news ads.
    #todo - would a list of keywords be better since there's usually 10+ ads?
    df = pd.read_csv(file, keep_default_na=False)

    entered = df.apply(lambda x: keyword in x['utm_source'], axis=1)
    weekly_optin = df.apply(lambda x: keyword in x['utm_source'] and x['second_optin'] == 'yes_news' and x['parenting_feed'] == 'yes', axis=1)
    monthly_optin = total_optin = df.apply(lambda x: keyword in x['utm_source'] and x['second_optin'] == 'yes_news' and x['parenting_feed'] == 'yes_lite', axis=1)
    total_optin = df.apply(lambda x: keyword in x['utm_source'] and x['second_optin'] == 'yes_news', axis=1)
    nothanks_optin = df.apply(lambda x: keyword in x['utm_source'] and x['parenting_feed'] == 'superlite', axis=1)
    zip = df.apply(lambda x: keyword in x['utm_source'] and x['userstate'] != '', axis=1)
    unsub = df.apply(lambda x: keyword in x['utm_source'] and x['permission_status'] == 'no', axis=1)
    blocked = df.apply(lambda x: keyword in x['utm_source'] and x['status'] == 'blocked', axis=1)
    #todo - these don't need to show every time. Add totals type
    total_news_entered = df.apply(lambda x: 'ad_news_corona_' in x['utm_source'], axis=1)
    total_news_still_subscribed = df.apply(lambda x: x['status'] == 'reachable' and x['permission_status'] == 'yes', axis=1)
    total_news_blocks = df.apply(lambda x: 'ad_news_corona_' in x['utm_source'] and x['status'] == 'blocked', axis=1)
    total_news_unsub = df.apply(lambda x: 'ad_news_corona_' in x['utm_source'] and x['permission_status'] == 'no', axis=1)
    total_petition_entered = df.apply(lambda x: 'ad_petition' in x['utm_source'], axis=1)

    entered_num = len(entered[entered == True].index)
    weekly_optin_num = len(weekly_optin[weekly_optin == True].index)
    monthly_optin_num = len(monthly_optin[monthly_optin == True].index)
    total_optin_num = len(total_optin[total_optin == True].index)
    nothanks_optin_num = len(nothanks_optin[nothanks_optin == True].index)
    zip_num = len(zip[zip == True].index)
    unsub_num = len(unsub[unsub == True].index)
    blocked_num = len(blocked[blocked == True].index)
    total_news_entered_num = len(total_news_entered[total_news_entered == True].index)
    total_news_still_subscribed_num = len(total_news_still_subscribed[total_news_still_subscribed == True].index)
    total_news_blocks_num = len(total_news_blocks[total_news_blocks == True].index)
    total_news_unsub_num = len(total_news_unsub[total_news_unsub == True].index)
    total_petition_entered_num = len(total_petition_entered[total_petition_entered == True].index)

    print('entered = ', entered_num, '\n')
    print('weekly optin = ', weekly_optin_num, '\n')
    print('monthly optin = ', monthly_optin_num, '\n')
    print('total optin = ', total_optin_num, '\n')
    print('nothanks optin = ', nothanks_optin_num, '\n')
    print('zip num = ', zip_num, '\n')
    print('unsub num = ', unsub_num, '\n')
    print('blocked num = ', blocked_num, '\n')
    print('total news entered = ', total_news_entered_num, '\n')
    print('total news still subscribed = ', total_news_still_subscribed_num, '\n')
    print('total news blocks = ', total_news_blocks_num, '\n')
    print('total news unsub = ', total_news_unsub_num, '\n')
    print('total petition entered = ', total_petition_entered_num, '\n')


def get_petition_metrics(file, keyword, saw_attribute, petition_name):

    df = pd.read_csv(file, keep_default_na=False) #keep_default_na is key or empty cells get NaN -> type errors
    saw_str = 'test_attribute_' + saw_attribute # todo - decide if user should input ta number or entire string. only number would limit how flexible it can be to other type of saw variables.
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

    print('broadcast = ', broadcast_num, '\n')
    print('total sigs = ', total_sig_num, '\n')
    print('broadcast sigs = ', broadcast_sig_num, '\n')
    print('shared = ', shared_num, '\n')
    print('viral sig = ', viral_sig_num, '\n')
    print('soft unsub = ', soft_unsub_num, '\n')
    print('unsub num = ', unsub_num, '\n')
    print('blocked num = ', blocked_num, '\n')
    print('remaining = ', remaining_num, '\n')