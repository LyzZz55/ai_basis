# ai_basis

## 本部分内容是Agent2相关的内容

### 有关输入：

本部分接受agent1的输入，有关输入的具体要求按照Agent1给出的要求得到，具体输入格式如下：

在本文件 xxx[Main].py 的相对路径下，另设一文件路径 /part1_in 在此相对目录下接受一个json文件并按照json要求读取同一相对目录下的txt文件作为输入，然后连携Agent1的输入进行运行和操作


### 有关输出：

类似输入，为便于输入输出复用，主程序在相对目录下生成一个/outputs的文件夹，其中包含生成的txt, md, xlsx等各种格式的文件作为所需输出和Agent3的输入，然后给出一个json格式文件作为读取的方法

Agent3连携读入Agent1,2输出时可以参考本程序utils和[Main]里相关代码实现


输出的json格式示例:
```
{
    "files": [
        {
            "path": "outputs/Content_Idea_Repository.xlsx",
            "comment": "内容创意库及优先级排序矩阵",
            "type": "excel"
        },
        {
            "path": "outputs/Detailed_Content_Series_Blueprints.txt",
            "comment": "内容主题系列的详细规划蓝图",
            "type": "text"
        },
        {
            "path": "outputs/Cross-Platform_Content_Repurposing_Guide.txt",
            "comment": "旗舰内容的“一鱼多吃”跨平台分发指南",
            "type": "text"
        },
        {
            "path": "outputs/Flagship_Brief_1_程序员“代码续命”能量包.txt",
            "comment": "旗舰内容 '程序员“代码续命”能量包' 的深度策划案/大纲",
            "type": "text"
        },
        {
            "path": "outputs/Draft_Copy_AB_Testing_Proposals.txt",
            "comment": "社交媒体帖子的A/B测试文案初稿",
            "type": "text"
        },
        {
            "path": "outputs/Master_Editorial_Calendar.xlsx",
            "comment": "未来1-3个月的精细化内容日历",
            "type": "excel"
        }
    ]
}
```
### 有关生成的内容：

主要包含上述6个文件

**注意**：根据Agent1输入的关键词的不同，产出的文件名称也会随之改变，并无固定的文件名称。但是大致内容应与上述一致。

具体地，主要包括以下六个方面：（请主要关注文件的格式，生成的内容可能会随版本后续更新发生改变，但格式不变，适配于下一步读取工作）

#### 1. 多维度创意风暴与筛选

一个xlsx文件，相关内容为根据Agent1提供一些初步的创新点并按照重要性顺序提取前几个关键部分

#### 2. 内容主题与系列规划

一个txt文件，主要关于各个内容主题系列的详细规划（定位、目标等）

#### 3. 内容形式与平台适配

一个txt文件，主要是各个创意衍生出来的内容形式及其在各个不同平台上以较高适配度生成的相关发布策略和内容调整

#### 4. 旗舰内容深度策划

一个txt文件，同样基于大模型生成一些提取到的关键词并展开相关的内容策划

#### 5. 撰写A/B测试文案

一个txt文件，存储两个生发出来的内容文案，一个偏感性激进，另一个偏理性自然

#### 6. 创建内容日历

一个xlsx文件，根据以上内容创建一个按照时间对对应内容策划和相应适配平台进行具体内容发布的时间表






















