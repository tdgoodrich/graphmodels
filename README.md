# MASE November Project

### Contact Info 
Name: Timothy Goodrich  
Email: tdgoodri@ncsu.edu

### High Level Goal
Train a cluster-based learner on software engineering bug data, and tune it with differential evolution.  

### Details
1. Scikit-Learn will be used for data mining, and differential evolution will be implemented in C++. 
2. The data sets are {ant, camel, ivy, jedit, log4j, lucene, poi, synapse, velocity, xalan, xerces} from the tera-PROMISE repository (defect, CK). These were specifically chosen to match the datasets from "How to Learn Useful Changes to Software Projects" by Krishna, et al. 
3. I am planning on using the DBSCAN clustering algorithm, based on the overview seen here: [http://scikit-learn.org/stable/modules/clustering.html](http://scikit-learn.org/stable/modules/clustering.html).
4. If I have time I might run a DE tuner on the DE tuner, we will see how fast the clustering methods run.

### How to run

`make [dataset]` (no `.arff`) to run logistic regression with 10-fold cv, will print abcd report

### Datasets

[Link to PROMISE Repository](http://openscience.us/repo/defect/ck/)

Currently available:  
* ant
* camel
* ivy
* jedit
* log4j
* lucene
* poi
* synapse
* velocity
* xalan
* xerces