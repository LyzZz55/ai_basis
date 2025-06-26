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























以下是Agent2有关内容最初策划的备份

**Agent 2: 内容创意孵化与多维形式策划Agent (Content Idea Incubation & Multi-Dimensional Format Planning Agent)**

* **核心输入 (Core Inputs - Highly Detailed):**
  * Agent 1输出的全部战略文档和洞察报告。
  * 品牌方提供的现有内容资产库访问权限或样本（如博客文章、产品图片/视频库、设计素材、FAQ文档）。
  * 特定营销活动需求（如新品上市推广、节日促销、品牌周年庆、公益活动等）。
  * 明确的内容创作预算档位（来自Agent 1或用户确认）。
  * 任何已知的法律、合规、伦理红线或品牌禁忌（如不可使用的词语、图像，需要规避的话题）。
* **细化子任务与处理流程 (Detailed Sub-tasks & Processing Flow):**
  1.  **多维度创意风暴与筛选 (Multi-Dimensional Ideation & Filtering):**
      * **基于信息支柱：** 针对`Brand_Social_Media_Strategic_Playbook.docx`中的每个核心信息支柱，结合每个`Target_Audience_Persona_Portfolio.pdf`的痛点、兴趣点和用户旅程阶段，进行发散性创意构思。
      * **结合趋势与热点：** 将Agent 1识别的行业趋势、社交热点、成功竞品案例作为灵感来源，思考如何与品牌信息结合。
      * **运用创意方法论：** 内部调用SCAMPER、六顶思考帽、逆向思考等创意方法论的逻辑，生成多样化创意点。
      * **初步筛选与打分：** 根据创意与品牌定位的契合度、目标受众的吸引力、可执行性、潜在传播力、预算符合度等标准，对海量创意点进行初步筛选和内部评分。
  2.  **内容主题与系列规划 (Content Pillar & Series Planning):**
      * 将筛选后的优质创意点归类，围绕核心信息支柱，规划出3-5个可持续的内容主题系列 (Content Series) 或内容栏目。
      * 每个系列/栏目应有明确的定位、目标受众细分、核心价值传递和大致的更新频次。
  3.  **内容形式与平台适配精细化 (Content Format & Platform Adaptation Refinement):**
      * 为每个内容主题系列下的具体创意点，匹配最合适的1-2种主要内容表现形式（如深度图文、条漫、Vlog、短剧本、科普动画、数据可视化报告、互动H5、播客、在线研讨会、UGC活动等）。
      * **跨平台分发与再创作策略：** 规划核心内容“一鱼多吃”的策略，例如：一篇深度行业报告可拆解为：
        * 微信公众号：完整版PDF下载 + 图文精炼解读。
        * 微博：核心观点长图 + 9宫格金句海报 + 互动抽奖。
        * 抖音/快手：核心观点动画短视频 + 真人出镜解读。
        * 小红书：报告中的实用Tips + 精美排版笔记。
        * B站：深度解读视频 + 配合报告的教程。
      * 明确各平台内容的侧重点和优化方向（如标题党优化、视觉优化、互动引导优化）。
  4.  **旗舰内容深度策划与脚本/大纲撰写 (Flagship Content Deep Planning & Script/Outline Writing):**
      * 选取3-5个最具代表性或战略意义的“旗舰级”内容创意，进行深度策划。
      * **图文类 (微信长文/博客/深度报告)：** 详细大纲（包含各级标题、核心论点、数据/案例支撑点、图表规划、SEO关键词布局）、引人入胜的开头、强有力的结尾、明确的CTA。
      * **视频类 (短视频/Vlog/动画)：** 详细分镜头脚本或故事板大纲（场景描述、人物动作/对话、镜头语言、BGM/音效建议、时长控制、字幕要点）。
      * **音频类 (播客)：** 节目主题、嘉宾构想（如有）、核心议题与流程大纲、互动环节设计。
      * **互动类 (H5/小游戏/UGC活动)：** 活动主题、核心玩法/机制、用户参与路径、激励机制、预期效果、技术实现要点。
  5.  **初步文案撰写与A/B测试方案 (Initial Copywriting & A/B Testing Plan):**
      * 为部分社交媒体帖子（如未来1-2周的核心平台帖子）撰写A/B两种不同风格或侧重点的文案初稿（标题、正文、CTA）。
      * 针对关键转化环节（如活动报名页、产品落地页），设计文案A/B测试的变量和衡量指标。
  6.  **内容日历精细化编排 (Detailed Editorial Calendar Creation):**
      * 创建至少1-3个月的内容日历 (Content Calendar)，具体到每日/每周。
      * **字段包括：** 发布日期、发布时间（基于Agent 1对目标受众活跃时间的分析）、目标平台、内容主题/标题、内容系列/栏目、主要形式、辅助形式（跨平台分发）、核心创意点/Brief链接、状态（策划中/待设计/待发布等）、负责人（留空）、关联营销活动、主要CTA、预期KPIs（来自Agent 1初步框架）。
      * 确保内容组合的多样性（信息性、娱乐性、互动性、促销性按比例搭配，如经典的4-1-1法则或80/20法则）和发布的持续性与节奏感。
      * 整合重要的行业会议、节假日、品牌纪念日等，提前规划相关主题内容。
* **API与工具细化调用 (Detailed API & Tool Usage):**
  * **LLMs (OpenAI GPT-4/Claude 3 Opus/Gemini Advanced via API):**
    * **创意生成：** 基于Agent 1的策略输入，生成大量初步内容创意点、标题选项、Slogan。
    * **大纲撰写：** 为博客、文章、视频脚本、播客等生成详细大纲。
    * **文案初稿：** 为社交媒体帖子、广告语、邮件等撰写A/B版文案。
    * **内容改写与适配：** 将长内容改写为适合不同平台的短内容，或调整语气风格。
  * **内容灵感与趋势发现工具API (如 BuzzSumo API, AnswerThePublic (通过爬虫或间接方式获取数据), Google Trends API):** 验证创意热度，发现用户常问问题，拓展相关话题。
  * **项目管理与协作工具API (如 Trello API, Asana API, Monday.com API, Airtable API, Notion API):** 将生成的内容日历和内容Brief结构化地输出到这些平台，方便团队协作。
  * **SEO关键词工具API (复用Agent 1的工具):** 在撰写大纲和文案时，确保融入目标SEO关键词。
  * **Canva API (若未来提供更强创作能力) / Veed.io API (视频编辑类):** 理论上可用于根据文本描述生成初步的图文排版概念或视频剪辑片段（目前更多是辅助）。
* **内部逻辑与知识库 (Internal Logic & Knowledge Base):**
  * 创意方法论模型库（SCAMPER, 结构化思维导图等）。
  * 内容形式与平台最佳实践数据库（如各平台理想视频时长、图文比例、互动机制）。
  * 内容 repurposing 逻辑规则库（如长文转短视频的关键点提取逻辑）。
  * A/B测试设计原则与常见变量库。
  * 内容日历模板与内容类型配比算法（如基于“英雄-枢纽-卫生”（Hero-Hub-Help）内容模型）。
  * 各行业优秀内容案例库（用于启发，持续更新）。
* **输出 (结构化数据与深度报告) (Outputs - Structured Data & In-depth Reports):**
  * `Content_Idea_Repository_&_Prioritization_Matrix.xlsx`: 包含所有脑暴创意点、筛选标准打分、优先级排序、所属内容主题系列。
  * `Detailed_Content_Series_Blueprints.docx`: 每个内容主题系列的详细规划（定位、目标、核心价值、代表性创意示例、建议形式与频次）。
  * `Flagship_Content_Creative_Briefs_Package.zip`: 包含3-5个旗舰级内容的深度策划文档（图文大纲、视频脚本/故事板、活动策划案等）。
  * `Draft_Copy_AB_Testing_Proposals.docx`: 针对部分帖子的A/B文案初稿及测试衡量建议。
  * `Master_Editorial_Calendar_(Next_1-3_Months).xlsx/Google Sheets Link`: 包含所有细化字段的交互式内容日历。
  * `Cross-Platform_Content_Repurposing_Guide.pdf`: 针对核心内容形式，提供详细的跨平台分发和再创作指导。
  * **传递给Agent 3的数据:** 上述所有输出，特别是`Master_Editorial_Calendar`, `Flagship_Content_Creative_Briefs_Package`, `Draft_Copy_AB_Testing_Proposals`，以及Agent 1输出的`Brand_Social_Media_Strategic_Playbook.docx`（尤其是“人设”和“语调”部分，指导视觉风格）。
