"""Adapted from d2l-zh chapter_linear-networks/linear-regression-scratch.md.

Source commit: e6b18ccea71451a55fcd861d7b96fddf2587b09a
License: Apache-2.0
Modifications: removed the d2l helper package, used direct PyTorch operations,
added deterministic seeds, packaged the flow into functions, and added checks.
"""

import random

import torch


def synthetic_data(w, b, num_examples):
    """Generate y = Xw + b + noise."""
    x = torch.normal(0, 1, (num_examples, len(w)))
    y = x @ w + b
    y += torch.normal(0, 0.01, y.shape)
    return x, y.reshape((-1, 1))


def data_iter(batch_size, features, labels):
    """Yield shuffled mini-batches."""
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i : min(i + batch_size, num_examples)]
        )
        yield features[batch_indices], labels[batch_indices]


def linear_regression(x, w, b):
    return x @ w + b


def squared_loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2


def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


def train(seed=42, num_epochs=3, learning_rate=0.03, batch_size=10):
    torch.manual_seed(seed)
    random.seed(seed)

    true_w = torch.tensor([2.0, -3.4])
    true_b = 4.2
    features, labels = synthetic_data(true_w, true_b, 1000)

    w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
    b = torch.zeros(1, requires_grad=True)

    for epoch in range(num_epochs):
        for x, y in data_iter(batch_size, features, labels):
            loss = squared_loss(linear_regression(x, w, b), y)
            loss.sum().backward()
            sgd([w, b], learning_rate, batch_size)

        with torch.no_grad():
            epoch_loss = squared_loss(
                linear_regression(features, w, b), labels
            ).mean()
        print(f"epoch {epoch + 1}, loss {float(epoch_loss):.6f}")

    with torch.no_grad():
        final_loss = squared_loss(
            linear_regression(features, w, b), labels
        ).mean()
        w_error = torch.abs(true_w - w.reshape(true_w.shape)).max()
        b_error = torch.abs(true_b - b).max()

    return {
        "true_w": true_w,
        "true_b": true_b,
        "learned_w": w.detach().reshape(-1),
        "learned_b": b.detach().reshape(()),
        "final_loss": final_loss,
        "max_w_error": w_error,
        "b_error": b_error,
    }


def main():
    result = train()
    print(f"true w: {result['true_w'].tolist()}")
    print(f"learned w: {result['learned_w'].tolist()}")
    print(f"true b: {float(result['true_b']):.6f}")
    print(f"learned b: {float(result['learned_b']):.6f}")
    print(f"max w error: {float(result['max_w_error']):.6f}")
    print(f"b error: {float(result['b_error']):.6f}")

    assert result["final_loss"] < 0.01
    assert result["max_w_error"] < 0.1
    assert result["b_error"] < 0.1
    print("checks passed")


if __name__ == "__main__":
    main()
