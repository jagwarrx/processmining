# !pip install pm4py
from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.visualization.petrinet import factory as vis_factory
import cv2

def Alphaminer(file):
	log = xes_importer.import_log(file)
	net, initial_marking, final_marking = alpha_miner.apply(log)
	gviz = vis_factory.apply(net, initial_marking, final_marking)
	location = "/mnt/c/Users/harim/Downloads/alphaminer.png"
	vis_factory.save(gviz, location)
	#vis_factory.view(gviz)
	return location

def Hueristics(file):
	#import os
	from pm4py.objects.log.importer.xes import factory as xes_importer
	log = xes_importer.import_log(file)

	from pm4py.algo.discovery.dfg import factory as dfg_factory
	dfg = dfg_factory.apply(log)

	from pm4py.visualization.dfg import factory as dfg_vis_factory
	gviz = dfg_vis_factory.apply(dfg, log=log, variant="frequency")
	location = "/mnt/c/Users/harim/Downloads/dfg.png"
	dfg_vis_factory.save(gviz, location)
	return location