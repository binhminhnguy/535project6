# Bias Analysis in Federated Learning for Heterogeneous Sensors

**Motivation**

Federated learning focuses on training machine learning models collaboratively while ensuring participants' data remains private. Various forms of sensitive data, including images, audio, text, and sensor information, can be gathered for model training, but this data is vulnerable to exploitation by adversaries, jeopardizing the privacy of the involved parties. As adversarial techniques advance and attacks on machine learning models become more sophisticated, the risk of an adversary recovering confidential data used in training is growing. Federated learning provides a solution by enabling data from different sources to be used in a unified learning system, while still maintaining the privacy of each party's data.

Our group has interest and experience in working with machine learning frameworks and IoT devices. We also have experience in security engineering with multiple projects in data encryption in ECE 371 and 547. 

**Design Goals**

- Variations in feature distribution in federating learning leads to biases. Our goal is to model this bias towards different groups.

**Deliverable**

-  Understanding different federated learning techniques including - Federated averaging, Tilted Empirical Risk Minimization, and agnostic federated learning.
  
-  Use different datasets for training and assessing two federated learning techniques.
  
-  Examine the enhancement in the variance of accuracy among individual client groups when employing various federated learning techniques

**System Blocks**

- Provided Data -> Federated Learning (using Laptop with CUDA-enabled GPU)

**HW/SW Requirements**

-  Python

-  Laptop with CUDA-enabled GPU

**Team Members Responsibilities**

-  Manh Cuong La: Setup, Software, Research - Communication-Efficient Learning of Deep Networks from Decentralized Data and CIFAR-10. 

-  Binh Minh Nguyen: Networking, algorithm designs, Research- Agnostic Federated Learning

-  Ronit Ghai: Analyze data and testing, Research - Tilted Empirical Risk Minimization and FashionMNISTFashionMNIST

-  Robert Lewandowski: Writing, additional part from Professor, Research - FedAvg and TERM. 

**Project Timeline**

Our team will work on the project for at least 2 hours weekly. We will then spend 30 minutes each week to meet and report on the work done and the challenge.


**References**

- Communication-Efficient Learning of Deep Networks from Decentralized Data (https://arxiv.org/abs/1602.05629)

- Tilted Empirical Risk Minimization (TERM) (https://openreview.net/pdf?id=K5YasWXZT3O)

- Agnostic Federated Learning (AFL) (https://arxiv.org/pdf/1902.00146.pdf)

- FedAvg (https://github.com/alexbie98/fedavg)

- TERM (https://github.com/litian96/TERM)

- AFL (https://github.com/YuichiNAGAO/agnostic_federated_learning)

- CIFAR-10 (https://www.kaggle.com/c/cifar-10/data)

- FashionMNIST (https://github.com/zalandoresearch/fashion-mnist)

