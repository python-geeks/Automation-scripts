import argparse
import os

import cv2

from keras.applications.vgg16 import VGG16, preprocess_input

import numpy as np

from sklearn.cluster import KMeans

from tensorflow.keras.models import Model


parser = argparse.ArgumentParser(description='Summarize the given text')
parser.add_argument('-p', '--path', help="Path to the directory", type=str)
parser.add_argument('-c', '--cluster', help="Number of cluster", type=int)
parser.add_argument('-o', '--output', help="output location (default: OUTPUT)",
                    type=str, default="./OUTPUT/")
args = parser.parse_args()

if not (args.path):
    parser.error("input path is not provided")
if not (args.cluster):
    parser.error("number of cluster is not provided")

PATH_TO_FILES = args.path
CLUSTER = args.cluster
OUTPUT = args.output


def get_model():
    base_model = VGG16(weights='imagenet', include_top=True)
    model = Model(inputs=base_model.input,
                  outputs=base_model.layers[-2].output)
    return model


def get_files(path_to_files, size):
    fn_imgs = []
    files = [file for file in os.listdir(path_to_files)]
    for file in files:
        img = cv2.resize(cv2.imread(os.path.join(path_to_files, file)), size)
        fn_imgs.append([file, img])
    return dict(fn_imgs)


def feature_vector(img_arr, model):
    if img_arr.shape[2] == 1:
        img_arr = img_arr.repeat(3, axis=2)
    arr4d = np.expand_dims(img_arr, axis=0)
    arr4d_pp = preprocess_input(arr4d)
    return model.predict(arr4d_pp)[0, :]


def feature_vectors(imgs_dict, model):
    f_vect = {}
    for fn, img in imgs_dict.items():
        f_vect[fn] = feature_vector(img, model)
    return f_vect


def clustering(img_feature_vector):
    images = list(img_feature_vector.values())
    kmeans = KMeans(n_clusters=CLUSTER, init='k-means++')
    kmeans.fit(images)
    y_kmeans = kmeans.predict(images)
    file_names = list(imgs_dict.keys())
    return y_kmeans, file_names


def separate(y_kmeans, file_names):
    n_clusters = CLUSTER
    cluster_path = OUTPUT
    path_to_files = PATH_TO_FILES
    if (not os.path.exists(cluster_path)):
        os.mkdir(cluster_path)
    for c in range(0, n_clusters):
        if not os.path.exists(cluster_path + 'cluster_' + str(c)):
            os.mkdir(cluster_path + 'cluster_' + str(c))
    for fn, cluster in zip(file_names, y_kmeans):
        image = cv2.imread(os.path.join(path_to_files, fn))
        cv2.imwrite(cluster_path + 'cluster_' + str(cluster) + '/' + fn, image)


if __name__ == '__main__':

    imgs_dict = get_files(path_to_files=PATH_TO_FILES, size=(224, 224))
    model = get_model()
    img_feature_vector = feature_vectors(imgs_dict, model)
    y_kmeans, file_names = clustering(img_feature_vector)
    separate(y_kmeans, file_names)
