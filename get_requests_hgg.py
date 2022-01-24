import sys
from rest import McM
from json import dumps
sys.path.append('/home/users/hmei/myWorkspace/dis/')
from utils import pprint

#mcm = McM(dev=True)
mcm = McM(dev=False)

# Example to get  ALL requesst which are member of a given campaign and are submitted
# It uses a generic search for specified columns: query='status=submitted'
# Queries can be combined: query='status=submitted&member_of_campaign=Summer12'
# campaign_requests = mcm.get('requests', query='member_of_campaign=*Summer20*&status=submitted')

#campaign_requests = mcm.get('requests', query='prepid=HIG-RunIISummer20UL16wmLHEGEN-*&dataset_name=GluGluToHHTo2G*_node_cHHH*_TuneCP5_13TeV-powheg-pythia8')
#for request in campaign_requests:
#    print(request['prepid'])
#
#1. read dataset name from txt
#2. get prepid, should be a unique ID using special string (RunIISummer20ULYEAR) + ds name
#3. yes or no
#4. write to tuple (prepID, name, yes/no), make 3 version for 3 years

fname_samplelist = "./metadata/Hgg_UL19_MC_name.txt"
f_samplelist = open(fname_samplelist, 'r')
samplelist = f_samplelist.readlines()
samplelist = [line[:-1] for line in samplelist]

def get_Hgg_MC_status(year, tag):

    #preid_tag = "*RunIISummer20UL{}*".format(year)
    preid_tag = "*RunIISummer19UL{}*".format(year)

    import subprocess
    subprocess.call("mkdir -p results/{}".format(tag), shell=True)
    file1 = open("results/{}/Hgg_UL{}_MC_status.txt".format(tag, year), "w")  # write mode

    for sample in samplelist:

        if sample in ["DoubleMuon", "DoubleEG", "SingleElectron", "SingleMuon"]: continue
        #if sample != "GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8": continue
        dataset_name = sample
        query = 'prepid={}&dataset_name={}'.format(preid_tag, dataset_name)
        sample_requests = mcm.get('requests', query=query)

        if (sample_requests is None) or (len(sample_requests) == 0):
            print "No prepID for {} under {}".format(dataset_name, preid_tag)
            file1.write("No prepID for {} under {}\n".format(dataset_name, preid_tag))
        else:
            for sample_request in sample_requests:

                # if miniAOD in prepID and status is done, good
                # if miniAOD in prepID and not done, print priority and status
                # if not miniAOD and not done, print status and priority

                prepid, status, priority = sample_request['prepid'], sample_request['status'], sample_request['priority']
                if "MiniAOD" in prepid:
                    print "| {} | {} | {} | {} |".format(prepid, dataset_name, priority, status)
                    file1.write("| {} | {} | {} | {} |\n".format(prepid, dataset_name, priority, status) )
                if ("MiniAOD" not in prepid) and (status != "done"):
                    print "| {} | {} | {} | {} |".format(prepid, dataset_name, priority, status)
                    file1.write("| {} | {} | {} | {} |\n".format(prepid, dataset_name, priority, status) )

                #if "MiniAOD" in sample_request['prepid']:
                #    pprint(sample_request)

    file1.close()

get_Hgg_MC_status("16", "19UL")
get_Hgg_MC_status("17", "19UL")
get_Hgg_MC_status("18", "19UL")
