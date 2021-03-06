from zisan.ObjDetect.Interface import ObjDetect_train, ObjDetect_Preprocess
import os

'''
Before running train, you must keep the data path in the correct position
Details you can read the Doc: http://jintupersonal.com/zisan/Doc/

'''


if __name__ == "__main__":  
    current_path = os.path.dirname(__file__)
    
    pr=ObjDetect_Preprocess(classnames=['Yourclass1','Yourclass2'],currentpath=current_path) # cuurentpath is needed
    #pr.clear_data() #clear all data  
    trainModel=ObjDetect_train(current_path)
    trainModel.Run(cfg='yolov3-tiny.cfg',epochs=20)
    