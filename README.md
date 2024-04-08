# NTT data machine learning code

## Description of each file:
1. *clip_images*: clips images based on bounding box defined in CSV file
2. *convert_tf_lite.ipynb*: converts the Tensorflow lite to a TensorFlow lite model
3. *metadata_writer_for_image_classifier.py*: adds metadata to a TensorFlow lite model
4. *transfer_learning_with_hub.ipynb*: file to train a custom tensor flow model using transfer learning
5. *roboflow_dataset*: folder contains the dataset obtained from roboflow identifying router features

# How to run code:
1. Run the *clip_images.py* file ```python3 clip_images.py```
2. To create a TensorFlow model run the *transfer_learning_with_hub.ipynb* file.
3. Run *convert_tf_lite.ipynb* updating the path of the saved model to the location where the model from the previous step is exported.
4. Run the *metadata_writer_for_image_classifier.py* ```python3 metadata_writer_for_image_classifier.py --label_file=location_of_label_file --export_directory=export_dir_for_model --model_file=location_of_model``` where *location_of_label_file* is the plain text label file that gives the labels of the model,*export_dir_model* is the export directory for the model,*location_of_model* is the location where the tflite model without metadata is stored
5. Add the exported model in the res folder of the Android application
