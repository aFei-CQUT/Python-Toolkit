import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

# 创建公式列表
eqs = []
# 传热
eqs.append(r"$q = -k \frac{dT}{dx}$")  # 傅里叶定律
eqs.append(r"$Q = U A \Delta T$")  # 热传递公式
eqs.append(r"$\text{Nu} = \frac{hL}{k}$")  # 纳维-斯托克斯数
eqs.append(r"$\frac{dT}{dt} = \frac{k}{\rho c_p} \nabla^2 T$")  # 热传导方程

# 流体力学
eqs.append(r"$\tau = \mu \frac{du}{dy}$")  # 牛顿粘性定律
eqs.append(r"$\text{Re} = \frac{\rho v D}{\mu}$")  # 雷诺数
eqs.append(r"$\text{Pr} = \frac{\mu c_p}{k}$")  # 普朗特数
eqs.append(r"$\text{Sc} = \frac{\mu}{\rho D}$")  # 施密特数
eqs.append(r"$\frac{d\rho}{dt} + \nabla \cdot (\rho \vec{v}) = 0$")  # 连续性方程

# 物料和能量平衡
eqs.append(r"$\text{F}_A - \text{F}_A^0 = -\frac{dX}{dV}$")  # 物料平衡方程
eqs.append(r"$\text{F}_A = \text{F}_A^0 \exp(-kt)$")  # 一阶反应浓度
eqs.append(r"$\Delta H = H_{product} - H_{reactant}$")  # 反应焓变
eqs.append(r"$Q = \Delta H \cdot n$")  # 热量计算
eqs.append(r"$\text{dH} = \text{C}_p \text{dT}$")  # 热容方程

# 热力学
eqs.append(r"$\text{PV} = nRT$")  # 理想气体方程
eqs.append(r"$\Delta G = \Delta H - T\Delta S$")  # 吉布斯自由能
eqs.append(r"$K_c = \frac{[C]^c[D]^d}{[A]^a[B]^b}$")  # 反应平衡常数
eqs.append(r"$\text{K}_p = \text{K}_c (RT)^{\Delta n}$")  # 平衡常数关系

# 传质
eqs.append(r"$J = -D \frac{dC}{dx}$")  # 传质流量
eqs.append(r"$\text{Sh} = \frac{K_c D}{d}$")  # 施密特数公式
eqs.append(r"$\text{Nt} = \frac{D}{vL}$")  # 纳特数

# 其他
eqs.append(r"$\text{G} = \text{H} - T\text{S}$")  # 吉布斯自由能公式
eqs.append(r"$J = -D \frac{dC}{dx}$")  # 传质流量
eqs.append(r"$\text{Z} = \frac{P}{RT}$")  # 压力和温度关系
eqs.append(r"$\text{B} = \frac{V_{real}}{V_{ideal}}$")  # 比体积
eqs.append(r"$k = \frac{\text{d}\ln{C}}{\text{d}t}$")  # 反应速率常数

eqs.append(r"$\text{Cp} = \frac{\text{dH}}{\text{d}T}$")  # 定压热容
eqs.append(r"$\text{Cv} = \frac{\text{dU}}{\text{d}T}$")  # 定容热容
eqs.append(r"$\text{M} = \frac{w}{n}$")  # 物质的量浓度
eqs.append(r"$\text{V} = \text{nRT}/P$")  # 体积计算

# 设置图形大小和坐标轴
fig, ax = plt.subplots(figsize=(16, 9))

# 隐藏所有 spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# 定义公式大小范围
min_font_size = 16
max_font_size = 32

# 设置图形的边距
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

# 随机化布局
for eq in eqs:
    size = np.random.uniform(min_font_size, max_font_size)
    x, y = np.random.uniform(0.05, 0.95), np.random.uniform(0.05, 0.95)
    alpha = np.random.uniform(0.25, 0.75) if size < (min_font_size + max_font_size) / 2 else 0.5
    
    # 临时绘制公式并计算边界
    text_obj = ax.text(x, y, eq, ha='center', va='center', color="black", alpha=alpha,
                       transform=ax.transAxes, fontsize=size, clip_on=True)
    
    # 检查公式是否超出边界
    bbox = text_obj.get_window_extent(renderer=fig.canvas.get_renderer())
    bbox = bbox.transformed(ax.transAxes.inverted())
    
    # 如果公式超出边界，则重新设置位置
    while (bbox.x0 < 0 or bbox.x1 > 1 or bbox.y0 < 0 or bbox.y1 > 1):
        x, y = np.random.uniform(0.05, 0.95), np.random.uniform(0.05, 0.95)
        text_obj.set_x(x)
        text_obj.set_y(y)
        bbox = text_obj.get_window_extent(renderer=fig.canvas.get_renderer())
        bbox = bbox.transformed(ax.transAxes.inverted())

    ax.text(x, y, eq, ha='center', va='center', color="black", alpha=alpha,
            transform=ax.transAxes, fontsize=size, clip_on=True)

# 去掉坐标刻度
ax.set_xticks([])
ax.set_yticks([])

# 保存和展示图像
plt.savefig('chemical_engineering_formulas_random.png', dpi=300, bbox_inches='tight')
plt.show()
