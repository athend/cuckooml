# Cuckoo Sandbox ML GSoC Proposal




![Alt text](img/malware.png?raw=true "Process")

                                            Malware Analysis Framework Schematic



## Review of Data Sample

There are 199 total malware reports given to us. The reports were studied and from the analysis more relevant details for the project were uncovered

## Report Analysis

- info - This is the Cuckoo metadata
- signatures - Representative of malicious behavior or indicator (Severity levels etc)
- target - Metadata of the given file
- virustotal - Pretty important and Gets antivirus signatures from VirusTotal.com for various results
- static - Static analysis
- dropped - Dropped files analysis
- behavior - Different classes that analyze behavior dynamically
- debug - Debug information
- strings - Extract strings from analyzed file
- network - Network analysis

Referred to https://github.com/cuckoosandbox/cuckoo/tree/master/modules/processing & http://docs.cuckoosandbox.org/en/latest/customization/processing/ to gain understanding of the sample reports

## Features

1. JSON data - parse stage  
2. JSON data - run relevant queries on the dataset to aid in clustering  

## Clustering, Classifying and Anomaly Detection

Studying of two learning concepts seem fruitful for malware analysis:  
1. Clustering of behavior - which enables identifying novel classes of malware with similar behavior  
2. Classification of behavior - which allows to assign malware to known classes of behavior  

A set of malware binaries often contains similar variants of the same family which exhibit almost identical behavioral patterns. As a consequence, the embedded reports form dense clouds in the vector space. We  can exploit this dense representation by subsuming groups of similar behavior using prototypes — reports being typical for a group of homogeneous behavior. By restricting the
computation of learning methods to prototypes and later propagating results to all embedded data, we can accelerate clustering as well as classification techniques. The extracted prototypes correspond to regular reports and thus can be easily inspected by a human analyst.


![Alt text](img/clust.png?raw=true "Cluster")

Behavior analysis using prototypes: (a) prototypes of data, (b) clustering using pro-
totypes, and (c) classification using prototypes. Black lines in Figure (b) indicate prototypes
joined by linkage clustering. Black lines in Figure (c) represent the class decision boundary.


Algorithm 1 Prototype extraction

1: prototypes ← ∅  
2: distance [ x ] ← ∞ for all x ∈ reports  
3: while max ( distance ) > dp do  
4: choose z such that distance [ z ]= max ( distance )  
5: for x ∈ reports and x ≠ z do  
6: if distance [ x ] > || ˆ φ ( x ) − ˆ φ ( z ) || then  
7: distance [ x ] ←|| ˆ φ ( x ) − ˆ φ ( z ) ||  
8: add z to prototypes 


Algorithm 2 Clustering using prototypes 

1: for z , z 0 ∈ prototypes do  
2: distance [ z , z0 ] ←|| ˆ φ ( z ) − ˆ φ ( z0 ) ||  
3: while min ( distance ) < dc do  
4: merge clusters z , z0 with minimum distance [ z , z0 ]  
5: update distance using complete linkage  
6: for x ∈ reports do  
7: z ← nearest prototype to x  
8: assign x to cluster of z  
9: reject clusters with less than m members 



Algorithm 3 Classification using prototypes 

1: for x ∈ reports do  
2: z ← nearest prototype to x  
3: if || ˆ φ ( z ) − ˆ φ ( x ) || > d r then  
4: reject x as unknown class  
5: else  
6: assign x to cluster of z 

### Enter Incremental Analysis - the whole point

Based on a joint formulation of classification and clustering, we can have an incremental approach to analysis of
malware behavior. To realize an incremental analysis, we need to keep track of intermediate results, such as clusters 
determined during previous runs of the algorithm. Fortunately, the concept of prototypes enables us to store discovered
clusters in a concise representation and, moreover, provides a significant speed-up if used for classification.

Algorithm 4 Incremental Analysis 

1: rejected ← ∅ , prototypes ← ∅  
2: for reports ← data source ∪ rejected do  
3: classify reports to known clusters using prototypes . see Algorithm 3  
4: extract prototypes from remaining reports . see Algorithm 1  
5: cluster remaining reports using prototypes . see Algorithm 2  
6: prototypes ← prototypes ∪ prototypes of new clusters  
7: rejected ← rejected reports from clustering 


The reports to be analyzed are received from a data source in regular intervals. In the first processing phase, the in-
coming reports are classified using prototypes of known clusters (line 3 of algorithm). Thereby, variants
of known malware are efficiently identified and filtered from further analysis. In the following phase,
prototypes are extracted from the remaining reports and subsequently used for clustering of 
behavior (line 4–5). The prototypes of the new clusters are stored along with the original set of prototypes,
such that they can be applied in a next run for classification. This procedure—alternating between classification 
and clustering—is repeated incrementally, where the amount of unknown malware is continuously reduced and the
prevalent classes of malware are automatically discovered.
The number of reports available during one incremental run, however, may be insufficient for determining all
clusters of malware behavior. For example, infrequent malware variants may only be represented by few samples 
in the embedding space. To compensate for this lack of information, we reject clusters with fewer than
m members and feed the corresponding reports back to the data source. Consequently, infrequent malware is ag-
glomerated until sufficient data is available for clustering. 


