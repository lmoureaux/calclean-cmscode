import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("thinning")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
infile=open(sys.argv[2])
outfile=(sys.argv[3])

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(infile.readlines())
)

process.output = cms.OutputModule("PoolOutputModule",
   outputCommands =  cms.untracked.vstring(	
	'keep recoGenParticles_hiGenParticles__HLT',
	'keep HBHERecHitsSorted_hbhereco__RECO',
	'keep SiPixelClusteredmNewDetSetVector_siPixelClusters__RECO',
	'keep SiStripClusteredmNewDetSetVector_siStripClusters__RECO',
	'keep HFRecHitsSorted_hfreco__RECO',
	'keep HORecHitsSorted_horeco__RECO',
	'keep CaloTowersSorted_towerMaker__RECO',
	'keep EcalRecHitsSorted_ecalRecHit_EcalRecHitsEB_RECO',
	'keep recoCandidatesOwned_caloTowers__RECO',
	'keep CSCDetIdCSCSegmentsOwnedRangeMap_cscSegments__RECO',
	'keep CSCDetIdCSCRecHit2DsOwnedRangeMap_csc2DRecHits__RECO',
	'keep TrajectorySeeds_ancientMuonSeed__RECO',
	'keep EcalRecHitsSorted_ecalPreshowerRecHit_EcalRecHitsES_RECO',
	'keep EcalRecHitsSorted_ecalRecHit_EcalRecHitsEE_RECO',
	'keep CastorRecHitsSorted_castorreco__RECO',
	'keep patMuons_patMuonsWithTrigger__RECO',
	'keep patMuons_patMuonsWithoutTrigger__RECO',
	'keep TrackingRecHitsOwned_standAloneMuons__RECO',
	'keep L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap__HLT',
	'keep recoHcalNoiseRBXs_hcalnoise__RECO',
	'keep recoCastorTowers_CastorTowerReco__RECO',
	'keep recoTrackExtras_hiSelectedTracks__RECO',
	'keep recoCaloClusters_multi5x5BasicClustersUncleaned_multi5x5EndcapBasicClusters_RECO',
	'keep recoCaloClusters_multi5x5BasicClustersCleaned_multi5x5EndcapBasicClusters_RECO',
	'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_RECO',
	'keep recoCaloClusters_islandBasicClusters_islandEndcapBasicClusters_RECO',
	'keep TrackingRecHitsOwned_tevMuons_default_RECO',
	'keep TrackingRecHitsOwned_globalMuons__RECO',
	'keep TrackingRecHitsOwned_tevMuons_picky_RECO',
	'keep recoMuons_muons__RECO',
	'keep ZDCDataFramesSorted_hcalDigis__RECO',
	'keep recoEvtPlanes_hiEvtPlane_recoLevel_RECO',
	'keep recoTracks_hiSelectedTracks__RECO',
	'keep TrackingRecHitsOwned_tevMuons_dyt_RECO',
	'keep TrackingRecHitsOwned_hiSelectedTracks__RECO',
	'keep recoCastorJetIDedmValueMap_ak7CastorJetID__RECO',
	'keep ZDCRecHitsSorted_zdcreco__RECO',
	'keep DTLayerIdDTRecHit1DPairsOwnedRangeMap_dt1DCosmicRecHits__RECO',
	'keep DTLayerIdDTRecHit1DPairsOwnedRangeMap_dt1DRecHits__RECO',
	'keep DTChamberIdDTRecSegment4DsOwnedRangeMap_dt4DCosmicSegments__RECO',
	'keep patCompositeCandidates_onia2MuMuPatStaSta__RECO',
	'keep L1MuGMTReadoutCollection_gtDigis__RECO',
	'keep TrackingRecHitsOwned_tevMuons_firstHit_RECO',
	'keep recoTrackExtras_standAloneMuons__RECO',
	'keep patCompositeCandidates_onia2MuMuPatTraTra__RECO',
	'keep patTriggerObjectStandAlones_patTrigger__RECO',
	'keep DTChamberIdDTRecSegment4DsOwnedRangeMap_dt4DSegments__RECO',
	'keep L1GlobalTriggerReadoutRecord_gtDigis__RECO',
	'keep patCompositeCandidates_onia2MuMuPatGlbGlb__RECO',
	'keep Level1TriggerScalerss_scalersRawToDigi__RECO',
	'keep triggerTriggerEvent_hltTriggerSummaryAOD__HLT',
	'keep recoBasicJets_ak7BasicJets__RECO',
	'keep recoTracks_standAloneMuons__RECO',
	'keep recoTracks_standAloneMuons_UpdatedAtVtx_RECO',
	'keep patTriggerObjectStandAlones_muonMatchHLTL1_propagatedReco_RECO',
	'keep patTriggerObjectStandAlones_muonL1Info_propagatedReco_RECO',
	'keep EcalTrigPrimCompactColl_ecalCompactTrigPrim__RECO',
	'keep patTriggerObjectStandAlones_muonL1Info_l1muons_RECO',
	'keep LumiScalerss_scalersRawToDigi__RECO',
	'keep RPCDetIdRPCRecHitsOwnedRangeMap_rpcRecHits__RECO',
	'keep patTriggerObjectStandAlonesedmAssociation_muonMatchHLTL1_propagatedReco_RECO',
	'keep patTriggerObjectStandAlonesedmAssociation_muonL1Info_propagatedReco_RECO',
	'keep patTriggerObjectStandAlonesedmAssociation_muonMatchHLTCtfTrack__RECO',
	'keep patTriggerObjectStandAlonesedmAssociation_muonMatchHLTTrackMu__RECO',
	'keep recoCentrality_hiCentrality__RECO',
	'keep patTriggerObjectStandAlonesedmAssociation_muonMatchHLTL1__RECO',
	'keep patTriggerObjectStandAlonesedmAssociation_muonMatchHLTL2__RECO',
	'keep patTriggerObjectStandAlonesedmAssociation_muonMatchHLTL3__RECO',
	'keep patTriggerObjectStandAlonesedmAssociation_muonL1Info__RECO',
	'keep recoTrackExtras_globalMuons__RECO',
	'keep recoCandidateedmPtredmValueMap_muonL1Info_l1ToReco_RECO',
	'keep recoTrackExtras_tevMuons_default_RECO',
	'keep recoTrackExtras_tevMuons_picky_RECO',
	'keep recoTrackExtras_tevMuons_dyt_RECO',
	'keep recoTrackExtras_tevMuons_firstHit_RECO',
	'keep recoCandidateedmPtredmValueMap_muonL1Info__RECO',
	'keep recoIsoDepositedmValueMap_muIsoDepositCalByAssociatorTowers_ecal_RECO',
	'keep recoVertexs_hiSelectedVertex__RECO',
	'keep recoVertexs_hiPixelAdaptiveVertex__RECO',
	'keep recoIsoDepositedmValueMap_muons_ecal_RECO',
	'keep recoCaloMuons_calomuons__RECO',
	'keep recoCaloMuons_muons__RECO',
	'keep recoTracks_tevMuons_default_RECO',
	'keep recoTracks_globalMuons__RECO',
	'keep recoTracks_tevMuons_picky_RECO',
	'keep recoTracks_tevMuons_dyt_RECO',
	'keep recoTracks_tevMuons_firstHit_RECO',
	'keep l1extraL1MuonParticles_l1extraParticles__RECO',
	'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower__RECO',
	'keep recoIsoDepositedmValueMap_muIsoDepositCalByAssociatorTowers_hcal_RECO',
	'keep recoIsoDepositedmValueMap_muons_hcal_RECO',
	'keep recoSuperClusters_multi5x5SuperClustersWithPreshower__RECO',
	'keep recoIsoDepositedmValueMap_muIsoDepositTk__RECO',
	'keep recoSuperClusters_multi5x5SuperClustersUncleaned_multi5x5EndcapSuperClusters_RECO',
	'keep recoIsoDepositedmValueMap_muons_tracker_RECO',
	'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_preshowerXClusters_RECO',
	'keep recoSuperClusters_multi5x5SuperClustersCleaned_multi5x5EndcapSuperClusters_RECO',
	'keep recoSuperClusters_multi5x5SuperClusters_multi5x5EndcapSuperClusters_RECO',
	'keep EcalTriggerPrimitiveDigisSorted_ecalTPSkim__RECO',
	'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_preshowerYClusters_RECO',
	'keep recoIsoDepositedmValueMap_muIsoDepositJets__RECO',
	'keep recoSuperClusters_correctedIslandEndcapSuperClusters__RECO',
	'keep recoIsoDepositedmValueMap_muons_jets_RECO',
	'keep recoMuonTimeExtraedmValueMap_muons_combined_RECO',
	'keep recoSuperClusters_correctedEndcapSuperClustersWithPreshower__RECO',
	'keep recoIsoDepositedmValueMap_muIsoDepositCalByAssociatorTowers_ho_RECO',
	'keep L1AcceptBunchCrossings_scalersRawToDigi__RECO',
	'keep HcalNoiseSummary_hcalnoise__RECO',
	'keep recoIsoDepositedmValueMap_muons_ho_RECO',
	'keep recoSuperClusters_islandSuperClusters_islandEndcapSuperClusters_RECO',
	'keep BeamSpotOnlines_scalersRawToDigi__RECO',
	'keep recoMuonTimeExtraedmValueMap_muons_csc_RECO',
	'keep recoCaloClusters_islandBasicClusters_islandBarrelBasicClusters_RECO',
	'keep recoBeamSpot_offlineBeamSpot__RECO',
	'keep recoSuperClusters_correctedIslandBarrelSuperClusters__RECO',
	'keep recoSuperClusters_islandSuperClusters_islandBarrelSuperClusters_RECO',
	'keep recoVertexs_hiPixelMedianVertex__RECO',
	'keep l1extraL1EtMissParticles_l1extraParticles_MET_RECO',
	'keep DcsStatuss_scalersRawToDigi__RECO',
	'keep recoVertexs_hiPixelClusterVertex__RECO',
	'keep recoCaloClusters_uncleanedHybridSuperClusters_hybridBarrelBasicClusters_RECO',
	'keep recoSuperClusters_correctedHybridSuperClusters__RECO',
	'keep recoSuperClusters_uncleanedHybridSuperClusters__RECO',
	'keep l1extraL1JetParticles_l1extraParticles_Tau_RECO',
	'keep recoCaloClusters_cleanedHybridSuperClusters_hybridBarrelBasicClusters_RECO',
	'keep recoCaloClusters_hybridSuperClusters_hybridBarrelBasicClusters_RECO',
	'keep TrajectorysToOnerecoTracksAssociation_hiSelectedTracks__RECO',
	'keep edmTriggerResults_TriggerResults__HLT',
	'keep recoSuperClusters_cleanedHybridSuperClusters__RECO',
	'keep recoSuperClusters_hybridSuperClusters__RECO',
	'keep recoMuonTimeExtraedmValueMap_muons_dt_RECO',
	'keep l1extraL1HFRingss_l1extraParticles__RECO',
	'keep floatedmValueMap_muonMatchHLTL1_deltaPhi_RECO',
	'keep edmConditionsInEventBlock_conditionsInEdm__RECO',
	'keep floatedmValueMap_muonL1Info_deltaPhi_RECO',
	'keep floatedmValueMap_muonMatchHLTL1_deltaR_RECO',
	'keep floatedmValueMap_muonL1Info_deltaR_RECO',
	'keep l1extraL1EtMissParticles_l1extraParticles_MHT_RECO',
	'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_RECO',
	'keep recoSuperClusters_uncleanedOnlyCorrectedHybridSuperClusters__RECO',
	'keep l1extraL1EmParticles_l1extraParticles_Isolated_RECO',
	'keep recoCaloClusters_hybridSuperClusters_uncleanOnlyHybridBarrelBasicClusters_RECO',
	'keep recoTracksToOnerecoTracksAssociation_tevMuons_firstHit_RECO',
	'keep recoTracksToOnerecoTracksAssociation_tevMuons_default_RECO',
	'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_multi5x5PreshowerXClustersShape_RECO',
	'keep recoTracksToOnerecoTracksAssociation_tevMuons_picky_RECO',
	'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_multi5x5PreshowerYClustersShape_RECO',
	'keep l1extraL1JetParticles_l1extraParticles_Forward_RECO',
	'keep recoTracksToOnerecoTracksAssociation_tevMuons_dyt_RECO',
	'keep L1GctJetCands_gctDigis_tauJets_RECO',
	'keep intedmValueMap_muonL1Info_quality_RECO',
	'keep recoCaloJets_iterativeConePu5CaloJets__RECO',
	'keep L1GctEtMisss_gctDigis__RECO',
	'keep intedmValueMap_muonL1Info_isolated_RECO',
	'keep intedmValueMap_muonL1Info_bx_RECO',
	'keep L1GctHFBitCountss_gctDigis__RECO',
	'keep recoSuperClusters_multi5x5SuperClusters_uncleanOnlyMulti5x5EndcapSuperClusters_RECO',
	'keep L1GctJetCands_gctDigis_forJets_RECO',
	'keep edmTriggerResults_TriggerResults__RECO',
	'keep recoCaloClusters_multi5x5SuperClusters_uncleanOnlyMulti5x5EndcapBasicClusters_RECO',
	'keep recoSuperClusters_multi5x5SuperClustersUncleaned_multi5x5BarrelSuperClusters_RECO',
	'keep recoSuperClusters_uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower__RECO',
	'keep recoCaloClusters_multi5x5BasicClustersUncleaned_multi5x5BarrelBasicClusters_RECO',
	'keep edmTriggerResults_TriggerResults__RECO',
	'keep recoSuperClusters_multi5x5SuperClustersCleaned_multi5x5BarrelSuperClusters_RECO',
	'keep recoCaloClusters_multi5x5BasicClustersCleaned_multi5x5BarrelBasicClusters_RECO',
	'keep edmTriggerResults_TriggerResults__UPCPhyicsSkim',
	'keep L1GctEtTotals_gctDigis__RECO',
	'keep l1extraL1JetParticles_l1extraParticles_Central_RECO',
	'keep L1GctEmCands_gctDigis_isoEm_RECO',
	'keep recoSuperClusters_uncleanedOnlyMulti5x5SuperClustersWithPreshower__RECO',
	'keep L1GctEmCands_gctDigis_nonIsoEm_RECO',
	'keep L1GctJetCands_gctDigis_cenJets_RECO',
	'keep l1extraL1EmParticles_l1extraParticles_NonIsolated_RECO',
	'keep DetIdedmEDCollection_siPixelDigis__RECO',
	'keep DetIdedmEDCollection_siStripDigis__RECO',
	'keep recoPhotons_photons__RECO',
	'keep L1GctHFRingEtSumss_gctDigis__RECO',
	'keep doubles_iterativeConePu5CaloJets_sigmas_RECO',
	'keep doubles_iterativeConePu5CaloJets_rhos_RECO',
	'keep L1TriggerScalerss_scalersRawToDigi__RECO',
	'keep L1GctEtHads_gctDigis__RECO',
	'keep L1GctHtMisss_gctDigis__RECO',
	'keep recoPhotonCores_photonCore__RECO',
	'keep doubles_ak7BasicJets_sigmas_RECO',
	'keep doubles_ak7BasicJets_rhos_RECO',
	'keep L1GctJetCountss_gctDigis__RECO',
	'keep double_iterativeConePu5CaloJets_sigma_RECO',
	'keep double_iterativeConePu5CaloJets_rho_RECO',
	'keep double_ak7BasicJets_sigma_RECO',
	'keep double_ak7BasicJets_rho_RECO',
   ),
    fileName = cms.untracked.string(outfile)
)

process.e = cms.EndPath(process.output)
