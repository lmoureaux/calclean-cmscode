import FWCore.ParameterSet.Config as cms
import sys
import FWCore.ParameterSet.Types as CfgTypes
import PhysicsTools.PythonAnalysis.LumiList as LumiList

if len(sys.argv) > 2:
	infile=open(sys.argv[2])
	outfile=(sys.argv[3])
	process = cms.Process("UPCTreeMaker")

	process.load("FWCore.MessageService.MessageLogger_cfi")
	process.load('Configuration.StandardSequences.MagneticField_38T_cff')
	process.load("Configuration.StandardSequences.ReconstructionHeavyIons_cff")
	process.load("Configuration.StandardSequences.GeometryDB_cff")
	process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
	process.load("HeavyIonsAnalysis.Configuration.collisionEventSelection_cff")
	process.load("Analyzers.UPCTriggerAnalyzer.upcPixelClusterShapeAnalyzer_cfi")
	process.load("Analyzers.UPCTriggerAnalyzer.upcPixelTrack_cff")

	process.MessageLogger.cerr.FwkReport.reportEvery = 10
	process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1)); 

	process.source = cms.Source("PoolSource",
	    fileNames = cms.untracked.vstring(infile.readlines())
	)

	process.TFileService = cms.Service("TFileService",
	    fileName = cms.string(outfile)
	)

	process.HeavyIonGlobalParameters=cms.PSet(centralityVariable= cms.string("PixelHits"),#HFhits"),#"PixelHits"),
		centralitySrc = cms.InputTag("hiCentrality")
	)
	
	process.triggerSelection = cms.EDFilter( "TriggerResultsFilter",
		 triggerConditions = cms.vstring("HLT_HIUPCNeuMuPixel_SingleTrack_v1"),
		 hltResults = cms.InputTag("TriggerResults::HLT"),
		 l1tResults = cms.InputTag("gtDigis"),
		 daqPartitions = cms.uint32( 0x01 ),
		 l1tIgnoreMask = cms.bool( False ),
		 l1techIgnorePrescales = cms.bool( False ),
		 throw = cms.bool( True )
	)

	process.GlobalTag.globaltag = 'GR_R_44_V12::All'

	process.l1bitana = cms.EDAnalyzer('L1BitAnalyzer',
		l1GtRR=cms.InputTag("gtDigis"),
		hltresults=cms.InputTag("TriggerResults::HLT")	
	)
	
	process.eclustbana = cms.EDAnalyzer('UPCEcalClusterAnalyzer',
        	ecalClusterCollection=cms.string("islandBarrelSuperClusters")
	)

	process.eclusteana = cms.EDAnalyzer('UPCEcalClusterAnalyzer',
		ecalClusterCollection=cms.string("islandEndcapSuperClusters")
	)

	process.upcmuana = cms.EDAnalyzer('UPCMuonAnalyzer',
		muonLabel=cms.InputTag("muons")
	)	
	
	process.upctrackpix=cms.EDAnalyzer('UPCTrackAnalyzer',
		trackCollection=cms.string("hiPixelTracks")
	)

	process.upctrackselana = cms.EDAnalyzer('UPCTrackAnalyzer',
		trackCollection=cms.string("hiSelectedTracks")
	)

	process.upcvertexana = cms.EDAnalyzer('UPCVertexAnalyzer',
		vertexCollection=cms.string("hiSelectedVertex")
	)

	process.upcrunana = cms.EDAnalyzer('UPCRunAnalyzer')

	process.upccentralityana = cms.EDAnalyzer('UPCCentralityAnalyzer',
		centralityVariable=process.HeavyIonGlobalParameters.centralityVariable
	)

	process.zdcana = cms.EDAnalyzer('ZDCAnalyzer')

	process.ecalesana = cms.EDAnalyzer('UPCEcalAnalyzer',
		ecalCollection=cms.string("EcalRecHitsES")
	)
	
	process.ecaleeana = cms.EDAnalyzer('UPCEcalAnalyzer',
		ecalCollection=cms.string("EcalRecHitsEE")
	)

	process.ecalebana = cms.EDAnalyzer('UPCEcalAnalyzer',
		ecalCollection=cms.string("EcalRecHitsEB")
	)

	process.hfana = cms.EDAnalyzer('UPCHFEnergyAnalyzer')	

	process.rechitana = cms.EDAnalyzer('UPCRecHitAnalyzer',
		TotalChargeThreshold=cms.untracked.double(0.0),
		FillEB=cms.untracked.bool(True),	
		FillEE=cms.untracked.bool(True),
		FillHBHESumOnly=cms.untracked.bool(True),	
		FillHFSumOnly=cms.untracked.bool(True),
		FillEBSumOnly=cms.untracked.bool(True),	
		FillEESumOnly=cms.untracked.bool(True)
	)

	process.maxcalana = cms.EDAnalyzer('UPCMaxCalAnalyzer')

	process.siTrackSeq = cms.Sequence(process.siPixSeq+process.upctrackpix)
	process.trackSeq = cms.Sequence(process.upctrackselana)
	process.runSeq = cms.Sequence(process.siPixelRecHits+process.upcPixelClusterShapeAnalyzer+process.upcvertexana+process.upccentralityana)
        process.zdcSeq = cms.Sequence(process.zdcana)
	process.ecalSeq = cms.Sequence(process.ecalesana+process.ecaleeana+process.ecalebana)
	process.ecalclustSeq = cms.Sequence(process.eclustbana+process.eclusteana)
	process.muSeq = cms.Sequence(process.upcmuana)
	process.triggerSeq = cms.Sequence(process.l1bitana)
	process.rechitSeq = cms.Sequence(process.rechitana)

	process.path = cms.Path(#process.triggerSelection+
					process.maxcalana+ 
					process.triggerSeq+
					process.runSeq+
					process.muSeq+
					process.siTrackSeq+
					process.trackSeq+
					process.zdcSeq+
					process.rechitSeq
	#				process.ecalclustSeq
	)
else:
	print 'error: no input file'	
