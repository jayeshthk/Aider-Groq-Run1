import torch
import torch.nn as nn
import torch.nn.functional as F

class SelfAttention(nn.Module):
    def __init__(self, num_heads, hidden_size):
        super(SelfAttention, self).__init__()
        self.num_heads = num_heads
        self.hidden_size = hidden_size
        self.query_linear = nn.Linear(hidden_size, hidden_size)
        self.key_linear = nn.Linear(hidden_size, hidden_size)
        self.value_linear = nn.Linear(hidden_size, hidden_size)
        self.dropout = nn.Dropout(0.1)

    def forward(self, x):
        batch_size, seq_len, hidden_size = x.size()
        query = self.query_linear(x).view(batch_size, seq_len, self.num_heads, hidden_size // self.num_heads)
        key = self.key_linear(x).view(batch_size, seq_len, self.num_heads, hidden_size // self.num_heads)
        value = self.value_linear(x).view(batch_size, seq_len, self.num_heads, hidden_size // self.num_heads)
        attention_scores = torch.matmul(query, key.transpose(-1, -2)) / math.sqrt(hidden_size // self.num_heads)
        attention_scores = F.softmax(attention_scores, dim=-1)
        attention_scores = self.dropout(attention_scores)
        output = attention_scores * value
        output = output.view(batch_size, seq_len, hidden_size)
        return output
