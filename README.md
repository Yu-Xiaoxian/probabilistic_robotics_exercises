# [Probabilistic Robotics Exercises](https://github.com/Yu-Xiaoxian/probabilistic_robotics_exercises)
# [《概率机器人》课后习题解答](https://github.com/Yu-Xiaoxian/probabilistic_robotics_exercises)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Yu-Xiaoxian/probabilistic_robotics_exercises/master)

Detailed Solutions for exercises of book "Probabilistic Robotics" in both English &amp; Chinese. Chinese Version will be finished first.

## 介绍

《概率机器人》课后习题解答，使用人工智能界比较流行的工具链「Python + Jupyter Notebook」，Python 实现作业的代码，Jupyter Notebook 增加文字描述并显示代码执行结果，做到图文并茂。

有三种方式可以看到渲染结果：
1. 直接在[Github](https://github.com/Yu-Xiaoxian/probabilistic_robotics_exercises/blob/master/简介.ipynb)上查看渲染结果
2. 在[nbviewer](https://nbviewer.org/github/Yu-Xiaoxian/probabilistic_robotics_exercises/blob/master/简介.ipynb)上在线看到效果
3. 本地运行

## 本地运行
首先安装 Jupyter
```shell
pip install notebook
```

```shell
git clone http://github.com/Yu-Xiaoxian/probabilistic_robotics_exercises.git
cd probabilistic_robotics_exercises
jupyter notebook
```

启动后会在命令行显示以下信息

```shell
[I 14:07:44.075 NotebookApp] Writing notebook server cookie secret to /run/user/1000/jupyter/notebook_cookie_secret
[I 14:07:45.058 NotebookApp] Serving notebooks from local directory: ****/probabilistic_robotics_exercises
[I 14:07:45.059 NotebookApp] 0 active kernels
[I 14:07:45.059 NotebookApp] The Jupyter Notebook is running at:
[I 14:07:45.060 NotebookApp] http://localhost:8888/
[I 14:07:45.060 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

访问 Jupyter Server http://localhost:8888 就可以看到了界面了

## 其他说明

解题过程中我参考了[pptacher](https://github.com/pptacher/probabilistic_robotics)的解答，作者[Pierre-Paul TACHER](https://github.com/pptacher)是法国的一名学者，他的解答严谨而简练，展现了法国人高水准的数学水平。为保证解答的准确性，我先自己求解，然后和pptacher 的答案进行对比，如果出现不一致再仔细检查推导过程。此外我在解答过程中会尽可能地偷懒，如使用在线工具求解矩阵特征向量，尽可能降低解答过程的繁琐程度。

## Reference

[E-Book 课本电子版](https://github.com/Yvon-Shong/Probabilistic-Robotics)

[Referenced Exercise 其他习题解答](https://github.com/pptacher/probabilistic_robotics)
