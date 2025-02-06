import torch
import torch.nn as nn

class TransformerTimeSeries(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(TransformerTimeSeries, self).__init__()
        self.encoder = nn.Transformer(
            d_model=hidden_size,
            nhead=8,
            num_encoder_layers=num_layers,
            batch_first=True
        )
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.encoder(x)
        return self.fc(x[:, -1, :])

# Example usage
if __name__ == "__main__":
    model = TransformerTimeSeries(5, 64, 2, 1)
    print(model)
