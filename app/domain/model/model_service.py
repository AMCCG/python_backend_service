import numpy as np
import tensorflow as tf


class ModelService:

    def __init__(self):
        self.input_details = None
        self.output_details = None
        self.interpreter = None
        self.load_tflite_model()

    def load_tflite_model(self):
        export_dir = 'app/domain/model/saved_model/1'
        converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
        tflite_model = converter.convert()
        # Load TFLite model and allocate tensors.
        self.interpreter = tf.lite.Interpreter(model_content=tflite_model)
        self.interpreter.allocate_tensors()
        # Get input and output tensors.
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        print(self.input_details)
        print(self.output_details)
        pass

    def predict(self, input: int) -> int:
        to_predict = np.array([[input]], dtype=np.float32)
        print("to predict {}".format(to_predict))
        self.interpreter.set_tensor(self.input_details[0]['index'], to_predict)
        self.interpreter.invoke()
        tflite_result = self.interpreter.get_tensor(self.output_details[0]['index'])
        result = round(np.array(tflite_result)[0][0])
        print(result)
        return str(result)
