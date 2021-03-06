#include "TStyle.h"
#include <memory>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <TTree.h>
#include <TLorentzVector.h>
#include <TClonesArray.h>
#include "TFile.h"


void setStyle() {
 TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

 // For the canvas:
 tdrStyle->SetCanvasBorderMode(0);
 tdrStyle->SetCanvasColor(kWhite);
 tdrStyle->SetCanvasDefH(600); //Height of canvas
 tdrStyle->SetCanvasDefW(600); //Width of canvas
 tdrStyle->SetCanvasDefX(0);   //POsition on screen
 tdrStyle->SetCanvasDefY(0);

 // For the Pad:
 tdrStyle->SetPadBorderMode(0);
 tdrStyle->SetPadColor(kWhite);
 tdrStyle->SetPadGridX(false);
 tdrStyle->SetPadGridY(false);
 tdrStyle->SetGridColor(0);
 tdrStyle->SetGridStyle(3);
 tdrStyle->SetGridWidth(1);

 // For the frame:
 tdrStyle->SetFrameBorderMode(0);
 tdrStyle->SetFrameBorderSize(1);
 tdrStyle->SetFrameFillColor(0);
 tdrStyle->SetFrameFillStyle(0);
 tdrStyle->SetFrameLineColor(1);
 tdrStyle->SetFrameLineStyle(1);
 tdrStyle->SetFrameLineWidth(1);

 // For the histo:
 // tdrStyle->SetHistFillColor(1);
 // tdrStyle->SetHistFillStyle(0);
 tdrStyle->SetHistLineColor(1);
 tdrStyle->SetHistLineStyle(1);
 tdrStyle->SetHistLineWidth(1);

 tdrStyle->SetEndErrorSize(1);
 // tdrStyle->SetErrorMarker(20);
 // tdrStyle->SetErrorX(0.);
 tdrStyle->SetMarkerStyle(20);
 tdrStyle->SetMarkerSize(1.0);

 // For the fit/function:
 tdrStyle->SetOptFit(0);
 tdrStyle->SetFitFormat("5.4g");
 tdrStyle->SetFuncStyle(1);
 tdrStyle->SetFuncColor(1);
 tdrStyle->SetFuncWidth(2);

 // For the date:
 tdrStyle->SetOptDate(0);

 // For the statistics box:
 tdrStyle->SetOptFile(0);
 tdrStyle->SetOptStat(0);
 tdrStyle->SetStatColor(0);

 // Margins:
 tdrStyle->SetPadTopMargin(0.05);
 tdrStyle->SetPadBottomMargin(0.13);
 tdrStyle->SetPadLeftMargin(0.14);
 tdrStyle->SetPadRightMargin(0.05);

 // For the Global title:
 tdrStyle->SetOptTitle(0);
 tdrStyle->SetTitleFont(42);
 tdrStyle->SetTitleColor(1);
 tdrStyle->SetTitleTextColor(1);
 tdrStyle->SetTitleFillColor(10);
 tdrStyle->SetTitleFontSize(0.05);

 // For the axis titles:
 tdrStyle->SetTitleColor(1, "XYZ");
 tdrStyle->SetTitleFont(42, "XYZ");
 tdrStyle->SetTitleSize(0.05, "XYZ");
 tdrStyle->SetTitleXOffset(1.0);
 tdrStyle->SetTitleYOffset(1.2);

 // For the axis labels:
 tdrStyle->SetLabelColor(1, "XYZ");
 tdrStyle->SetLabelFont(42, "XYZ");
 tdrStyle->SetLabelOffset(0.007, "XYZ");
 tdrStyle->SetLabelSize(0.05, "XYZ");

 // For the axis:
 tdrStyle->SetAxisColor(1, "XYZ");
 tdrStyle->SetStripDecimals(kTRUE);
 tdrStyle->SetTickLength(0.03, "XYZ");
 tdrStyle->SetNdivisions(510, "XYZ");
 tdrStyle->SetPadTickX(1);
 tdrStyle->SetPadTickY(1);

 // Change for log plots:
 tdrStyle->SetOptLogx(0);
 tdrStyle->SetOptLogy(0);
 tdrStyle->SetOptLogz(0);

 // for the legends
 tdrStyle->SetLegendBorderSize(0);
 //tdrStyle->SetLegendFillColor(0);

 tdrStyle->SetPalette(1);

 tdrStyle->cd();
}





// saves to according folder inside plots folder

// mkdir plots
// mkdir plots/_jpsi_Direct_Aym
// mkdir plots/_jpsi_Direct_Sam
// mkdir plots/_jpsi_Direct_Sam2
// mkdir plots/_jpsi_TagAndProbe_Aym
// mkdir plots/_jpsi_TagAndProbe_Sam
// mkdir plots/_jpsi_TagAndProbe_Sam2

void DrawerDimuon(){ // draws plots for dimuon eff reconstruction compared to direct dimuon eff (form event numbers), needs root files produced by MuonEff with DimuonAna=1

bool save=1;

// which root file do you want to use for plots?

TString title = "_jpsi_Direct_Aym"; // as in MuonEff: Direct, TagAndProbe; Sam, Sam2, Aym


TFile* f1 = new TFile("./EfficiencyOutput/DimuonAna/output_file"+title+".root","read");



// UPC Efficiency
  TH1F *UPCTrigEffDirect = (TH1F *)f1->Get("effTrigSel");
  TH1F *UPCTrigEffMuonsSep = (TH1F *)f1->Get("TrigEffUPCsep");
  TH1F *UPCTrigEffMuonsAve = (TH1F *)f1->Get("TrigEffUPC");
  TH1F *EffTrigMu1 = (TH1F *)f1->Get("effTrig");
  TH1F *EffTrigMu2 = (TH1F *)f1->Get("effTrig2");




//**************CANVAS**************//

  setStyle();



// UPC Efficiency sep
  TCanvas *c1 = new TCanvas("c1","c1",600,600);
  //c1->SetLogy();

  UPCTrigEffDirect->GetXaxis()->SetRangeUser(0,3);
  UPCTrigEffDirect->GetYaxis()->SetRangeUser(0,1);
  UPCTrigEffDirect->GetXaxis()->SetTitleOffset(1);
  UPCTrigEffDirect->GetYaxis()->SetTitleOffset(1.22);
 
  UPCTrigEffDirect->GetXaxis()->SetTitle("p_{T}^{dimuon}");

  UPCTrigEffMuonsSep->SetStats(0); // gets rid of annoying stat box

  UPCTrigEffDirect->SetMarkerStyle(8);
  UPCTrigEffDirect->SetMarkerColor(kRed);
  UPCTrigEffMuonsSep->SetLineColor(kBlue);

  UPCTrigEffDirect->Draw("p");
  UPCTrigEffMuonsSep->Draw("same");
 
  TLegend *l1 = new TLegend(0.20,0.70,0.45,0.80,NULL,"brNDC");
  l1->AddEntry(UPCTrigEffMuonsSep,"UPC Efficiency","");
  l1->AddEntry(UPCTrigEffDirect,"direct","p");
  l1->AddEntry(UPCTrigEffMuonsSep,"sep muons","p");
  l1->SetFillColor(10);
  l1->Draw();

  c1->Update();
  if (save) c1->SaveAs("./EfficiencyOutput/plots/"+title+"/DirToSep"+title+".png");




// UPC Efficiency ave
  TCanvas *c2 = new TCanvas("c2","c2",600,600);
  //c1->SetLogy();

  UPCTrigEffDirect->GetXaxis()->SetRangeUser(0,3);
  UPCTrigEffDirect->GetXaxis()->SetTitleOffset(1);
  UPCTrigEffDirect->GetYaxis()->SetTitleOffset(1.22);
 
  UPCTrigEffDirect->GetXaxis()->SetTitle("p_{T}^{dimuon}");

  UPCTrigEffMuonsAve->SetStats(0); // gets rid of annoying stat box

  UPCTrigEffDirect->SetMarkerStyle(8);
  UPCTrigEffDirect->SetMarkerColor(kRed);
  UPCTrigEffMuonsAve->SetLineColor(kBlue);

  UPCTrigEffDirect->Draw("p");
  UPCTrigEffMuonsAve->Draw("same");
 
  TLegend *l2 = new TLegend(0.20,0.70,0.45,0.80,NULL,"brNDC");
  l2->AddEntry(UPCTrigEffMuonsAve,"UPC Efficiency","");
  l2->AddEntry(UPCTrigEffDirect,"direct","p");
  l2->AddEntry(UPCTrigEffMuonsAve,"ave muons","p");
  l2->SetFillColor(10);
  l2->Draw();

  c2->Update();
  if (save) c2->SaveAs("./EfficiencyOutput/plots/"+title+"/DirToAve"+title+".png");





// Muons Eff

  TCanvas *c3 = new TCanvas("c3","c3",600,600);
  //c3->SetLogy();

  EffTrigMu1->GetXaxis()->SetRangeUser(0,3);
  EffTrigMu1->GetYaxis()->SetRangeUser(0,1);
  EffTrigMu1->GetXaxis()->SetTitleOffset(1);
  EffTrigMu1->GetYaxis()->SetTitleOffset(1.22);
 
  EffTrigMu1->GetXaxis()->SetTitle("p_{T}^{dimuon}");


  EffTrigMu2->SetStats(0); // gets rid of annoying stat box



  EffTrigMu1->SetMarkerStyle(8);
  EffTrigMu1->SetMarkerColor(kRed);
  EffTrigMu2->SetLineColor(kBlue);

  EffTrigMu1->Draw("p");
  EffTrigMu2->Draw("same");
 
  TLegend *l3 = new TLegend(0.20,0.70,0.45,0.80,NULL,"brNDC");
  l3->AddEntry(EffTrigMu2,"Efficiency","");
  l3->AddEntry(EffTrigMu1,"Muons 1","p");
  l3->AddEntry(EffTrigMu2,"Muons 2","p");
  l3->SetFillColor(10);
  l3->Draw();

  c3->Update();
  if (save) c3->SaveAs("./EfficiencyOutput/plots/"+title+"/MuonsEff"+title+".png");


}


