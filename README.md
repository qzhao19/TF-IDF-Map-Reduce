# TF-IDF-Map-Reduce

# Overview
The subject TF-IDF (Term Frequency-Inverse Document Frequency) consists in calculating the TF-IDF score for each word in a set of documents, for each document. We must provide 2 types of implementation for the MapReduce algorithm that will allow the calculation of the TF-IDF score:
- Map Reduce Python Hadoop Streaming
- Spark

The aim is to perform an experimental analysis to compare the performance of 2 implementations. To do this, we will perform a scalability test (the ability of a product to adapt to a change in the order of magnitude of demand) to compare the performance of the 2 implementations.

# Prerequisites

- Python 3.5
- pyspark

# Usage

The file file_generation.py allows you to automatically create.txt files in the desired language and of different sizes.  To do this, simply enter the following command in the terminal once you are in the folder containing the Python file: 

    python  file_generation.py  langue  taille  nombre_documents

The language can be here: "Latin", "French" or "english", the size can be: "1" or "2", the number of documents for the study will be 5, but you can create as many as you want.

To launch the MapReduce script, simply enter the following command in the terminal:

    chmod +x StepOneMapper.py
    chmod +x StepOneReducer.py
    cat test1.txt|./StepOneMapper.py|sort -k 1,1|./StepOneReducer.py>StepOneResult.txt
    cat StepOneResult_1.txt|./StepTwoMapper.py|sort -k 1,1|./StepTwoReducer.py>StepTwoResult.txt
    cat StepTwoResult_1.txt|./StepThreeMapper.py|sort -k 1,1|./StepThreeReducer.py

For run Spark, you should enter following command:

    python  tfidf-spark.py
