﻿import os, sys
lib_path = os.path.abspath(os.path.join('..', 'PcaSycData'))
sys.path.append(lib_path)

from genpop_data import GenPopData
from pca_synth_data import PcaSynthData
from pca_alleles import AllelesPCA
from population import Population

if False:
    psd = PcaSynthData(5, 3.5, 2, 800)
    psd.test()
elif False:
    # read and process data in GenPop file 'genepop_western_alaska_chinook_RAD.txt'
    gpd = GenPopData("genepop_western_alaska_chinook_RAD.txt")
     gpd.toFile('alaska_chinook.pickle')
    apop = Population(None)
    apop.fromFile('alaska_chinook.pickle')

    fishies = gpd.fishies()                     # list of all fish (and alleles) in file
    afishies = apop.fishies()
    fishies = gpd.fishies(gpd.popnames()[2])    # list of all fish (and alleles) in third population
    afishies = apop.fishies(apop.popnames()[2])

    alleles = gpd.alleles()                     # all alleles of all populations
    alleles = gpd.alleles(gpd.popnames()[2])    # all alleles in third population
elif True:
    #apop = GenPopData("genepop_western_alaska_chinook_RAD.txt")
    apop = Population(None)
    apop.fromFile('alaska_chinook.pickle')
    apca = AllelesPCA(apop)
    mean = apca.popmean(apop.popnames()[2])
