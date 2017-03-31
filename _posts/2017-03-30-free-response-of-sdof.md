---
layout: post
title: 单自由度系统的自由响应
categories:
- NVH
---

这世间, 每时每刻存在振动. 振动形式分类:

- 自由振动
    - 单自由度系统
    - 多自由度系统
- 强迫振动
    - 单自由度系统
    - 多自由度系统

现在简单讲讲单自由度系统的自由振动

# 1 自由振动

什么是自由振动? 

我们以最简单的弹簧质量系统为例. 如下图a所示:

![fig-1-mass-damping-system](https://dn-jeremiahzhang.qbox.me/NVH-EV-F-1-9-SDOF-viscous-damping.JPG)

其中:

- m 为系统质量
- c 为系统阻尼(假设为粘性阻尼)
- k 为系统刚度
- x(t) 为系统的位移响应
- 另外: 不计地面摩擦 比较理想的情况

那么, 什么是该系统的自由振动呢？就是我给予上述质量为m的物体一个初始条件, 让它动起来, 其后就没有任何外界输入, 任凭其自由响应去. 这个初始条件（初始激励物体动力来的条件）可最后转化为:

1. 初始速度 $$v_0$$
2. 初始位移 $$x_0$$

# 2 自由振动响应

上面的弹簧质量系统, 设定好方向, 可以根据牛顿第二运动定律:(eq 1.24) 

$$m\ddot{x} = -f_c - f_k$$

得到其运动微分方程(eq 1.25):

$$m\ddot{x(t)} + c\dot{x(t)} + kx(t) = 0$$

解该运动微分方程, 根据阻尼比$$\zeta = \frac{c}{2m\omega_n} = \frac{m}{2\sqrt{km}}$$, 系统有分为三种不同形式：

1. 临界阻尼系统 $$\zeta = 1$$
2. 欠阻尼系统 $$\zeta < 1$$
3. 过阻尼系统 $$\zeta > 1$$

不同形式下, 系统响应也不同.

## 2.1 临界阻尼系统

什么是临界阻尼系统? 就是其阻尼正好为临界阻尼 $$c = c_cr$$, 

$$c_{cr} = 2m\omega_n = 2\sqrt{k m}$$  

此时, 系统响应为(eq(1.45))

$$x(t) = (a_1 + a_2t)e^{-\omega_nt}$$  

而 eq (1.46)：

$$ a_1 = x_0 $$  
$$ a_2 = v_0 + \omega_n x_0 $$  

$$x_0$$为初始位移, $$v_0$$为初始速度.

## 2.2 欠阻尼系统

对于欠阻尼系统, $$c < c_{cr}$$, 系统响应为:

$$x(t) = A e^{-\zeta \omega_n t}\sin(\omega_d t + \phi)$$  

其中：

$$\omega_d = \omega_n \sqrt{1 - \zeta ^ 2}$$  
$$ A = \sqrt{\frac{(v_0 + \zeta \omega_n x_0)^2 + (x_0 \omega_d)^2)}{\omega_d ^2}}$$  
$$\phi = \tan^{-1}(\frac{x_0 \omega_d}{v_0 + \zeta \omega x_0})$$

## 2.3 过阻尼系统

过阻尼系统中, $$ c > c_{cr} $$, 系统响应为:  

$$x(t) = e^{-\zeta \omega_n t}(a_1 e^{-\omega_n \sqrt{\zeta^2-1}t} + a_2 e^{\omega_n \sqrt{\zeta^2 -1}t})$$

其中, 

$$a_1 = \frac{-v_0 + (-\zeta + \sqrt{\zeta^2 -1}) \omega_n x_0}{2 \omega_n \sqrt{\zeta^2 -1}}$$  
$$a_2 = \frac{v_0 + (\zeta + \sqrt{\zeta^2 -1}) \omega_n x_0}{2 \omega_n \sqrt{\zeta^2 -1}}$$

---

# 3 matlab 实现

[**vtb_1_1_freeSDOF**](https://github.com/JeremiahZhang/Alpha2Omega/blob/master/nvh/vtbCopyCoding/vtb_1_1_freeSDOF.m) 如下:

```
function vtb_1_1_freeSDOF(m, c, k, x0, v0, tf)

% Free response of a single degree of freedom system.
%% method 1:
%   vtb_1_1_freeSDOF(m, c, k, x0, v0, tf) if the number of 
%   parameters is six(6):
%       m     is the mass 
%       c     is the damping
%       k     is the stiffness
%       x0    is the initial condition, initial displacement
%       v0    is the initial condition, initial velocity
%       tf    is the finial time to plot the response
%% method 2:
%   vtb_1_1_freeSDOF(zeta, w, x0, v0, tf) if the number of 
%   parameters is five(5):
%       zeta: the damping ratio
%       w:    natural frequency in rad/s
%       x0    is the initial condition, initial displacement
%       v0    is the initial condition, initial velocity
%       tf    is the finial time to plot the response
%% example: 
% Free respone for 
% m = 1
% c = 0.01
% k = 2
% x0 = 1
% v0 = 0
% tf = 100, for 100 sec
% in Matlab console, type:
% vtb_1_1_freeSDOF(1, 0.01, 2, 1, 0, 100)

%% This loop determines which method you are using
% if you choose method 2, there is only 5 argv
if nargin == 5
    z = m;
    w = c;
    x0 = k;
    v0 = x0;
    tf = v0;
    m = 1;
    c = 2 * m * w * z;  % from eq(1.30)
    k = w ^ 2;
end

% The default method is method 1, there are 6 parameters
w = sqrt(k / m); % the natural frequency of the SDOF system
z = c /(2 * m * w); % zeta the damping ratio eq(1.30)
wd = w * sqrt(1 - z^2); % the damped natural frequency eq(1.37)

fprintf('The natural frequency is %.3g rad/s.\n', w);
fprintf('The damping ratio is %.3g.\n', z);
fprintf('The damped natural frequency is %.3g. \n', wd);

t = 0 : tf/1000: tf;
% different damping ratio
if z < 1 % 欠阻尼
    A = sqrt(((v0 + z*w*x0)^2 + (x0*wd)^2) / (wd^2)); % 响应幅值, eq(1.38)
    phi = atan2((x0*wd), (v0 + z*w*x0)); % 相位角, eq(1.38)
    x = A * exp(-z*w*t) .* sin(wd*t + phi); % 系统响应 eq(1.36)
    fprintf('响应幅值 A = %.3g\n', A);
    fprintf('相位角 phi = %.3g\n', phi);
elseif z == 1 % 临界阻尼
    a1 = x0; % eq(1.46)
    a2 = v0 + w*x0; % eq(1.46)
    x = (a1 + a2*t) .* exp(-w*t); % eq(1.45)
    fprintf('系数 a1 = %.3g\n', a1);
    fprintf('系数 a2 = %.3g\n', a2);
else
    a1 = (-v0 + (-z + sqrt(z^2 - 1)) * w * x0) / (2 * w * sqrt(z^2 - 1)); % eq(1.42)
    a2 = (v0 + (z + sqrt(z^2 - 1)) * w * x0) / (2 * w * sqrt(z^2 - 1)); % eq(1.43)
    x = exp(-z*w*t) .* (a1 * exp(-w*sqrt(z^2-1)*t) + a2 * exp(w*sqrt(z^2-1)*t)); % eq(1.41)
    fprintf('系数 a1 = %.3g\n', a1);
    fprintf('系数 a2 = %.3g\n', a2);
end

figure

plot(t, x);
xlabel('时间t');
ylabel('响应-位移x');
title('位移-时间')

grid on
```

对于质量 $$m=1, k=4$$, 其临界阻尼为 $$c_{cr} = 2 \sqrt{km} = 4$$

1. 临界阻尼时, (阻尼为4) 在matlab中运行

```
vtb_1_1_freeSDOF(1, 4, 4, 1, 0, 100)
```

绘制图形如下：

![1 NVH-critial-damping-sdof](https://dn-jeremiahzhang.qbox.me/NVH-critial-damping-sdof.jpg)

系统位移在5s内很快衰减为0

2. 过阻尼时, (阻尼设为10), 在matlab中运行

```
vtb_1_1_freeSDOF(1,10, 4, 0.1, 0, 30)
```

绘制图形如下:

![2 NVH-over-damping-sdof](https://dn-jeremiahzhang.qbox.me/NVH-over-damping-sdof.jpg)

系统位移衰减比临界阻尼时的慢.

3. 欠阻尼时, (阻尼设为0.5), 在matlab中运行

```
vtb_1_1_freeSDOF(1, .5, 4, 0.1, 0, 30)
```

绘制图形如下:

![3 NVH-under-damping-sdof](https://dn-jeremiahzhang.qbox.me/NVH-under-damping-sdof.jpg)

系统位移呈振荡形式逐渐衰减为0.

---

# reference

- [Inman, Engineering Vibration, 4th Edition](https://www.pearsonhighered.com/program/Inman-Engineering-Vibration-4th-Edition/PGM198634.html)
- [vibrationtoolbox/vibration_toolbox](https://github.com/vibrationtoolbox/vibration_toolbox)

# Log

    Beta 1.0
    @Anifacc   
    2017-03-31

---