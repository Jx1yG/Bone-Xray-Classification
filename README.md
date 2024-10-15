# Bone X-ray Classification with Deep Learning and Transfer Learning

This project implements a deep learning model to classify bone X-ray images into normal and abnormal categories and by body part (e.g., elbow, finger, forearm). We utilize the **Stanford MURA dataset** and apply transfer learning using **ResNet50** to achieve competitive performance in detecting abnormalities and identifying the anatomical region.

## Table of Contents
- Project Overview
- Installation
- Dataset
- Usage
- Results
- License
- Acknowledgments
- References

## Project Overview
X-ray imaging is a commonly used diagnostic tool for bone conditions. In this project, we build a Convolutional Neural Network (CNN) using transfer learning to automate the classification of X-ray images from the Stanford MURA dataset. The model predicts whether the image is normal or abnormal and identifies the body part.

## Installation
To run this project, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bone-xray-classification.git
   cd bone-xray-classification
   ```

2. **Install required dependencies**:
   Install the necessary Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

## Dataset
This project uses the **Stanford MURA dataset**, which is not included in this repository due to licensing restrictions. To obtain the dataset, follow the steps below:

1. Visit the [Stanford AIMI MURA dataset page](https://stanfordaimi.azurewebsites.net/datasets/3e00d84b-d86e-4fed-b2a4-bfe3effd661b).
2. Request access and download the dataset following the instructions provided on the website.
3. Once downloaded, place the dataset in the following structure within the project directory:
   ```bash
   /project-directory
   └── data/
       └── MURA-v1.1/
           ├── train/
           ├── valid/
           └── ...
   ```
4. Ensure you comply with the [MURA dataset license](https://stanfordaimi.azurewebsites.net/datasets/3e00d84b-d86e-4fed-b2a4-bfe3effd661b) when using the dataset.

## Usage
Once you have set up the dataset, you can run the following commands to train the model and evaluate its performance:

1. **Preprocess the dataset**:
   Resize images and normalize pixel values:
   ```bash
   python data_processing.py
   ```

2. **Train the model**:
   To train the model, use the following command:
   ```bash
   python train_model.py
   ```

3. **model architecture**:
   Once training is complete, evaluate the model using:
   ```bash
   python model_architecture.py
   ```

## Results
The model achieved the following performance metrics:
- **Abnormality Detection**: 87.2% accuracy, 83% precision, 85% recall
- **Body Part Classification**: 82.6% accuracy, 80% precision

The training and validation accuracy curves and confusion matrices for both tasks are shown in the `results/` folder.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code with proper attribution. See the `LICENSE` file for more details.

**Please note**: The MURA dataset is subject to its license and cannot be redistributed. You must download the dataset from the official [Stanford AIMI website](https://stanfordaimi.azurewebsites.net/datasets/3e00d84b-d86e-4fed-b2a4-bfe3effd661b) and comply with its terms.

## Acknowledgments
We would like to acknowledge the Stanford Machine Learning Group for providing the MURA dataset used in this project.

## References
1. S. Rajpurkar et al., "MURA: Large dataset for abnormality detection in musculoskeletal radiographs," arXiv preprint arXiv:1712.06957, 2017.
2. K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 2016, pp. 770–778.
3. A. Krizhevsky, I. Sutskever, and G. Hinton, "ImageNet classification with deep convolutional neural networks," in *Advances in Neural Information Processing Systems*, 2012, pp. 1097–1105.
