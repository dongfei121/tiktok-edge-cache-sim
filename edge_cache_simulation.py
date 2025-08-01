import random
import matplotlib.pyplot as plt

# Simulation settings
cache_size = 5  # Number of videos that can be cached at edge
video_pool = [f"video_{i}" for i in range(10)]  # 10 different videos
num_requests = 50  # Number of video requests
edge_cache = []  # Simulate as a simple LRU cache

# Delay settings (in milliseconds)
delay_hit = 10
delay_miss = 100

# Tracking results
requests = []
delays = []
hits = 0

# Simulate LRU caching
for i in range(num_requests):
    video = random.choice(video_pool)
    requests.append(video)

    if video in edge_cache:
        # Cache hit
        delays.append(delay_hit)
        hits += 1
        edge_cache.remove(video)
        edge_cache.insert(0, video)
    else:
        # Cache miss
        delays.append(delay_miss)
        edge_cache.insert(0, video)
        if len(edge_cache) > cache_size:
            edge_cache.pop()

# Cache hit rate
hit_rate = hits / num_requests * 100

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(range(num_requests), delays, marker='o', label='Response Delay (ms)')
plt.title(f'Edge Caching Simulation for TikTok-like Video Requests\nCache Size: {cache_size}, Hit Rate: {hit_rate:.2f}%')
plt.xlabel('Request Number')
plt.ylabel('Delay (ms)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
