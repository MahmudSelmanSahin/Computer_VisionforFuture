# Computer Vision and Software Terms Glossary

A comprehensive glossary of terms for developers working on computer vision projects.

## Table of Contents
- [Computer Vision Fundamentals](#computer-vision-fundamentals)
- [Image Processing](#image-processing)
- [Machine Learning & Deep Learning](#machine-learning--deep-learning)
- [Neural Network Architectures](#neural-network-architectures)
- [Object Detection & Recognition](#object-detection--recognition)
- [Image Segmentation](#image-segmentation)
- [Feature Detection & Extraction](#feature-detection--extraction)
- [Frameworks & Libraries](#frameworks--libraries)
- [Software Development Terms](#software-development-terms)
- [Performance Metrics](#performance-metrics)

---

## Computer Vision Fundamentals

### Computer Vision (CV)
A field of artificial intelligence that enables computers to derive meaningful information from digital images, videos, and other visual inputs.

### Image
A 2D array of pixels representing visual information. Can be grayscale (single channel) or color (typically RGB with 3 channels).

### Pixel
The smallest unit of a digital image, representing a single point with color and intensity values.

### Resolution
The dimensions of an image, typically expressed as width × height in pixels (e.g., 1920×1080).

### Color Space
A specific organization of colors (e.g., RGB, HSV, LAB, grayscale) used to represent images.

### RGB
Red, Green, Blue color model where colors are represented by combining these three primary colors.

### Grayscale
An image representation using only shades of gray, typically ranging from 0 (black) to 255 (white).

### Channel
A single component of an image (e.g., R, G, or B in RGB images).

---

## Image Processing

### Preprocessing
Operations performed on images before feeding them to a model, including resizing, normalization, and augmentation.

### Normalization
Scaling pixel values to a standard range (e.g., 0-1 or -1 to 1) to improve model training.

### Image Augmentation
Techniques to artificially expand training datasets by applying transformations like rotation, flipping, scaling, and color adjustments.

### Filtering
Applying kernels or masks to images to enhance or extract specific features (e.g., edge detection, blurring).

### Convolution
A mathematical operation that applies a filter/kernel to an image to extract features.

### Kernel/Filter
A small matrix used in convolution operations to detect patterns like edges, corners, or textures.

### Edge Detection
Identifying boundaries where pixel intensities change sharply (e.g., Canny, Sobel edge detectors).

### Thresholding
Converting grayscale images to binary by setting pixels above a threshold to white and below to black.

### Morphological Operations
Image processing operations based on shapes, including erosion, dilation, opening, and closing.

### Histogram
A graphical representation of pixel intensity distribution in an image.

### Histogram Equalization
Technique to improve image contrast by redistributing pixel intensities.

---

## Machine Learning & Deep Learning

### Machine Learning (ML)
A subset of AI where systems learn from data to make predictions or decisions without explicit programming.

### Deep Learning (DL)
A subset of machine learning using neural networks with multiple layers to learn hierarchical representations.

### Neural Network
A computing system inspired by biological neural networks, consisting of interconnected nodes (neurons) organized in layers.

### Training
The process of adjusting model parameters using labeled data to minimize prediction errors.

### Inference
Using a trained model to make predictions on new, unseen data.

### Epoch
One complete pass through the entire training dataset during model training.

### Batch Size
The number of training samples processed before updating model parameters.

### Learning Rate
A hyperparameter controlling how much model weights are adjusted during training.

### Overfitting
When a model learns training data too well, including noise, resulting in poor generalization to new data.

### Underfitting
When a model is too simple to capture the underlying patterns in the data.

### Transfer Learning
Using a pre-trained model on one task as a starting point for a related task.

### Fine-tuning
Adjusting pre-trained model weights on a new dataset for a specific task.

### Loss Function
A measure of how well the model's predictions match the actual labels, used to guide training.

### Optimizer
An algorithm (e.g., Adam, SGD) that adjusts model weights to minimize the loss function.

### Gradient Descent
An optimization algorithm that iteratively adjusts parameters in the direction that reduces the loss.

### Backpropagation
Algorithm for computing gradients of the loss function with respect to network weights.

---

## Neural Network Architectures

### Convolutional Neural Network (CNN)
A deep learning architecture specifically designed for processing grid-like data such as images.

### Convolutional Layer
A layer that applies convolution operations to extract spatial features from inputs.

### Pooling Layer
A layer that reduces spatial dimensions of feature maps, commonly using max pooling or average pooling.

### Fully Connected Layer (Dense Layer)
A layer where every neuron is connected to every neuron in the previous layer.

### Activation Function
A non-linear function applied to neuron outputs (e.g., ReLU, Sigmoid, Tanh, Softmax).

### ReLU (Rectified Linear Unit)
An activation function that outputs the input if positive, otherwise zero: f(x) = max(0, x).

### Dropout
A regularization technique that randomly deactivates neurons during training to prevent overfitting.

### Batch Normalization
A technique to normalize layer inputs, improving training speed and stability.

### ResNet (Residual Network)
A CNN architecture using skip connections to enable training of very deep networks.

### VGG
A CNN architecture known for using small 3×3 filters in deep networks.

### Inception
A CNN architecture using multiple filter sizes in parallel to capture features at different scales.

### MobileNet
A lightweight CNN architecture designed for mobile and embedded devices.

### EfficientNet
A family of models that balance network depth, width, and resolution for optimal efficiency.

---

## Object Detection & Recognition

### Object Detection
Identifying and locating objects in images by drawing bounding boxes around them.

### Object Recognition/Classification
Identifying what objects are present in an image without necessarily locating them.

### Bounding Box
A rectangle defined by coordinates (x, y, width, height) that encloses an object in an image.

### Anchor Box
Pre-defined bounding boxes of various sizes and aspect ratios used in object detection algorithms.

### Region Proposal
A technique to identify regions in an image likely to contain objects.

### R-CNN (Region-based CNN)
An object detection approach using region proposals and CNNs.

### Fast R-CNN
An improved version of R-CNN with faster training and inference.

### Faster R-CNN
Further improvement using Region Proposal Networks (RPNs) for end-to-end training.

### YOLO (You Only Look Once)
A real-time object detection algorithm that predicts bounding boxes and classes in a single forward pass.

### SSD (Single Shot Detector)
A real-time object detection method using multiple feature maps at different scales.

### Non-Maximum Suppression (NMS)
A post-processing technique to eliminate duplicate detections by keeping only the highest confidence boxes.

### Intersection over Union (IoU)
A metric measuring overlap between predicted and ground truth bounding boxes.

---

## Image Segmentation

### Segmentation
Partitioning an image into multiple segments or regions, typically to identify objects or boundaries.

### Semantic Segmentation
Classifying each pixel in an image into a category (e.g., road, sky, person) without distinguishing individual instances.

### Instance Segmentation
Identifying and delineating each distinct object instance in an image.

### Panoptic Segmentation
Combining semantic and instance segmentation to label all pixels with class and instance information.

### U-Net
A CNN architecture for image segmentation, featuring an encoder-decoder structure with skip connections.

### Mask R-CNN
An extension of Faster R-CNN that adds a branch for predicting segmentation masks.

### FCN (Fully Convolutional Network)
A network architecture that uses only convolutional layers for dense prediction tasks like segmentation.

---

## Feature Detection & Extraction

### Feature
A distinctive characteristic or property extracted from an image (e.g., edges, corners, textures).

### Feature Extraction
The process of identifying and extracting relevant features from raw image data.

### Feature Vector
A numerical representation of image features used for comparison or classification.

### Keypoint
A distinctive point in an image (e.g., corners, blobs) that can be reliably detected.

### Descriptor
A numerical representation of image region around a keypoint, used for matching.

### SIFT (Scale-Invariant Feature Transform)
An algorithm for detecting and describing local features invariant to scale and rotation.

### SURF (Speeded Up Robust Features)
A faster alternative to SIFT for feature detection and description.

### ORB (Oriented FAST and Rotated BRIEF)
A fast, free alternative to SIFT/SURF for feature detection.

### HOG (Histogram of Oriented Gradients)
A feature descriptor used for object detection, particularly for pedestrian detection.

---

## Frameworks & Libraries

### TensorFlow
An open-source deep learning framework developed by Google.

### PyTorch
An open-source deep learning framework developed by Facebook, known for its dynamic computation graph.

### Keras
A high-level neural networks API that runs on top of TensorFlow.

### OpenCV (Open Source Computer Vision Library)
A library of programming functions for real-time computer vision tasks.

### scikit-learn
A machine learning library for Python providing simple tools for data analysis.

### ONNX (Open Neural Network Exchange)
An open format for representing machine learning models, enabling interoperability between frameworks.

### PIL/Pillow
Python Imaging Library for opening, manipulating, and saving image files.

### NumPy
A fundamental package for scientific computing in Python, used extensively for array operations.

### Matplotlib
A plotting library for creating visualizations in Python.

### CUDA
NVIDIA's parallel computing platform enabling GPU acceleration for deep learning.

### cuDNN
NVIDIA's GPU-accelerated library for deep neural networks.

---

## Software Development Terms

### Repository (Repo)
A storage location for software code, typically managed with version control systems like Git.

### Version Control
A system for tracking changes to code over time (e.g., Git).

### Git
A distributed version control system for tracking changes in source code.

### GitHub
A web-based platform for hosting and collaborating on Git repositories.

### Branch
An independent line of development in a Git repository.

### Commit
A snapshot of changes to a repository at a specific point in time.

### Pull Request (PR)
A request to merge changes from one branch into another, typically reviewed before merging.

### Fork
A copy of a repository that allows independent development.

### Clone
Creating a local copy of a remote repository.

### API (Application Programming Interface)
A set of rules and protocols for building and interacting with software applications.

### REST API
An architectural style for designing networked applications using HTTP requests.

### Docker
A platform for developing, shipping, and running applications in containers.

### Container
A lightweight, standalone package containing everything needed to run an application.

### Virtual Environment
An isolated Python environment with its own dependencies, separate from the system Python.

### Requirements.txt
A file listing Python package dependencies for a project.

### CI/CD (Continuous Integration/Continuous Deployment)
Automated processes for testing and deploying code changes.

### IDE (Integrated Development Environment)
A software application providing comprehensive facilities for software development (e.g., VS Code, PyCharm).

### Jupyter Notebook
An interactive computing environment for creating and sharing documents with live code, equations, and visualizations.

---

## Performance Metrics

### Accuracy
The proportion of correct predictions among total predictions.

### Precision
The proportion of true positive predictions among all positive predictions: TP / (TP + FP).

### Recall (Sensitivity)
The proportion of true positives identified among all actual positives: TP / (TP + FN).

### F1 Score
The harmonic mean of precision and recall: 2 × (Precision × Recall) / (Precision + Recall).

### Confusion Matrix
A table showing true positives, true negatives, false positives, and false negatives.

### mAP (mean Average Precision)
A common metric for object detection that averages precision across different recall levels and classes.

### FPS (Frames Per Second)
A measure of processing speed, indicating how many images can be processed per second.

### Latency
The time delay between input and output, critical for real-time applications.

### True Positive (TP)
A correct positive prediction.

### False Positive (FP)
An incorrect positive prediction (Type I error).

### True Negative (TN)
A correct negative prediction.

### False Negative (FN)
An incorrect negative prediction (Type II error).

### ROC Curve (Receiver Operating Characteristic)
A graph showing the trade-off between true positive rate and false positive rate.

### AUC (Area Under the Curve)
The area under the ROC curve, indicating overall model performance (0 to 1, higher is better).

---

## Additional Resources

For more in-depth learning:
- **OpenCV Documentation**: https://docs.opencv.org/
- **TensorFlow Tutorials**: https://www.tensorflow.org/tutorials
- **PyTorch Tutorials**: https://pytorch.org/tutorials/
- **Papers with Code**: https://paperswithcode.com/
- **Computer Vision: Algorithms and Applications** by Richard Szeliski
- **Deep Learning** by Ian Goodfellow, Yoshua Bengio, and Aaron Courville

---

**Note**: This glossary is a living document. As the field of computer vision evolves, new terms and concepts emerge. Contributions and updates are welcome!
