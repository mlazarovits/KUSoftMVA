import numpy as np
from scipy import interp
import matplotlib.pyplot as plt
from itertools import cycle
import copy
from sklearn.metrics import roc_curve, auc
from ROOT import TH1D, TFile, TEfficiency, TCanvas, TGraph, TLatex, TGraphAsymmErrors, TMultiGraph, TLegend, SetOwnership


def plotLoss(history,outName):
	plt.figure()
	plt.plot(history.history['val_loss'],label='val loss')
	plt.plot(history.history['loss'],label='training loss')
	plt.xlabel('Epoch')
	plt.ylabel('Loss')
	plt.legend()
	plt.title(outName+' Loss')
	plt.savefig('plots/'+outName+'_Loss.pdf',dpi=500)
	plt.close()


def plotPrecision(history,outName):
	plt.figure()
	plt.plot(history.history['val_precision_1'],label='val precision')
	plt.plot(history.history['precision_1'],label='training precision')
	plt.xlabel('Epoch')
	plt.ylabel('Precision')
	plt.legend()
	plt.title(outName+' Precision')
	plt.savefig('plots/'+outName+'_Precision.pdf',dpi=500)
	plt.close()


	



def makeEfficiency(y_test,y_predClasses,pt,definedIds,outName):
	nClasses = len(definedIds)
	passedHists = [TH1D("num_"+str(ID), "label "+str(ID), 41, -0.5, 40.5 ) for i,ID in enumerate(definedIds)]
	totalHists =  [TH1D("eff_"+str(ID), "label "+str(ID), 41, -0.5, 40.5 ) for i,ID in enumerate(definedIds)]
	
	#break it down by class
	for j, ID in enumerate(definedIds):
		for i, n in enumerate(zip(y_test,y_predClasses)):
			if n[0] == ID:
				if n[0] == n[1]: #correct match
					passedHists[j].Fill(pt.iloc[i])
					totalHists[j].Fill(pt.iloc[i])
				elif n[0] != n[1]: #incorrect match
					totalHists[j].Fill(pt.iloc[i])
	goodEff = [ TEfficiency(passedHists[i],totalHists[i]) for i in range(nClasses) ]
	for i, ID in enumerate(goodEff):
		ID.SetTitle("class "+str(definedIds[i])+" eff")
	outfile = TFile("./test.root","RECREATE")

	[ outfile.WriteTObject(x) for x in goodEff ]
	plotEfficiency(goodEff,outName,outfile)

	
	


def plotROCcurves(y_test,y_score,n_classes,outName):
	# Plot linewidth.
	lw = 2
	# Compute ROC curve and ROC area for each class
	fpr = dict()
	tpr = dict()
	roc_auc = dict()
	# print(y_test.shape,y_score.shape,n_classes)
	for i in range(n_classes):
		# print(i)
		fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
		roc_auc[i] = auc(fpr[i], tpr[i])

	# Compute micro-average ROC curve and ROC area
	fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
	roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

	# Compute macro-average ROC curve and ROC area

	# First aggregate all false positive rates
	all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

	# Then interpolate all ROC curves at this points
	mean_tpr = np.zeros_like(all_fpr)
	for i in range(n_classes):
	    mean_tpr += interp(all_fpr, fpr[i], tpr[i])

	# Finally average it and compute AUC
	mean_tpr /= n_classes

	fpr["macro"] = all_fpr
	tpr["macro"] = mean_tpr
	roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

	# Plot all ROC curves
	plt.figure()
	plt.plot(fpr["micro"], tpr["micro"],
	         label='micro-average ROC curve (area = {0:0.2f})'
	               ''.format(roc_auc["micro"]),
	         color='deeppink', linestyle=':', linewidth=4)

	plt.plot(fpr["macro"], tpr["macro"],
	         label='macro-average ROC curve (area = {0:0.2f})'
	               ''.format(roc_auc["macro"]),
	         color='navy', linestyle=':', linewidth=4)

	colors = cycle(['aqua', 'darkorange', 'cornflowerblue','darkviolet','limegreen'])
	for i, color in zip(range(n_classes), colors):
	    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
	             label='ROC curve of class {0} (area = {1:0.2f})'
	             ''.format(i, roc_auc[i]))

	plt.plot([0, 1], [0, 1], 'k--', lw=lw)
	plt.xlim([0.0, 1.0])
	plt.ylim([0.0, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title(outName+'ROC Curves')
	plt.legend(loc="lower right")
	plt.savefig('plots/'+outName+"_ROCcurves.pdf",dpi=500)
	plt.close()


	# Zoom in view of the upper left corner.
	plt.figure(2)
	plt.xlim(0, 0.2)
	plt.ylim(0.8, 1)
	plt.plot(fpr["micro"], tpr["micro"],
	         label='micro-average ROC curve (area = {0:0.2f})'
	               ''.format(roc_auc["micro"]),
	         color='deeppink', linestyle=':', linewidth=4)

	plt.plot(fpr["macro"], tpr["macro"],
	         label='macro-average ROC curve (area = {0:0.2f})'
	               ''.format(roc_auc["macro"]),
	         color='navy', linestyle=':', linewidth=4)

	colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
	for i, color in zip(range(n_classes), colors):
	    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
	             label='ROC curve of class {0} (area = {1:0.2f})'
	             ''.format(i, roc_auc[i]))

	plt.plot([0, 1], [0, 1], 'k--', lw=lw)
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title(outName+'ROC Curves zoomed')
	plt.legend(loc="lower right")
	plt.savefig('plots/'+outName+"_ROCcurvesZoom.pdf",dpi=500)
	plt.close()




def plotEfficiency(effs,outName,outFile):
	cv = TCanvas("cv","cv",800,600)
	leg = TLegend(0.35,0.2,0.95,0.4)
	gr_effs = []
	mg = TMultiGraph()
	cv.cd()
	cv.SetGridx()
	cv.SetGridy()
	cv.SetLeftMargin(0.13)
	cv.SetRightMargin(0.04)
	cv.SetBottomMargin(0.15)
	cv.SetTopMargin(0.085)
	effs[0].Draw("AP")
	cv.Update()
	gr_effs.append(effs[0].GetPaintedGraph())
	for i in range(1,len(effs)):
		effs[i].Draw("same")
		cv.Update()
		gr_effs.append(effs[i].GetPaintedGraph())
	cv.Update()
	chopcolor = int(len(gr_effs))
	chopmarker = int(len(gr_effs)/2)
	for i in range(len(gr_effs)):
		gr_effs[i].SetMarkerSize(1.5)
		gr_effs[i].SetLineWidth(2)
		gr_effs[i].GetYaxis().SetRangeUser(0.0,1.0)
		if int(i / chopmarker) == 0:
			gr_effs[i].SetMarkerStyle(22) #triangle
		elif int(i / chopmarker) == 1:
			gr_effs[i].SetMarkerStyle(21) #square
		elif int(i /chopmarker) == 2:
			gr_effs[i].SetMarkerStyle(20)  #circle
		if int(i % chopcolor) == 0:
			gr_effs[i].SetMarkerColor(632-7)
			gr_effs[i].SetLineColor(632-7)
		elif int(i % chopcolor) == 1:
			gr_effs[i].SetMarkerColor(600-7)
			gr_effs[i].SetLineColor(600-7)
		elif int(i % chopcolor) == 2:
			gr_effs[i].SetMarkerColor(416-7)
			gr_effs[i].SetLineColor(416-7)
		else:
			gr_effs[i].SetMarkerColor(432-7)
			gr_effs[i].SetLineColor(432-7)
		leg.AddEntry(gr_effs[i])
	for i, gr in enumerate(gr_effs):
		mg.Add(copy.deepcopy(gr_effs[i]))
	leg.SetTextFont(132)
	leg.SetTextSize(0.03)
	leg.SetFillColor(0)
	leg.SetLineColor(0)
	leg.SetShadowColor(0)
	mg.Draw("AP")
	leg.Draw("SAME")
	cv.Update()
	g_PlotTitle = outName
	mg.GetXaxis().SetTitle('Muon pT (GeV)')
	mg.GetYaxis().SetTitle("#epsilon")
	l = TLatex()
	l.SetTextFont(132)
	l.SetNDC()
	l.SetTextSize(0.035)
	l.SetTextFont(42)
	l.SetTextSize(0.03)
	l.SetTextFont(61)
	l.DrawLatex(0.16,0.92,"CMS")
	l.SetTextFont(52)
	l.DrawLatex(0.21,0.92,"Preliminary")
	l.SetTextFont(132)
	l.SetNDC()
	l.SetTextSize(0.05)
	l.SetTextFont(132)
	l.DrawLatex(0.40,0.92,g_PlotTitle)
	cv.Update()
	outFile.cd()
	outFile.WriteTObject(cv)
	cv.Close()




