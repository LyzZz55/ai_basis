# 使用方法

## 环境配置

根据本地创建 python 环境，并使用 requirements.txt 给出所需依赖

```bash
pip install -r path/to/requirements.txt
```

## API 配置

配置你的.env

```
FLOW_API=""
GEMINI_API=''
SILICONFLOW_API_KEY=""
WANX_KEY=""
```

## 内容填充

填写 user_in 下的所有 txt 文件
`user_in` 文件夹下各 txt 文件内容说明如下：

- **basic.txt**  
  填写品牌基础信息，包括品牌全名、行业细分、官网、社交媒体账号等。

- **enemy.txt**  
  列出直接与间接竞争对手，包括品牌名称、定位、主要特点等。

- **facing.txt**  
  描述品牌当前的核心目标受众（TA）画像，包括基础属性、心理特征、行为数据等。

- **serve.txt**  
  详细说明品牌核心产品/服务，包括产品名称、描述、独特卖点（USP）、目标客户、价格区间及核心功能。

- **target.txt**  
  明确品牌阶段性营销目标（如季度目标），包括认知度、ROI、用户增长、会员体系等，并给出预算范围。

- **value.txt**  
  介绍品牌故事、使命愿景及核心价值观，如成分透明、可持续发展、环保理念等。

## 运行

```python
python3 agent_general.py -i user_in/in.json
```
