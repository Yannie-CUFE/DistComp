#! /bin/bash
hadoop fs -rm -r yangle/lmout1

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input yangle/test.csv \
-output yangle/lmout1 \
-file ./lmmapper.py \
-file ./lmreducer.py \
-mapper "python lmmapper.py" \
-reducer "python lmreducer.py" \
-numReduceTasks 1

hadoop fs -cat yangle/lmout1/part-*

export beta_hat=$(hadoop fs -cat yangle/lmout1/part-* | tail -n 1)
echo ${beta_hat}
export XTX=$(hadoop fs -cat yangle/lmout1/part-* | head -n 1)
echo ${XTX}

hadoop fs -rm -r yangle/lmout2
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input yangle/test.csv \
-output yangle/lmout2 \
-file ./lmsigma_mapper.py  \
-file ./lmsigma_reducer.py \
-mapper "python lmsigma_mapper.py" \
-reducer "python lmsigma_reducer.py" \
-cmdenv "beta_hat=${beta_hat}" \
-cmdenv "XTX=${XTX}" \
-numReduceTasks 1

hadoop fs -cat yangle/lmout2/part-*
