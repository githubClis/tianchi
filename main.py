import numpy as np
import matplotlib.pyplot as plt

# 生成测试结果数据
test_results = np.array([0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1])

# 统计测试结果中每个类别出现的次数
unique, counts = np.unique(test_results, return_counts=True)
class_counts = dict(zip(unique, counts))

# 绘制饼图
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(class_counts.values(), labels=class_counts.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Test Results')

# 显示图像
plt.show()