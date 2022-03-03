import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps

#mcm = McM(dev=True)
mcm = McM(dev=False)

# Example to get  ALL requesst which are member of a given campaign and are submitted
# It uses a generic search for specified columns: query='status=submitted'
# Queries can be combined: query='status=submitted&member_of_campaign=Summer12'
# campaign_requests = mcm.get('requests', query='member_of_campaign=*Summer20*&status=submitted')

# Example to retrieve single request dictionary
# More methods are here:
# https://cms-pdmv.cern.ch/mcm/restapi/requests/

'''
single_request_prepid = 'TOP-Summer12-00368'
single_request = mcm.get('requests', single_request_prepid, method='get')
print('Single request "%s":\n%s' % (single_request_prepid, dumps(single_request, indent=4)))
'''

# Example how to get multiple requests using range
'''
requests_query = """
    B2G-Fall13-00001
    B2G-Fall13-00005 -> B2G-Fall13-00015
"""
range_of_requests = mcm.get_range_of_requests(requests_query)
print('Found %s requests' % (len(range_of_requests)))
for request in range_of_requests:
    print(request['prepid'])
'''
#campaign_requests = mcm.get('requests', query='prepid=HIG-RunIISummer20UL16wmLHEGEN-*&dataset_name=GluGluToHHTo2G*_node_cHHH*_TuneCP5_13TeV-powheg-pythia8')

#[u'validation', u'total_events', u'config_id', u'events_per_lumi', u'cmssw_release', u'mcdb_id', u'transient_output_modules', u'sequences', u'block_black_list', u'block_white_list', u'interested_pwg', u'process_string', u'ppd_tags', u'fragment_tag', u'generator_parameters', u'cadi_line', u'flown_with', u'priority', u'version', u'generators', u'memory', u'pilot', u'type', u'_rev', u'status', u'keep_output', u'energy', u'tags', u'fragment', u'time_event', u'pwg', u'reqmgr_name', u'approval', u'name_of_fragment', u'pileup_dataset_name', u'analysis_id', u'input_dataset', u'member_of_chain', u'prepid', u'extension', u'size_event', u'notes', u'completed_events', u'output_dataset', u'member_of_campaign', u'_id', u'dataset_name', u'history']

def get_single_query(tag):

    #file1 = open("results/ggtautau_UL_MC_status.txt", "w")  # write mode
    file1 = open("results/{}_UL_MC_status.txt".format(tag), "w")  # write mode

    #campaign_requests = mcm.get('requests', query='prepid=HIG-RunIISummer20UL1*-*&dataset_name=*2G2Tau*pythia8')
    #campaign_requests = mcm.get('requests', query='prepid=HIG-RunIISummer20UL1*-*&dataset_name=*NMSSM_XYH_Y_gg_H_tautau*pythia8')
    campaign_requests = mcm.get('requests', query='prepid=HIG-RunIISummer20UL1*-*&dataset_name=*{}*pythia8'.format(tag))
    for sample_request in campaign_requests:
        name, prepid, status, priority, n_events = sample_request['dataset_name'], sample_request['prepid'], sample_request['status'], sample_request['priority'], sample_request['total_events']
        #print ("name: {}, prepID: {}, status: {}, priority: {}".format(name, prepid, status, priority))
        #print (sample_request.keys())
        if ("MiniAOD" in prepid) :
            print ("| {} | {} | {} | {} | {} |".format(name, prepid, status, priority, n_events))
            file1.write("| {} | {} | {} | {} | {} |\n".format(prepid, name, priority, status, n_events) )
        if ("MiniAOD" not in prepid) and (status != "done"):
            print ("| {} | {} | {} | {} | {} |".format(name, prepid, status, priority, n_events))
            file1.write("| {} | {} | {} | {} | {} |\n".format(prepid, name, priority, status, n_events) )

    file1.close()

get_single_query("NMSSM_XYH_Y_gg_H_tautau")
get_single_query("NMSSM_XYH_Y_tautau_H_gg")
get_single_query("2G2Tau")
