./start-hadoop.sh
hdfs dfs -rm -r ./output/output_lot2_exo1
hadoop jar hadoop-streaming-2.7.2.jar -file mapper_lot2_exo1.py -mapper "python3 mapper_lot2_exo1.py" -file reducer_lot2_exo1.py -reducer "python3 reducer_lot2_exo1.py" -input input/dataw_fro03.csv -output output/output_lot2_exo1

