# Deep Learning Fundamentals

This README covers the core Deep Learning concepts learned so far:

1. What is Deep Learning?
2. Deep Learning vs Traditional Machine Learning
3. Perceptron and Artificial Neuron
4. Neural Network Structure
5. Weights and Biases
6. Forward Propagation
7. Activation Functions
8. Loss / Cost Functions
9. Backpropagation and Chain Rule
10. Gradient Descent
11. Batch, Stochastic, and Mini-Batch Gradient Descent
12. Optimizers
13. Learning Rate, Epochs, and Batch Size
14. Complete Neural Network Training Flow

---

# 1. What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses **multi-layer neural networks** to automatically learn complex patterns from data.

```text
Artificial Intelligence
        |
        v
Machine Learning
        |
        v
Deep Learning
```

Traditional ML often requires manually engineered features.

Deep Learning can automatically learn useful representations/features from raw data.

## Example: Image Classification

Traditional ML:

```text
Image
  |
  v
Feature Engineering
  |
  +--> Color
  +--> Edges
  +--> Shape
  +--> Texture
  |
  v
ML Algorithm
  |
  v
Cat / Dog
```

Deep Learning:

```text
Image
  |
  v
Neural Network
  |
  +--> Edges
  +--> Shapes
  +--> Object Parts
  +--> High-level Features
  |
  v
Cat / Dog
```

---

# 2. Deep Learning vs Traditional ML

| Feature | Traditional ML | Deep Learning |
|---|---|---|
| Feature engineering | Usually required | Mostly learned automatically |
| Dataset size | Often works well with smaller datasets | Usually benefits from large datasets |
| Compute | Usually lower | Usually higher |
| Training | Generally faster | Generally slower |
| Hardware | CPU often sufficient | GPU/TPU often useful |
| Interpretability | Often easier | Usually harder |
| Images | Can work with engineered features | Excellent |
| Text | Traditional techniques available | Excellent |
| Audio/Video | Limited compared with DL | Excellent |
| Tabular data | Often very strong | Not always best |

## When to use Deep Learning?

Deep Learning is especially useful for:

- Images
- Text
- Audio
- Video
- Large-scale sensor/time-series data
- Complex, high-dimensional data

Traditional ML can be preferable for:

- Small datasets
- Structured/tabular data
- Problems with strong manually engineered features

> Deep Learning is not automatically better than traditional ML.

---

# 3. Perceptron

A **perceptron** is one of the simplest neural-network models.

It takes inputs, applies weights, adds a bias, and produces an output.

```text
x1 ----\
x2 -----\
x3 ------> Weighted Sum + Bias
          |
          v
      Activation
          |
          v
       Output
```

The basic calculation is:

```text
z = w1*x1 + w2*x2 + ... + wn*xn + b
```

Then:

```text
output = activation(z)
```

The original perceptron commonly uses a **step function**.

```text
if z >= 0
    output = 1
else
    output = 0
```

---

# 4. Perceptron vs Neuron vs Layer

A useful hierarchy is:

```text
One Perceptron
      |
      v
One basic neuron

Multiple neurons
      |
      v
One layer

Multiple layers
      |
      v
Neural Network

Multiple hidden layers
      |
      v
Deep Neural Network
```

More precisely, a perceptron is a specific type of artificial neuron.

## Single-layer Perceptron

Multiple neurons can exist in one computational layer:

```text
             +--> Neuron 1 --> Output
Input -------+--> Neuron 2 --> Output
             +--> Neuron 3 --> Output
```

There is no hidden layer.

## Multi-Layer Perceptron

```text
Input Layer
     |
     v
Hidden Layer
     |
     v
Output Layer
```

With multiple hidden layers:

```text
Input
  |
  v
Hidden 1
  |
  v
Hidden 2
  |
  v
Hidden 3
  |
  v
Output
```

This is a deep neural network.

---

# 5. Neural Network Structure

A basic neural network contains:

```text
Input Layer
      |
      v
Hidden Layer(s)
      |
      v
Output Layer
```

Example:

```text
x1 ----\
x2 -----\       h1 ----\
x3 ------>      h2 -----\      y
x4 -----/       h3 ------>     |
             Hidden Layer      Output
```

## Input Layer

Contains the input features.

Examples:

### Tabular data

```text
Age
Salary
Experience
```

### Image

```text
Pixel values
```

### NLP

```text
Token representations
```

The input layer generally represents the input rather than performing the main neural computation.

---

# 6. Weights

A weight determines how strongly an input influences a neuron.

For example:

```text
x1 = Experience
x2 = Salary

w1 = 0.8
w2 = 0.3
```

The neuron calculates:

```text
z = (x1 * w1) + (x2 * w2) + b
```

The model **learns the weights during training**.

---

# 7. Bias

Bias is an additional learned parameter.

```text
z = w1*x1 + w2*x2 + b
```

Bias provides an adjustable offset and allows the neuron/network to represent more flexible functions.

Both weights and biases are learned during training.

---

# 8. Artificial Neuron

A modern artificial neuron can be represented as:

```text
Inputs
   |
   v
Weighted Sum + Bias
   |
   v
Activation Function
   |
   v
Neuron Output
```

Mathematically:

```text
z = Σ(wi * xi) + b

a = f(z)
```

Where:

- `x` = input
- `w` = weight
- `b` = bias
- `z` = weighted sum
- `f` = activation function
- `a` = neuron output

---

# 9. Forward Propagation

Forward propagation means **moving the input forward through the network to produce a prediction**.

```text
Input
  |
  v
Hidden Layer 1
  |
  v
Hidden Layer 2
  |
  v
Output
```

For one neuron:

```text
z = w1*x1 + w2*x2 + b

a = f(z)
```

For multiple layers:

```text
X
 |
 v
Z1 = W1X + B1
 |
 v
H1 = f(Z1)
 |
 v
Z2 = W2H1 + B2
 |
 v
H2 = f(Z2)
 |
 v
Output
```

## Important

Forward propagation answers:

> "What does the model predict?"

No weights are updated during forward propagation.

---

# 10. Activation Functions

Activation functions introduce **non-linearity** into neural networks.

Without non-linear activation functions, stacking multiple linear layers would still produce essentially a linear transformation.

The basic flow is:

```text
Weighted Sum
     |
     v
Activation Function
     |
     v
Neuron Output
```

---

# 11. Sigmoid

Formula:

```text
sigmoid(x) = 1 / (1 + e^(-x))
```

Output range:

```text
0 to 1
```

Example:

```text
z = -2  -> approximately 0.12
z =  0  -> 0.50
z =  2  -> approximately 0.88
```

## When to use?

Commonly used in the output layer for **binary classification**.

Example:

```text
Spam / Not Spam

Output = 0.92
```

Interpretation:

```text
92% estimated probability of class 1
```

## Problem

Sigmoid can suffer from the **vanishing gradient problem**, especially for large positive or negative inputs.

Therefore, it is generally not the default choice for hidden layers in modern deep networks.

---

# 12. Tanh

Tanh outputs values between:

```text
-1 and +1
```

Example:

```text
-2 -> approximately -0.96
 0 -> 0
 2 -> approximately 0.96
```

## Advantages

- Zero-centered
- Can work better than sigmoid in some situations

## When to use?

Historically common in:

- RNNs
- LSTMs
- Some hidden layers

It can also suffer from vanishing gradients.

---

# 13. ReLU

ReLU = Rectified Linear Unit.

Formula:

```text
ReLU(x) = max(0, x)
```

Examples:

```text
-5 -> 0
-2 -> 0
 0 -> 0
 2 -> 2
 5 -> 5
```

## When to use?

ReLU is a very common choice for **hidden layers**.

Advantages:

- Simple
- Computationally efficient
- Helps with gradient flow for positive inputs
- Works well in many deep networks

## Problem: Dying ReLU

For negative inputs:

```text
ReLU(x) = 0
gradient = 0
```

A neuron can potentially stop learning if it remains in this region.

---

# 14. Leaky ReLU

Leaky ReLU addresses the dying-ReLU problem by allowing a small negative output.

Conceptually:

```text
x > 0  -> x
x <= 0 -> small negative value
```

For example, with `alpha = 0.01`:

```text
-5 -> -0.05
 5 ->  5
```

## When to use?

It can be used as an alternative to ReLU when you want to maintain a small gradient for negative inputs.

---

# 15. Softmax

Softmax is commonly used for **multi-class classification** where each input belongs to one class.

Example:

```text
Cat
Dog
Horse
```

The network might produce:

```text
Cat   -> 0.70
Dog   -> 0.20
Horse -> 0.10
```

The probabilities sum to:

```text
1.00
```

## When to use?

Multi-class classification:

```text
Image
  |
  v
Neural Network
  |
  v
Softmax
  |
  +--> Cat   0.70
  +--> Dog   0.20
  +--> Horse 0.10
```

---

# 16. Activation Function Cheat Sheet

| Activation | Range | Typical Use |
|---|---|---|
| Sigmoid | 0 to 1 | Binary classification output |
| Tanh | -1 to +1 | RNN/LSTM historically |
| ReLU | 0 to infinity | Common hidden layers |
| Leaky ReLU | Negative to positive | Alternative to ReLU |
| Softmax | Probabilities sum to 1 | Multi-class classification |

Memory trick:

```text
Sigmoid    -> Binary
Tanh       -> -1/+1
ReLU       -> Hidden layers
Leaky ReLU -> ReLU alternative
Softmax    -> Multiple classes
```

---

# 17. Loss / Cost Function

The loss function measures:

> "How wrong is the model's prediction?"

Training flow:

```text
Input
  |
  v
Forward Propagation
  |
  v
Prediction
  |
  v
Loss Function
  |
  v
Backpropagation
```

Lower loss generally means the prediction is closer to the target according to the chosen loss function.

---

# 18. MSE — Mean Squared Error

MSE is commonly used for regression.

Formula:

```text
MSE = (1/n) * Σ(y - y_hat)^2
```

Example:

```text
Actual       Prediction
10           8
20           18
30           33
```

Errors:

```text
2
2
-3
```

Squared errors:

```text
4
4
9
```

MSE:

```text
(4 + 4 + 9) / 3
= 5.67
```

## Use MSE for:

- House price prediction
- Temperature prediction
- Sales prediction
- Salary prediction
- Other regression problems

---

# 19. Binary Cross-Entropy

Used for **binary classification**.

Examples:

```text
Spam / Not Spam
Fraud / Not Fraud
Churn / Not Churn
Cat / Not Cat
```

Formula:

```text
L = -[y*log(y_hat) + (1-y)*log(1-y_hat)]
```

Usually paired with:

```text
Sigmoid + Binary Cross-Entropy
```

Example:

```text
Actual = 1
Prediction = 0.9
```

Loss is small.

But:

```text
Actual = 1
Prediction = 0.1
```

Loss is much larger.

Cross-entropy strongly penalizes confident incorrect predictions.

---

# 20. Categorical Cross-Entropy

Used for **multi-class classification** where each sample belongs to one class.

Example:

```text
Cat
Dog
Horse
```

Model:

```text
Cat   = 0.70
Dog   = 0.20
Horse = 0.10
```

If the actual class is Cat:

```text
Loss = -log(0.70)
```

The higher the probability assigned to the correct class, the lower the loss.

Usually paired with:

```text
Softmax + Categorical Cross-Entropy
```

---

# 21. Loss Function Cheat Sheet

| Problem | Output | Loss |
|---|---|---|
| Regression | Linear/no probability activation | MSE |
| Binary classification | Sigmoid | Binary Cross-Entropy |
| Multi-class classification | Softmax | Categorical Cross-Entropy |

Memory trick:

```text
Regression       -> MSE
Binary           -> Binary Cross-Entropy
Multi-class      -> Categorical Cross-Entropy
```

---

# 22. Backpropagation

Backpropagation is the process used to calculate **how much each weight and bias contributed to the prediction error**.

The flow is:

```text
Prediction
    |
    v
Loss
    |
    v
Backpropagation
    |
    v
Gradients
```

Backpropagation uses the **chain rule** to calculate gradients.

---

# 23. Chain Rule

Suppose:

```text
w -> z -> activation -> prediction -> Loss
```

The loss depends indirectly on the weight.

The chain rule allows us to calculate:

```text
dL/dw
```

For example:

```text
∂L/∂w
=
∂L/∂a
*
∂a/∂z
*
∂z/∂w
```

This allows the network to work backward through multiple layers.

---

# 24. Why Backpropagation Goes Backward

Forward:

```text
Input
  |
  v
Layer 1
  |
  v
Layer 2
  |
  v
Output
  |
  v
Loss
```

Backward:

```text
Loss
  |
  v
Output
  |
  v
Layer 2
  |
  v
Layer 1
```

The gradients flow backward.

That is why it is called:

> Backpropagation.

---

# 25. Gradient

A gradient tells us how the loss changes when a parameter changes.

Conceptually:

```text
Gradient
    |
    v
Which direction should the weight move?
How strongly should it move?
```

For a weight:

```text
∂L/∂w
```

If the gradient is positive, gradient descent generally decreases the weight.

If the gradient is negative, gradient descent generally increases the weight.

---

# 26. Gradient Descent

Gradient Descent is an optimization algorithm used to minimize the loss.

Basic update:

```text
w_new = w_old - learning_rate * gradient
```

Example:

```text
Weight = 5
Gradient = 2
Learning Rate = 0.1

New Weight
= 5 - (0.1 * 2)
= 4.8
```

So:

```text
5.0 -> 4.8
```

The model repeatedly updates parameters to reduce the loss.

---

# 27. Learning Rate

Learning rate controls the **size of each parameter update**.

```text
Large learning rate
    |
    v
Large steps

Small learning rate
    |
    v
Small steps
```

## Learning rate too large

The model may overshoot the minimum:

```text
Minimum
   ^
   |
  / \
 /   \
/     \
  <--- jumps around
```

Training may become unstable.

## Learning rate too small

Training may be extremely slow.

Therefore, choosing an appropriate learning rate is important.

---

# 28. Batch Gradient Descent

Batch Gradient Descent calculates the gradient using the **entire training dataset** before updating the parameters.

Example:

```text
1000 samples

All 1000
   |
   v
Calculate gradient
   |
   v
Update weights
```

Advantages:

- Stable gradient
- Smooth updates

Disadvantages:

- Expensive for large datasets
- High computation/memory requirement

---

# 29. Stochastic Gradient Descent

SGD uses **one training sample** to calculate each update.

```text
Sample 1 -> Gradient -> Update
Sample 2 -> Gradient -> Update
Sample 3 -> Gradient -> Update
...
```

Advantages:

- Frequent updates
- Low memory per update
- Useful for large datasets

Disadvantages:

- Noisy updates
- Loss can fluctuate
- Can be less stable

---

# 30. Mini-Batch Gradient Descent

Mini-batch uses a small group of samples for each update.

Example:

```text
Dataset = 10,000
Batch size = 100
```

Training:

```text
Batch 1 -> 100 samples -> Update
Batch 2 -> 100 samples -> Update
Batch 3 -> 100 samples -> Update
...
```

Updates per epoch:

```text
10,000 / 100 = 100
```

Mini-batch training is extremely common in modern deep learning.

---

# 31. Batch vs SGD vs Mini-Batch

| Method | Samples per update | Updates per epoch |
|---|---:|---:|
| Batch GD | Entire dataset | 1 |
| SGD | 1 | N |
| Mini-Batch GD | Small batch | N / batch size |

Memory trick:

```text
Batch       -> ALL
SGD         -> ONE
Mini-Batch  -> SOME
```

---

# 32. Epoch

An epoch means:

> **One complete pass through the training dataset.**

Example:

```text
Dataset = 10,000 images
Batch size = 100
```

One epoch:

```text
Batch 1
Batch 2
...
Batch 100
```

After Batch 100:

```text
1 Epoch completed
```

If:

```text
epochs = 20
```

the model processes the training dataset approximately 20 times.

---

# 33. Optimizers

An optimizer determines **how gradients are used to update model parameters**.

Basic relationship:

```text
Backpropagation
      |
      v
Calculate gradients
      |
      v
Optimizer
      |
      v
Update weights
```

---

# 34. SGD Optimizer

Basic idea:

```text
Use the current gradient
```

Update:

```text
w = w - learning_rate * gradient
```

Advantages:

- Simple
- Low memory
- Can generalize well

Disadvantages:

- Can converge slowly
- Can be noisy

---

# 35. Momentum

Momentum adds information from previous updates.

Instead of only considering:

```text
Current gradient
```

it also considers:

```text
Previous movement
```

Conceptually:

```text
Current Gradient
       +
Previous Direction
       |
       v
   Momentum
       |
       v
Weight Update
```

Benefits:

- Reduces oscillations
- Can accelerate convergence
- Helps maintain useful directions

---

# 36. RMSProp

RMSProp adapts the effective learning rate based on the recent magnitude of gradients.

Conceptually:

```text
Large historical gradients
       |
       v
Smaller effective step

Small historical gradients
       |
       v
Larger effective step
```

Benefits:

- Adaptive learning rates
- Handles different gradient scales
- Can improve convergence

---

# 37. Adam

Adam stands for:

> Adaptive Moment Estimation

Adam combines ideas from:

```text
Momentum + RMSProp
```

It tracks:

1. A moving average of gradients
2. A moving average of squared gradients

Conceptually:

```text
Gradient
   |
   +------> First Moment
   |         Direction
   |
   +------> Second Moment
             Magnitude
                |
                v
              Adam
                |
                v
          Weight Update
```

Adam is a popular general-purpose optimizer.

---

# 38. Optimizer Comparison

| Optimizer | Main Idea |
|---|---|
| SGD | Current gradient |
| Momentum | Current gradient + previous direction |
| RMSProp | Adaptive learning rate based on gradient magnitude |
| Adam | Momentum-like first moment + RMSProp-like second moment |

Memory trick:

```text
SGD      -> Current gradient
Momentum -> Remember previous direction
RMSProp  -> Adapt step size
Adam     -> Momentum + RMSProp
```

---

# 39. Important: Gradient Descent vs Optimizer

These terms are related.

Gradient Descent is the basic optimization idea:

```text
Move in the opposite direction of the gradient
```

Optimizers provide different strategies for doing this.

For example:

```text
SGD
Momentum
RMSProp
Adam
```

So:

```text
Gradient
   |
   v
Optimizer
   |
   v
Weight Update
```

---

# 40. Batch Size

Batch size determines:

> **How many samples are processed before one parameter update.**

Example:

```text
Dataset = 10,000
Batch size = 100
```

Then:

```text
100 samples
   |
   v
Gradient
   |
   v
Update weights
```

Then another 100 samples.

---

# 41. Learning Rate vs Batch Size vs Epochs

These are different concepts.

### Learning Rate

```text
How BIG is each parameter update?
```

### Batch Size

```text
How MANY samples are used for one update?
```

### Epochs

```text
How MANY times do we process the entire dataset?
```

Remember:

```text
Learning Rate -> HOW BIG?
Batch Size    -> HOW MANY?
Epochs        -> HOW MANY TIMES?
```

---

# 42. Complete Neural Network Training Process

All the concepts now connect together:

```text
                         TRAINING

Dataset
   |
   v
Split into mini-batches
   |
   v
Input Batch
   |
   v
Forward Propagation
   |
   +--> Weighted Sum
   |
   +--> Activation
   |
   v
Prediction
   |
   v
Loss Function
   |
   v
Loss
   |
   v
Backpropagation
   |
   +--> Chain Rule
   |
   v
Gradients
   |
   v
Optimizer
   |
   v
Learning Rate
   |
   v
Update Weights + Biases
   |
   v
Next Batch
   |
   v
All batches completed
   |
   v
One Epoch
   |
   v
Next Epoch
```

---

# 43. Image Classification Example

Suppose we want to classify:

```text
Cat
Dog
Horse
```

## Training

```text
Image + Correct Label
        |
        v
Neural Network
        |
        v
Forward Propagation
        |
        v
Softmax
        |
        v
Predictions
        |
        v
Categorical Cross-Entropy
        |
        v
Loss
        |
        v
Backpropagation
        |
        v
Gradients
        |
        v
Adam / SGD / etc.
        |
        v
Update Weights
```

Repeat for many batches and epochs.

---

# 44. After Training: Prediction

Once training is complete, the model has learned its weights.

For a new image:

```text
New Image
   |
   v
Trained Neural Network
   |
   v
Forward Propagation
   |
   v
Softmax
   |
   +--> Cat   = 0.90
   +--> Dog   = 0.07
   +--> Horse = 0.03
```

Prediction:

```text
Cat
```

The actual label is **not provided to the model during prediction**.

The trained weights are used to generate the prediction.

---

# 45. NLP Example

The same fundamental process applies to NLP.

Suppose we want sentiment classification:

```text
"I love this product"
```

During training:

```text
Text + Label
     |
     v
Tokenization
     |
     v
Numerical Representation
     |
     v
Neural Network
     |
     v
Prediction
     |
     v
Loss
     |
     v
Backpropagation
     |
     v
Update weights
```

After training:

```text
"I really enjoyed this product"
              |
              v
        Trained Model
              |
              v
        Positive = 96%
        Negative = 4%
```

Again, the model receives the new text but not the correct answer.

---

# 46. Training vs Testing

This distinction is extremely important.

## Training

The correct label is available:

```text
Input + Actual Label
        |
        v
Model
        |
        v
Prediction
        |
        v
Compare with Actual
        |
        v
Loss
        |
        v
Backpropagation
        |
        v
Update weights
```

## Testing / Prediction

The model receives the input:

```text
Input
  |
  v
Trained Model
  |
  v
Prediction
```

The model does **not** use the test label to update its weights.

For evaluation, the true test labels may be kept separately and compared with predictions after the model has made them.

---

# 47. Most Important Relationships

## Forward Propagation

```text
Input -> Prediction
```

Question answered:

> What does the model predict?

## Loss Function

```text
Prediction -> Error
```

Question answered:

> How wrong is the prediction?

## Backpropagation

```text
Loss -> Gradients
```

Question answered:

> How should each parameter change?

## Optimizer

```text
Gradients -> Parameter Updates
```

Question answered:

> How should I use those gradients to update the parameters?

---

# 48. Final Mental Model

Memorize this complete flow:

```text
                 NEURAL NETWORK LEARNING

Input
  |
  v
Weights + Biases
  |
  v
Forward Propagation
  |
  v
Activation Functions
  |
  v
Prediction
  |
  v
Loss Function
  |
  v
"How wrong?"
  |
  v
Backpropagation
  |
  v
Chain Rule
  |
  v
Gradients
  |
  v
Optimizer
  |
  v
Learning Rate
  |
  v
Update Weights + Biases
  |
  v
Next Batch
  |
  v
Next Epoch
  |
  v
Better Model
```

---

# 49. Interview Quick Revision

### What is Deep Learning?

> A subset of machine learning that uses multi-layer neural networks to learn complex representations from data.

### What is a perceptron?

> A basic computational model that calculates a weighted sum of inputs plus a bias and applies an activation function.

### What are weights?

> Learned parameters that determine the influence of inputs on neurons.

### What is bias?

> A learned offset that provides additional flexibility to the neuron.

### What is forward propagation?

> The process of passing input through the network layer by layer to produce a prediction.

### Why do we need activation functions?

> To introduce non-linearity so the network can learn complex relationships.

### What is a loss function?

> It measures how different the model's prediction is from the target.

### What is backpropagation?

> A method for calculating gradients of the loss with respect to network parameters by propagating the error backward through the network.

### What is the chain rule?

> A calculus rule used in backpropagation to calculate how changes in earlier parameters affect the final loss through a sequence of functions.

### What is gradient descent?

> An optimization method that updates parameters in the opposite direction of the gradient to minimize loss.

### Batch vs SGD vs Mini-Batch?

> Batch uses the entire dataset per update, SGD uses one sample, and mini-batch uses a small group of samples.

### What is an optimizer?

> An algorithm that determines how gradients are used to update model parameters.

### SGD vs Momentum vs RMSProp vs Adam?

> SGD uses the current gradient, Momentum incorporates previous updates, RMSProp adapts the learning rate based on gradient magnitude, and Adam combines momentum-like and adaptive-learning-rate ideas.

### What is learning rate?

> The step size used when updating model parameters.

### What is an epoch?

> One complete pass through the training dataset.

### What is batch size?

> The number of samples processed before a parameter update.

---

# 50. One-Page Cheat Sheet

```text
DEEP LEARNING
     |
     v
Neural Networks
     |
     +--> Input Layer
     |
     +--> Hidden Layers
     |
     +--> Output Layer
              |
              v
         Prediction


NEURON
     |
     v
z = Σ(wx) + b
     |
     v
Activation
     |
     v
Output


ACTIVATIONS
     |
     +--> Sigmoid      -> Binary output
     +--> Tanh         -> -1 to +1
     +--> ReLU         -> Hidden layers
     +--> Leaky ReLU   -> ReLU alternative
     +--> Softmax      -> Multi-class output


LOSS
     |
     +--> MSE                  -> Regression
     +--> Binary Cross-Entropy -> Binary classification
     +--> Categorical CE       -> Multi-class classification


TRAINING
     |
     v
Forward Propagation
     |
     v
Prediction
     |
     v
Loss
     |
     v
Backpropagation
     |
     v
Chain Rule
     |
     v
Gradients
     |
     v
Optimizer
     |
     v
Update Parameters


OPTIMIZERS
     |
     +--> SGD
     +--> Momentum
     +--> RMSProp
     +--> Adam


TRAINING PARAMETERS
     |
     +--> Learning Rate -> How big is the update?
     +--> Batch Size    -> How many samples per update?
     +--> Epochs        -> How many passes through data?
```

---

# Key Takeaways

1. **A neuron calculates a weighted sum + bias and applies an activation function.**
2. **Multiple neurons form layers.**
3. **Multiple layers form neural networks.**
4. **Forward propagation produces predictions.**
5. **Loss functions measure prediction error.**
6. **Backpropagation calculates gradients.**
7. **The chain rule makes backpropagation possible.**
8. **Optimizers use gradients to update weights and biases.**
9. **Learning rate controls the size of updates.**
10. **Batch size controls how many samples are used per update.**
11. **An epoch is one complete pass through the training dataset.**
12. **Sigmoid is commonly used for binary output.**
13. **Softmax is commonly used for multi-class output.**
14. **ReLU is commonly used in hidden layers.**
15. **MSE is commonly used for regression.**
16. **Cross-entropy is commonly used for classification.**
17. **Training uses labels to calculate loss and update weights; prediction uses the learned weights without providing the answer to the model.**