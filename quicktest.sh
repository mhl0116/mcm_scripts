# still need to run ~/myWorkspace/dis/start.sh to set environment properly

cern-get-sso-cookie --cert /home/users/hmei/.globus/usercert.pem --key /home/users/hmei/.globus/userkey_nopass.pem -r -o /home/users/hmei/private/ssocookie.txt -u https://cms-pdmv.cern.ch/mcm/restapi
cp /home/users/hmei/private/ssocookie.txt /home/users/hmei/private/mcm-prod-cookie.txt
#python get_requests.py
python get_requests_hgg.py

# then goin to results, and do parse.py
# then check parse.sh to see if there is useful example commands
