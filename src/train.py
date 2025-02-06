import torch
import torch.optim as optim
import torch.nn as nn
from models import TransformerTimeSeries

def train_transformer():
    model = TransformerTimeSeries(input_size=5, hidden_size=64, num_layers=2, output_size=1)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()
    
    for epoch in range(10):
        optimizer.zero_grad()
        inputs = torch.randn(32, 10, 5)
        outputs = torch.randn(32, 1)
        predictions = model(inputs)
        loss = criterion(predictions, outputs)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

if __name__ == "__main__":
    train_transformer()
