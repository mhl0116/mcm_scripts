#grep done Hgg_UL16_MC_status.txt > Hgg_UL16_MC_done.txt
#grep -v done Hgg_UL16_MC_status.txt > Hgg_UL16_MC_notReady.txt
#grep -v done Hgg_UL16_MC_status.txt | grep -v NanoAOD | grep -v PtH | grep -v "No prepID" > Hgg_UL16_MC_notReady.txt
#grep APV Hgg_UL16_MC_notReady.txt > Hgg_UL16APV_MC_notReady.txt
#grep -v APV Hgg_UL16_MC_notReady.txt > Hgg_UL16NotAPV_MC_notReady.txt

grep done Hgg_UL17_MC_status.txt > Hgg_UL17_MC_done.txt
grep -v done Hgg_UL17_MC_status.txt > Hgg_UL17_MC_notReady.txt
grep -v done Hgg_UL17_MC_status.txt | grep -v NanoAOD | grep -v PtH | grep -v "No prepID" > Hgg_UL17_MC_notReady.txt

grep done Hgg_UL17_MC_status.txt > Hgg_UL17_MC_done.txt
grep -v done Hgg_UL17_MC_status.txt > Hgg_UL17_MC_notReady.txt
grep -v done Hgg_UL17_MC_status.txt | grep -v NanoAOD | grep -v PtH | grep -v "No prepID" > Hgg_UL17_MC_notReady.txt
grep done Hgg_UL18_MC_status.txt > Hgg_UL18_MC_done.txt
grep -v done Hgg_UL18_MC_status.txt > Hgg_UL18_MC_notReady.txt
grep -v done Hgg_UL18_MC_status.txt | grep -v NanoAOD | grep -v PtH | grep -v "No prepID" > Hgg_UL18_MC_notReady.txt

#grep -v done *tautau*concise.txt | awk -F ":" '{print $2}' > ggtautau_notReady_20220303.txt
#grep done *tautau*concise.txt | awk -F ":" '{print $2}' > ggtautau_done_20220303.txt

#grep done *tautau*concise.txt | awk -F ":" '{print $2}' > ggtautau_done_20220303.txt
#grep done *2G2Tau*concise.txt | awk -F ":" '{print $2}' >> ggtautau_done_20220303.txt
#grep -v done *tautau*concise.txt | awk -F ":" '{print $2}' > ggtautau_notReady_20220303.txt
#grep -v done *2G2Tau*concise.txt | awk -F ":" '{print $2}' >> ggtautau_notReady_20220303.txt


