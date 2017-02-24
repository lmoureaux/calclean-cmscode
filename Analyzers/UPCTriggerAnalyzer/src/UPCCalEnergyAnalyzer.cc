#include "Analyzers/UPCTriggerAnalyzer/interface/UPCCalEnergyAnalyzer.h"

using namespace edm;
using namespace std;

UPCCalEnergyAnalyzer::UPCCalEnergyAnalyzer(const ParameterSet& iConfig){}

UPCCalEnergyAnalyzer::~UPCCalEnergyAnalyzer(){}

void UPCCalEnergyAnalyzer::beginJob(){
	mFileServer->file().cd();

	CaloTree = new TTree("CaloTree","CaloTree");
		
	CaloTree->Branch("CaloSize",&CaloSize);
	CaloTree->Branch("CaloEnergy",CaloEnergy,"CaloEnergy[CaloSize]/F");
	CaloTree->Branch("CaloHadEnergy",CaloHadEnergy,"CaloEnergyHad[CaloSize]/F");
	CaloTree->Branch("CaloEmEnergy",CaloEmEnergy,"CaloEnergyEm[CaloSize]/F");
	CaloTree->Branch("CaloEta",CaloEta,"CaloEta[CaloSize]/F");
	CaloTree->Branch("CaloPhi",CaloPhi,"CaloPhi[CaloSize]/F");
  CaloTree->Branch("CaloHFHits",CaloHFHits,"CaloHFHits[CaloSize]/I");
  CaloTree->Branch("CaloHBHits",CaloHBHits,"CaloHBHits[CaloSize]/I");
  CaloTree->Branch("CaloHEHits",CaloHEHits,"CaloHEHits[CaloSize]/I");
  CaloTree->Branch("CaloEEHits",CaloEEHits,"CaloEEHits[CaloSize]/I");
  CaloTree->Branch("CaloEBHits",CaloEBHits,"CaloEBHits[CaloSize]/I");
}


void UPCCalEnergyAnalyzer::analyze(const Event& iEvent, const EventSetup& iSetup)
{
	Handle<CaloTowerCollection> calotower;
	iEvent.getByType(calotower);

	if(!calotower.failedToGet()){
		CaloSize=0;
		for(CaloTowerCollection::const_iterator calt=(&*calotower)->begin();calt!=(&*calotower)->end();calt++){
			CaloEnergy[CaloSize]=calt->energy();
			CaloHadEnergy[CaloSize]=calt->hadEnergy();
			CaloEmEnergy[CaloSize]=calt->emEnergy();
			CaloEta[CaloSize]=calt->eta();
			CaloPhi[CaloSize]=calt->phi();

      CaloHFHits[CaloSize] = 0;
      CaloHBHits[CaloSize] = 0;
      CaloHEHits[CaloSize] = 0;
      CaloEEHits[CaloSize] = 0;
      CaloEBHits[CaloSize] = 0;

      vector<DetId> detIds = calt->constituents();
      const vector<DetId>::const_iterator end = detIds.end();
      for (vector<DetId>::const_iterator it = detIds.begin(); it != end; ++it) {
        if (it->det() == DetId::Hcal) {
          // HCAL
          HcalSubdetector subdet = (HcalSubdetector) it->subdetId();

          if (subdet == HcalForward) {
            CaloHFHits[CaloSize]++;
          }
          if (subdet == HcalBarrel) {
            CaloHBHits[CaloSize]++;
          }
          if (subdet == HcalEndcap) {
            CaloHEHits[CaloSize]++;
          }
        } else if (it->det() == DetId::Ecal) {
          // ECAL
          EcalSubdetector subdet = (EcalSubdetector) it->subdetId();

          if (subdet == EcalBarrel) {
            CaloEBHits[CaloSize]++;
          }
          if (subdet == EcalEndcap) {
            CaloEEHits[CaloSize]++;
          }
        }
			}

			CaloSize++;
		}
	}

	CaloTree->Fill();
}
