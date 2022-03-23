#| HIG-RunIISummer20UL16DIGIPremix-02245 | GluGluHToGG_M-120_TuneCP5_13TeV-powheg-pythia8 | 85015 | submitted 
#| HIG-RunIISummer20UL16HLT-02250 | GluGluHToGG_M-120_TuneCP5_13TeV-powheg-pythia8 | 85015 | submitted |
#| HIG-RunIISummer20UL16MiniAODv2-02241 | GluGluHToGG_M-120_TuneCP5_13TeV-powheg-pythia8 | 85015 | submitted |
#| HIG-RunIISummer20UL16RECO-02250 | GluGluHToGG_M-120_TuneCP5_13TeV-powheg-pythia8 | 85015 | submitted |
#| HIG-RunIISummer20UL16SIM-02250 | GluGluHToGG_M-120_TuneCP5_13TeV-powheg-pythia8 | 85015 | submitted |
#| HIG-RunIISummer20UL16wmLHEGEN-01121 | GluGluHToGG_M-120_TuneCP5_13TeV-powheg-pythia8 | 85015 | submitted |
#
#loop over input list
#if no dataset in tmp list, save it
#if alread has a similar list, compare prepid based on priority
#if same save both, otherwise save the one that is more upstream

def parse_mc(inputfname, yeartag, specialtag=""):

    #f_outlist = open("Hgg_UL16NotAPV_MC_notReady_concise.txt", "w")  # write mode
    #f_inlist = open("Hgg_UL16NotAPV_MC_notReady.txt", 'r')
    #f_outlist = open("Hgg_{}_MC_notReady_concise.txt".format(tag), "w")  # write mode
    #f_inlist = open("Hgg_{}_MC_notReady.txt".format(tag), 'r')
    f_outlist = open("{}_{}{}_concise.txt".format(inputfname, yeartag, specialtag), "w")  # write mode
    f_inlist = open("{}.txt".format(inputfname), 'r')
    inlist = f_inlist.readlines()
    inlist = [line[:-1] for line in inlist]

    prep_id_rank = {"LHEGEN":1, "SIM":2, "DIGI": 3, "HLT": 4, "RECO": 5, "MiniAOD": 6}
    def get_rank(prepid):
        for key in prep_id_rank.keys():
            if key in prepid:
                return prep_id_rank[key]

    outlist_prepID = []
    outlist_dataset_name = []
    outlist_priority = []
    outlist_status = []
    outlist_totalevents = []
    for line in inlist:
        line = line.split("|")
        if len(line) == 1: continue
        prep_id, dataset_name, priority, status, totalevents = line[1].strip(), line[2].strip(), line[3].strip(), line[4].strip(), line[5].strip()

        #if dataset_name != "GluGluToRadionToHHTo2G2Tau_M-900_narrow_TuneCP5_13TeV-madgraph-pythia8": continue
        if yeartag not in prep_id: continue #yeartag : UL16, UL17, UL18
        if yeartag == "UL16" and specialtag == "" and "APV" in prep_id: continue
        if specialtag != "" and specialtag not in prep_id: continue
        if "NanoAOD" in prep_id: continue

        if dataset_name not in outlist_dataset_name:
            outlist_prepID.append(prep_id)
            outlist_dataset_name.append(dataset_name)
            outlist_priority.append(priority)
            outlist_status.append(status)
            outlist_totalevents.append(totalevents)
        else:
            # find the datasetname saved in outlist and its index
            current_idx = outlist_dataset_name.index(dataset_name)
            current_rank = get_rank(outlist_prepID[current_idx])
            new_rank = get_rank(prep_id)
            if new_rank <= current_rank:
                outlist_prepID[current_idx] = prep_id
                outlist_dataset_name[current_idx] = dataset_name
                outlist_priority[current_idx] = priority
                outlist_status[current_idx] = status
                outlist_totalevents[current_idx] = totalevents 

    print len(outlist_priority)
    for i in range(len(outlist_priority)):
        prep_id = outlist_prepID[i]
        name = outlist_dataset_name[i]
        priority = outlist_priority[i]
        status = outlist_status[i]
        totalevents = outlist_totalevents[i]
        f_outlist.write("|{}|{}|{}|{}|{}|\n".format(prep_id, name, priority, status, totalevents))

    f_outlist.close()

#Hgg_{}_MC_notReady.txt
#parse_mc("UL16APV")
#parse_mc("UL17")
#parse_mc("UL18")
#parse_mc("ggtautau_UL_MC_status", "UL16")
#parse_mc("ggtautau_UL_MC_status", "UL16", "APV")
#parse_mc("ggtautau_UL_MC_status", "UL17")
#parse_mc("ggtautau_UL_MC_status", "UL18")

#tag = "NMSSM_XYH_Y_tautau_H_gg_UL_MC_status"
#tag = "NMSSM_XYH_Y_gg_H_tautau_UL_MC_status"

#tags = ["2G2Tau_UL_MC_status", "NMSSM_XYH_Y_gg_H_tautau_UL_MC_status", "NMSSM_XYH_Y_tautau_H_gg_UL_MC_status"]
tags = ["20UL/Hgg_UL16_MC_status", "20UL/Hgg_UL17_MC_status", "20UL/Hgg_UL18_MC_status"]
for tag in tags:
    for era in ["UL16", "UL17", "UL18"]:
        parse_mc(tag, era)
        if era == "UL16":
            parse_mc(tag, era, "APV")
