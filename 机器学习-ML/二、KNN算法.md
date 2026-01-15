## KNN算法简介

### **学习目标：**

1.理解K近邻算法的思想

2.知道K值选择对结果影响

3.知道K近邻算法分类流程

4.知道K近邻算法回归流程

### 【理解】KNN算法思想

K-近邻算法（K Nearest Neighbor，简称KNN）。比如：根据你的“邻居”来推断出你的类别

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/e721a0358da9417092b9cc0864df1e61.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=8e2b70ed6f5d215b41e9e826ed7de6e4be7ada71)

KNN算法思想：如果一个样本在特征空间中的 k 个最相似的样本中的大多数属于某一个类别，则该样本也属于这个类别

思考：如何确定样本的相似性？

**样本相似性**：样本都是属于一个任务数据集的。样本距离越近则越相似。

利用K近邻算法预测电影类型

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/b457e59ad5c9409eb479ecc3f7dc3b61.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=39d399de44d482df0a2063e230be1a8afe94c0f5)

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/508a267711364062897e6a0a41a3363d.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=749d8d96a9004a4905be9a8ae14cb6f29f35a18f)

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/1b291f4d860f4941a5d6762ae8ae4faa.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=e2db1a663daedea9594f72d7493bc1c7d63c35c4)

### 【知道】K值的选择

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/bd867b66b2b54d2cb5d9d8b15ab64952.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=021f71c9fbfd98951cb6f52774ef3bcbf2cd7a38)

### 【知道】KNN的应用方式

- 解决问题：分类问题、回归问题

- 算法思想：若一个样本在特征空间中的 k 个最相似的样本大多数属于某一个类别，则该样本也属于这个类别

- 相似性：欧氏距离

- 分类问题的处理流程：

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/2191c76e79154eb6877ab82e7e17de26.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=1b23df7f2732ef9f6c80912a8995ea40f28c3344)

1.计算未知样本到每一个训练样本的距离

2.将训练样本根据距离大小升序排列

3.取出距离最近的 K 个训练样本

4.进行多数表决，统计 K 个样本中哪个类别的样本个数最多

5.将未知的样本归属到出现次数最多的类别

- 回归问题的处理流程：

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/c08e2ebb710442d69952fdbe2dcc373f.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=f0e5df1f896d934ddaf64ab55f5734e9fd449f2c)

1.计算未知样本到每一个训练样本的距离

2.将训练样本根据距离大小升序排列

3.取出距离最近的 K 个训练样本

4.把这个 K 个样本的目标值计算其平均值

5.作为将未知的样本预测的值

## API介绍

### **学习目标：**

1.掌握KNN算法分类API

2.掌握KNN算法回归API

### 【实操】分类API

KNN分类API：

```
sklearn.neighbors.KNeighborsClassifier(n_neighbors=5) 
```

Python

n_neighbors：int,可选（默认= 5），k_neighbors查询默认使用的邻居数

### 【实操】回归API

KNN分类API：

```
sklearn.neighbors.KNeighborsRegressor(n_neighbors=5)
```

Python

```
# 1.工具包from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor# from sklearn.neighbors import KNeighborsRegressor
# 2.数据(特征工程)# 分类# x = [[0,2,3],[1,3,4],[3,5,6],[4,7,8],[2,3,4]]# y = [0,0,1,1,0]x = [[0,1,2],[1,2,3],[2,3,4],[3,4,5]]y = [0.1,0.2,0.3,0.4]
# 3.实例化# model =KNeighborsClassifier(n_neighbors=3)model =KNeighborsRegressor(n_neighbors=3)
# 4.训练model.fit(x,y)
# 5.预测print(model.predict([[4,4,5]]))
```

Python

## 距离度量方法

### **学习目标：**

1.掌握欧氏距离的计算方法

2.掌握曼哈顿距离的计算方法

3.了解切比雪夫距离的计算方法

4.了解闵可夫斯基距离的计算方法

### 【掌握】欧式距离

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/adec481b840e447ea04835078ac9e986.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=7fd73496cacfdaca600789e658310960f367c328)

### 【掌握】曼哈顿距离

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/6a82b7a9e775400fae8a93e9c98ddee3.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=68cb00e8a9b76437d0b3e287522ab98c3a4b080c)

### 【了解】切比雪夫距离

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/57bb72149b1e494facc4386d0f3f9fdc.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=2515dda0f424f359f09cc2ca8588d013ea260d4e)

### 【了解】闵氏距离

•闵可夫斯基距离 Minkowski Distance 闵氏距离，不是一种新的距离的度量方式。而是距离的组合 是对多个距离度量公式的概括性的表述

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/d03428be1405413facdcfb7a95d3754f.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=0411a1dc8d11a9ae8e3a29190b01a6acd2c511af)

## 特征预处理

### **学习目标：**

1.知道为什么进行归一化、标准化

2.能应用归一化API处理数据

3.能应用标准化API处理数据

4.使用KNN算法进行鸢尾花分类

### 【知道】为什么进行归一化、标准化

特征的**单位或者大小相差较大，或者某特征的方差相比其他的特征要大出几个数量级**，**容易影响（支配）目标结果**，使得一些模型（算法）无法学习到其它的特征。

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/26bef759d4b3411a8948c7fdd0806a0c.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=442fbb5e4c443b5e0a3d46aad5a3bf93d04fa983)

### 【掌握】归一化

通过对原始数据进行变换把数据映射到【mi,mx】(默认为[0,1])之间

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/50be82db97574446a63fbe7f7d1bea79.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=ed040ab38df7773e388fbb8dbf41b35f0ddd63e0)

数据归一化的API实现

```
sklearn.preprocessing.MinMaxScaler (feature_range=(0,1)… )
```

Plain Text

feature_range 缩放区间

- 调用 fit_transform(X) 将特征进行归一化缩放

归一化受到最大值与最小值的影响，这种方法容易受到异常数据的影响, 鲁棒性较差，适合传统精确小数据场景

### 【掌握】标准化

通过对原始数据进行标准化，转换为均值为0标准差为1的标准正态分布的数据

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/8af6476bd9a74d3d98804e6fe6b6f47e.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=be21c8d8f109e6624386f8037e3100fcb297be17)

- mean 为特征的平均值

- σ 为特征的标准差

数据标准化的API实现

```
sklearn.preprocessing. StandardScaler()
```

Python

调用 fit_transform(X) 将特征进行归一化缩放

```
# 1.导入工具包from sklearn.preprocessing import MinMaxScaler,StandardScaler
# 2.数据(只有特征)x = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]
# 3.实例化(归一化,标准化)# process =MinMaxScaler()process =StandardScaler()
# 4.fit_transform 处理1data =process.fit_transform(x)# print(data)
print(process.mean_)print(process.var_)
```

Python

对于标准化来说，如果出现异常点，由于具有一定数据量，少量的异常点对于平均值的影响并不大

### 【实操】利用KNN算法进行鸢尾花分类

鸢尾花Iris Dataset数据集是机器学习领域经典数据集，鸢尾花数据集包含了150条鸢尾花信息，每50条取自三个鸢尾花中之一：Versicolour、Setosa和Virginica

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/5415cf3db8fc4486b36cef90977877c5.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=fa2dfd705261e52165bc14bfd0334501f7542f71)

每个花的特征用如下属性描述：

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/6fdd4beb46854c38a5689f921a5f2a85.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=f39982944e472746334081bb3f0d16142c90c7b4)

代码实现：

```
# 导入工具包from sklearn.datasets import load_iris # 加载鸢尾花测试集的.import seaborn as snsimport pandas as pdimport matplotlib.pyplot as pltfrom sklearn.model_selection import train_test_split # 分割训练集和测试集的from sklearn.preprocessing import StandardScaler # 数据标准化的from sklearn.neighbors import KNeighborsClassifier # KNN算法 分类对象from sklearn.metrics import accuracy_score # 模型评估的, 计算模型预测的准确率

# 1. 定义函数 dm01_loadiris(), 加载数据集.def dm01_loadiris(): # 1. 加载数据集, 查看数据 iris_data = load_iris() print(iris_data) # 字典形式, 键: 属性名, 值: 数据. print(iris_data.keys())
 # 1.1 查看数据集 print(iris_data.data[:5]) # 1.2 查看目标值. print(iris_data.target) # 1.3 查看目标值名字. print(iris_data.target_names) # 1.4 查看特征名. print(iris_data.feature_names) # 1.5 查看数据集的描述信息. print(iris_data.DESCR) # 1.6 查看数据文件路径 print(iris_data.filename)
# 2. 定义函数 dm02_showiris(), 显示鸢尾花数据.def dm02_showiris(): # 1. 加载数据集, 查看数据 iris_data = load_iris() # 2. 数据展示 # 读取数据, 并设置 特征名为列名. iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names) # print(iris_df.head(5)) iris_df['label'] = iris_data.target
 # 可视化, x=花瓣长度, y=花瓣宽度, data=iris的df对象, hue=颜色区分, fit_reg=False 不绘制拟合回归线. sns.lmplot(x='petal length (cm)', y='petal width (cm)', data=iris_df, hue='label', fit_reg=False) plt.title('iris data') plt.show()

# 3. 定义函数 dm03_train_test_split(), 实现: 数据集划分def dm03_train_test_split(): # 1. 加载数据集, 查看数据 iris_data = load_iris() # 2. 划分数据集, 即: 特征工程(预处理-标准化) x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=22) print(f'数据总数量: {len(iris_data.data)}') print(f'训练集中的x-特征值: {len(x_train)}') print(f'训练集中的y-目标值: {len(y_train)}') print(f'测试集中的x-特征值: {len(x_test)}')
# 4. 定义函数 dm04_模型训练和预测(), 实现: 模型训练和预测def dm04_model_train_and_predict(): # 1. 加载数据集, 查看数据 iris_data = load_iris()
 # 2. 划分数据集, 即: 数据基本处理 x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=22)
 # 3. 数据集预处理-数据标准化(即: 标准的正态分布的数据集) transfer = StandardScaler() # fit_transform(): 适用于首次对数据进行标准化处理的情况，通常用于训练集, 能同时完成 fit() 和 transform()。 x_train = transfer.fit_transform(x_train) # transform(): 适用于对测试集进行标准化处理的情况，通常用于测试集或新的数据. 不需要重新计算统计量。 x_test = transfer.transform(x_test)
 # 4. 机器学习(模型训练) estimator = KNeighborsClassifier(n_neighbors=5) estimator.fit(x_train, y_train)
 # 5. 模型评估. # 场景1: 对抽取出的测试集做预测. # 5.1 模型评估, 对抽取出的测试集做预测. y_predict = estimator.predict(x_test) print(f'预测结果为: {y_predict}')
 # 场景2: 对新的数据进行预测. # 5.2 模型预测, 对测试集进行预测. # 5.2.1 定义测试数据集. my_data = [[5.1, 3.5, 1.4, 0.2]] # 5.2.2 对测试数据进行-数据标准化. my_data = transfer.transform(my_data) # 5.2.3 模型预测. my_predict = estimator.predict(my_data) print(f'预测结果为: {my_predict}')
 # 5.2.4 模型预测概率, 返回每个类别的预测概率 my_predict_proba = estimator.predict_proba(my_data) print(f'预测概率为: {my_predict_proba}')
 # 6. 模型预估, 有两种方式, 均可. # 6.1 模型预估, 方式1: 直接计算准确率, 100个样本中模型预测正确的个数. my_score = estimator.score(x_test, y_test) print(my_score) # 0.9666666666666667
 # 6.2 模型预估, 方式2: 采用预测值和真实值进行对比, 得到准确率. print(accuracy_score(y_test, y_predict))

# 在main方法中测试.if __name__ == '__main__': # 1. 调用函数 dm01_loadiris(), 加载数据集. # dm01_loadiris()
 # 2. 调用函数 dm02_showiris(), 显示鸢尾花数据. # dm02_showiris()
 # 3. 调用函数 dm03_train_test_split(), 查看: 数据集划分 # dm03_train_test_split()
 # 4. 调用函数 dm04_模型训练和预测(), 实现: 模型训练和预测 dm04_model_train_and_predict()
```

Python

## 超参数选择的方法

### **学习目标：**

1.知道交叉验证是什么？

2.知道网格搜索是什么？

3.知道交叉验证网格搜索API函数用法

4.能实践交叉验证网格搜索进行模型超参数调优

5.利用KNN算法实现手写数字识别

### 【知道】交叉验证

交叉验证是一种数据集的分割方法，将训练集划分为 n 份，其中一份做验证集、其他n-1份做训练集集

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/7913a875a3f14037a2fd08460bfa97b6.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=163f99c3772f0f85e0cad455b8c5c9bdfdb0d974)

**交叉验证法原理**：将数据集划分为 cv=10 份：

1.第一次：把第一份数据做验证集，其他数据做训练

2.第二次：把第二份数据做验证集，其他数据做训练

3.... 以此类推，总共训练10次，评估10次。

4.使用训练集+验证集多次评估模型，取平均值做交叉验证为模型得分

5.若k=5模型得分最好，再使用全部训练集(训练集+验证集) 对k=5模型再训练一边，再使用测试集对k=5模型做评估

### 【知道】网格搜索

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/d261aa1c32a047748c04d264dc0bf899.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=b4aa577ee7ab9923de1807f2c55cda1675d3371e)

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/0f99dce7b7d742c7b641eb5840f0fc12.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=d13bc2898f8462b4cf787d3c2bc1a57608f7f2a7)

交叉验证网格搜索的API:

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/d1844ba8ae424d09919a3a40e02042c9.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=bfac5671ca8c052e481f2a3bd1421e950e4ce5e5)

交叉验证网格搜索在鸢尾花分类中的应用：

```
from sklearn.datasets import load_iris # 加载鸢尾花测试集的.from sklearn.model_selection import train_test_split, GridSearchCV # 分割训练集和测试集的, 网格搜索的from sklearn.preprocessing import StandardScaler # 数据标准化的from sklearn.neighbors import KNeighborsClassifier # KNN算法 分类对象from sklearn.metrics import accuracy_score # 模型评估的, 计算模型预测的准确率

# 1. 获取数据集.iris_data = load_iris()
# 2. 数据基本处理-划分数据集.x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=22)
# 3. 数据集预处理-数据标准化.transfer = StandardScaler()x_train = transfer.fit_transform(x_train)x_test = transfer.transform(x_test)
# 4. 模型训练.# 4.1 创建估计器对象.estimator = KNeighborsClassifier()# 4.2 使用校验验证网格搜索. 指定参数范围.param_grid = {"n_neighbors": range(1, 10)}# 4.3 具体的 网格搜索过程 + 交叉验证.# 参1: 估计器对象, 参2: 参数范围, 参3: 交叉验证的折数.estimator = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=5)# 具体的模型训练过程.estimator.fit(x_train, y_train)

# 4.4 交叉验证, 网格搜索结果查看.print(estimator.best_score_) # 模型在交叉验证中, 所有参数组合中的最高平均测试得分print(estimator.best_estimator_) # 最优的估计器对象.print(estimator.cv_results_) # 模型在交叉验证中的结果.print(estimator.best_params_) # 模型在交叉验证中的结果.

# 5. 得到最优模型后, 对模型重新预测.estimator = KNeighborsClassifier(n_neighbors=6)estimator.fit(x_train, y_train)print(f'模型评估: {estimator.score(x_test, y_test)}') # 因为数据量和特征的问题, 该值可能小于上述的平均测试得分.
```

Python

### 利用KNN算法实现手写数字识别

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/de1a05d6ced04ce09c4b5d38c6d3496e.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=8aba096e3a352cc06c13cade1b8e6ce444fd68a7)

MNIST手写数字识别 是计算机视觉领域中 "hello world"级别的数据集

- 1999年发布，成为分类算法基准测试的基础

- 随着新的机器学习技术的出现，MNIST仍然是研究人员和学习者的可靠资源。

本次案例中，我们的目标是从数万个手写图像的数据集中正确识别数字。

### 数据介绍

数据文件 train.csv 和 test.csv 包含从 0 到 9 的手绘数字的灰度图像。

- 每个图像高 28 像素，宽28 像素，共784个像素。

- 每个像素取值范围[0,255]，取值越大意味着该像素颜色越深

- 训练数据集（train.csv）共785列。第一列为 "标签"，为该图片对应的手写数字。其余784列为该图像的像素值

- 训练集中的特征名称均有pixel前缀，后面的数字（[0,783])代表了像素的序号。

像素组成图像如下：

```
000 001 002 003 ... 026 027028 029 030 031 ... 054 055056 057 058 059 ... 082 083 | | | | ...... | |728 729 730 731 ... 754 755756 757 758 759 ... 782 783
```

Python

数据集示例如下:

![](https://ima-notebook-prod.image.myqcloud.com/2/euj3C84o4TSOPtfpda0fYP/0b1db278d61b4ddeadfd3497222e6f68.webp?q-sign-algorithm=sha1&q-ak=AKID9IDtLZZKqGRO7hVFnMn0zjXTXovoTtAN&q-sign-time=1768453434;1768482234&q-key-time=1768453434;1768482234&q-header-list=&q-url-param-list=&q-signature=e9b0f659eb3fa9397a001b95831bbbfd80cd0e9c)

```
import matplotlib.pyplot as pltimport pandas as pdfrom sklearn.model_selection import train_test_splitfrom sklearn.neighbors import KNeighborsClassifierimport joblibfrom collections import Counter

# 1. 显示图片.def show_digit(idx): # 1.1 加载数据. data = pd.read_csv('手写数字识别.csv') # 1.2非法值校验. if idx < 0 or idx > len(data) - 1: return # 1.3 打印数据基本信息 x = data.iloc[:, 1:] y = data.iloc[:, 0] print(f'数据基本信息: {x.shape})') print(f'类别数据比例: {Counter(y)}')
 # 显示图片 # 1.4 将数据形状修改为: 28*28 digit = x.iloc[idx].values.reshape(28, 28) # 1.5 关闭坐标轴标签 plt.axis('off') # 1.6 显示图像 plt.imshow(digit, cmap='gray') # 灰色显示 plt.show()

# 2. 训练模型.def train_model(): # 1. 加载数据. data = pd.read_csv('手写数字识别.csv') x = data.iloc[:, 1:] y = data.iloc[:, 0]
 # 2.数据预处理, 归一化. x = x / 255
 # 3. 分割训练集和测试集. # stratify: 按照y的类别比例进行分割 x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=21)
 # 4. 训练模型 estimator = KNeighborsClassifier(n_neighbors=3) estimator.fit(x_train, y_train)
 # 5. 模型评估 my_score = estimator.score(x_test, y_test) print(f'测试集准确率为: {my_score:.2f}')
 # 6. 模型保存. joblib.dump(estimator, 'model/knn.pth')
# 3. 测试模型.def use_model(): # 1. 读取图片 img = plt.imread('data/demo.png') # 灰度图, 28*28像素 plt.imshow(img, cmap='gray') plt.show()
 # 2. 加载模型. estimator = joblib.load('model/knn.pth')
 # 3. 预测图片. img = img.reshape(1, -1) # 形状从: (28, 28) => (1, 784) # print(img.shape) y_test = estimator.predict(img) print(f'您绘制的数字是: {y_test}')
# 在main函数中测试if __name__ == '__main__': # 1. 调用函数, 查看图片. # show_digit(0) # show_digit(10) # show_digit(100)
 # 2. 训练模型. # train_model()
 # 3. 测试模型 use_model()
```

Python

## 作业

1.完成KNN算法部分的思维导图

2.说明常见的距离度量方法

3.说明特征预处理的方法

4.编写KNN代码实现鸢尾花分类案例

5.编写KNN代码实现手写数字识别（特征预处理，交叉验证网格搜索）