pushd $(dirname $0) > /dev/null

# deletes tf_files folder if already exists
rm -rf tf_files

python -m retrain \
    --bottleneck_dir=tf_files/bottlenecks \
    --how_many_training_steps=500 \
    --model_dir=tf_files/models/ \
    --summaries_dir=tf_files/training_summaries/mobilenet_0.50_224 \
    --output_graph=tf_files/retrained_graph.pb \
    --output_labels=tf_files/retrained_labels.txt \
    --architecture=mobilenet_0.50_224 \
    --image_dir=dataset
popd > /dev/null
