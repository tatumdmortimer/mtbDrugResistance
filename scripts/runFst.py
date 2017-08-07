#!/usr/bin/env python

import subprocess

drugs = [
    "AMI",
    "CAP",
    "EMB",
    "Et",
    "INH",
    "K",
    "MOX",
    "OFL",
    "PRO",
    "PZA",
    "RIF",
    "STR"]

for drug in drugs:
    res = []
    susc = []

    with open("/home/tmortimer/data/mtuberculosis/drugResistance/susceptibilityInfo/{0}_susceptible.txt".format(drug), "r") as infile:
        for line in infile:
            line = line.strip()
            susc.append(line)

    with open("/home/tmortimer/data/mtuberculosis/drugResistance/susceptibilityInfo/{0}_resistant.txt".format(drug), "r") as infile:
        for line in infile:
            line = line.strip()
            res.append(line)

    with open("../in/samples.txt", "r") as infile:
        with open("wcFst_{0}.txt".format(drug), "w") as outfile:
            samples = []
            for line in infile:
                line = line.strip()
                samples.append(line)
            res_index = []
            susc_index = []
            for r in res:
                try:
                    res_index.append(str(samples.index(r)))
                except ValueError:
                    continue
            for s in susc:
                try:
                    susc_index.append(str(samples.index(s)))
                except ValueError:
                    continue
            target = ",".join(res_index)
            background = ",".join(susc_index)
            subprocess.call(
                ["/opt/PepPrograms/vcflib/bin/wcFst", "--target", target,
                "--background", background, "--file",
                "../in/vcflib_compatible.vcf.gz", "--type", "GT"],
                stdout=outfile)
