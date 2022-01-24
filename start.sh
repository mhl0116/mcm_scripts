#!/usr/bin/env sh

# Need python2.7 from CMSSW
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_9; 
cmsenv; 
cd -; 
export LANG=en_US.UTF-8


[ -d myenv ] || virtualenv myenv
source myenv/bin/activate
export PYTHONPATH=`pwd`/myenv/lib/python2.7/site-packages:$PYTHONPATH
pip install requests  flask pygments
pip install requests-cache==0.5.0

cern-get-sso-cookie --cert "/home/users/hmei/.globus/usercert.pem" --key "/home/users/hmei/.globus/userkey_nopass.pem" -r -o "/home/users/hmei/private/ssocookie.txt" -u "https://cms-pdmv.cern.ch/mcm/public/restapi"

cp /home/users/hmei/private/ssocookie.txt /home/users/hmei/private/mcm-prod-cookie.txt

