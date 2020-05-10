import numpy as np
from scipy import interp
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.metrics import roc_curve, auc
from ROOT import TH1D, TFile, TEfficiency, TCanvas, TGraph


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





def plotEfficiency(y_test,y_predClasses,x_test,definedIds):
	nClasses = len(definedIds)
	passedHists = [TH1D("num_"+str(i), "label "+str(ID), 41, -0.5, 40.5 ) for i,ID in enumerate(definedIds)]
	totalHists =  [TH1D("den_"+str(i), "label "+str(ID), 41, -0.5, 40.5 ) for i,ID in enumerate(definedIds)]

	#break it down by class
	for j, ID in enumerate(definedIds):
		for i, n in enumerate(zip(y_test,y_predClasses)):
			print(i,j)
			if n[0] == ID:
				if n[0] == n[1]: #correct match
					passedHists[j].Fill(x_test['Muon_pt'].loc[i])
					totalHists[j].Fill(x_test['Muon_pt'].loc[i])
				elif n[0] != n[1]: #incorrect match
					totalHists[j].Fill(x_test['Muon_pt'].loc[i])



	goodEff = [ TEfficiency(passedHists[i],totalHists[i]) for i in range(nClasses) ]


	outfile = TFile("./test.root","RECREATE")
	[ outfile.WriteTObject(x) for x in goodEff ]


def plotROCcurves(y_test,y_score,classes,outName):
	n_classes = len(classes)
	# Plot linewidth.
	lw = 2

	# Compute ROC curve and ROC area for each class
	fpr = dict()
	tpr = dict()
	roc_auc = dict()
	for i in range(n_classes):
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
	             ''.format(classes[i], roc_auc[i]))

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
	             ''.format(classes[i], roc_auc[i]))

	plt.plot([0, 1], [0, 1], 'k--', lw=lw)
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title(outName+'ROC Curves zoomed')
	plt.legend(loc="lower right")
	plt.savefig('plots/'+outName+"_ROCcurvesZoom.pdf",dpi=500)
	plt.close()



