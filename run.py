from linkedin_search import lkd_login,get_url,make_search, get_args

from datetime import datetime
import time

import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    args = get_args()
    job_decriptions = ['Business Data Analyst','Data Analyst','Business Analyst']
    driver = lkd_login()
    print('Login complete!')
    print(f"{datetime.now().strftime('%H:%M')}")
    while True:
        for job_des in args.keywords:
            url = get_url(job_des,args)
            #print('url generated!')
            make_search(driver,url,job_des,args)
        
        print(f"-----------------> {datetime.now().strftime('%H:%M')}: Waiting {args.wait_time}min...")
        time.sleep(60*args.wait_time)