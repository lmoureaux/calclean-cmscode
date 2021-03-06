#ifndef UPCGENPARTICLEANALYZER_H
#define UPCGENPARTICLEANALYZER_H

#include <string>

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

//TFile Service
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

//Root Classes
#include "TTree.h"
#include "TFile.h"
#include "TLorentzVector.h"

using namespace reco;
using namespace std;

class UPCGenParticleAnalyzer : public edm::EDAnalyzer{
public:
	explicit UPCGenParticleAnalyzer(const edm::ParameterSet&);
	~UPCGenParticleAnalyzer();
private:
	virtual void beginJob();
	virtual void analyze(const edm::Event&, const edm::EventSetup&);
	virtual void getParticles(edm::Handle<vector<reco::GenParticle> >, 
             vector<double>&, vector<double>&, vector<double>&, 
             vector<double>&, vector<double>&, vector<double>&,
	     vector<double>&, vector<double>&);
        float calcPolHXCosTheta(TLorentzVector, TLorentzVector);

	edm::Service<TFileService> mFileServer;

	string genParticleCollection; 
	string treeName; 

	int nParticles;
        double polCosTheta;
	vector<double>  x, y, z, 
			px, py, pz, eta,
			mass, charge;
 
	TTree* GenPartTree;
};
DEFINE_FWK_MODULE(UPCGenParticleAnalyzer);
#endif
