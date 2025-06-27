### 智能化品牌内容营销策划系统

**系统核心目标：** 在用户提供品牌基础信息、营销目标和初步受众画像后，通过三大核心 Agent 的深度协作和智能分析，自主生成一套全面、可执行、且高度定制化的社交媒体内容营销活动方案，包括市场洞察、策略定位、内容创意、视觉风格、发布排期及初步的推广和效果衡量框架。

---

#### **Agent 1: 市场洞察与策略定位 Agent (Market Insight & Strategic Positioning Agent)**

- **核心输入 (Core Inputs - Highly Detailed):**
  - **品牌深度信息 (In-depth Brand Information):**
    - **基础资料：** 品牌全名、所属行业细分、官方网站 URL、所有现有社交媒体平台链接。
    - **产品/服务详情：** 核心产品/服务列表，每个产品/服务的详细描述、独特销售主张 (USP)、目标客户、价格区间、主要功能与优势。
    - **品牌资产：** Logo 源文件 (SVG/AI preferred)、现有品牌视觉识别手册 (VI Guide, if any)、品牌故事、使命、愿景、核心价值观。
    - **营销目标 (SMART 原则)：** 具体、可衡量、可实现、相关性、时限性（例如：“在未来 6 个月内，针对 18-25 岁女性用户，通过小红书和抖音平台，将品牌 Z 的认知度提升 20%，并带来 500 个产品试用装申请”）。
    - **预算范围 (可选)：** 内容创作的大致预算范围 (如：低/中/高)，推广预算范围。
    - **竞争对手清单 (用户提供)：** 3-5 个用户认为的主要竞争对手。
    - **历史营销数据 (可选，若能 API 接入或文档上传)：** 过去 1-2 年营销活动报告（包括活动目标、执行情况、关键指标如 ROI/CPA/CTR、成功经验、失败教训）、网站流量分析报告、社交媒体后台分析数据。
    - **现有受众理解：** 品牌方目前对目标受众的描述（ demographics, psychographics, pain points）。
- **细化子任务与处理流程 (Detailed Sub-tasks & Processing Flow):**
  1.  **品牌资产数字化与初步分析 (Brand Asset Digitization & Initial Analysis):**
      - 抓取并解析品牌官网、现有社交媒体内容，提取当前品牌信息传递、内容主题、互动数据、粉丝评论情感。
      - 对提供的品牌 VI、故事等文档进行 NLP 分析，提炼核心品牌关键词和价值主张。
      - 初步评估品牌当前在线声量和情感倾向。
  2.  **全方位竞争对手深度剖析 (Comprehensive Competitor Deep-Dive):**
      - **智能识别补充：** 基于用户提供的列表和行业信息，通过市场分析工具智能识别另外 3-5 个潜在或间接竞争对手。
      - **多维度数据采集：** 对每个选定的竞争对手（共 6-10 个）：
        - **社交媒体表现：** 活跃平台、粉丝规模与增长率、发帖频率、内容类型分布（图文/视频/直播/互动）、平均互动率 (点赞、评论、分享)、热门帖子分析。
        - **内容策略逆向工程：** 分析其内容主题、叙事角度、视觉风格、文案语调、常用的#标签、主要营销活动类型。
        - **受众画像与情感：** 分析其粉丝评论、提及品牌的 UGC，推断其受众特征及对该品牌的情感。
        - **广告投放情况 (可选，若工具支持)：** 预估其在社交媒体的广告投放策略和创意。
        - **网站流量与 SEO 策略 (可选)：** 简要分析其网站流量来源及主要关键词排名，以了解其整体数字营销协同性。
      - **生成竞品对比矩阵：** 清晰展示各竞品在关键维度上的表现和策略差异。
  3.  **行业趋势与社交聆听 (Industry Trends & Social Listening):**
      - **宏观趋势：** 分析所在行业的最新市场报告、权威媒体资讯，识别宏观发展趋势、新兴技术/概念。
      - **社交热点与话题追踪：** 利用社交聆听工具，实时监测与品牌行业、产品、目标受众相关的热门话题、病毒内容、网络迷因 (Memes)、挑战赛等。
      - **关键词与#标签生态分析：** 识别行业核心关键词、长尾关键词、以及各类平台上的热门/潜力#标签簇。
      - **KOL/KOC 识别与分析：** 找出行业内有影响力的意见领袖 (KOL) 和关键意见消费者 (KOC)，分析其内容特点、粉丝画像、合作品牌。
  4.  **目标受众 360° 画像构建 (360° Target Audience Persona Development):**
      - **数据融合：** 整合品牌方提供的初步画像、竞品受众分析、行业社交聆听数据。
      - **多维细化：** 构建 2-4 个高度具体的目标受众画像 (Personas)，每个画像包含：
        - **基本人口统计学：** 姓名（虚拟）、年龄、性别、地理位置、职业、收入水平、教育背景、家庭状况。
        - **生活方式与价值观：** 兴趣爱好、日常习惯、消费观念、关注的社会议题、生活目标与追求。
        - **数字行为特征：** 常用的社交媒体平台、活跃时段、内容偏好（图文/短视频/直播/深度文章）、信息获取渠道、信任的 KOL/KOC。
        - **痛点与需求：** 与品牌产品/服务相关的未被满足的需求、使用现有解决方案的痛点。
        - **购买决策驱动因素：** 影响其购买决策的关键因素（价格、品牌、口碑、功能、情感连接等）。
        - **品牌互动偏好：** 期望与品牌建立怎样的关系，喜欢怎样的互动方式。
      - **用户旅程初步映射：** 针对每个 Persona，初步勾勒其在认知、兴趣、考虑、购买、忠诚等阶段的行为特征和信息需求。
  5.  **品牌差异化定位与沟通策略制定 (Brand Differentiation & Communication Strategy Formulation):**
      - **SWOT 分析与机会识别：** 结合内外部环境分析，明确品牌的核心优势、劣势、市场机会与潜在威胁。
      - **独特销售主张 (USP) 精炼：** 在市场竞争格局和目标受众需求的基础上，打磨或重塑品牌/产品的核心 USP。
      - **品牌“人设”与“语调”定义：** 为品牌在社交媒体上设定一个鲜明、一致且吸引目标受众的“人格化形象”（如：智慧导师型、幽默玩伴型、精致生活家型）和相应的沟通语调（如：专业严谨、亲切活泼、犀利风趣、温暖治愈）。
      - **核心信息屋 (Message House) 构建：** 围绕 USP 和品牌人设，构建包含 1 个核心信息、3-4 个支持性信息支柱和相应证据/例证的核心信息架构。
      - **平台选择与角色分配：** 根据目标受众画像的平台偏好、各平台特性及营销目标，推荐 2-3 个核心运营的社交媒体平台，并明确每个平台在整体营销策略中扮演的角色和侧重的内容方向（例如：微信公众号做深度内容沉淀和用户服务，微博做热点追踪和即时互动，小红书做生活方式种草和 UGC 激励，抖音做短平快趣味科普和品牌形象展示）。
- **API 与工具细化调用 (Detailed API & Tool Usage):**
  - **社交聆听与分析平台 API (如 Brandwatch, Talkwalker, Synthesio, Meltwater, Hootsuite Insights, Sprout Social Listening):** 用于实时抓取和分析社交媒体提及、情感、趋势、KOL 数据。输入关键词、品牌名、竞品名，获取提及量、情感分布、热门帖子、影响者列表。
  - **SEO 与内容营销工具 API (如 SEMrush, Ahrefs, Moz API, Google Trends API, Keyword Planner API):** 用于关键词研究、竞争对手网站流量分析、内容热度分析、相关话题发现。
  - **广告平台 API (如 Facebook Marketing API, TikTok Ads API, Google Ads API - 若有权限访问或用于分析公开数据):** 分析竞品广告投放的创意形式、文案特点和可能的受众定向策略（通过公开的广告库等）。
  - **消费者洞察平台 API (如 Nielsen API, GWI (GlobalWebIndex) API - 若有企业订阅):** 获取更深度的消费者行为和偏好数据。
  - **LLMs (OpenAI GPT-4/Claude 3 Opus/Gemini Advanced via API):** 用于文本摘要（如竞品报告、行业资讯）、情感分析（辅助社交聆听工具）、Persona 初稿生成、USP 及核心信息屋的草拟与润色。
  - **爬虫技术 (Web Scraping - 需遵守 robots.txt 和法律法规):** 用于抓取竞品网站、社交媒体公开页面信息，作为 API 的补充。
  - **知识图谱 API (如 Google Knowledge Graph API - 已不直接对外，但类似概念，或自建):** 用于关联品牌、产品、行业概念，发现潜在联系和洞察。
- **内部逻辑与知识库 (Internal Logic & Knowledge Base):**
  - 预置的行业分类体系与关键词库。
  - Persona 构建框架与模板库（如包含动机、目标、痛点、行为等字段）。
  - 品牌原型理论知识库（如 12 种品牌原型），辅助“人设”定义。
  - 竞争分析模型库（如波特五力模型、SWOT 分析模板的逻辑结构）。
  - 各社交平台特性与用户画像数据库（持续更新）。
  - 内容营销漏斗模型与用户旅程映射逻辑。
- **输出 (结构化数据与深度报告) (Outputs - Structured Data & In-depth Reports):**
  - `Comprehensive_Market_And_Competitor_Intelligence_Report.pdf/.pptx`:
    - **第一部分：品牌现状评估 (Brand Current State Assessment):** 包括在线声量、情感概览、现有内容资产分析。
    - **第二部分：深度竞争格局分析 (In-depth Competitive Landscape Analysis):** 每个核心竞品的详细档案（社交表现、内容策略、视觉风格、受众反馈等），以及横向对比矩阵图。
    - **第三部分：行业趋势与机会洞察 (Industry Trends & Opportunity Insights):** 当前及未来 1-2 年行业内容趋势、热门话题和技术应用、KOL/KOC 生态图谱。
  - `Detailed_Target_Audience_Persona_Portfolio.pdf`: 2-4 个图文并茂的目标受众画像，包含所有细化维度，并附带每个 Persona 的典型用户旅程地图（AIDA 或类似模型）。
  - `Brand_Social_Media_Strategic_Playbook.docx`:
    - **核心定位：** 精炼后的 USP、品牌社交媒体“人设”定义及阐释、沟通“语调”指南（含示例）。
    - **信息架构：** 核心信息屋 (Message House) 详情。
    - **平台战略：** 推荐的核心社交媒体平台组合，各平台在营销矩阵中的角色定位、核心目标和内容方向。
    - **初步 KPI 框架：** 建议与营销目标和平台角色挂钩的初步关键绩效指标 (KPIs) 类型。
  - **传递给 Agent 2 的数据:** 上述所有报告，特别是`Detailed_Target_Audience_Persona_Portfolio.pdf` 和 `Brand_Social_Media_Strategic_Playbook.docx`，以及竞品优秀内容案例的具体链接和分析，行业热门内容形式示例。

---

#### **Agent 2: 内容创意孵化与多维形式策划 Agent (Content Idea Incubation & Multi-Dimensional Format Planning Agent)**

- **核心输入 (Core Inputs - Highly Detailed):**
  - Agent 1 输出的全部战略文档和洞察报告。
  - 品牌方提供的现有内容资产库访问权限或样本（如博客文章、产品图片/视频库、设计素材、FAQ 文档）。
  - 特定营销活动需求（如新品上市推广、节日促销、品牌周年庆、公益活动等）。
  - 明确的内容创作预算档位（来自 Agent 1 或用户确认）。
  - 任何已知的法律、合规、伦理红线或品牌禁忌（如不可使用的词语、图像，需要规避的话题）。
- **细化子任务与处理流程 (Detailed Sub-tasks & Processing Flow):**
  1.  **多维度创意风暴与筛选 (Multi-Dimensional Ideation & Filtering):**
      - **基于信息支柱：** 针对`Brand_Social_Media_Strategic_Playbook.docx`中的每个核心信息支柱，结合每个`Target_Audience_Persona_Portfolio.pdf`的痛点、兴趣点和用户旅程阶段，进行发散性创意构思。
      - **结合趋势与热点：** 将 Agent 1 识别的行业趋势、社交热点、成功竞品案例作为灵感来源，思考如何与品牌信息结合。
      - **运用创意方法论：** 内部调用 SCAMPER、六顶思考帽、逆向思考等创意方法论的逻辑，生成多样化创意点。
      - **初步筛选与打分：** 根据创意与品牌定位的契合度、目标受众的吸引力、可执行性、潜在传播力、预算符合度等标准，对海量创意点进行初步筛选和内部评分。
  2.  **内容主题与系列规划 (Content Pillar & Series Planning):**
      - 将筛选后的优质创意点归类，围绕核心信息支柱，规划出 3-5 个可持续的内容主题系列 (Content Series) 或内容栏目。
      - 每个系列/栏目应有明确的定位、目标受众细分、核心价值传递和大致的更新频次。
  3.  **内容形式与平台适配精细化 (Content Format & Platform Adaptation Refinement):**
      - 为每个内容主题系列下的具体创意点，匹配最合适的 1-2 种主要内容表现形式（如深度图文、条漫、Vlog、短剧本、科普动画、数据可视化报告、互动 H5、播客、在线研讨会、UGC 活动等）。
      - **跨平台分发与再创作策略：** 规划核心内容“一鱼多吃”的策略，例如：一篇深度行业报告可拆解为：
        - 微信公众号：完整版 PDF 下载 + 图文精炼解读。
        - 微博：核心观点长图 + 9 宫格金句海报 + 互动抽奖。
        - 抖音/快手：核心观点动画短视频 + 真人出镜解读。
        - 小红书：报告中的实用 Tips + 精美排版笔记。
        - B 站：深度解读视频 + 配合报告的教程。
      - 明确各平台内容的侧重点和优化方向（如标题党优化、视觉优化、互动引导优化）。
  4.  **旗舰内容深度策划与脚本/大纲撰写 (Flagship Content Deep Planning & Script/Outline Writing):**
      - 选取 3-5 个最具代表性或战略意义的“旗舰级”内容创意，进行深度策划。
      - **图文类 (微信长文/博客/深度报告)：** 详细大纲（包含各级标题、核心论点、数据/案例支撑点、图表规划、SEO 关键词布局）、引人入胜的开头、强有力的结尾、明确的 CTA。
      - **视频类 (短视频/Vlog/动画)：** 详细分镜头脚本或故事板大纲（场景描述、人物动作/对话、镜头语言、BGM/音效建议、时长控制、字幕要点）。
      - **音频类 (播客)：** 节目主题、嘉宾构想（如有）、核心议题与流程大纲、互动环节设计。
      - **互动类 (H5/小游戏/UGC 活动)：** 活动主题、核心玩法/机制、用户参与路径、激励机制、预期效果、技术实现要点。
  5.  **初步文案撰写与 A/B 测试方案 (Initial Copywriting & A/B Testing Plan):**
      - 为部分社交媒体帖子（如未来 1-2 周的核心平台帖子）撰写 A/B 两种不同风格或侧重点的文案初稿（标题、正文、CTA）。
      - 针对关键转化环节（如活动报名页、产品落地页），设计文案 A/B 测试的变量和衡量指标。
  6.  **内容日历精细化编排 (Detailed Editorial Calendar Creation):**
      - 创建至少 1-3 个月的内容日历 (Content Calendar)，具体到每日/每周。
      - **字段包括：** 发布日期、发布时间（基于 Agent 1 对目标受众活跃时间的分析）、目标平台、内容主题/标题、内容系列/栏目、主要形式、辅助形式（跨平台分发）、核心创意点/Brief 链接、状态（策划中/待设计/待发布等）、负责人（留空）、关联营销活动、主要 CTA、预期 KPIs（来自 Agent 1 初步框架）。
      - 确保内容组合的多样性（信息性、娱乐性、互动性、促销性按比例搭配，如经典的 4-1-1 法则或 80/20 法则）和发布的持续性与节奏感。
      - 整合重要的行业会议、节假日、品牌纪念日等，提前规划相关主题内容。
- **API 与工具细化调用 (Detailed API & Tool Usage):**
  - **LLMs (OpenAI GPT-4/Claude 3 Opus/Gemini Advanced via API):**
    - **创意生成：** 基于 Agent 1 的策略输入，生成大量初步内容创意点、标题选项、Slogan。
    - **大纲撰写：** 为博客、文章、视频脚本、播客等生成详细大纲。
    - **文案初稿：** 为社交媒体帖子、广告语、邮件等撰写 A/B 版文案。
    - **内容改写与适配：** 将长内容改写为适合不同平台的短内容，或调整语气风格。
  - **内容灵感与趋势发现工具 API (如 BuzzSumo API, AnswerThePublic (通过爬虫或间接方式获取数据), Google Trends API):** 验证创意热度，发现用户常问问题，拓展相关话题。
  - **项目管理与协作工具 API (如 Trello API, Asana API, Monday.com API, Airtable API, Notion API):** 将生成的内容日历和内容 Brief 结构化地输出到这些平台，方便团队协作。
  - **SEO 关键词工具 API (复用 Agent 1 的工具):** 在撰写大纲和文案时，确保融入目标 SEO 关键词。
  - **Canva API (若未来提供更强创作能力) / Veed.io API (视频编辑类):** 理论上可用于根据文本描述生成初步的图文排版概念或视频剪辑片段（目前更多是辅助）。
- **内部逻辑与知识库 (Internal Logic & Knowledge Base):**
  - 创意方法论模型库（SCAMPER, 结构化思维导图等）。
  - 内容形式与平台最佳实践数据库（如各平台理想视频时长、图文比例、互动机制）。
  - 内容 repurposing 逻辑规则库（如长文转短视频的关键点提取逻辑）。
  - A/B 测试设计原则与常见变量库。
  - 内容日历模板与内容类型配比算法（如基于“英雄-枢纽-卫生”（Hero-Hub-Help）内容模型）。
  - 各行业优秀内容案例库（用于启发，持续更新）。
- **输出 (结构化数据与深度报告) (Outputs - Structured Data & In-depth Reports):**
  - `Content_Idea_Repository_&_Prioritization_Matrix.xlsx`: 包含所有脑暴创意点、筛选标准打分、优先级排序、所属内容主题系列。
  - `Detailed_Content_Series_Blueprints.docx`: 每个内容主题系列的详细规划（定位、目标、核心价值、代表性创意示例、建议形式与频次）。
  - `Flagship_Content_Creative_Briefs_Package.zip`: 包含 3-5 个旗舰级内容的深度策划文档（图文大纲、视频脚本/故事板、活动策划案等）。
  - `Draft_Copy_AB_Testing_Proposals.docx`: 针对部分帖子的 A/B 文案初稿及测试衡量建议。
  - `Master_Editorial_Calendar_(Next_1-3_Months).xlsx/Google Sheets Link`: 包含所有细化字段的交互式内容日历。
  - `Cross-Platform_Content_Repurposing_Guide.pdf`: 针对核心内容形式，提供详细的跨平台分发和再创作指导。
  - **传递给 Agent 3 的数据:** 上述所有输出，特别是`Master_Editorial_Calendar`, `Flagship_Content_Creative_Briefs_Package`, `Draft_Copy_AB_Testing_Proposals`，以及 Agent 1 输出的`Brand_Social_Media_Strategic_Playbook.docx`（尤其是“人设”和“语调”部分，指导视觉风格）。

---

#### **Agent 3: 视觉传达设计与发布执行细化 Agent (Visual Communication Design & Publication Execution Detailing Agent)**

- **核心输入 (Core Inputs - Highly Detailed):**
  - Agent 1 输出的 `Brand_Social_Media_Strategic_Playbook.docx` (含品牌“人设”、“语调”、核心信息屋) 和 `Detailed_Target_Audience_Persona_Portfolio.pdf` (用于分析视觉偏好)。
  - Agent 2 输出的 `Master_Editorial_Calendar`, `Flagship_Content_Creative_Briefs_Package`, `Draft_Copy_AB_Testing_Proposals`。
  - 品牌方提供的现有视觉资产（Logo 源文件、官方 VI 手册、现有图片/视频素材库、字体文件）。
  - 用户提供的视觉偏好参考案例（如喜欢的其他品牌视觉、图片链接）。
  - 内容创作预算中分配给视觉设计的部分。
- **细化子任务与处理流程 (Detailed Sub-tasks & Processing Flow):**
  1.  **现有视觉资产评估与延展性分析 (Existing Visual Asset Audit & Extensibility Analysis):**
      - 评估现有 Logo、VI 手册等是否与 Agent 1 定义的品牌“人设”和“语调”匹配，是否适合在数字和社交媒体上传播。
      - 分析现有视觉资产在不同平台、不同内容形式上的应用潜力和局限性。
  2.  ~~\*竞品与行业视觉趋势深度研究 (Competitor & Industry Visual Trend Deep Research):\*\*~~
      - 回顾 Agent 1 的竞品分析，侧重于其视觉传达策略（色彩、构图、字体、图片/视频风格、品牌元素应用）。
      - 研究当前社交媒体上与品牌行业和目标受众相关的视觉设计流行趋势（如特定滤镜风格、排版方式、动态效果、插画风格）。
  3.  **社交媒体视觉识别系统 (Social VI System) 构建与风格定义:**
      - **色彩体系 (Color Palette):** 扩展或优化品牌主色、辅助色，定义适用于社交媒体的强调色、背景色。确保色彩组合的易读性和情感表达准确性，并考虑无障碍设计。提供 HEX, RGB, CMYK 值。
      - **字体系统 (Typography System):** 推荐 1-2 款主标题字体、1 款正文字体（考虑版权、多语言支持、跨平台显示效果）。定义不同场景下的字号、字重、行距规范。
      - **图像风格指南 (Imagery Style Guide):**
        - **摄影：** 主题（人物/产品/场景）、构图（黄金分割/对称/引导线）、光线（自然光/影棚光）、色调（暖色调/冷色调/高饱和/低饱和）、景深、人物情绪、后期风格。
        - **插画/图形元素：** 风格（扁平风/孟菲斯/3D 拟物/手绘/像素风）、线条粗细、图形符号系统、数据可视化图表规范。
      - **视频风格指南 (Video Style Guide):** 节奏（快/慢）、转场效果、字幕样式、配乐风格、画面调色（LUTs 建议）、动态 Logo 演绎。
      - **版式与构图原则 (Layout & Composition Principles):** 栅格系统应用、留白、视觉焦点引导、信息层级排布、品牌元素（如 Logo）在不同版式中的规范应用。
  4.  **多平台视觉模板概念设计 (Multi-Platform Visual Template Conceptual Design):**
      - 针对`Master_Editorial_Calendar`中高频出现的内容类型和核心平台（如微信公众号头图/长图文内配图、微博九宫格、小红书笔记封面/内页、抖音短视频封面/字幕条/贴片），设计 3-5 套可复用、易编辑的视觉模板概念。
      - 每个模板概念应包含布局草图、关键视觉元素示例、色彩和字体应用说明。
      - **重点是“概念设计”和“规范定义”，而非最终成品制作。**
  5.  **AI 辅助视觉内容初步生成与风格探索 (AI-Assisted Visual Content Prototyping & Style Exploration):**
      - 针对`Flagship_Content_Creative_Briefs_Package`中的部分内容，利用 AI 图像/视频生成工具，根据已定义的视觉风格指南，生成：
        - **情绪板 (Mood Board) 元素：** 快速生成符合色彩、图像风格的图片，组合成多个情绪板，供用户选择或进一步迭代视觉方向。
        - **关键视觉画面 (Key Visuals) 草稿：** 为重要图文内容或视频场景生成概念性插图、背景图、产品展示氛围图。
        - **短视频动态分镜 (Video Storyboard Animatics):** 将视频脚本转化为简单的动态分镜预览，帮助理解节奏和视觉流程。
        - **模板元素示例：** 生成符合模板规范的图标、装饰性图形、背景纹理等。
      - **目标是快速验证视觉风格的可行性，提供创作灵感，并生成可供人类设计师参考的视觉原型。**
  6.  **文案与视觉匹配度审核与优化建议 (Copy & Visual Alignment Review & Optimization):**
      - 审阅 Agent 2 提供的`Draft_Copy_AB_Testing_Proposals`和内容日历中的文案，确保其与规划的视觉风格和具体视觉呈现方式（如图片内容、视频画面）高度匹配、相得益彰。
      - 提出调整文案以更好配合视觉，或调整视觉方案以更好传达文案核心信息的建议。
  7.  **精细化发布策略与推广触点建议 (Refined Publishing Strategy & Promotion Touchpoint Suggestions):**
      - **最佳发布时间窗口：** 结合 Agent 1 的受众分析和各平台特性，给出更精准的每日/每周最佳发布时间窗口建议（可细化到小时）。
      - **高级#标签策略：** 除了通用和行业标签，建议品牌专属#标签，以及如何组合使用不同层级（热门、长尾、活动）的#标签矩阵以最大化曝光。
      - **互动引导与 UGC 激励细化：** 针对不同内容类型，设计更具体的互动引导文案（如提问、投票、有奖评论）和 UGC 活动细则（如参与方式、评选标准、奖励机制）。
      - **KOL/KOC 合作建议（初步）：** 基于 Agent 1 识别的 KOL/KOC 列表和 Agent 2 的内容规划，初步匹配合适的合作人选和合作内容方向（如产品测评、联合直播、内容共创）。
      - **付费推广初步建议：** 针对旗舰内容或重点营销活动，建议在哪些平台、针对哪些受众画像、使用何种广告形式（如信息流广告、搜索广告、KOL 商单）进行小范围预算的付费推广测试。
  8.  **效果追踪指标体系与分析维度建议 (Performance Tracking Metrics & Analysis Dimensions):**
      - 基于 Agent 1 的初步 KPI 框架和 Agent 2 规划的内容，细化每个平台、每种内容类型的核心、次核心、诊断性 KPIs。
      - **示例：**
        - **认知层：** 曝光量、覆盖人数、品牌搜索量增长。
        - **互动层：** 点赞、评论、分享、收藏、转发率、互动率、UGC 产出数量。
        - **引导层：** 点击率 (CTR)、落地页访问量、表单提交数、App 下载量。
        - **转化层 (若可追踪)：** 销售额、订单量、ROI。
        - **品牌健康度：** 粉丝增长数、净推荐值 (NPS)、品牌声量情感正负比。
      - 建议数据分析的维度（如按内容主题、按 Persona、按发布时段）和报告频率（如周报/月报）。
- **API 与工具细化调用 (Detailed API & Tool Usage):**
  - **AI 图像生成平台 API (Midjourney (通过 bot 接口或第三方封装), DALL-E 3 API, Stable Diffusion API (如 Stability AI API, Getimg.ai), Adobe Firefly API):** 根据文本描述和风格指令，生成情绪板素材、关键视觉草图、插画元素、模板背景等。强调 Prompt Engineering 的重要性。
  - **AI 视频生成/编辑工具 API (Runway Gen-2 API, Pictory.ai API, Synthesia.io API (虚拟人), Lumen5 API, Kapwing API (部分功能)):** 生成短视频概念片、动态图文、AI 语音合成、自动字幕、初步剪辑。
  - **设计协作平台 API (Figma API, Adobe Creative Cloud API (有限), Canva API):** 理论上可用于将生成的视觉规范、模板概念、AI 素材结构化地导入设计平台，或生成可供设计师编辑的初步文件。
  - **色彩工具 API (Adobe Color API, Colormind API, Coolors API):** 获取配色方案建议、色彩信息转换、对比度检查。
  - **字体库 API (Google Fonts API, Adobe Fonts API):** 浏览、筛选并获取字体信息。
  - **素材库 API (Pexels API, Unsplash API, Getty Images API, Shutterstock API):** 作为 AI 生成素材的补充，寻找符合风格的高质量摄影图片或视频片段。
  - **社交媒体管理平台 API (Sprout Social API, Hootsuite API, Buffer API, Agorapulse API):** 用于获取更精细的受众活跃时间分析、#标签效果分析，或辅助内容排程（虽然本系统侧重策划）。
  - **LLMs (复用):** 撰写视觉风格描述文档、AI 生成工具的 Prompts 优化、#标签策略描述、互动引导文案、KPI 定义解释。
- **内部逻辑与知识库 (Internal Logic & Knowledge Base):**
  - 视觉设计原理知识库（色彩心理学、版式理论、字体搭配原则）。
  - 各社交平台官方视觉规范与最佳实践（尺寸、比例、格式）。
  - 行业与受众视觉偏好数据库（持续学习）。
  - AI 生成工具 Prompt 模板库与优化策略。
  - #标签分类与热度数据库。
  - 营销 KPI 体系与计算公式库。
- **输出 (结构化数据与深度报告) (Outputs - Structured Data & In-depth Reports):**
  - `Social_Media_Visual_Identity_System_Guide.pdf`:
    - 详细的色彩体系、字体系统、图像风格指南、视频风格指南、版式与构图原则。
    - 至少 2-3 个完整的情绪板 (Mood Boards) 展示整体视觉感受。
    - 3-5 套核心内容类型的视觉模板概念设计稿及使用说明。
  - `AI_Assisted_Visual_Prototypes_Package.zip`: 包含 AI 生成的关键视觉草图、短视频动态分镜、情绪板元素等，按内容 Brief 或日历条目组织。
  - `Master_Editorial_Calendar_V2_With_Visual_Directives.xlsx/Google Sheets Link`: 更新版内容日历，为每个条目添加了明确的视觉风格指导、模板选用建议、AI 原型素材链接或具体视觉需求描述。
  - `Refined_Distribution_And_Engagement_Strategy.docx`:
    - 各平台精准发布时间窗口建议。
    - 详细的#标签矩阵策略（品牌/活动/内容/热门/长尾）。
    - 具体的互动引导和 UGC 激励活动细则。
    - KOL/KOC 初步合作方向和名单建议。
    - 小额付费推广测试方案（平台、受众、形式、预算建议）。
  - `Comprehensive_KPI_Framework_And_Reporting_Template.xlsx`:
    - 详细的 KPI 指标库（含定义、计算公式、追踪工具建议）。
    - 针对不同营销目标的 KPI 组合建议。
    - 内容营销效果分析报告模板（周/月），包含数据可视化图表示例。
