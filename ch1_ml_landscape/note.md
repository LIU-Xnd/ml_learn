<<< note chapter 1 >>> [BACK](../readme.md)

### Reinforcement Learning

Observe --> Act --> Reward --> Update policy --> Iterate.

---

## Batch and Online Learning

whether or not the system can learn incrementally from a stream of incoming data.

### Batch Learning

Offline. 

### Online Learning

On the fly.

## Instance-based vs Model-based

### Instance-based

Instance; similarity.

### Model-based

Model; predictions.

# Challenges

## Sampling Bias

Nonresponse bias; sampling tendency.

## Overfitting the Training Data

Obviously this pattern occurred in the training data by pure chance, but the model has no way to tell whether a pattern is real or simply the result of noise in the data.

### Solutions

Simplify the model; Gather more training data; Reduce the noise.

Constraining a model to make it simpler and reduce the risk of overfitting is called regularization.

The amount of regularization to apply during learning can be controlled by a hyperparameter.

## Underfitting the Training Data

# Testing and Validating

Test; Train.

Cross-validation.

## Data Mismatch

If train good and test bad, is it because of Overfit or Mismatch? (e.g. Pics from web and mobile)

Andrew Ng - train-dev set. Split pics from web to train and train-dev to test the overfitness.

### No Free Lunch Theorem

David Wolpert demonstrated that if you make absolutely no assumption about the data, then there is no reason to prefer one model over any other. This is called the No Free Lunch (NFL) theorem.

# <<< Exercises >>>

1. How would you define Machine Learning?

ML is learing patterns from samples with the help of computing devices, optimizing a given measurement of performance under some assumptions about the data, so as to predict information about new data.

2. Can you name four types of problems where it shines?

Img recognition; speech rec; company revenue prediction; sale strategy making / recommendation policy making.

3. What is a labeled training set?

A set of data in the form of {(X, y)}, where y is known a priori and is (closely related to) the value/factor of new data to predict.

4. What are the two most common supervised tasks?

Classification; Regression.

5. Can you name four common unsupervised tasks?

Clustering; PCA (representation learning); FA; Density estimation.

6. What type of Machine Learning algorithm would you use to allow a robot to walk in various unknown terrains?

Reinforment learning.

7. What type of algorithm would you use to segment your customers into multiple groups?

Clustering.

8. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?

9. What is an online learning system?

It allows data on the fly, fed to the system batch by batch without needing to start over from zero. It's practical for memory-limited machine.

10. What is out-of-core learning?

It's learning when data is too huge to fit in the memory. Basically it refers to online learning.

11. What type of learning alg relies on a similarity measure to make predictions?

Clustering / Unsupervised learning / k-NN.

12. What is the difference between a model parameter and a learning algorithm’s hyperparameter?

Param is learnt and adjusted in the meantime of model training; hyperparam is given a priori and remain constant in a given process of model training.

13. What do model-based learning algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?

i) It find the optinal params for the model to fit the data.
ii) Minimize error / least-squares with a regularization term.
iii) After learning params p for the model y=f(x;p)+e, they predict the y for a new x by y=f(x;p).

14. Can you name four of the main challenges in Machine Learning?

Insufficient data; overfitting; underfitting; sample bias.

15. If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?

i) It's overfitting (or data mismatch in some case).
ii) Regularizing/Simplifying the model; reorganising the training and testing data; gaining more data.

16. What is a test set, and why would you want to use it?

It's a set of data not for training but to test the performance of the model to generalize on other data. We use it to measure the general performance of model to avoid overfitting.

17. What is the purpose of a validation set?

To in some sense constrain the model from overfitting.

18. What is the train-dev set, when do you need it, and how do you use it?

It's split from the original train set and the data from the two share similar sources or potential features (so that there is no data mismatch) and is used when we are not sure between data mismatch and overfitting. We train model on train set and then test it on the train-dev set to see the overfitness.

19. What can go wrong if you tune hyperparams using the test set?

It will overfit in the real sense.
