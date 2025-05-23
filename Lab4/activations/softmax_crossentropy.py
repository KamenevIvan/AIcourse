import numpy as np

class SoftmaxCrossEntropyLoss:
    def __init__(self):
        self.probs = None
        self.labels = None

    def forward(self, logits, labels):
        """
        logits: (batch_size, num_classes)
        labels: (batch_size,) — индексы классов
        """
        logits = logits - np.max(logits, axis=1, keepdims=True)  # стабильность
        exp_logits = np.exp(logits)
        probs = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

        self.probs = probs
        self.labels = labels

        # log вероятности правильных классов
        log_likelihood = -np.log(probs[np.arange(len(labels)), labels])
        loss = np.mean(log_likelihood)
        return loss

    def backward(self):
        """
        Возвращает градиенты по логитам: dL/dz
        """
        batch_size = self.probs.shape[0]
        grad = self.probs.copy()
        grad[np.arange(batch_size), self.labels] -= 1
        grad /= batch_size
        return grad

#Test

np.random.seed(0)
logits = np.random.randn(4, 3)
labels = np.array([0, 2, 1, 1])

loss_fn = SoftmaxCrossEntropyLoss()
loss = loss_fn.forward(logits, labels)
grad = loss_fn.backward()

print("Loss:", loss)
print("Gradient:\n", grad)
