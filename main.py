import numpy as np
import matplotlib
matplotlib.use('Agg')  # 非交互式后端，避免弹出窗口
import matplotlib.pyplot as plt

# 1. 模拟生成 100 个无人小车超声波雷达的测距数据，加入随机噪声
np.random.seed(42)  # 固定随机种子，使结果可复现
true_distance = 50.0  # 真实距离（单位：cm）
num_samples = 100
noise = np.random.normal(0, 3.0, num_samples)  # 高斯噪声，均值0，标准差3
raw_data = true_distance + noise  # 含噪声的原始数据

# 2. 滑动平均滤波算法（Moving Average）
def moving_average(data, window_size=5):
    """对输入数据执行滑动平均滤波"""
    smoothed = []
    for i in range(len(data)):
        if i < window_size - 1:
            # 前 window_size-1 个点取已有点的平均值
            avg = np.mean(data[:i + 1])
        else:
            avg = np.mean(data[i - window_size + 1 : i + 1])
        smoothed.append(avg)
    return np.array(smoothed)

filtered_data = moving_average(raw_data, window_size=5)

# 3. 绘制对比图表
plt.figure(figsize=(12, 5))
plt.plot(raw_data, label='Raw Noisy Data', alpha=0.6, linewidth=1)
plt.plot(filtered_data, label='Filtered (Moving Average)', linewidth=2)
plt.xlabel('Sample Point')
plt.ylabel('Distance (cm)')
plt.title('Ultrasonic Radar Distance Data - Moving Average Filter Comparison')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# 4. 保存为 PNG 文件，不弹出窗口
plt.savefig('radar_filter_result.png', dpi=150)
print("Chart saved as radar_filter_result.png")
