import FWCore.ParameterSet.Config as cms
import sys
import FWCore.ParameterSet.Types as CfgTypes
import PhysicsTools.PythonAnalysis.LumiList as LumiList

if len(sys.argv) > 2:
	infile=[sys.argv[2]]
	for x in sys.argv[3:(len(sys.argv)-2)]:
		infile.append(x)

	outfile='L1BitTree.root'

	process = cms.Process("FSCTreeMaker")

	process.load("FWCore.MessageService.MessageLogger_cfi")
	process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

	process.MessageLogger.cerr.FwkReport.reportEvery = 10
	#	process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True))

	nEventz=int(sys.argv[len(sys.argv)-1])
	process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(nEventz))

	process.source = cms.Source("PoolSource",
	    fileNames = cms.untracked.vstring(infile)
	)

	process.GlobalTag.globaltag = 'STARTHI44_V12::All'

	process.TFileService = cms.Service("TFileService",
	    fileName = cms.string(outfile)
	)

	process.GtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
	    DaqGtInputTag = cms.InputTag( "rawDataRepacker" ),
	    DaqGtFedId = cms.untracked.int32( 813 ),
	    ActiveBoardsMask = cms.uint32( 0xffff ),
	    UnpackBxInEvent = cms.int32( 5 ),
	    Verbosity = cms.untracked.int32( 0 )
	)

	process.l1bitAna = cms.EDAnalyzer('L1BitAnalyzer',
		l1GtRR=cms.InputTag("GtDigis")
	)

	process.path = cms.Path(process.GtDigis*process.l1bitAna)
else:
	print 'error: no input file'	
