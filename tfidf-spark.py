
"""
PROJET BD DAUHPINE 
TF-IDF with Spark using PySpark
"""

import os 
from pyspark.sql import SparkSession

try :
    os.remove("metastore_db/db.lck")
    os.remove("metastore_db/dbex.lck")
except :
    pass

def buildSparkSession(app_name, memory='4g', executors=4):
    return SparkSession.builder\
                     .appName(app_name)\
                     .config('spark.executors.memory', memory)\
                     .config('spark.executors.instances', executors)\
                     .getOrCreate()
                
spark_session = buildSparkSession(app_name='ok-google')


import time
start = time.time()

#Creation of a vector where each element is a document (each document is transformed in a line)
import os 
files_list = os.listdir('files')
documents =[]

for file in files_list:
    filename ="files/"+file
    lines = spark_session.sparkContext.textFile(filename).collect()
    my_str =""   #String which correponds to the file 
    for line in lines:
        my_str = my_str+line
        documents.append(my_str)

sentenceData = spark_session.createDataFrame([
        (0.0, documents[0]),
        (1.0, documents[1]),
        (2.0, documents[2]),
        (3.0, documents[3]),
        (4.0, documents[4])
    ], ["label", "sentence"]) 


from pyspark.ml.feature import HashingTF, IDF, Tokenizer

#For each documents we separate its words 
tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
wordsData = tokenizer.transform(sentenceData)

#Maps a sequence of terms to their term frequencies using the hashing trick.
hashingTF = HashingTF(inputCol="words", outputCol="tf", numFeatures=20)

featurizedData = hashingTF.transform(wordsData)
#print(featurizedData.take(1))

"""
# CountVectorizer can also be used to get term frequency vectors
from pyspark.ml.feature import CountVectorizer
from pyspark.ml import Pipeline
countvectorizer = CountVectorizer(minTF=1.0, minDF=1.0, vocabSize=20, inputCol='words', outputCol='features(vocabSize), [index], [term frequency]')
featurizedData_countvect = countvectorizer.fit(wordsData).transform(wordsData).show(truncate=False)
"""

#Frequency of documents that contain a specific term
idf = IDF(inputCol="tf", outputCol="tfidf")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)
rescaledData.select("words", "tfidf").show(truncate=False)

"""
#Summation of all terms TF-IDF

from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType

sum_ = udf(lambda v: float(v.values.sum()), DoubleType())
rescaledData.withColumn("idf_sum", sum_("idf")).show()
"""

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
#Have an understandable format for time
print("Execution time=", "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
