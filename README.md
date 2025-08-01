# Edge Caching Simulation for TikTok-like Video Requests

This project simulates a simplified edge caching mechanism for short video content delivery, inspired by platforms such as TikTok. The simulation evaluates how a Least Recently Used (LRU) cache at the edge can improve response times by serving popular content locally.

## Description

- **Cache Strategy**: LRU (Least Recently Used)
- **Simulation Requests**: 50 video requests
- **Video Pool**: 10 unique videos
- **Edge Cache Capacity**: 5 videos
- **Latency**:
  - Cache hit: 10ms
  - Cache miss (cloud fetch): 100ms

## Results

- **Cache Hit Rate**: 40.00%
- **Average Delay Improvement**: Significant for cached content

## Files

- `edge_cache_simulation.py`: The main simulation script.
- `edge_caching_simulation.png`: Visualization of delay per request.

## Requirements

- Python 3
- `matplotlib`

## Run

```bash
pip install matplotlib
python edge_cache_simulation.py
```

## Author

This project is part of the Fog and Edge Computing CA at National College of Ireland.
