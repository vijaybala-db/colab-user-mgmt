def get_users():
    import os, gspread_pandas as gsp
    os.environ['GSPREAD_PANDAS_CONFIG_DIR'] = os.getcwd()  # Location of google_secret.json
    spreadsheet = gsp.Spread('1CZZYi-BQEMT80ZkG6ky3qYULdEzoFKL64VGGz8hU9Es')  # 2023-05-17 Chicago Champion Event
    df = spreadsheet.sheet_to_df(sheet='enb-championevent-users')
    return df.to_dict(orient='records')

def print_users_tf(users):
    import re
    for user in users:
        resource_name = re.sub('[^0-9a-zA-Z_]+', '-', user['email'])
        print(f'''resource "databricks_user" "{resource_name}" {{
    user_name = "{user['email']}"
    allow_cluster_create = {user['allow_cluster_create'].lower()}
}}\n\n''')
        

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--users', action="store_true", help="Generate users.tf from spreadsheet")
args = parser.parse_args()
if args.users:
    users = get_users()
    print_users_tf(users)
else:
    parser.print_help()